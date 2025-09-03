#!/usr/bin/env python3
"""
Compile dynamic README from template parts and current repository state.
Generates badges, statistics, and dynamic content sections.
"""

import os
import re
import sys
import json
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

def load_template() -> str:
    """Load the README template."""
    template_path = Path('.github/readme-template.md')
    if template_path.exists():
        return template_path.read_text(encoding='utf-8')
    
    # Fallback to current README as template if no template exists
    readme_path = Path('README.md')
    if readme_path.exists():
        return readme_path.read_text(encoding='utf-8')
    
    # Default template if neither exists
    return """# AILIS (AI Layer Interface Specification)

{{ project_description }}

## 📊 Project Status

{{ workflow_badges }}

{{ project_stats }}

## 📋 Proposals

{{ proposal_listing }}

## 🤝 Contributing

{{ contributing_info }}

## 📚 Documentation

{{ documentation_links }}

---

{{ footer }}
"""

def generate_workflow_badges() -> str:
    """Generate workflow status badges."""
    workflows = []
    workflow_dir = Path('.github/workflows')
    
    if workflow_dir.exists():
        for workflow_file in workflow_dir.glob('*.yml'):
            # Skip certain utility workflows
            if workflow_file.name in ['readme-compilation.yml', 'metrics-collection.yml']:
                continue
                
            try:
                with open(workflow_file, 'r') as f:
                    workflow_content = yaml.safe_load(f)
                    
                workflow_name = workflow_content.get('name', workflow_file.stem)
                workflows.append({
                    'name': workflow_name,
                    'file': workflow_file.name,
                    'badge_name': workflow_name.replace(' ', '%20')
                })
            except Exception as e:
                print(f"Warning: Could not parse workflow {workflow_file}: {e}")
    
    badges = []
    for workflow in workflows:
        badge_url = f"https://github.com/DollhouseMCP/AILIS/actions/workflows/{workflow['file']}/badge.svg"
        action_url = f"https://github.com/DollhouseMCP/AILIS/actions/workflows/{workflow['file']}"
        badges.append(f"[![{workflow['name']}]({badge_url})]({action_url})")
    
    return " ".join(badges)

