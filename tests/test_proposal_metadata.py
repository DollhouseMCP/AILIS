"""
Tests for proposal_metadata.py hook

Run with: python -m pytest tests/test_proposal_metadata.py
"""

import pytest
from docs.hooks.proposal_metadata import (
    extract_metadata,
    format_metadata_box,
    insert_after_first_heading,
    on_page_markdown,
    on_page_content
)


class MockPage:
    """Mock Page object for testing"""
    def __init__(self, src_path):
        self.file = MockFile(src_path)


class MockFile:
    """Mock File object for testing"""
    def __init__(self, src_path):
        self.src_path = src_path


def test_extract_metadata_with_all_fields():
    """Test extracting all metadata fields"""
    markdown = """
    Status: Draft
    Author: John Doe
    Date: 2025-01-15
    RFC: 001
    Version: 1.0

    # Title
    Content here
    """
    metadata = extract_metadata(markdown)

    assert metadata['status'] == 'Draft'
    assert metadata['authors'] == 'John Doe'
    assert metadata['date'] == '2025-01-15'
    assert metadata['rfc'] == '001'
    assert metadata['version'] == '1.0'


def test_extract_metadata_case_insensitive():
    """Test that metadata extraction is case-insensitive"""
    markdown = """
    status: draft
    AUTHOR: Jane Smith
    """
    metadata = extract_metadata(markdown)

    assert metadata['status'] == 'draft'
    assert metadata['authors'] == 'Jane Smith'


def test_extract_metadata_empty():
    """Test extracting from markdown with no metadata"""
    markdown = """
    # Just a title
    No metadata here
    """
    metadata = extract_metadata(markdown)

    assert len(metadata) == 0


def test_format_metadata_box():
    """Test formatting metadata as admonition"""
    metadata = {
        'status': 'Draft',
        'authors': 'Test Author',
        'date': '2025-01-15'
    }

    result = format_metadata_box(metadata)

    assert '!!! info "Proposal Metadata"' in result
    assert '**Status**: 📝 Draft' in result
    assert '**Authors**: Test Author' in result
    assert '**Date**: 2025-01-15' in result


def test_format_metadata_box_with_emojis():
    """Test that status emojis are correctly applied"""
    test_cases = [
        ('draft', '📝'),
        ('review', '👀'),
        ('final', '✅'),
        ('declined', '❌')
    ]

    for status, emoji in test_cases:
        metadata = {'status': status}
        result = format_metadata_box(metadata)
        assert f'{emoji} {status}' in result


def test_insert_after_first_heading():
    """Test inserting content after first H1"""
    markdown = """# Main Title

Some content here"""

    content = "New content"
    result = insert_after_first_heading(markdown, content)

    assert result.startswith('# Main Title\n\nNew content\n')


def test_insert_after_first_heading_no_heading():
    """Test inserting when no heading exists"""
    markdown = "Just some text"
    content = "New content"

    result = insert_after_first_heading(markdown, content)

    assert result.startswith('New content\n\n')


def test_on_page_markdown_proposal_page():
    """Test processing a proposal page"""
    page = MockPage('proposals/test.md')
    markdown = """Status: Draft

# Test Proposal
Content"""

    result = on_page_markdown(markdown, page, None, None)

    # Should contain metadata box
    assert '!!! info "Proposal Metadata"' in result
    assert '**Status**: 📝 Draft' in result


def test_on_page_markdown_non_proposal_page():
    """Test that non-proposal pages are not modified"""
    page = MockPage('docs/test.md')
    markdown = "# Regular Page\nContent"

    result = on_page_markdown(markdown, page, None, None)

    assert result == markdown  # Should be unchanged


def test_on_page_markdown_error_handling():
    """Test that errors don't fail the build"""
    page = MockPage('proposals/test.md')
    # This should trigger an error in processing but not raise
    markdown = None

    result = on_page_markdown(markdown, page, None, None)

    # Should return empty string for None input
    assert result == ""


def test_on_page_markdown_invalid_input_type():
    """Test handling of non-string markdown input"""
    page = MockPage('proposals/test.md')

    # Test with integer
    result = on_page_markdown(123, page, None, None)
    assert result == 123  # Returns original invalid input

    # Test with list
    result = on_page_markdown([], page, None, None)
    assert result == []


def test_on_page_markdown_invalid_page_object():
    """Test handling of invalid page object"""
    markdown = "# Test"

    # Page without file attribute
    class BadPage:
        pass

    page = BadPage()
    result = on_page_markdown(markdown, page, None, None)
    assert result == markdown  # Returns unchanged


def test_on_page_content_proposal_class():
    """Test adding proposal class to HTML"""
    page = MockPage('proposals/test.md')
    html = '<article>Content</article>'

    result = on_page_content(html, page, None, None)

    assert '<article class="proposal-page"' in result


def test_on_page_content_non_proposal():
    """Test that non-proposal pages don't get class"""
    page = MockPage('docs/test.md')
    html = '<article>Content</article>'

    result = on_page_content(html, page, None, None)

    assert result == html  # Unchanged


def test_on_page_content_error_handling():
    """Test that HTML processing errors are handled"""
    page = MockPage('proposals/test.md')
    html = None

    result = on_page_content(html, page, None, None)

    # Should return original without raising
    assert result is None


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
