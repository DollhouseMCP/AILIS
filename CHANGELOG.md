# Changelog

All notable changes to the AILIS proposal will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [0.1.0] - 2026-02-15

### ✨ Features

- Add detailed layer breakdown to README template (4d4cf1c by Mick Darling)
- Implement comprehensive Tier 2 automation workflows (#4) (2301fce by Mick Darling)
- Implement comprehensive automation workflows (Tier 1) (#3) (89ced17 by Mick Darling)
- feat: Implement comprehensive Tier 2 automation workflows ([#4](https://github.com/DollhouseMCP/AILIS/pull/4) by @mickdarling)
- feat: Implement comprehensive automation workflows (Tier 1) ([#3](https://github.com/DollhouseMCP/AILIS/pull/3) by @mickdarling)

### 🐛 Bug Fixes

- Remove push trigger from changelog automation to prevent infinite PR loop (#53) (10f6227 by Mick Darling)
- Remove redundant Introduction link from navigation (#51) (8b31488 by Mick Darling)
- Don't exclude root README.md from build (#49) (fc4181b by Mick Darling)
- Don't exclude root README.md from build (e9da053 by Mick Darling)
- Resolve MkDocs strict mode build failures (#45) (122e283 by Mick Darling)
- Update docs/index.md links to use symlinked paths (4bbcace by Mick Darling)
- Correct newline escaping in changelog automation (#42) (f23546f by Mick Darling)
- Use symlinks in docs/ for external files instead of ../ paths (42e5e9c by Mick Darling)
- prevent changelog automation self-trigger loop (#21) (74086c1 by Mick Darling)
- use max-depth to prevent checking .github directory (3287848 by Mick Darling)
- properly configure link validation to skip template files (dbc2bd2 by Mick Darling)
- properly handle template files in link validation (bccb5fa by Mick Darling)
- configure markdown link checker to handle directory links properly (aad6877 by Mick Darling)
- remove mlc_config.json and use default link checking behavior (794baf8 by Mick Darling)
- trigger link validation when mlc_config.json changes (c218a0c by Mick Darling)
- improve link validation configuration for relative paths (36108f1 by Mick Darling)
- Resolve YAML syntax errors in workflow (98f2294 by Mick Darling)
- Address code review feedback for workflow robustness (c89728c by Mick Darling)
- Update README compilation workflow to handle branch protection (def7d64 by Mick Darling)
- Add missing line break after L14 layer description (7a48412 by Mick Darling)
- Remove parenthetical from L14 to fix word wrapping (2dd18a1 by Mick Darling)
- Correct line break formatting in L14 description (d12f612 by Mick Darling)
- fix: Stop changelog automation infinite PR loop ([#53](https://github.com/DollhouseMCP/AILIS/pull/53) by @mickdarling)
- fix: Remove redundant Introduction link from navigation ([#51](https://github.com/DollhouseMCP/AILIS/pull/51) by @mickdarling)
- fix: Don't exclude root README.md from build ([#49](https://github.com/DollhouseMCP/AILIS/pull/49) by @mickdarling)
- fix: Resolve MkDocs strict mode build failures ([#45](https://github.com/DollhouseMCP/AILIS/pull/45) by @mickdarling)
- fix: Correct newline escaping in changelog automation ([#42](https://github.com/DollhouseMCP/AILIS/pull/42) by @mickdarling)

### 📚 Documentation

- Add session notes for changelog loop fix and site name update (3329050 by Mick Darling)
- Add full AILIS name to site header for clarity (#54) (7eb104e by Mick Darling)
- update session notes for link validation fix (ffcb635 by Mick Darling)
- Update changelog for v0.1.0 (#19) (2da82ea by github-actions[bot])
- add comprehensive session notes for link validation fix session (80bfe15 by Mick Darling)
- make AILIS framework neutral and objective (0c54bb1 by Mick Darling)
- address reviewer feedback - consolidate workflow and document config (71cd12f by Mick Darling)
- Add L8 to underserved layers analysis (41649de by Mick Darling)
- Enhance README with detailed layer breakdown (546ddf3 by Mick Darling)
- docs: Add full AILIS name to site header ([#54](https://github.com/DollhouseMCP/AILIS/pull/54) by @mickdarling)
- docs: Update changelog for v0.1.0 ([#19](https://github.com/DollhouseMCP/AILIS/pull/19) by @github-actions[bot])

### 🔄 Other Changes

- Revert "fix: Don't exclude root README.md from build" (85ec946 by Mick Darling)
- Fix validation issues with symlinked files (#40) (078083d by Mick Darling)
- Set up GitHub workflows for documentation website (#33) (21961a4 by Mick Darling)
- Fix failing tests in PR validation (#35) (4d7d407 by Mick Darling)
- Resolve YAML multiline string parsing errors and add validation infrastructure (#18) (9b1eddb by Mick Darling)
- Resolve YAML parsing errors in proposal-lifecycle (#16) (98e4b8f by Mick Darling)
- Repair workflow YAML syntax and permissions (#14) (23c8514 by Mick Darling)
- Resolve workflow failures for changelog and proposal lifecycle (#13) (1369691 by Mick Darling)
- Merge pull request #11 from DollhouseMCP/hotfix/link-validation (f74b875 by Mick Darling)
- Merge pull request #10 from DollhouseMCP/hotfix/readme-workflow-protection (f8659ba by Mick Darling)
- Initial AILIS Repository Setup (#1) (16486e2 by Mick Darling)
- Merge pull request #2 from DollhouseMCP/add-claude-github-actions-1756580443831 (553cc48 by Mick Darling)
- "Claude Code Review workflow" (89dd442 by Mick Darling)
- "Claude PR Assistant workflow" (b988e4f by Mick Darling)
- Initial repository setup for AILIS proposal (dbe8d5d by Mick Darling)
- Fix validation issues with symlinked files ([#40](https://github.com/DollhouseMCP/AILIS/pull/40) by @mickdarling)
- Set up GitHub workflows for documentation website ([#33](https://github.com/DollhouseMCP/AILIS/pull/33) by @mickdarling)
- Fix failing tests in PR validation ([#35](https://github.com/DollhouseMCP/AILIS/pull/35) by @mickdarling)
- Hotfix: Resolve workflow failures for changelog and proposal lifecycle ([#13](https://github.com/DollhouseMCP/AILIS/pull/13) by @mickdarling)
- Hotfix: README compilation workflow for branch protection ([#10](https://github.com/DollhouseMCP/AILIS/pull/10) by @mickdarling)
- Hotfix: Link validation configuration for relative paths ([#11](https://github.com/DollhouseMCP/AILIS/pull/11) by @mickdarling)
- Hotfix: Prevent changelog automation self-trigger loop ([#21](https://github.com/DollhouseMCP/AILIS/pull/21) by @mickdarling)
- Hotfix: Resolve YAML multiline string parsing errors and add validation infrastructure ([#18](https://github.com/DollhouseMCP/AILIS/pull/18) by @mickdarling)
- Hotfix: Resolve YAML parsing errors in proposal-lifecycle ([#16](https://github.com/DollhouseMCP/AILIS/pull/16) by @mickdarling)
- Hotfix: Repair workflow YAML syntax and permissions ([#14](https://github.com/DollhouseMCP/AILIS/pull/14) by @mickdarling)
- Initial AILIS Repository Setup ([#1](https://github.com/DollhouseMCP/AILIS/pull/1) by @mickdarling)
- Add Claude Code GitHub Workflow ([#2](https://github.com/DollhouseMCP/AILIS/pull/2) by @mickdarling)

### 👥 Contributors

- @Mick Darling
- @github-actions[bot]
- @mickdarling

## [Unreleased]

### Added

- Initial AILIS framework proposal (v0.1)
- 16-layer model for AI systems
- Core proposal documents:
  - AILIS Primer - Overview of the layer model
  - AILIS Cheat Sheet - Quick reference
  - Blog post draft explaining the concept
- Repository structure for community contributions
- Issue templates for proposals, feedback, and use cases
- Pull request template for proposal submissions
- Contribution guidelines with RFC-style workflow
- GitHub labels for proposal stages

### Changed

- Restructured repository to support proposal workflow
- Updated contributing guidelines with formal process

### Process

- Established 4-week minimum review period for proposals
- Set up branch protection for main branch
- Created directories for proposals, reference implementations, and case studies

## [0.1.0] - 2025-08-30

### Added

- Initial release of AILIS proposal
- Basic repository structure
- Core documentation

---

## Versioning Guidelines

- **Major versions (X.0.0)** - Significant changes to core layers or fundamental concepts
- **Minor versions (0.X.0)** - New proposals accepted, additions to framework
- **Patch versions (0.0.X)** - Clarifications, examples, documentation improvements

## How to Update

When making changes:

1. Add entry under `[Unreleased]`
2. Categorize as: Added, Changed, Deprecated, Removed, Fixed, Security
3. When releasing, move unreleased items to new version section
4. Tag release in git: `git tag -a v0.2.0 -m "Release version 0.2.0"`
