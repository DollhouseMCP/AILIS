"""
Integration tests for MkDocs build with proposal_metadata hook

These tests build actual MkDocs sites to ensure the hook works in practice.

Run with: python -m pytest tests/test_mkdocs_integration.py -v
"""

import pytest
import tempfile
import shutil
import subprocess
import os
from pathlib import Path


@pytest.fixture
def temp_mkdocs_project():
    """Create a temporary MkDocs project for testing"""
    tmpdir = tempfile.mkdtemp()

    try:
        # Create minimal mkdocs.yml
        mkdocs_config = """
site_name: Test Site
theme:
  name: material
plugins:
  - search
hooks:
  - docs/hooks/proposal_metadata.py
"""
        with open(os.path.join(tmpdir, 'mkdocs.yml'), 'w') as f:
            f.write(mkdocs_config)

        # Create directory structure
        os.makedirs(os.path.join(tmpdir, 'proposals'), exist_ok=True)
        os.makedirs(os.path.join(tmpdir, 'docs', 'hooks'), exist_ok=True)

        # Copy the hook file
        hook_source = Path(__file__).parent.parent / 'docs' / 'hooks' / 'proposal_metadata.py'
        hook_dest = os.path.join(tmpdir, 'docs', 'hooks', 'proposal_metadata.py')
        shutil.copy(hook_source, hook_dest)

        # Create index.md
        with open(os.path.join(tmpdir, 'index.md'), 'w') as f:
            f.write('# Test Site\n\nWelcome to the test site.')

        yield tmpdir

    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


def test_mkdocs_build_with_proposal(temp_mkdocs_project):
    """Test that MkDocs builds successfully with a proposal containing metadata"""
    # Create a proposal with metadata
    proposal_content = """Status: Draft
Author: Test Author
Date: 2025-01-15

# Test Proposal

This is a test proposal.
"""
    proposal_path = os.path.join(temp_mkdocs_project, 'proposals', 'test.md')
    with open(proposal_path, 'w') as f:
        f.write(proposal_content)

    # Build the site
    result = subprocess.run(
        ['mkdocs', 'build', '--strict'],
        cwd=temp_mkdocs_project,
        capture_output=True,
        text=True
    )

    # Check build succeeded
    assert result.returncode == 0, f"Build failed: {result.stderr}"

    # Check that the site directory was created
    site_dir = os.path.join(temp_mkdocs_project, 'site')
    assert os.path.exists(site_dir), "Site directory was not created"

    # Check that proposal HTML was generated
    proposal_html = os.path.join(site_dir, 'proposals', 'test', 'index.html')
    assert os.path.exists(proposal_html), "Proposal HTML was not generated"

    # Check that metadata was injected
    with open(proposal_html, 'r') as f:
        html_content = f.read()
        assert 'Proposal Metadata' in html_content, "Metadata box not found in HTML"
        assert 'Draft' in html_content, "Status not found in HTML"
        assert 'Test Author' in html_content, "Author not found in HTML"


def test_mkdocs_build_with_non_proposal(temp_mkdocs_project):
    """Test that non-proposal pages are not modified"""
    # Create a regular doc page
    doc_content = """# Regular Documentation

This is not a proposal.
"""
    docs_dir = os.path.join(temp_mkdocs_project, 'docs')
    os.makedirs(docs_dir, exist_ok=True)
    doc_path = os.path.join(docs_dir, 'guide.md')
    with open(doc_path, 'w') as f:
        f.write(doc_content)

    # Build the site
    result = subprocess.run(
        ['mkdocs', 'build', '--strict'],
        cwd=temp_mkdocs_project,
        capture_output=True,
        text=True
    )

    assert result.returncode == 0, f"Build failed: {result.stderr}"

    # Check that doc HTML was generated
    doc_html = os.path.join(temp_mkdocs_project, 'site', 'docs', 'guide', 'index.html')
    assert os.path.exists(doc_html), "Doc HTML was not generated"

    # Check that metadata was NOT injected
    with open(doc_html, 'r') as f:
        html_content = f.read()
        assert 'Proposal Metadata' not in html_content, "Metadata should not be in non-proposal"


def test_mkdocs_build_with_malformed_proposal(temp_mkdocs_project):
    """Test that malformed proposals don't break the build"""
    # Create a proposal with unusual content
    proposal_content = """# Malformed Proposal

No metadata here, just content.

Status: This is not at the start
"""
    proposal_path = os.path.join(temp_mkdocs_project, 'proposals', 'malformed.md')
    with open(proposal_path, 'w') as f:
        f.write(proposal_content)

    # Build should still succeed
    result = subprocess.run(
        ['mkdocs', 'build', '--strict'],
        cwd=temp_mkdocs_project,
        capture_output=True,
        text=True
    )

    assert result.returncode == 0, f"Build failed: {result.stderr}"


def test_mkdocs_build_with_multiple_proposals(temp_mkdocs_project):
    """Test building with multiple proposals"""
    # Create multiple proposals
    for i in range(3):
        proposal_content = f"""Status: {'Draft' if i == 0 else 'Review' if i == 1 else 'Final'}
Author: Author {i}

# Proposal {i}

Content for proposal {i}.
"""
        proposal_path = os.path.join(temp_mkdocs_project, 'proposals', f'proposal{i}.md')
        with open(proposal_path, 'w') as f:
            f.write(proposal_content)

    # Build should succeed
    result = subprocess.run(
        ['mkdocs', 'build', '--strict'],
        cwd=temp_mkdocs_project,
        capture_output=True,
        text=True
    )

    assert result.returncode == 0, f"Build failed: {result.stderr}"

    # Check all proposals were built
    for i in range(3):
        proposal_html = os.path.join(
            temp_mkdocs_project, 'site', 'proposals', f'proposal{i}', 'index.html'
        )
        assert os.path.exists(proposal_html), f"Proposal {i} HTML not found"


if __name__ == '__main__':
    pytest.main([__file__, '-v', '-s'])
