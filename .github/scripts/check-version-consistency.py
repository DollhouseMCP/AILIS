#!/usr/bin/env python3
"""
Check version consistency across different files in the repository.
Supports multiple file formats and provides detailed reporting.
"""

import json
import sys
import re
from pathlib import Path
from typing import Dict, List, Optional, Any, Set

# Optional imports with fallbacks
try:
    import toml
except ImportError:
    toml = None

try:
    import yaml
except ImportError:
    yaml = None

try:
    from packaging import version
except ImportError:
    version = None


class VersionChecker:
    def __init__(self):
        self.versions = {}
        self.issues = []
        self.recommendations = []
        
    def extract_version_from_package_json(self, file_path: Path) -> Optional[str]:
        """Extract version from package.json."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                return data.get('version')
        except Exception as e:
            self.issues.append({
                'severity': 'Warning',
                'message': f'Could not parse {file_path}: {e}'
            })
            return None
            
    def extract_version_from_pyproject_toml(self, file_path: Path) -> Optional[str]:
        """Extract version from pyproject.toml."""
        if toml is None:
            self.issues.append({
                'severity': 'Warning',
                'message': f'Cannot parse {file_path}: toml module not available'
            })
            return None
            
        try:
            data = toml.load(file_path)
            # Check different possible locations
            locations = [
                ['project', 'version'],
                ['tool', 'poetry', 'version'],
                ['tool', 'setuptools', 'version'],
                ['version']
            ]
            
            for location in locations:
                current = data
                try:
                    for key in location:
                        current = current[key]
                    return str(current)
                except KeyError:
                    continue
                    
            return None
        except Exception as e:
            self.issues.append({
                'severity': 'Warning', 
                'message': f'Could not parse {file_path}: {e}'
            })
            return None
            
    def extract_version_from_cargo_toml(self, file_path: Path) -> Optional[str]:
        """Extract version from Cargo.toml."""
        if toml is None:
            self.issues.append({
                'severity': 'Warning',
                'message': f'Cannot parse {file_path}: toml module not available'
            })
            return None
            
        try:
            data = toml.load(file_path)
            return data.get('package', {}).get('version')
        except Exception as e:
            self.issues.append({
                'severity': 'Warning',
                'message': f'Could not parse {file_path}: {e}'
            })
            return None
            
    def extract_version_from_text_file(self, file_path: Path) -> Optional[str]:
        """Extract version from plain text file."""
        try:
            content = file_path.read_text().strip()
            # Remove 'v' prefix if present
            if content.startswith('v'):
                content = content[1:]
            return content
        except Exception as e:
            self.issues.append({
                'severity': 'Warning',
                'message': f'Could not read {file_path}: {e}'
            })
            return None
            
    def extract_version_from_changelog(self, file_path: Path) -> Optional[str]:
        """Extract latest version from CHANGELOG.md."""
        try:
            content = file_path.read_text()
            
            # Look for version patterns in changelog
            patterns = [
                r'##\\s*\\[([0-9]+\\.[0-9]+\\.[0-9]+[^\\]]*?)\\]',  # ## [1.0.0]
                r'##\\s*v?([0-9]+\\.[0-9]+\\.[0-9]+[^\\s]*)',       # ## v1.0.0 or ## 1.0.0
                r'#\\s*v?([0-9]+\\.[0-9]+\\.[0-9]+[^\\s]*)',        # # v1.0.0 or # 1.0.0
            ]
            
            for pattern in patterns:
                matches = re.findall(pattern, content, re.MULTILINE | re.IGNORECASE)
                if matches:
                    return matches[0]  # Return first (presumably latest) version
                    
            return None
        except Exception as e:
            self.issues.append({
                'severity': 'Warning',
                'message': f'Could not parse changelog {file_path}: {e}'
            })
            return None
            
    def extract_version_from_markdown(self, file_path: Path) -> List[str]:
        """Extract version references from markdown files."""
        versions = []
        try:
            content = file_path.read_text()
            
            # Look for version patterns
            patterns = [
                r'Version\\s+([0-9]+\\.[0-9]+\\.[0-9]+[^\\s]*)',
                r'v([0-9]+\\.[0-9]+\\.[0-9]+[^\\s]*)',
                r'version:\\s*([0-9]+\\.[0-9]+\\.[0-9]+[^\\s]*)',
                r'\\[([0-9]+\\.[0-9]+\\.[0-9]+[^\\]]*?)\\]',
            ]
            
            for pattern in patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                versions.extend(matches)
                
        except Exception as e:
            self.issues.append({
                'severity': 'Warning',
                'message': f'Could not parse {file_path}: {e}'
            })
            
        return list(set(versions))  # Remove duplicates
        
    def scan_repository(self):
        """Scan repository for version information."""
        repo_root = Path('.')
        
        # File patterns to check
        file_patterns = {
            '**/package.json': self.extract_version_from_package_json,
            '**/pyproject.toml': self.extract_version_from_pyproject_toml,
            '**/Cargo.toml': self.extract_version_from_cargo_toml,
            'VERSION': self.extract_version_from_text_file,
            'version.txt': self.extract_version_from_text_file,
            'CHANGELOG.md': self.extract_version_from_changelog,
        }
        
        print("🔍 Scanning repository for version information...")
        
        for pattern, extractor in file_patterns.items():
            for file_path in repo_root.glob(pattern):
                if file_path.is_file():
                    print(f"   Checking {file_path}")
                    extracted_version = extractor(file_path)
                    
                    if extracted_version:
                        self.versions[str(file_path)] = {
                            'version': extracted_version,
                            'type': 'primary',
                            'consistent': True  # Will be updated later
                        }
        
        # Check markdown files for version references
        for md_file in repo_root.glob('**/*.md'):
            if md_file.name in ['CHANGELOG.md', 'README.md']:
                continue  # Skip files we handle specifically
                
            versions_found = self.extract_version_from_markdown(md_file)
            if versions_found:
                self.versions[str(md_file)] = {
                    'version': versions_found[0] if len(versions_found) == 1 else versions_found,
                    'type': 'reference',
                    'consistent': True,
                    'all_versions': versions_found if len(versions_found) > 1 else None
                }
                
    def analyze_consistency(self) -> bool:
        """Analyze version consistency."""
        if not self.versions:
            self.issues.append({
                'severity': 'Info',
                'message': 'No version files found in repository'
            })
            return True
            
        print(f"📊 Analyzing {len(self.versions)} version sources...")
        
        # Get all primary versions
        primary_versions = []
        for file_path, info in self.versions.items():
            if info['type'] == 'primary' and info['version']:
                if isinstance(info['version'], str):
                    primary_versions.append(info['version'])
                    
        if not primary_versions:
            self.issues.append({
                'severity': 'Warning',
                'message': 'No primary version files found'
            })
            return True
            
        # Check if all primary versions are the same
        unique_versions = list(set(primary_versions))
        
        if len(unique_versions) == 1:
            canonical_version = unique_versions[0]
            print(f"✅ Consistent primary version: {canonical_version}")
            
            # Check if reference versions match
            consistent = True
            for file_path, info in self.versions.items():
                if info['type'] == 'reference':
                    ref_versions = info.get('all_versions', [info['version']]) if info['version'] else []
                    if isinstance(ref_versions, str):
                        ref_versions = [ref_versions]
                        
                    # Check if any reference version matches canonical
                    if ref_versions and canonical_version not in ref_versions:
                        self.versions[file_path]['consistent'] = False
                        consistent = False
                        self.issues.append({
                            'severity': 'Warning',
                            'message': f'{file_path} references version(s) {ref_versions} but primary version is {canonical_version}'
                        })
                        
            return consistent
            
        else:
            print(f"❌ Inconsistent primary versions found: {unique_versions}")
            
            # Mark all as inconsistent
            for file_path, info in self.versions.items():
                if info['type'] == 'primary':
                    self.versions[file_path]['consistent'] = False
                    
            self.issues.append({
                'severity': 'Error',
                'message': f'Inconsistent primary versions: {", ".join(unique_versions)}'
            })
            
            self.recommendations.extend([
                'Choose one canonical version across all primary version files',
                'Update all package.json, pyproject.toml, Cargo.toml files to use the same version',
                'Consider using a single VERSION file as the source of truth'
            ])
            
            return False
            
    def generate_recommendations(self):
        """Generate recommendations for version management."""
        if not self.recommendations:
            if len(self.versions) > 1:
                self.recommendations.extend([
                    'Consider using automated version bumping tools',
                    'Add version consistency checks to your CI/CD pipeline',
                    'Document your versioning strategy in CONTRIBUTING.md'
                ])
            elif len(self.versions) == 0:
                self.recommendations.extend([
                    'Consider adding a VERSION file to track releases',
                    'Add version information to package files if using package managers',
                    'Include version information in CHANGELOG.md'
                ])
                
    def save_results(self, consistent: bool):
        """Save results to file for workflow consumption."""
        # Determine primary version
        primary_version = None
        for info in self.versions.values():
            if info['type'] == 'primary' and info.get('consistent', True):
                primary_version = info['version']
                break
                
        results = {
            'consistent': consistent,
            'primary_version': primary_version,
            'versions': self.versions,
            'issues': self.issues,
            'recommendations': self.recommendations,
            'summary': {
                'total_files': len(self.versions),
                'primary_files': len([v for v in self.versions.values() if v['type'] == 'primary']),
                'reference_files': len([v for v in self.versions.values() if v['type'] == 'reference'])
            }
        }
        
        with open('.version-check-results.json', 'w') as f:
            json.dump(results, f, indent=2)
            
        # Also set GitHub Actions output
        print(f"::set-output name=consistent::{str(consistent).lower()}")
        if primary_version:
            print(f"::set-output name=primary_version::{primary_version}")
            
    def run_check(self) -> bool:
        """Run the complete version consistency check."""
        self.scan_repository()
        consistent = self.analyze_consistency()
        self.generate_recommendations()
        self.save_results(consistent)
        
        print(f"\\n📊 Version Check Summary:")
        print(f"   Files checked: {len(self.versions)}")
        print(f"   Issues found: {len(self.issues)}")
        print(f"   Consistent: {'✅' if consistent else '❌'}")
        
        return consistent


def main():
    """Main execution function."""
    checker = VersionChecker()
    
    try:
        consistent = checker.run_check()
        
        if not consistent:
            print("\\n❌ Version inconsistencies detected!")
            for issue in checker.issues:
                if issue['severity'] == 'Error':
                    print(f"   ERROR: {issue['message']}")
            sys.exit(1)
        else:
            print("\\n✅ Version consistency check passed!")
            
    except Exception as e:
        print(f"❌ Error during version check: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()