#!/usr/bin/env python3
"""
Generate table of contents for markdown files.
Supports automatic TOC insertion and updating.
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple


class TOCGenerator:
    def __init__(self):
        self.toc_start_marker = "<!-- TOC_START -->"
        self.toc_end_marker = "<!-- TOC_END -->"
        
    def extract_headings(self, content: str) -> List[Dict[str, any]]:
        """Extract headings from markdown content."""
        headings = []
        lines = content.split('\\n')
        
        in_code_block = False
        for i, line in enumerate(lines):
            # Track code blocks to skip headings inside them
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                continue
                
            if in_code_block:
                continue
                
            # Match ATX-style headings (# ## ### etc)
            heading_match = re.match(r'^(#{1,6})\\s+(.+)$', line.strip())
            if heading_match:
                level = len(heading_match.group(1))
                text = heading_match.group(2).strip()
                
                # Clean up heading text (remove markdown formatting)
                clean_text = re.sub(r'[*_`]', '', text)
                clean_text = re.sub(r'\\[([^\\]]+)\\]\\([^)]+\\)', r'\\1', clean_text)  # Remove links
                
                # Generate anchor (GitHub style)
                anchor = self.generate_anchor(clean_text)
                
                headings.append({
                    'level': level,
                    'text': clean_text,
                    'anchor': anchor,
                    'line': i + 1
                })
                
        return headings
        
    def generate_anchor(self, text: str) -> str:
        """Generate GitHub-style anchor from heading text."""
        # Convert to lowercase
        anchor = text.lower()
        
        # Replace spaces with hyphens
        anchor = re.sub(r'\\s+', '-', anchor)
        
        # Remove special characters except hyphens and alphanumeric
        anchor = re.sub(r'[^a-z0-9\\-]', '', anchor)
        
        # Remove consecutive hyphens
        anchor = re.sub(r'-+', '-', anchor)
        
        # Remove leading/trailing hyphens
        anchor = anchor.strip('-')
        
        return anchor
        
    def generate_toc(self, headings: List[Dict[str, any]], max_depth: int = 6, min_depth: int = 1) -> str:
        """Generate table of contents from headings."""
        if not headings:
            return ""
            
        # Filter headings by depth
        filtered_headings = [h for h in headings if min_depth <= h['level'] <= max_depth]
        
        if not filtered_headings:
            return ""
            
        # Find the minimum level to use as base indentation
        min_level = min(h['level'] for h in filtered_headings)
        
        toc_lines = []
        toc_lines.append("## Table of Contents")
        toc_lines.append("")
        
        for heading in filtered_headings:
            # Calculate indentation (2 spaces per level)
            indent_level = (heading['level'] - min_level) * 2
            indent = " " * indent_level
            
            # Create TOC entry
            toc_entry = f"{indent}- [{heading['text']}](#{heading['anchor']})"
            toc_lines.append(toc_entry)
            
        return "\\n".join(toc_lines)
        
    def update_toc_in_content(self, content: str, toc: str) -> Tuple[str, bool]:
        """Update or insert TOC in content."""
        start_pos = content.find(self.toc_start_marker)
        end_pos = content.find(self.toc_end_marker)
        
        # If both markers exist, replace content between them
        if start_pos != -1 and end_pos != -1:
            before_toc = content[:start_pos + len(self.toc_start_marker)]
            after_toc = content[end_pos:]
            
            new_content = f"{before_toc}\\n\\n{toc}\\n\\n{after_toc}"
            return new_content, True
            
        # If no markers exist, try to insert after first heading
        lines = content.split('\\n')
        insert_position = None
        
        for i, line in enumerate(lines):
            if re.match(r'^#\\s+', line):  # First H1 heading
                # Look for a good position after the heading (skip description)
                insert_position = i + 1
                
                # Skip empty lines and description paragraphs
                while insert_position < len(lines):
                    if (lines[insert_position].strip() == "" or 
                        not lines[insert_position].startswith('#')):
                        insert_position += 1
                    else:
                        break
                break
                
        if insert_position is not None:
            # Insert TOC with markers
            toc_block = [
                "",
                self.toc_start_marker,
                "",
                toc,
                "",
                self.toc_end_marker,
                ""
            ]
            
            new_lines = lines[:insert_position] + toc_block + lines[insert_position:]
            return "\\n".join(new_lines), True
            
        # If no suitable position found, append at the end
        toc_block = [
            "",
            self.toc_start_marker,
            "",
            toc,
            "",
            self.toc_end_marker
        ]
        
        return content + "\\n" + "\\n".join(toc_block), True
        
    def process_file(self, file_path: Path, max_depth: int = 6, min_depth: int = 1) -> bool:
        """Process a single markdown file to update its TOC."""
        if not file_path.exists():
            print(f"❌ File not found: {file_path}")
            return False
            
        try:
            # Read file content
            content = file_path.read_text(encoding='utf-8')
            original_content = content
            
            # Extract headings
            headings = self.extract_headings(content)
            
            if not headings:
                print(f"ℹ️  No headings found in {file_path}")
                return True
                
            # Generate TOC
            toc = self.generate_toc(headings, max_depth, min_depth)
            
            if not toc:
                print(f"ℹ️  No TOC generated for {file_path}")
                return True
                
            # Update content with TOC
            updated_content, changed = self.update_toc_in_content(content, toc)
            
            if changed and updated_content != original_content:
                # Write updated content back to file
                file_path.write_text(updated_content, encoding='utf-8')
                print(f"✅ Updated TOC in {file_path}")
                print(f"   Generated {len(headings)} heading entries")
                return True
            else:
                print(f"ℹ️  TOC already up to date in {file_path}")
                return True
                
        except Exception as e:
            print(f"❌ Error processing {file_path}: {e}")
            return False


def main():
    """Main execution function."""
    if len(sys.argv) < 2:
        print("Usage: python3 generate-toc.py <file_path> [max_depth] [min_depth]")
        print("Example: python3 generate-toc.py README.md 3 1")
        sys.exit(1)
        
    file_path = Path(sys.argv[1])
    max_depth = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    min_depth = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    
    generator = TOCGenerator()
    
    print(f"🔧 Generating TOC for {file_path}...")
    print(f"   Depth range: H{min_depth} to H{max_depth}")
    
    success = generator.process_file(file_path, max_depth, min_depth)
    
    if success:
        print("✅ TOC generation completed successfully!")
    else:
        print("❌ TOC generation failed!")
        sys.exit(1)


if __name__ == '__main__':
    main()