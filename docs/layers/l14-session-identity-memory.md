---
title: L14 - Session, Identity & Memory
---

# L14 - Session, Identity & Memory

L14 covers portable session state, user and agent identity, capability tokens, memory tiers, consent, continuity, and ownership of context across tools and providers. It is one of the places where AI systems most visibly touch human trust.

<div class="ailis-layer-infographic lane-protocol" aria-label="L14 session identity and memory infographic">
  <div><strong>L14</strong><span>Session, Identity & Memory</span></div>
  <ol>
    <li>Session envelope</li>
    <li>Identity</li>
    <li>Memory tiers</li>
    <li>Consent</li>
  </ol>
</div>

## What belongs here

L14 asks who or what is acting, what context is portable, what memory can be used, which permissions apply, and how continuity is preserved across providers or sessions.

## Representative projects and standards

| Project or standard | Why it might fit | Adjacent layers |
| --- | --- | --- |
| [Letta](https://docs.letta.com/) | Agent memory and state management inspired by MemGPT concepts. | L14 memory, L12 planning |
| [Zep](https://help.getzep.com/) | Memory layer for AI agents and assistants. | L14 memory, L9 retrieval |
| [mem0](https://docs.mem0.ai/) | Memory infrastructure for personalized AI applications. | L14 memory, L16 applications |
| [LangGraph memory](https://langchain-ai.github.io/langgraph/concepts/memory/) | Short-term and long-term memory concepts in graph-based agents. | L12 planning, L14 memory |
| [OAuth 2.0](https://oauth.net/2/) | Authorization framework relevant to delegated access and capability tokens. | L14 identity, L15 governance |
| [W3C Verifiable Credentials](https://www.w3.org/TR/vc-data-model-2.0/) | Standardized credential model that may inform portable identity and claims. | L14 identity, L11 registry |

## Boundary questions

- What belongs in a portable session envelope, and what should stay application-local?
- Should memory be treated as retrieval infrastructure, user-owned state, or both?
- How can identity and authorization travel across model providers, tools, and agent hosts without leaking private context?

## Signals to watch

- Agent memory products becoming independent infrastructure rather than application features.
- Stronger consent and inspection models for long-term memory.
- Capability-token patterns being adapted for AI tool access.

## Links

- [Previous layer: L13 Transport & Flow Semantics](../l13-transport-flow-semantics/)
- [Back to the primer layer](../../proposals/AILIS_Primer/#l14-session-identity-memory)
- [Next layer: L15 Governance, Safety & Schema](../l15-governance-safety-schema/)