def get_project_stats() -> Dict[str, Any]:
    """Get current project statistics."""
    return {
        'contributors': os.getenv('REPO_CONTRIBUTORS', '0'),
        'commits': os.getenv('REPO_COMMITS', '0'),
        'proposals': os.getenv('REPO_PROPOSALS', '0'),
        'workflows': os.getenv('REPO_WORKFLOWS', '0'),
        'last_updated': os.getenv('LAST_UPDATED', datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC'))
    }

def generate_proposal_listing() -> str:
    """Generate dynamic proposal listing."""
    proposals_dir = Path('proposals')
    if not proposals_dir.exists():
        return "_No proposals directory found._"
    
    # Get proposal files
    proposal_files = []
    for proposal_file in proposals_dir.glob('*.md'):
        if proposal_file.name == 'README.md':
            continue
            
        try:
            content = proposal_file.read_text(encoding='utf-8')
            
            # Extract title from first heading
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else proposal_file.stem
            
            # Extract status or state information
            status = 'Draft'  # Default status
            if 'status:' in content.lower():
                status_match = re.search(r'status:\s*([^\n]+)', content, re.IGNORECASE)
                if status_match:
                    status = status_match.group(1).strip()
            
            # Get file stats
            stat = proposal_file.stat()
            modified = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d')
            
            proposal_files.append({
                'file': proposal_file.name,
                'title': title,
                'status': status,
                'modified': modified
            })
        except Exception as e:
            print(f"Warning: Could not process proposal {proposal_file}: {e}")
    
    if not proposal_files:
        return "_No proposal files found._"
    
    # Sort by modification date (newest first)
    proposal_files.sort(key=lambda x: x['modified'], reverse=True)
    
    # Generate table
    table = ["| Proposal | Status | Last Updated |", "|----------|--------|--------------|"]
    for proposal in proposal_files:
        link = f"[{proposal['title']}](proposals/{proposal['file']})"
        table.append(f"| {link} | {proposal['status']} | {proposal['modified']} |")
    
    return "\\n".join(table)

def get_contributing_info() -> str:
    """Get contributing information."""
    contributing_path = Path('CONTRIBUTING.md')
    if contributing_path.exists():
        return """See our [Contributing Guidelines](CONTRIBUTING.md) for details on how to participate in the AILIS project.

We follow an RFC-style process for proposals with a minimum 4-week review period."""
    
    return """Contributions are welcome! Please open an issue to discuss your ideas before submitting a pull request."""

def get_documentation_links() -> str:
    """Generate documentation links."""
    links = []
    
    # Core documentation files
    doc_files = {
        'CONTRIBUTING.md': 'Contributing Guidelines',
        'FEEDBACK.md': 'Feedback Areas',
        'CHANGELOG.md': 'Changelog',
        'docs/': 'Additional Documentation'
    }
    
    for file_path, description in doc_files.items():
        path = Path(file_path)
        if path.exists():
            if path.is_file():
                links.append(f"- [{description}]({file_path})")
            else:
                links.append(f"- [{description}]({file_path})")
    
    # Add session notes if they exist
    session_notes_dir = Path('docs/session-notes')
    if session_notes_dir.exists():
        links.append("- [Development Session Notes](docs/session-notes/)")
    
    return "\\n".join(links) if links else "_Documentation is being developed._"

def get_project_description() -> str:
    """Get project description."""
    return """A proposed 16+ layer model for understanding and discussing AI system architectures. 
Think of it as an OSI model for AI systems - a framework for organizing our thinking about the AI stack.

> **Note**: This is a proposal and conversation starter, not a prescriptive standard. 
> We're exploring ideas and seeking community feedback."""

def get_footer() -> str:
    """Generate footer content."""
    stats = get_project_stats()
    return f"""*This README is automatically updated. Last generated: {stats['last_updated']}*

**Repository Statistics**: {stats['contributors']} contributors • {stats['commits']} commits • {stats['proposals']} proposals • {stats['workflows']} workflows"""

def compile_readme():
    """Compile the final README."""
    template = load_template()
    
    # Prepare replacement values
    replacements = {
        'project_description': get_project_description(),
        'workflow_badges': generate_workflow_badges(),
        'project_stats': f"**Active Proposals**: {get_project_stats()['proposals']} | **Contributors**: {get_project_stats()['contributors']} | **Workflows**: {get_project_stats()['workflows']}",
        'proposal_listing': generate_proposal_listing(),
        'contributing_info': get_contributing_info(),
        'documentation_links': get_documentation_links(),
        'footer': get_footer()
    }
    
    # Perform template replacements
    compiled_readme = template
    for key, value in replacements.items():
        compiled_readme = compiled_readme.replace(f"{{{{ {key} }}}}", value)
    
    # Clean up any remaining template variables
    compiled_readme = re.sub(r'\\{\\{\\s*\\w+\\s*\\}\\}', '', compiled_readme)
    
    return compiled_readme

def main():
    """Main execution function."""
    try:
        print("🔧 Compiling dynamic README...")
        
        compiled_content = compile_readme()
        
        # Write to README.md
        readme_path = Path('README.md')
        readme_path.write_text(compiled_content, encoding='utf-8')
        
        print("✅ README compilation completed successfully!")
        
        # Print summary
        stats = get_project_stats()
        print(f"📊 Project Statistics:")
        print(f"   - Contributors: {stats['contributors']}")
        print(f"   - Commits: {stats['commits']}")
        print(f"   - Proposals: {stats['proposals']}")
        print(f"   - Workflows: {stats['workflows']}")
        print(f"   - Last Updated: {stats['last_updated']}")
        
    except Exception as e:
        print(f"❌ Error compiling README: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()