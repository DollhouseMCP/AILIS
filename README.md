# AILIS: A Proposed Layer Model for AI Systems

*Version 0.1 - Early Draft for Discussion*

## What if we had a common language for the AI stack?

The AI ecosystem is evolving rapidly, with countless tools, platforms, and frameworks emerging daily. Yet we lack a shared mental model—a common way to discuss where different capabilities sit, how they interact, and where the gaps might be.

This repository contains **AILIS** (AI Layer Interface Specification), a proposal exploring whether a layered model—similar to the OSI model in networking—might help us better understand and discuss AI system architectures.

## Why explore this?

In networking, the OSI model gave us a shared vocabulary. When someone says "Layer 3," everyone understands we're discussing routing and addressing, not physical cables or application logic. 

Could something similar help in AI? We're not sure, but we think it's worth exploring together.

## The AILIS 16+ Proposal

We're proposing a 16-layer model (plus cross-cutting concerns) that attempts to map the AI stack from physical infrastructure up through application logic:

- **L0-L2**: Infrastructure and compute fabric
- **L3-L7**: Model compilation, quantization, and inference
- **L8-L10**: Context, knowledge, and tool invocation
- **L11-L15**: The "missing middle"—addressing, routing, transport, sessions, and governance
- **L16**: Application and domain logic

The proposal suggests that layers 11-15 might be particularly underserved in today's ecosystem, creating friction when building multi-provider, privacy-aware, cost-conscious AI systems.

## This is a conversation starter

**We don't claim to have all the answers.** This proposal is intentionally incomplete and likely wrong in places. We're sharing it early because we believe the best ideas emerge from open discussion.

We're particularly interested in:
- Does this framing resonate or feel forced?
- What's missing or miscategorized?
- Are there better ways to think about these boundaries?
- What existing work should we learn from?

## Explore the Proposal

- [📄 AILIS Primer](proposal/AILIS_Primer.md) - Overview of the layer model
- [🔍 Detailed Explorations](explorations/) - Deeper dives into specific layers
- [💭 Design Considerations](explorations/design/) - Our thinking on various architectural decisions
- [💬 Discussions](discussions/) - Community feedback and alternative approaches

## Join the Conversation

This is an open invitation to think together about how we might better organize our understanding of AI systems. Whether you're building infrastructure, developing applications, or researching new approaches, your perspective would be valuable.

### How to Contribute

- **Share your thoughts**: Open an issue with feedback, criticisms, or alternatives
- **Propose changes**: Submit PRs with improvements or corrections
- **Join discussions**: Participate in ongoing conversations about specific aspects
- **Share use cases**: Help us understand where this model works or breaks down

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details, and [FEEDBACK.md](FEEDBACK.md) for specific areas where we're seeking input.

## Context and Origins

This proposal emerges from work at [Dollhouse MCP](https://github.com/DollhouseMCP), where we've been building tools for AI persona management and composition. In trying to explain where our tools fit in the broader ecosystem, we found ourselves wishing for a clearer map.

Rather than create Yet Another Vendor Stack Diagram™, we wondered: could we contribute something more broadly useful?

## License

- Documentation and specifications: [CC-BY 4.0](LICENSE-DOCS)
- Code and examples: [Apache 2.0](LICENSE)

We chose these licenses to enable the widest possible collaboration and adoption, should any of these ideas prove useful.

## Status

**Early Draft** - This is version 0.1 of a proposal. Everything here is subject to change based on community feedback. We're not trying to create a standard—we're trying to start a useful conversation.

## Acknowledgments

This proposal draws inspiration from:
- The OSI network model
- The work of countless AI infrastructure teams
- Open specifications like OpenAPI and GraphQL
- The Model Context Protocol (MCP) community

---

*Questions? Thoughts? We'd love to hear from you. Open an issue or reach out through the Dollhouse MCP community channels.*