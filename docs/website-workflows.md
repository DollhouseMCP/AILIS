# Website Workflows Documentation

This document describes the GitHub Actions workflows that build, deploy, and maintain the AILIS documentation website.

## Overview

The AILIS website is built using [MkDocs Material](https://squidfunk.github.io/mkdocs-material/), a modern documentation framework. The site is automatically built from the repository's markdown files and deployed to GitHub Pages.

## Workflows

### 🌐 Website Build & Deploy

**File**: `.github/workflows/website-build-deploy.yml`

**Purpose**: Builds the documentation site and deploys it to GitHub Pages.

**Triggers**:
- Push to `main` branch (when documentation files change)
- Manual trigger via workflow dispatch

**What it does**:
1. Checks out the repository with full git history
2. Installs MkDocs Material and all required plugins
3. Gathers site statistics (proposal count, page count, etc.)
4. Builds the static site using `mkdocs build`
5. Validates the build output
6. Uploads the site as an artifact
7. Deploys to GitHub Pages

**Key Features**:
- **Strict mode**: Build fails on warnings or errors
- **Git metadata**: Includes last-modified dates for all pages
- **Build validation**: Checks for required files and broken links
- **Artifacts**: Retains build artifacts for 30 days
- **Summary**: Provides detailed build report

**Environment Variables**:
- `SITE_PROPOSALS`: Number of proposals
- `SITE_PAGES`: Total page count
- `SITE_UPDATED`: Build timestamp
- `GIT_HASH`: Git commit hash

### 🔍 Website PR Preview

**File**: `.github/workflows/website-pr-preview.yml`

**Purpose**: Builds preview versions of the site for pull requests.

**Triggers**:
- Pull request opened, synchronized, or reopened
- Changes to documentation files or site configuration

**What it does**:
1. Checks out the PR branch
2. Builds a preview version of the site
3. Adds a preview banner to all pages
4. Uploads the preview as an artifact
5. Comments on the PR with preview information
6. Validates the preview build quality

**Key Features**:
- **Preview banner**: Clearly marks pages as preview builds
- **PR comments**: Automatic updates with build status
- **Quality validation**: Checks for broken links and accessibility issues
- **7-day retention**: Preview artifacts are kept for one week
- **No auto-deploy**: For security, previews are not automatically deployed

**How to view previews**:
1. Wait for the workflow to complete
2. Download the `preview-site-pr-{number}` artifact
3. Extract and open `index.html` locally
4. Or manually deploy to a preview service (Netlify, Vercel, etc.)

### 🏥 Website Health Check

**File**: `.github/workflows/website-health-check.yml`

**Purpose**: Monitors the deployed website for issues.

**Triggers**:
- Daily schedule (6 AM UTC)
- Manual trigger with check type selection

**What it does**:
1. Checks if the site is accessible
2. Validates all links on the live site
3. Analyzes site performance (page size, load time)
4. Verifies essential content is present
5. Checks security headers
6. Creates issues for critical failures
7. Auto-closes issues when problems are resolved

**Check Types** (manual trigger):
- **Full**: Complete health check including performance and security
- **Quick**: Basic availability check only
- **Links-only**: Just validate links

**Key Features**:
- **Automated monitoring**: Daily checks ensure site health
- **Issue management**: Auto-creates/closes issues
- **Performance tracking**: Monitors page size and load times
- **Link validation**: Comprehensive link checking with retries
- **Security checks**: Validates security headers

**What's checked**:
- ✅ Site availability (HTTP 200 response)
- ✅ Response time
- ✅ Internal and external links
- ✅ Page size and resource count
- ✅ Essential content presence
- ✅ Security headers (X-Frame-Options, CSP, HSTS)
- ✅ Accessibility basics

## Site Configuration

### MkDocs Configuration

The site is configured via `mkdocs.yml` in the repository root.

**Key settings**:
- **Theme**: Material Design with light/dark mode
- **Navigation**: Tabs, sections, breadcrumbs, back-to-top
- **Search**: Suggestions, highlighting, sharing
- **Features**: Code copying, content tabs, tooltips
- **Plugins**: Git metadata, search, minification, lightbox, RSS

**Installed Plugins**:
- `mkdocs-material`: Main theme
- `mkdocs-git-revision-date-localized-plugin`: Last updated dates
- `mkdocs-awesome-pages-plugin`: Flexible navigation
- `mkdocs-minify-plugin`: HTML/CSS/JS minification
- `mkdocs-glightbox`: Image lightbox
- `mkdocs-git-authors-plugin`: Contributor attribution
- `mkdocs-rss-plugin`: RSS feed generation

### Custom Styling

**CSS**: `docs/assets/stylesheets/extra.css`
- Proposal-specific styling
- RFC-style status badges
- Enhanced tables and code blocks
- Accessibility improvements
- Print styles

**JavaScript**: `docs/assets/javascripts/extra.js`
- Exploratory notices on proposal pages
- Layer reference highlighting
- Reading time estimates
- External link indicators
- Smooth scrolling
- Accessibility enhancements

### Hooks

**Proposal Metadata**: `docs/hooks/proposal_metadata.py`
- Automatically extracts metadata from proposals
- Adds status badges
- Formats metadata boxes
- Enhances proposal pages

## Directory Structure

```
/
├── mkdocs.yml                    # Site configuration
├── index.md                      # Homepage
├── proposals/
│   ├── index.md                  # Proposals landing page
│   └── *.md                      # Individual proposals
├── reference/
│   ├── index.md                  # Reference landing page
│   └── *.md                      # Code examples
├── studies/
│   ├── index.md                  # Case studies landing page
│   └── *.md                      # Individual case studies
├── docs/
│   ├── index.md                  # Documentation landing page
│   ├── assets/
│   │   ├── stylesheets/
│   │   │   └── extra.css         # Custom CSS
│   │   └── javascripts/
│   │       └── extra.js          # Custom JavaScript
│   ├── hooks/
│   │   └── proposal_metadata.py  # MkDocs hook
│   └── overrides/                # Theme overrides
└── includes/
    └── abbreviations.md          # Abbreviation definitions
```

## Building Locally

To build and preview the site locally:

```bash
# Install dependencies
pip install mkdocs-material \
  mkdocs-git-revision-date-localized-plugin \
  mkdocs-awesome-pages-plugin \
  mkdocs-minify-plugin \
  mkdocs-redirects \
  pymdown-extensions \
  mkdocs-rss-plugin \
  mkdocs-glightbox \
  mkdocs-git-authors-plugin

# Serve locally (with live reload)
mkdocs serve

# Build production site
mkdocs build

# Build with strict mode (fail on warnings)
mkdocs build --strict
```

The site will be available at `http://localhost:8000`.

## Deployment

### GitHub Pages Setup

The site is deployed to GitHub Pages automatically when changes are pushed to `main`.

**Required setup**:
1. Enable GitHub Pages in repository settings
2. Set source to "GitHub Actions"
3. Configure custom domain (if needed)
4. **(Optional)** Set `SITE_URL` repository variable for health checks:
   - Go to repository Settings → Secrets and variables → Actions → Variables
   - Add variable name: `SITE_URL`
   - Add variable value: `https://dollhousemcp.github.io/AILIS` (or your custom domain)
   - If not set, health checks will default to `https://dollhousemcp.github.io/AILIS`

**Permissions required**:
- `contents: write` - For pushing to gh-pages branch
- `pages: write` - For deploying to GitHub Pages
- `id-token: write` - For GitHub Pages deployment

### Custom Domain

To use a custom domain:

1. Add a `CNAME` file to `docs/` with your domain
2. Configure DNS records at your domain provider
3. Enable HTTPS in repository settings

## Troubleshooting

### Build Fails

**Problem**: MkDocs build fails with errors

**Solutions**:
- Check the workflow logs for specific errors
- Validate `mkdocs.yml` syntax
- Ensure all referenced files exist
- Test locally with `mkdocs build --strict`

### Broken Links

**Problem**: Health check reports broken links

**Solutions**:
- Check the link validation output in workflow summary
- Update or remove broken links
- Add redirects in `mkdocs.yml` for moved pages

### Preview Not Showing Changes

**Problem**: PR preview doesn't reflect recent changes

**Solutions**:
- Ensure workflow completed successfully
- Download the latest artifact (not an older one)
- Clear browser cache when viewing locally

### Deployment Fails

**Problem**: GitHub Pages deployment fails

**Solutions**:
- Check GitHub Pages is enabled in settings
- Verify source is set to "GitHub Actions"
- Check workflow permissions are correct
- Review deployment logs for specific errors

## Best Practices

### Writing Documentation

1. **Use semantic headings**: Maintain proper heading hierarchy (H1 → H2 → H3)
2. **Add alt text**: Include descriptive alt text for all images
3. **Link internally**: Use relative links for internal pages
4. **Include metadata**: Add frontmatter for page-specific settings
5. **Test locally**: Preview changes with `mkdocs serve` before committing

### Managing Proposals

1. **Use status markers**: Include status in proposal metadata
2. **Add RFC numbers**: Reference RFC/proposal numbers
3. **Date proposals**: Include creation and update dates
4. **Cross-reference**: Link related proposals and discussions

### Performance

1. **Optimize images**: Compress images before adding to repository
2. **Minimize large files**: Keep individual pages under 100KB if possible
3. **Use lazy loading**: For images and heavy content
4. **Test build time**: Monitor workflow duration

## Maintenance

### Regular Tasks

- **Weekly**: Review health check results
- **Monthly**: Update dependencies (`pip install --upgrade`)
- **Quarterly**: Audit and update documentation structure
- **As needed**: Respond to health check issues

### Updating Dependencies

```bash
# Update MkDocs and plugins
pip install --upgrade mkdocs-material \
  mkdocs-git-revision-date-localized-plugin \
  mkdocs-awesome-pages-plugin \
  mkdocs-minify-plugin \
  mkdocs-rss-plugin \
  mkdocs-glightbox \
  mkdocs-git-authors-plugin

# Test locally
mkdocs build --strict
mkdocs serve

# Update workflow if needed
# Edit .github/workflows/website-build-deploy.yml
```

### Monitoring

Key metrics to monitor:
- Build duration (should be < 2 minutes)
- Deploy duration (should be < 1 minute)
- Site availability (should be 99.9%+)
- Link health (no broken links)
- Page load time (< 3 seconds)

## Support

### Resources

- [MkDocs Material Documentation](https://squidfunk.github.io/mkdocs-material/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

### Getting Help

- **Technical issues**: Open an issue with label `website`
- **Content questions**: Start a discussion
- **Urgent problems**: Tag with `urgent` label

## Changelog

- **2025-01-15**: Initial website workflows created
  - Build and deploy workflow
  - PR preview workflow
  - Health check workflow
  - MkDocs configuration
  - Custom styling and JavaScript
