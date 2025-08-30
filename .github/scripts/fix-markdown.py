#!/usr/bin/env python3
"""
Fix markdown files to comply with lint rules.
Handles line length, emphasis style, blank lines, and code blocks.
"""

import re
import os
import sys
from pathlib import Path


def fix_line_length(content, max_length=120):
    """Break long lines at logical points."""
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Skip code blocks and tables
        if line.startswith('|') or line.startswith('```'):
            fixed_lines.append(line)
            continue
            
        # Skip lines that are already short enough
        if len(line) <= max_length:
            fixed_lines.append(line)
            continue
            
        # For long lines, try to break at punctuation or spaces
        if len(line) > max_length:
            # Don't break URLs
            if 'http' in line or 'www.' in line:
                fixed_lines.append(line)
                continue
                
            # Try to break at sentence boundaries
            words = line.split()
            current_line = ""
            for word in words:
                if len(current_line) + len(word) + 1 <= max_length:
                    current_line = current_line + " " + word if current_line else word
                else:
                    if current_line:
                        fixed_lines.append(current_line)
                    current_line = word
            if current_line:
                fixed_lines.append(current_line)
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)


def fix_emphasis_style(content):
    """Fix emphasis style according to markdownlint rules: bold=asterisk, italic=underscore."""
    # Replace bold __text__ with **text** (MD050 wants asterisk for strong)
    content = re.sub(r'__([^_]+)__', r'**\1**', content)
    # Replace italic *text* with _text_ (MD049 wants underscore for emphasis)
    content = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'_\1_', content)
    return content


def fix_blank_lines_around_headings(content):
    """Add blank lines around headings."""
    lines = content.split('\n')
    fixed_lines = []
    in_code_block = False
    
    for i, line in enumerate(lines):
        # Track code blocks
        if line.startswith('```'):
            in_code_block = not in_code_block
            fixed_lines.append(line)
            continue
            
        if in_code_block:
            fixed_lines.append(line)
            continue
            
        # Check if current line is a heading
        if re.match(r'^#+\s', line):
            # Add blank line before if previous line exists and isn't blank
            if i > 0 and fixed_lines and fixed_lines[-1].strip():
                fixed_lines.append('')
            fixed_lines.append(line)
            # Add blank line after if next line exists and isn't blank
            if i < len(lines) - 1 and lines[i + 1].strip() and not lines[i + 1].startswith('#'):
                fixed_lines.append('')
        else:
            # Avoid adding duplicate blank lines
            if line or not (fixed_lines and not fixed_lines[-1]):
                fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)


def fix_blank_lines_around_lists(content):
    """Add blank lines around lists."""
    lines = content.split('\n')
    fixed_lines = []
    in_code_block = False
    in_list = False
    
    for i, line in enumerate(lines):
        # Track code blocks
        if line.startswith('```'):
            in_code_block = not in_code_block
            fixed_lines.append(line)
            continue
            
        if in_code_block:
            fixed_lines.append(line)
            continue
            
        # Check if current line is a list item
        is_list_item = re.match(r'^(\s*[-*+]|\s*\d+\.)\s', line)
        
        if is_list_item:
            # Starting a new list
            if not in_list:
                # Add blank line before if previous line exists and isn't blank
                if i > 0 and fixed_lines and fixed_lines[-1].strip():
                    fixed_lines.append('')
                in_list = True
            fixed_lines.append(line)
        else:
            # Ending a list
            if in_list and line.strip():
                # Add blank line after list
                fixed_lines.append('')
                in_list = False
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)


def fix_code_block_languages(content):
    """Add language specifiers to code blocks."""
    # Find code blocks without language
    content = re.sub(r'^```$', r'```text', content, flags=re.MULTILINE)
    return content


def fix_trailing_newline(content):
    """Ensure file ends with single newline."""
    content = content.rstrip()
    return content + '\n'


def fix_markdown_file(file_path):
    """Fix all markdown issues in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False
    
    original_content = content
    
    # Apply fixes in order
    content = fix_emphasis_style(content)
    content = fix_blank_lines_around_headings(content)
    content = fix_blank_lines_around_lists(content)
    content = fix_code_block_languages(content)
    content = fix_line_length(content)
    content = fix_trailing_newline(content)
    
    # Only write if changed
    if content != original_content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed: {file_path}")
            return True
        except Exception as e:
            print(f"❌ Error writing {file_path}: {e}")
            return False
    else:
        print(f"✓ No changes needed: {file_path}")
        return True


def main():
    """Fix markdown files in the repository."""
    # Priority files that need fixing based on lint errors
    priority_files = [
        'proposals/AILIS_BlogPost_Draft.md',
        'proposals/AILIS_Primer.md',
        'proposals/AILIS_Cheat_Sheet.md',
        'proposals/README.md',
        'reference/README.md',
        'studies/README.md'
    ]
    
    base_path = Path('/Users/mick/Developer/DollhouseMCP Org/AILIS')
    
    print("🔧 Fixing markdown files...")
    print()
    
    fixed_count = 0
    for rel_path in priority_files:
        file_path = base_path / rel_path
        if file_path.exists():
            if fix_markdown_file(file_path):
                fixed_count += 1
        else:
            print(f"⚠️  File not found: {file_path}")
    
    print()
    print(f"✅ Fixed {fixed_count} files")
    
    return 0 if fixed_count > 0 else 1


if __name__ == '__main__':
    sys.exit(main())