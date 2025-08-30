#!/usr/bin/env python3
"""
Accessibility checker for AILIS markdown files.
Checks for proper heading hierarchy, alt text, and link text.
"""

import re
import os
import sys
import argparse
from pathlib import Path


def check_heading_hierarchy(file_path):
    """Check if headings follow proper hierarchy (no level jumps)."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except (OSError, UnicodeDecodeError) as e:
        print(f"Warning: Could not read {file_path}: {e}")
        return []
    
    headings = re.findall(r'^(#+)\s+(.+)', content, re.MULTILINE)
    if not headings:
        return []
    
    issues = []
    prev_level = 0
    
    for heading_marks, heading_text in headings:
        current_level = len(heading_marks)
        
        # Skip first heading level jump check
        if prev_level > 0 and current_level > prev_level + 1:
            issues.append(f"Heading level jump: '{heading_text}' (H{current_level} after H{prev_level})")
        
        prev_level = current_level
    
    return issues


def check_alt_text(file_path):
    """Check for images without alt text."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except (OSError, UnicodeDecodeError) as e:
        print(f"Warning: Could not read {file_path}: {e}")
        return []
    
    issues = []
    
    # Find images without alt text: ![](url)
    empty_alt_images = re.findall(r'!\[\]\([^)]+\)', content)
    if empty_alt_images:
        issues.extend([f"Image without alt text: {img}" for img in empty_alt_images])
    
    # Find images with only whitespace alt text: ![   ](url)  
    whitespace_alt_images = re.findall(r'!\[\s+\]\([^)]+\)', content)
    if whitespace_alt_images:
        issues.extend([f"Image with empty alt text: {img}" for img in whitespace_alt_images])
    
    return issues


def check_link_text(file_path):
    """Check for non-descriptive link text."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except (OSError, UnicodeDecodeError) as e:
        print(f"Warning: Could not read {file_path}: {e}")
        return []
    
    issues = []
    problematic_patterns = [
        (r'\[click here\]', "click here"),
        (r'\[here\]', "here"), 
        (r'\[read more\]', "read more"),
        (r'\[more\]', "more"),
        (r'\[link\]', "link"),
        (r'\[this\]', "this"),
    ]
    
    for pattern, description in problematic_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            issues.append(f"Non-descriptive link text: '{description}' ({len(matches)} occurrence(s))")
    
    return issues


def main():
    """Main accessibility checker function."""
    parser = argparse.ArgumentParser(description='Check accessibility of markdown files')
    parser.add_argument('--path', default='.', help='Path to check (default: current directory)')
    parser.add_argument('--report', help='Output report file path')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    args = parser.parse_args()
    
    all_issues = {}
    total_files_checked = 0
    
    print("🔍 Starting accessibility checks...")
    
    # Walk through all markdown files
    for root, dirs, files in os.walk(args.path):
        # Skip common directories that shouldn't be checked
        dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', '.github', 'venv', '__pycache__']]
        
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, args.path)
                total_files_checked += 1
                
                if args.verbose:
                    print(f"  Checking: {rel_path}")
                
                file_issues = []
                
                # Run all checks
                heading_issues = check_heading_hierarchy(file_path)
                alt_text_issues = check_alt_text(file_path)
                link_text_issues = check_link_text(file_path)
                
                file_issues.extend(heading_issues)
                file_issues.extend(alt_text_issues)
                file_issues.extend(link_text_issues)
                
                if file_issues:
                    all_issues[rel_path] = file_issues
    
    # Generate report
    if args.report:
        with open(args.report, 'w') as f:
            f.write("# Accessibility Check Report\n\n")
            if all_issues:
                for file_path, issues in all_issues.items():
                    f.write(f"## {file_path}\n\n")
                    for issue in issues:
                        f.write(f"- ❌ {issue}\n")
                    f.write("\n")
            else:
                f.write("✅ No accessibility issues found!\n")
    
    # Print summary
    print(f"\n📊 Accessibility Check Complete")
    print(f"Files checked: {total_files_checked}")
    
    if all_issues:
        print(f"Issues found in {len(all_issues)} files:")
        for file_path, issues in all_issues.items():
            print(f"  ❌ {file_path}: {len(issues)} issues")
            if args.verbose:
                for issue in issues:
                    print(f"     - {issue}")
        sys.exit(1)
    else:
        print("✅ No accessibility issues found!")
        sys.exit(0)


if __name__ == '__main__':
    main()