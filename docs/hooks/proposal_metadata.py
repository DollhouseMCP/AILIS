"""
AILIS Proposal Metadata Hook

Automatically extracts and processes metadata from proposal documents.
Enhances proposals with status, authors, and other RFC-style metadata.
"""

import re
from mkdocs.structure.pages import Page
from mkdocs.config import Config


def on_page_markdown(markdown: str, page: Page, config: Config, files) -> str:
    """
    Process proposal pages to extract and format metadata.

    Args:
        markdown: The raw markdown content
        page: The current page object
        config: MkDocs configuration
        files: All files in the site

    Returns:
        Modified markdown with enhanced metadata
    """
    # Only process proposal pages
    if not page.file.src_path.startswith('proposals/'):
        return markdown

    # Extract metadata from frontmatter or content
    metadata = extract_metadata(markdown)

    # Add metadata box if we found any
    if metadata:
        metadata_box = format_metadata_box(metadata)
        # Insert after the first heading
        markdown = insert_after_first_heading(markdown, metadata_box)

    return markdown


def extract_metadata(markdown: str) -> dict:
    """
    Extract metadata from markdown content.

    Looks for common patterns like:
    - Status: Draft/Review/Final
    - Author: Name
    - Date: YYYY-MM-DD
    - RFC: Number
    """
    metadata = {}

    # Status pattern
    status_match = re.search(r'^Status:\s*(.+)$', markdown, re.MULTILINE | re.IGNORECASE)
    if status_match:
        metadata['status'] = status_match.group(1).strip()

    # Author pattern
    author_match = re.search(r'^Authors?:\s*(.+)$', markdown, re.MULTILINE | re.IGNORECASE)
    if author_match:
        metadata['authors'] = author_match.group(1).strip()

    # Date pattern
    date_match = re.search(r'^Date:\s*(.+)$', markdown, re.MULTILINE | re.IGNORECASE)
    if date_match:
        metadata['date'] = date_match.group(1).strip()

    # RFC/Proposal number pattern
    rfc_match = re.search(r'^(?:RFC|Proposal):\s*(.+)$', markdown, re.MULTILINE | re.IGNORECASE)
    if rfc_match:
        metadata['rfc'] = rfc_match.group(1).strip()

    # Version pattern
    version_match = re.search(r'^Version:\s*(.+)$', markdown, re.MULTILINE | re.IGNORECASE)
    if version_match:
        metadata['version'] = version_match.group(1).strip()

    return metadata


def format_metadata_box(metadata: dict) -> str:
    """
    Format metadata as an admonition box.

    Args:
        metadata: Dictionary of extracted metadata

    Returns:
        Formatted markdown admonition
    """
    lines = ['!!! info "Proposal Metadata"', '']

    if 'status' in metadata:
        status = metadata['status'].lower()
        status_emoji = {
            'draft': '📝',
            'review': '👀',
            'final': '✅',
            'declined': '❌'
        }.get(status, '📋')
        lines.append(f'    **Status**: {status_emoji} {metadata["status"]}')

    if 'authors' in metadata:
        lines.append(f'    **Authors**: {metadata["authors"]}')

    if 'date' in metadata:
        lines.append(f'    **Date**: {metadata["date"]}')

    if 'rfc' in metadata:
        lines.append(f'    **RFC**: {metadata["rfc"]}')

    if 'version' in metadata:
        lines.append(f'    **Version**: {metadata["version"]}')

    lines.append('')
    return '\n'.join(lines)


def insert_after_first_heading(markdown: str, content: str) -> str:
    """
    Insert content after the first H1 heading.

    Args:
        markdown: Original markdown
        content: Content to insert

    Returns:
        Modified markdown
    """
    # Find first H1 heading
    heading_match = re.search(r'^# .+$', markdown, re.MULTILINE)

    if heading_match:
        insert_pos = heading_match.end()
        return markdown[:insert_pos] + '\n\n' + content + '\n' + markdown[insert_pos:]

    # If no heading found, prepend
    return content + '\n\n' + markdown


def on_page_content(html: str, page: Page, config: Config, files) -> str:
    """
    Post-process HTML content.

    Args:
        html: The rendered HTML
        page: The current page object
        config: MkDocs configuration
        files: All files in the site

    Returns:
        Modified HTML
    """
    # Add proposal-specific classes
    if page.file.src_path.startswith('proposals/'):
        html = html.replace('<article', '<article class="proposal-page"', 1)

    return html
