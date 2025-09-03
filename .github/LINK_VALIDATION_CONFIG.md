# Link Validation Configuration Documentation

## Configuration File: `mlc_config.json`

This configuration is used by the markdown-link-check GitHub Action to validate links in our documentation.

### Why Replacement Patterns Were Removed

We initially attempted to use replacement patterns to handle relative paths in template files:
```json
"replacementPatterns": [
  {
    "pattern": "^proposals/",
    "replacement": "{{GITHUB_WORKSPACE}}/proposals/"
  }
]
```

However, this approach failed because:
1. The `{{GITHUB_WORKSPACE}}` variable was treated as a literal string, not expanded
2. Template files in `.github/` have paths relative to the final compiled location, not their current location
3. The markdown-link-check action doesn't support the variable expansion we needed

### Current Solution

Instead of using replacement patterns, we:
1. **Exclude `.github/` directory entirely** from link checking (templates are intermediate files)
2. **Only check user-facing documentation** that readers actually access
3. **Use explicit file and folder paths** in the workflow configuration

### Ignore Patterns Explained

- `^http://localhost`, `^https://localhost`, `^http://127.0.0.1`, `^https://127.0.0.1` - Local development URLs
- `^javascript:` - JavaScript protocol links (not actual URLs)
- `^mailto:` - Email links (not web URLs)
- `^{{.*}}$` - Template variables (e.g., `{{ footer }}`) used in readme-template.md

### Why Empty Replacement Patterns

The `replacementPatterns` array is intentionally empty because:
- Replacement patterns with variables don't work as expected
- We solve the path issue by excluding template files instead
- All links in user-facing docs use correct relative paths

## Workflow Configuration

The link validation workflow uses:
- `file-path` to specify root-level markdown files
- `folder-path` to specify directories to check
- Excludes `.github/` directory by not including it in paths
- This prevents false positives from template files with different path contexts