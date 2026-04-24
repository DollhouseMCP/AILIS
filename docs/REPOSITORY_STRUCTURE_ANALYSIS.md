# AILIS Repository Structure & Automation Overview

## Executive Summary

The AILIS repository is a well-structured, proposal-based project for an AI Layer Interface Specification. It features:

- **Status**: Version 0.2.0 in development
- **Core Content**: 3 main proposals + 1 blog post draft (421 lines total)
- **Automation**: 15 GitHub workflows across validation, lifecycle, and content management
- **Supporting Scripts**: 9 Python automation scripts for workflow support
- **Publication Readiness**: Markdown-based with automated compilation and validation

---

## 1. DOCUMENTATION FILES & CONTENT STRUCTURE

### Root-Level Documentation

| File | Purpose | Size |
| --- | --- | --- |
| `README.md` | Main project introduction, framework overview, and calls to action | ~220 lines |
| `CONTRIBUTING.md` | RFC-style contribution workflow and guidelines | ~180+ lines |
| `FEEDBACK.md` | Areas where community input is actively sought | Core guidance |
| `CLAUDE.md` | AI assistant context and project philosophy | 4.7 KB |
| `CHANGELOG.md` | Semantic versioning changelog with automated updates | 3.3 KB |
| `LICENSE` | Apache 2.0 license | 11.3 KB |
| `LICENSE-DOCS` | CC-BY 4.0 for documentation | 1.9 KB |

### Proposals Directory (`/proposals`)

**Current Proposals:**

- `AILIS_Primer.md` (161 lines) - Primary framework specification with 16+ layer model
- `AILIS_Cheat_Sheet.md` (38 lines) - Quick reference guide for the layer model
- `AILIS_BlogPost_Draft.md` (187 lines) - Blog post version explaining the concept to broader audience
- `README.md` (35 lines) - Directory index and proposal submission instructions

**Naming Convention**: `AILIS-XXX-description.md`
**Proposal States**: Draft → Review (4 weeks min) → Final Comment → Accepted/Declined
**Submission**: Via GitHub issues + draft branch PRs with RFC workflow

### Reference Implementations Directory (`/reference`)

- `README.md` - Directory guide for schemas, examples, tools, and validators
- Currently a template awaiting contributions
- Purpose: Code examples demonstrating AILIS concepts

### Case Studies Directory (`/studies`)

- `README.md` - Directory for real-world system mappings
- Guide for submitting case studies with anonymization support
- Purpose: Validate framework against real systems

### Session Notes Directory (`/docs/session-notes`)

**Current Sessions:**

1. `session-notes-2025-08-30-initial-repository-setup.md`
2. `session-notes-2025-08-30-tier1-workflows-implementation.md`
3. `session-notes-2025-08-30-tier2-workflows-implementation.md`
4. `session-notes-2025-09-03-link-validation-fix.md`

**Purpose**: Historical development context and decision rationale

---

## 2. GITHUB WORKFLOWS DIRECTORY (`.github/workflows`)

### All 15 Workflows at a Glance

| Workflow | Trigger | Purpose | Size |
| --- | --- | --- | --- |
| `link-validation.yml` | Push (main), PR, weekly | Validate internal and external links | 2.3 KB |
| `markdown-lint.yml` | PR, push | Style and format checking for markdown | 1.8 KB |
| `spell-check.yml` | PR, push | Spell checking with project word list | 1.6 KB |
| `accessibility-check.yml` | PR, push | Check heading hierarchy, alt text, link text | 2.9 KB |
| `proposal-lifecycle.yml` | PR (proposals/), daily | Auto-label proposals and track stages | 11 KB |
| `proposal-stage-transitions.yml` | Issue labels | Handle stage transitions (draft→review→final→decision) | 7.6 KB |
| `readme-compilation.yml` | Push (main), PR, weekly | Dynamically update README with stats | 9.8 KB |
| `changelog-automation.yml` | Merged PRs, releases, manual | Extract PR titles/descriptions → changelog | 8.9 KB |
| `yaml-validation.yml` | Workflow file changes | Validate GitHub Actions workflow YAML | 2.2 KB |
| `validate-config.yml` | Config changes, manual | Validate all configuration files | 3.2 KB |
| `version-consistency.yml` | Workflow changes, manual | Check version consistency across files | 5.0 KB |
| `metrics-collection.yml` | Schedule (weekly), manual | Collect workflow performance metrics | 5.8 KB |
| `discussion-notifications.yml` | Discussions opened | Send discussion notifications | 9.9 KB |
| `claude-code-review.yml` | PR opened/updated | Add Claude AI code review comments | 2.0 KB |
| `claude.yml` | PR events | Generic Claude integration workflow | 2.0 KB |

**Total Workflows**: 15 (14 trigger-based, 1 utility)

### Workflow Organization by Category

**Content Quality & Validation** (6 workflows)

