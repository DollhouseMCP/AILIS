#!/usr/bin/env python3
"""
Workflow metrics collection for AILIS repository.
Tracks execution times, success rates, and other workflow statistics.
"""

import json
import os
import sys
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional


def get_github_headers() -> Dict[str, str]:
    """Get GitHub API headers with authentication."""
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print("Warning: No GITHUB_TOKEN provided, using unauthenticated requests")
        return {'Accept': 'application/vnd.github.v3+json'}
    
    return {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': f'token {token}',
        'User-Agent': 'AILIS-MetricsCollector/1.0'
    }


def fetch_workflow_runs(repo: str, workflow_file: str, days: int = 30) -> List[Dict[str, Any]]:
    """Fetch recent workflow runs from GitHub API."""
    headers = get_github_headers()
    since_date = (datetime.now() - timedelta(days=days)).isoformat()
    
    url = f"https://api.github.com/repos/{repo}/actions/workflows/{workflow_file}/runs"
    params = {
        'per_page': 100,
        'created': f'>{since_date}'
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        return response.json().get('workflow_runs', [])
    except requests.RequestException as e:
        if hasattr(e, 'response') and e.response is not None and e.response.status_code == 403 and 'rate limit' in str(e).lower():
            print(f"Rate limited. Consider using authenticated requests: {e}")
        else:
            print(f"Error fetching workflow runs: {e}")
        return []


def calculate_workflow_metrics(runs: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Calculate metrics from workflow runs."""
    if not runs:
        return {
            'total_runs': 0,
            'success_rate': 0,
            'avg_duration_minutes': 0,
            'latest_status': 'unknown'
        }
    
    total_runs = len(runs)
    successful_runs = len([r for r in runs if r['conclusion'] == 'success'])
    success_rate = (successful_runs / total_runs) * 100
    
    # Calculate average duration for completed runs
    durations = []
    for run in runs:
        if run['status'] == 'completed' and run['created_at'] and run['updated_at']:
            start = datetime.fromisoformat(run['created_at'].replace('Z', '+00:00'))
            end = datetime.fromisoformat(run['updated_at'].replace('Z', '+00:00'))
            duration = (end - start).total_seconds() / 60  # Convert to minutes
            durations.append(duration)
    
    avg_duration = sum(durations) / len(durations) if durations else 0
    
    return {
        'total_runs': total_runs,
        'successful_runs': successful_runs,
        'failed_runs': total_runs - successful_runs,
        'success_rate': round(success_rate, 1),
        'avg_duration_minutes': round(avg_duration, 2),
        'latest_status': runs[0]['conclusion'] if runs else 'unknown',
        'latest_run_date': runs[0]['created_at'] if runs else None
    }


def generate_metrics_report(repo: str, workflows: List[str], output_file: str = 'workflow-metrics.json'):
    """Generate comprehensive metrics report for all workflows."""
    print("📊 Collecting workflow metrics...")
    
    all_metrics = {
        'generated_at': datetime.now().isoformat(),
        'repository': repo,
        'period_days': 30,
        'workflows': {}
    }
    
    for workflow in workflows:
        print(f"  Analyzing {workflow}...")
        runs = fetch_workflow_runs(repo, workflow)
        metrics = calculate_workflow_metrics(runs)
        all_metrics['workflows'][workflow] = metrics
    
    # Calculate overall statistics
    total_runs = sum(w['total_runs'] for w in all_metrics['workflows'].values())
    total_successful = sum(w['successful_runs'] for w in all_metrics['workflows'].values())
    overall_success_rate = (total_successful / total_runs * 100) if total_runs > 0 else 0
    
    all_metrics['summary'] = {
        'total_workflows': len(workflows),
        'total_runs_all_workflows': total_runs,
        'overall_success_rate': round(overall_success_rate, 1),
        'avg_runs_per_workflow': round(total_runs / len(workflows), 1) if workflows else 0
    }
    
    # Write to file
    with open(output_file, 'w') as f:
        json.dump(all_metrics, f, indent=2)
    
    print(f"✅ Metrics report generated: {output_file}")
    return all_metrics


def print_metrics_summary(metrics: Dict[str, Any]):
    """Print human-readable metrics summary."""
    print("\n📈 Workflow Metrics Summary")
    print("=" * 50)
    
    summary = metrics['summary']
    print(f"Repository: {metrics['repository']}")
    print(f"Period: {metrics['period_days']} days")
    print(f"Total workflows: {summary['total_workflows']}")
    print(f"Total runs: {summary['total_runs_all_workflows']}")
    print(f"Overall success rate: {summary['overall_success_rate']}%")
    print()
    
    print("Per-Workflow Breakdown:")
    print("-" * 30)
    
    for workflow_name, data in metrics['workflows'].items():
        status_emoji = "✅" if data['latest_status'] == 'success' else "❌" if data['latest_status'] == 'failure' else "⚠️"
        print(f"{status_emoji} {workflow_name}")
        print(f"   Runs: {data['total_runs']} | Success Rate: {data['success_rate']}% | Avg Duration: {data['avg_duration_minutes']}min")
    
    print()


def main():
    """Main metrics collection function."""
    repo = os.environ.get('GITHUB_REPOSITORY')
    if not repo:
        print("Error: GITHUB_REPOSITORY environment variable not set")
        sys.exit(1)
    
    # Define workflows to track
    workflows = [
        'link-validation.yml',
        'markdown-lint.yml', 
        'spell-check.yml',
        'accessibility-check.yml',
        'proposal-lifecycle.yml',
        'discussion-notifications.yml'
    ]
    
    # Generate metrics report
    metrics = generate_metrics_report(repo, workflows)
    
    # Print summary
    print_metrics_summary(metrics)
    
    # Set GitHub Actions output if running in CI
    if os.environ.get('GITHUB_ACTIONS'):
        with open(os.environ.get('GITHUB_OUTPUT', '/dev/null'), 'a') as f:
            f.write(f"overall_success_rate={metrics['summary']['overall_success_rate']}\n")
            f.write(f"total_runs={metrics['summary']['total_runs_all_workflows']}\n")


if __name__ == '__main__':
    main()