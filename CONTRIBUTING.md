# Contributing to AILIS

Thank you for your interest in contributing to the AILIS proposal! This is an early-stage exploration, and we genuinely value all perspectives—whether supportive, critical, or offering alternatives.

## Quick Start

1. **Have an idea?** Open an issue using our templates
2. **Want to discuss?** Join the GitHub Discussions
3. **Ready to propose?** Follow the proposal workflow below

## Contribution Types

### 📝 Proposals
Formal additions or changes to the AILIS framework
- Use the "AILIS Proposal" issue template
- Create a `draft/proposal-name` branch
- Submit PR with detailed documentation
- Participate in 4-week review period

### 💬 Feedback
Critiques, concerns, or suggestions
- Use the "Feedback or Critique" issue template
- No formal process required - just share your thoughts
- Critical feedback is especially valuable

### 🔍 Use Cases
Real-world examples and case studies
- Use the "Use Case Submission" issue template
- Help us understand where AILIS works (or doesn't)
- Can be developed into full case studies

### 🛠 Reference Implementations
Code, schemas, and tools
- Submit to `/reference` directory
- Include clear documentation
- Keep examples minimal and focused

## The Proposal Workflow

### 1. Pre-Proposal Discussion
- Open an issue to discuss your idea
- Get community feedback
- Refine the concept

### 2. Draft Phase
```bash
# Create your proposal branch
git checkout -b draft/your-proposal-name

# Add your proposal document
proposals/AILIS-XXX-your-proposal.md
```

Proposal document should include:
- **Summary** - Brief overview (2-3 sentences)
- **Motivation** - Why is this needed?
- **Detailed Proposal** - Full specification
- **Alternatives** - Other approaches considered
- **Compatibility** - Impact on existing concepts
- **Open Questions** - Areas needing input

### 3. Review Phase (4 weeks minimum)
- Submit PR with `stage/draft` label
- Community provides feedback via PR reviews
- Iterate based on feedback
- Must remain in review for at least 4 weeks

### 4. Final Comment Period
- Label changes to `stage/final-comment`
- Last call for community input (1 week)
- Address any final concerns

### 5. Decision
- Maintainers and community reach consensus
- Proposal is either:
  - **Accepted** - Merged to main
  - **Declined** - Closed with rationale preserved

## Git Workflow

### Branches
- `main` - Accepted proposals only (protected)
- `draft/[proposal-name]` - Individual proposals
- `discussion/[topic]` - Exploratory work

### Branch Protection Rules (main)
- **Required PR reviews**: 2 approvals minimum
- **Dismiss stale reviews**: Enabled
- **Require conversation resolution**: Yes
- **Admin bypass**: Available for emergency fixes
- **No direct pushes**: All changes via PR

### Commit Messages
```
type: brief description

Longer explanation if needed.

Refs: #issue-number
```

Types: `proposal:`, `fix:`, `docs:`, `refactor:`, `test:`

Examples:
```
proposal: Add L17 for domain-specific reasoning

Introduces new layer for vertical AI applications
like medical diagnosis and legal research.

Refs: #42
```

```
docs: Clarify L11 registry manifest format

Adds JSON schema example and explains
version compatibility requirements.

Refs: #15
```

### Pull Requests
- Use the PR template
- Link related issues
- Be responsive to feedback
- Squash commits when merging

## Review Guidelines

### For Authors
- Be open to feedback and iteration
- Respond to reviews promptly
- Update proposals based on consensus
- Document rationale for decisions

### For Reviewers
- Focus on constructive critique
- Consider multiple perspectives
- Suggest specific improvements
- Respect different viewpoints

### Review Criteria
- **Clarity** - Is it understandable?
- **Motivation** - Is it needed?
- **Compatibility** - Does it fit with AILIS?
- **Completeness** - Are edge cases considered?
- **Simplicity** - Could it be simpler?

## Label Taxonomy

### Proposal Stages
- `stage/draft` - Proposal is under development
- `stage/review` - Open for community review (4 weeks)
- `stage/final-comment` - Last call for feedback
- `stage/accepted` - Proposal has been accepted
- `stage/declined` - Proposal will not proceed

### Content Types
- `proposal` - New proposal for AILIS
- `feedback` - Feedback or critique
- `use-case` - Real-world use case or example
- `alternative` - Alternative approach or design
- `breaking-change` - This change breaks compatibility

## Community Guidelines

### The Spirit of Contribution
We're exploring how to better understand AI systems. Your contribution might be:
- **Questions** that challenge assumptions
- **Critiques** highlighting problems
- **Alternatives** suggesting better approaches
- **Examples** testing the model
- **Clarifications** improving accessibility
- **Connections** to existing work

### Code of Conduct
- Be respectful and inclusive
- Welcome diverse perspectives
- Focus on ideas, not individuals
- Accept constructive criticism gracefully
- Help others contribute

## Getting Help

- **Questions?** Open a discussion
- **Stuck?** Ask in your PR/issue
- **Ideas?** Share them freely

## Recognition

All contributors will be acknowledged. Significant contributions may be invited to join as maintainers.

## License

By contributing, you agree that your contributions will be licensed under:
- Documentation: CC-BY 4.0
- Code: Apache 2.0

---

Remember: This is a proposal, not a standard. We're learning together, and every perspective helps improve our understanding.