- Link validation (internal + external)
- Markdown linting
- Spell checking
- Accessibility checking
- YAML validation
- Configuration validation

**Proposal Lifecycle Management** (2 workflows)

- Auto-labeling and stage tracking
- Stage transition handling with automation

**Documentation & Release** (3 workflows)

- README compilation with statistics
- Changelog automation from PRs
- Version consistency checking

**Community & Integration** (3 workflows)

- Discussion notifications
- Metrics collection
- Claude AI integration (code review)

**Infrastructure** (1 workflow)

- General Claude integration

---

## 3. CONTENT ORGANIZATION FOR WEBSITE PUBLICATION

### Current Architecture

**Structure is Publication-Ready**:

- Flat markdown files in logical directories
- No build system currently (content is ready-to-use)
- Automated compilation of dynamic README

### Publication Hierarchy

```text
Root Documentation (user-facing)
├── README.md (main entry point with badges)
├── CONTRIBUTING.md (how to participate)
├── FEEDBACK.md (what we need input on)
└── CHANGELOG.md (version history)

Formal Proposals
└── /proposals/
    ├── AILIS_Primer.md (framework spec)
    ├── AILIS_Cheat_Sheet.md (quick ref)
    ├── AILIS_BlogPost_Draft.md (general audience)
    └── [Future proposals...]

Reference Materials
└── /reference/
    ├── Schemas (to be added)
    ├── Code Examples (to be added)
    └── Tools & Validators (to be added)

Real-World Validation
└── /studies/
    └── Case studies (to be added)

Context & History
└── /docs/session-notes/
    └── Development decisions and learning
```

### Automated Content Enhancement

**README Compilation Workflow** generates:

- Repository statistics (contributors, commits, proposals)
- Workflow status badges
- Dynamic table of contents
- Last updated timestamp
- Auto-commits or PRs when main branch changes

**Metrics Collection** tracks:

- Workflow execution times
- Success rates
- Performance trends

### Static Assets Available

- `.github/readme-template.md` - Template for dynamic README sections
- `.github/pull_request_template.md` - PR submission guidance
- `.github/ISSUE_TEMPLATE/` - Issue templates (proposal, feedback, use-case)

---

## 4. EXISTING CONFIGURATION FILES & AUTOMATION

### Version Management

- `VERSION` file: `0.2.0` (semantic versioning)
- `.version-check-results.json` - Validation results cache

### Pre-commit Hooks (`.pre-commit-config.yaml`)

**Installed Hooks**:

1. **Custom Workflow Validation**
   - Python script validates all `.github/workflows/*.yml` files

2. **YAML Linting** (yamllint v1.32.0)
   - Max line length: 150 characters
   - Allows custom tags for GitHub Actions

3. **YAML Syntax Check** (pre-commit v4.5.0)
   - Unsafe mode enabled for custom YAML tags

4. **Markdown Linting** (markdownlint v0.37.0)
   - Auto-fix mode enabled

5. **Trailing Whitespace**
   - Removes trailing whitespace
   - Fixes end-of-file issues
   - Prevents large file commits (>1000KB)

### Validation & Quality Tools

**Spell Check Configuration** (`.github/cspell.json`)

- Language: English (US)
- Dictionaries: Standard + tech terms + companies
- **Custom Words**: AILIS, OSI, MLOps, DevOps, LLMs, RAG, Anthropic, Claude, etc.
- Ignores: npm packages, git, logs, locks
- Allows compound words, case-insensitive

**Link Validation** (`.github/mlc_config.json`)

- **Ignore Patterns**: localhost, JS protocols, mailto, template variables
- **HTTP Status Codes**: 200, 201, 202, 204, 206, 300-304, 307-308
- **Retry Logic**: 3 retries, 429 rate-limit handling
- **Timeout**: 30 seconds
- **External Tools**:
  - `markdown-link-check` for internal links
  - `lychee` for external links with exponential backoff

**Markdown Linting** (`.github/markdownlint.json`)

- Standard markdown linting rules applied to all .md files

### Git Configuration

**`.gitignore`** ignores:

- OS files (DS_Store, Thumbs.db)
- IDE/editor files (VSCode, Sublime, Nova)
- Build artifacts (build/, dist/, egg-info)
- Node modules and lock files
- Environment files (.env, .env.*)
- Logs and temp files
- Coverage and test reports
- Documentation builds (mkdocs, site/)
- Python cache (**pycache**, .pytest_cache)
- Package manager caches

### GitHub Automation Scripts

**Available Python Scripts** (`.github/scripts/`):

1. **`validate-workflows.py`** (5.7 KB)
   - Pre-commit hook for workflow validation
   - Validates YAML syntax and GitHub Actions structure

2. **`compile-readme.py`** (8.9 KB, executable)
   - Generates dynamic README with stats
   - Runs in readme-compilation workflow
   - Pulls: contributions, commits, proposals, workflows

