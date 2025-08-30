#!/usr/bin/env python3
"""
Generate changelog from git history, commits, and pull requests.
Supports conventional commit format and categorizes changes.
"""

import os
import re
import sys
import json
import requests
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import subprocess


class ChangelogGenerator:
    def __init__(self, github_token: Optional[str] = None):
        self.github_token = github_token
        self.repo_owner = "DollhouseMCP"
        self.repo_name = "AILIS"
        
        # Conventional commit types mapping
        self.commit_types = {
            'feat': {'label': '✨ Features', 'order': 1},
            'fix': {'label': '🐛 Bug Fixes', 'order': 2},
            'docs': {'label': '📚 Documentation', 'order': 3},
            'style': {'label': '🎨 Styling', 'order': 4},
            'refactor': {'label': '♻️ Refactoring', 'order': 5},
            'perf': {'label': '⚡ Performance', 'order': 6},
            'test': {'label': '🧪 Tests', 'order': 7},
            'build': {'label': '🏗️ Build System', 'order': 8},
            'ci': {'label': '👷 CI/CD', 'order': 9},
            'chore': {'label': '🔧 Maintenance', 'order': 10},
            'revert': {'label': '⏪ Reverts', 'order': 11}
        }
        
    def get_git_commits(self, since_tag: Optional[str] = None) -> List[Dict]:
        """Get commits from git history."""
        cmd = ['git', 'log', '--oneline', '--pretty=format:%H|%s|%an|%ad', '--date=short']
        
        if since_tag:
            cmd.append(f'{since_tag}..HEAD')
            
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            commits = []
            
            for line in result.stdout.strip().split('\\n'):
                if '|' in line:
                    parts = line.split('|', 3)
                    if len(parts) >= 4:
                        commits.append({
                            'sha': parts[0],
                            'message': parts[1],
                            'author': parts[2],
                            'date': parts[3]
                        })
            return commits
        except subprocess.CalledProcessError as e:
            print(f"Warning: Could not get git commits: {e}")
            return []
            
    def get_github_prs(self, since_date: Optional[str] = None) -> List[Dict]:
        """Get merged pull requests from GitHub API."""
        if not self.github_token:
            print("Warning: No GitHub token provided, skipping PR information")
            return []
            
        url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/pulls"
        params = {
            'state': 'closed',
            'sort': 'updated',
            'direction': 'desc',
            'per_page': 100
        }
        
        headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        try:
            response = requests.get(url, headers=headers, params=params, timeout=30)
            response.raise_for_status()
            
            prs = response.json()
            merged_prs = []
            
            for pr in prs:
                if pr.get('merged_at'):
                    # Convert merged_at to date for comparison
                    merged_date = pr['merged_at'][:10]  # YYYY-MM-DD
                    
                    if not since_date or merged_date >= since_date:
                        merged_prs.append({
                            'number': pr['number'],
                            'title': pr['title'],
                            'author': pr['user']['login'],
                            'merged_at': merged_date,
                            'body': pr.get('body', ''),
                            'url': pr['html_url']
                        })
                        
            return merged_prs
        except requests.RequestException as e:
            print(f"Warning: Could not fetch PRs: {e}")
            return []
            
    def parse_conventional_commit(self, message: str) -> Tuple[Optional[str], str, str]:
        """Parse conventional commit message."""
        # Pattern: type(scope): description
        pattern = r'^(\\w+)(\\([^)]+\\))?: (.+)'
        match = re.match(pattern, message)
        
        if match:
            commit_type = match.group(1)
            scope = match.group(2) if match.group(2) else ""
            description = match.group(3)
            return commit_type, scope, description
        
        return None, "", message
        
    def categorize_changes(self, commits: List[Dict], prs: List[Dict]) -> Dict[str, List[Dict]]:
        """Categorize commits and PRs by type."""
        categories = {}
        
        # Process commits
        for commit in commits:
            commit_type, scope, description = self.parse_conventional_commit(commit['message'])
            
            if commit_type and commit_type in self.commit_types:
                category = self.commit_types[commit_type]['label']
            else:
                category = '🔄 Other Changes'
                
            if category not in categories:
                categories[category] = []
                
            categories[category].append({
                'type': 'commit',
                'sha': commit['sha'][:7],
                'message': description,
                'author': commit['author'],
                'date': commit['date']
            })
            
        # Process PRs
        for pr in prs:
            commit_type, scope, description = self.parse_conventional_commit(pr['title'])
            
            if commit_type and commit_type in self.commit_types:
                category = self.commit_types[commit_type]['label']
            else:
                category = '🔄 Other Changes'
                
            if category not in categories:
                categories[category] = []
                
            categories[category].append({
                'type': 'pr',
                'number': pr['number'],
                'title': pr['title'],
                'author': pr['author'],
                'date': pr['merged_at'],
                'url': pr['url']
            })
            
        return categories
        
    def generate_version_section(self, version: str, date: str, categories: Dict[str, List[Dict]]) -> str:
        """Generate changelog section for a version."""
        lines = []
        
        # Version header
        version_clean = version.lstrip('v')
        lines.append(f"## [{version_clean}] - {date}")
        lines.append("")
        
        # Sort categories by order
        sorted_categories = sorted(
            categories.items(),
            key=lambda x: next((v['order'] for k, v in self.commit_types.items() 
                              if v['label'] == x[0]), 999)
        )
        
        for category, changes in sorted_categories:
            if not changes:
                continue
                
            lines.append(f"### {category}")
            lines.append("")
            
            for change in changes:
                if change['type'] == 'pr':
                    lines.append(f"- {change['title']} ([#{change['number']}]({change['url']}) by @{change['author']})")
                else:
                    lines.append(f"- {change['message']} ({change['sha']} by {change['author']})")
                    
            lines.append("")
            
        return "\\n".join(lines)
        
    def get_contributors_section(self, commits: List[Dict], prs: List[Dict]) -> str:
        """Generate contributors section."""
        contributors = set()
        
        for commit in commits:
            contributors.add(commit['author'])
            
        for pr in prs:
            contributors.add(pr['author'])
            
        if not contributors:
            return ""
            
        lines = []
        lines.append("### 👥 Contributors")
        lines.append("")
        
        for contributor in sorted(contributors):
            lines.append(f"- @{contributor}")
            
        lines.append("")
        return "\\n".join(lines)
        
    def load_existing_changelog(self) -> str:
        """Load existing changelog content."""
        changelog_path = Path('CHANGELOG.md')
        if changelog_path.exists():
            return changelog_path.read_text(encoding='utf-8')
            
        return """# Changelog

All notable changes to the AILIS project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

"""
        
    def update_changelog(self, version: str, since_tag: Optional[str], date: str, full_rebuild: bool = False) -> bool:
        """Update the changelog with new version."""
        print(f"📝 Generating changelog for version {version}")
        print(f"   Since: {since_tag or 'beginning'}")
        print(f"   Date: {date}")
        
        # Get data
        commits = self.get_git_commits(since_tag if not full_rebuild else None)
        
        # Calculate since date for PRs
        since_date = None
        if since_tag and not full_rebuild:
            try:
                result = subprocess.run(
                    ['git', 'log', '-1', '--format=%ad', '--date=short', since_tag], 
                    capture_output=True, text=True
                )
                since_date = result.stdout.strip()
            except subprocess.CalledProcessError:
                pass
                
        prs = self.get_github_prs(since_date)
        
        if not commits and not prs:
            print("ℹ️  No changes found to add to changelog")
            return False
            
        print(f"   Found {len(commits)} commits and {len(prs)} PRs")
        
        # Categorize changes
        categories = self.categorize_changes(commits, prs)
        
        # Generate new version section
        version_section = self.generate_version_section(version, date, categories)
        contributors_section = self.get_contributors_section(commits, prs)
        
        # Load existing changelog
        existing_content = self.load_existing_changelog()
        
        if full_rebuild:
            # For full rebuild, replace entire changelog
            new_content = existing_content.split('\\n')[:6]  # Keep header
            new_content.extend(['', version_section, contributors_section])
            updated_content = '\\n'.join(new_content)
        else:
            # Insert new version at the top
            lines = existing_content.split('\\n')
            
            # Find insertion point (after header)
            insert_idx = 6  # Default after standard header
            for i, line in enumerate(lines):
                if line.startswith('## ['):
                    insert_idx = i
                    break
                    
            # Insert new content
            new_lines = (lines[:insert_idx] + 
                        ['', version_section, contributors_section] + 
                        lines[insert_idx:])
            updated_content = '\\n'.join(new_lines)
        
        # Write updated changelog
        changelog_path = Path('CHANGELOG.md')
        changelog_path.write_text(updated_content, encoding='utf-8')
        
        print("✅ Changelog updated successfully")
        return True


def main():
    """Main execution function."""
    generator = ChangelogGenerator(os.getenv('GITHUB_TOKEN'))
    
    version = os.getenv('CURRENT_VERSION', 'v0.1.0')
    since_tag = os.getenv('SINCE_TAG')
    date = os.getenv('RELEASE_DATE', datetime.now().strftime('%Y-%m-%d'))
    full_rebuild = os.getenv('FULL_REBUILD', 'false').lower() == 'true'
    
    try:
        success = generator.update_changelog(version, since_tag, date, full_rebuild)
        
        if not success:
            print("ℹ️  Changelog is already up to date")
            
    except Exception as e:
        print(f"❌ Error generating changelog: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()