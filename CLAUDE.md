# Claude Code Project Guide for AILIS

Welcome Claude! This document provides essential context for working on the AILIS project.

## Project Overview
AILIS (AI Layer Interface Specification) is a **proposal** for a 16+ layer model to help understand and discuss AI system architectures. Think of it as an OSI model for AI systems. This is intentionally positioned as an exploration and conversation starter, NOT a prescriptive standard.

## Key Project Philosophy
- **Humble and exploratory** - We're asking questions, not providing all answers
- **Community-driven** - Every perspective is valuable, especially critiques
- **RFC-style process** - Formal enough for serious work, not bureaucratic
- **Open to alternatives** - We actively welcome competing ideas

## Important Documents to Review

### Core Proposals
- [`proposals/AILIS_Primer.md`](proposals/AILIS_Primer.md) - The main framework overview
- [`proposals/AILIS_Cheat_Sheet.md`](proposals/AILIS_Cheat_Sheet.md) - Quick reference

### Process Documentation
- [`CONTRIBUTING.md`](CONTRIBUTING.md) - RFC workflow and contribution process
- [`FEEDBACK.md`](FEEDBACK.md) - Areas where we need input

### Session History
- [`docs/session-notes/`](docs/session-notes/) - Historical development context
- Review recent sessions to understand project evolution

## Current Repository Structure
```
/proposals/         - Formal AILIS proposals (main content)
/reference/         - Code examples and implementations
/studies/           - Real-world case studies
/discussions/       - Community feedback and alternatives
/.github/           - Issue/PR templates
/docs/              - Additional documentation
  /session-notes/   - Development history
```

## Workflow Reminders

### Branch Strategy
- `main` - Protected, accepted proposals only
- `draft/[name]` - For new proposals
- `discussion/[topic]` - For exploratory work
- NO develop branch needed

### Creating Session Notes
When context gets low or significant work is completed:
1. Create new file: `docs/session-notes/session-notes-YYYY-MM-DD-brief-description.md`
2. Include:
   - Session overview and goals
   - Key decisions made
   - Technical implementation details
   - Challenges faced and solutions
   - Next steps identified
   - Context for future sessions

### Proposal Process
1. Ideas start as GitHub issues
2. Draft proposals on `draft/` branches
3. 4-week minimum review period
4. Community consensus determines acceptance

## Language & Tone Guidelines
- Use "might," "could," "perhaps" over "must," "should," "will"
- Frame as questions and explorations
- Acknowledge uncertainty explicitly
- Credit existing work and inspirations
- Avoid being prescriptive or authoritative

## Technical Standards

### Commit Messages
```
type: brief description

Longer explanation if needed.

Refs: #issue-number
```
Types: `proposal:`, `fix:`, `docs:`, `refactor:`, `test:`

### File Naming
- Proposals: `AILIS-XXX-description.md`
- Session notes: `session-notes-YYYY-MM-DD-description.md`
- Use kebab-case for file names

## Current Priorities
1. Building community engagement
2. Gathering real-world use cases
3. Refining the layer model based on feedback
4. Creating reference implementations
5. Maintaining humble, exploratory tone

## GitHub Configuration
- **Branch Protection**: 2 reviews required, admin bypass enabled
- **Labels**: Full taxonomy in CONTRIBUTING.md
- **Discussions**: Enabled for open conversation
- **Default Branch**: main

## Owner Context
- **Mick Darling** is the project originator
- Admin bypass is enabled so Mick can push emergency fixes
- Project emerged from Dollhouse MCP work but is now independent

## Common Tasks

### Starting a New Session
1. Review recent session notes
2. Check open issues and PRs
3. Review this CLAUDE.md for context
4. Create session notes at end

### Reviewing Proposals
1. Check against AILIS philosophy
2. Ensure humble/exploratory tone
3. Look for practical examples
4. Consider alternatives

### Handling Feedback
- Critical feedback is especially valuable
- Document alternatives thoroughly
- Update proposals based on consensus
- Preserve declined proposals with rationale

## Remember
This is a proposal to start conversations, not a standard to enforce compliance. Every session should maintain this humble, exploratory approach while still being technically rigorous and well-documented.

---
*Last updated: 2025-08-30*  
*This document should be updated as the project evolves*