3. **`generate-toc.py`** (8.0 KB, executable)
   - Generates table of contents for markdown files
   - Runs in readme-compilation workflow
   - Updates README with auto-generated TOC

4. **`generate-changelog.py`** (13 KB, executable)
   - Extracts changelog entries from merged PRs
   - Parses PR titles and descriptions
   - Creates semantic versioning changelog

5. **`check-version-consistency.py`** (14 KB, executable)
   - Validates version consistency across files
   - Supports: VERSION, package.json, pyproject.toml, YAML
   - Prevents version mismatches

6. **`check-accessibility.py`** (5.7 KB)
   - Validates heading hierarchy
   - Checks alt text and link quality
   - Ensures proper markdown accessibility

7. **`collect-metrics.py`** (6.4 KB)
   - Queries GitHub Actions API for workflow stats
   - Collects execution times and success rates
   - Generates metrics reports

8. **`fix-markdown.py`** (6.7 KB, executable)
   - Auto-fixes markdown formatting issues
   - Runs during pre-commit/CI

9. **`add-concurrency.sh`** (3.3 KB)
   - Utility for adding concurrency groups to workflows
   - Prevents workflow conflicts

### Issue & PR Templates

**Issue Templates** (`.github/ISSUE_TEMPLATE/`):

- `proposal.yml` - For submitting new proposals
- `feedback.yml` - For critiques and suggestions
- `use-case.yml` - For case study submissions

**Pull Request Template** (`.github/pull_request_template.md`)

- Guides proposal PR submission
- Links to CONTRIBUTING.md

### Documentation Templates

- `.github/readme-template.md` - Template for README sections
- `.github/LINK_VALIDATION_CONFIG.md` - Configuration documentation for link checking

---

## WEBSITE PUBLICATION READINESS ASSESSMENT

### Current State: ✅ Ready for Static Site Generation

**Strengths:**

1. **All content is Markdown** - Compatible with any static site generator
2. **Clean directory structure** - Natural navigation for site hierarchy
3. **Automated updates** - README, changelog, TOC auto-generated
4. **Link validation** - All internal/external links checked weekly
5. **Version tracking** - Semantic versioning with changelog
6. **Quality assurance** - Spell check, accessibility, markdown lint

**What Would Be Needed for Website:**

- Static site generator (Hugo, Jekyll, MkDocs, or custom)
- CSS styling and branding
- Search functionality (optional but recommended)
- Analytics (optional)
- Domain and hosting

**Recommended Generators:**

- **MkDocs** - Purpose-built for documentation, great for RFC-style projects
- **Hugo** - Fast, flexible, minimal dependencies
- **Jekyll** - GitHub-native, simplest GitHub Pages integration
- **Astro** - Modern, with great markdown support

**Pre-built Hooks:**

- Workflows can trigger site builds and deployments
- Metadata already in place (version, date, contributors)
- Content structure supports automated navigation generation

---

## KEY STATISTICS

| Metric | Value |
| --- | --- |
| **Total Markdown Files** | 16 |
| **Total Lines of Documentation** | ~2,000+ |
| **Proposal Documents** | 3 active + 1 draft (421 lines) |
| **GitHub Workflows** | 15 |
| **Automation Scripts** | 9 Python scripts |
| **Pre-commit Hooks** | 5 categories |
| **Link Validation Rules** | 8 ignore patterns |
| **Custom Words (Spell Check)** | 50+ |
| **Issue Templates** | 3 types |
| **Current Version** | 0.2.0 |

---

## AUTOMATION HIGHLIGHTS

### Most Important Workflows for Website

1. **Link Validation** - Ensures all links are current before publication
2. **README Compilation** - Auto-updates with stats and TOC
3. **Markdown Lint** - Ensures consistent formatting
4. **Spell Check** - Maintains professional documentation
5. **Accessibility Check** - Ensures content is accessible

### CI/CD Ready

The repository has strong CI/CD foundations:

- Every PR is validated for quality, links, and consistency
- Main branch only accepts merged, tested content
- Automation can trigger deployments to a website
- Version tracking enables proper release management

---

## RECOMMENDATIONS FOR PUBLICATION

### Phase 1: Static Site Setup

- Choose generator (recommend MkDocs for proposal-style docs)
- Create basic theme/styling
- Map current directory structure to site navigation

### Phase 2: Automation Integration

- Add workflow step to build and deploy site on main branch pushes
- Configure custom domain and HTTPS
- Set up redirects for old URLs (if migrating)

### Phase 3: Enhancement

- Add site search
- Create RSS feed for changelog
- Add discussion forum integration
- Email notifications for major updates

### Phase 4: Distribution

- Add OpenGraph meta tags for social sharing
- Create landing page with download options
- Add API documentation if reference implementations grow
- Consider publishing to npm, PyPI, or similar registries
