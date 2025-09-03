# AILIS: A Proposed Layer Model for AI Systems

*Version 0.1 - Early Draft for Discussion*

<!-- Workflow Status Badges -->
[![🔗 Link Validation](https://github.com/DollhouseMCP/AILIS/actions/workflows/link-validation.yml/badge.svg)](https://github.com/DollhouseMCP/AILIS/actions/workflows/link-validation.yml)
[![📝 Markdown Linting](https://github.com/DollhouseMCP/AILIS/actions/workflows/markdown-lint.yml/badge.svg)](https://github.com/DollhouseMCP/AILIS/actions/workflows/markdown-lint.yml)
[![📚 Spell Check](https://github.com/DollhouseMCP/AILIS/actions/workflows/spell-check.yml/badge.svg)](https://github.com/DollhouseMCP/AILIS/actions/workflows/spell-check.yml)
[![♿ Accessibility Check](https://github.com/DollhouseMCP/AILIS/actions/workflows/accessibility-check.yml/badge.svg)](https://github.com/DollhouseMCP/AILIS/actions/workflows/accessibility-check.yml)
[![📋 Proposal Lifecycle](https://github.com/DollhouseMCP/AILIS/actions/workflows/proposal-lifecycle.yml/badge.svg)](https://github.com/DollhouseMCP/AILIS/actions/workflows/proposal-lifecycle.yml)

## What if we had a common language for the AI stack?

The AI ecosystem is evolving rapidly, with countless tools, platforms, and frameworks emerging daily. Yet we lack a shared mental model—a common way to discuss where different capabilities sit, how they interact, and where the gaps might be.

This repository contains **AILIS** (AI Layer Interface Specification), a proposal exploring whether a layered model—similar to the OSI model in networking—might help us better understand and discuss AI system architectures.

## Why explore this?

In networking, the OSI model gave us a shared vocabulary. When someone says "Layer 3," everyone understands we're discussing routing and addressing, not physical cables or application logic. 

Could something similar help in AI? We're not sure, but we think it's worth exploring together.

## The AILIS 16+ Proposal

We're proposing a 16-layer model (plus cross-cutting concerns) that attempts to map the AI stack from physical infrastructure up through application logic:

### Infrastructure Foundation (L0-L2)
- **L0 – Facilities & Power**: Datacenters, power/cooling, physical security
- **L1 – Compute Fabric**: GPUs/TPUs/NPUs/CPUs, memory, interconnects  
- **L2 – System & Driver Runtime**: CUDA/ROCm/Metal, device memory management

### Model & Inference Stack (L3-L7)
- **L3 – ML Graph & Compilation**: XLA/TVM/TensorRT-LLM/ONNX Runtime
- **L4 – Numeric & Quantization**: FP16/FP8/INT4, sparsity, calibration
- **L5 – Tokenization & Encoders**: BPE tokenizers, CLIP, audio patchifiers
- **L6 – Model Parameters & Architecture**: Base/foundation weights, MoE, diffusion
- **L7 – Inference Engine & Decoding**: Serving runtimes, caching, speculative decoding

### AI Application Interface (L8-L10)
- **L8 – Context Construction & Prompting**: System prompts, templates, few-shot
- **L9 – Knowledge & Retrieval**: Vector/graph indexes, rerankers, grounding, citations
- **L10 – Tool & Function Invocation**: Typed tool I/O (MCP), function calling, API bindings

### The Orchestration Layers (L11-L15)
- **L11 – Addressing & Registry**: Signed manifests, discovery, capability vectors, fingerprints
- **L12 – Routing, Planning & Policy**: Rule DSL + bandits, budgets, privacy, fallback/parallel
- **L13 – Transport & Flow Semantics**: Idempotent runs, streaming, CANCEL/RESUME, multiplex
- **L14 – Session, Identity & Memory**: Portable session envelope, capability tokens, memory tiers
- **L15 – Governance, Safety & Schema**: Redaction, validation/repair, schema change control, audit

### Application Layer (L16)
- **L16 – Application & Domain Logic**: Product UX, workflows, agent frameworks

### Cross-Cutting Planes
- **Control**: Policy/configuration management
- **Management/Observability**: Telemetry, evaluations, monitoring
- **Security**: mTLS, key management, PII protection

## This is a conversation starter

**We don't claim to have all the answers.** This proposal is intentionally incomplete and likely wrong in places. We're sharing it early because we believe the best ideas emerge from open discussion.

We're particularly interested in:
- Does this framing resonate or feel forced?
- What's missing or miscategorized?
- Are there better ways to think about these boundaries?
- What existing work should we learn from?

## Explore the Proposal

- [📄 AILIS Primer](proposals/AILIS_Primer.md) - Overview of the layer model
- [📋 Quick Reference](proposals/AILIS_Cheat_Sheet.md) - One-page summary
- [📝 All Proposals](proposals/) - Current and upcoming proposals
- [🔬 Reference Implementations](reference/) - Code examples and tools
- [📊 Case Studies](studies/) - Real-world system mappings
- [💬 Discussions](https://github.com/DollhouseMCP/AILIS/discussions) - Community feedback and alternatives

## Join the Conversation

This is an open invitation to think together about how we might better organize our understanding of AI systems. Whether you're building infrastructure, developing applications, or researching new approaches, your perspective would be valuable.

### How to Contribute

We follow an RFC-style process for proposals:

1. **💡 Have an idea?** Open an issue to discuss
2. **📝 Ready to propose?** Create a `draft/your-proposal` branch
3. **👀 Get feedback** During 4-week review period
4. **✅ Reach consensus** Proposal accepted or declined with rationale

Quick ways to help:
- **Share feedback** - Use our issue templates
- **Submit use cases** - Show us real-world examples
- **Propose alternatives** - Challenge our assumptions
- **Review proposals** - Help evaluate new ideas

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full process, and [FEEDBACK.md](FEEDBACK.md) for specific areas where we're seeking input.

## Context and Origins

This proposal emerges from practical experience building AI tools and observing the challenges of interoperability in the current ecosystem. We found ourselves wishing for a clearer map to understand how different capabilities relate to each other.

Rather than create Yet Another Stack Diagram™, we wondered: could we contribute something more broadly useful to the community?

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

*Questions? Thoughts? We'd love to hear from you. Open an issue to start a discussion.*
