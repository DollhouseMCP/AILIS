---
title: L16 - Application & Domain Logic
---

<!-- markdownlint-disable MD013 MD033 -->

# L16 - Application & Domain Logic

L16 covers the product, workflow, domain rules, user experience, business process, and application-specific value created on top of the lower layers. It is the part users usually experience directly.

<div class="ailis-layer-infographic lane-research" aria-label="L16 application and domain logic infographic">
  <div><strong>L16</strong><span>Application & Domain Logic</span></div>
  <ol>
    <li>Workflow</li>
    <li>Domain rules</li>
    <li>User experience</li>
    <li>Outcome ownership</li>
  </ol>
</div>

## What belongs here

L16 is where AI systems become products, copilots, agents, research workflows, internal tools, creative systems, or domain-specific applications. It is not less technical than lower layers; it simply asks different questions about usefulness, accountability, and fit.

## Representative products and domains

| Product or domain | Why it might fit | Adjacent layers |
| --- | --- | --- |
| [ChatGPT](https://openai.com/chatgpt/) | General AI assistant product built on model, tool, memory, and governance layers. | L8 context, L14 memory, L15 safety |
| [Claude](https://www.anthropic.com/claude) | Assistant product and API surface with model, tool, and safety behavior visible to users. | L10 tools, L15 safety |
| [Microsoft Copilot](https://www.microsoft.com/en-us/microsoft-copilot) | Product family embedding AI into productivity workflows. | L14 identity, L16 workflows |
| [GitHub Copilot](https://github.com/features/copilot) | Developer-assistance product with IDE, codebase, and workflow integration. | L9 retrieval, L10 tools |
| [Cursor](https://www.cursor.com/) | AI coding environment where application UX and domain workflow are central. | L8 context, L10 tools |
| [Perplexity](https://www.perplexity.ai/) | Answer and research product where retrieval, citations, and UX combine. | L9 retrieval, L16 product |
| [Harvey](https://www.harvey.ai/) | Domain-focused AI product for legal and professional services workflows. | L15 governance, L16 domain logic |

## Boundary questions

- When does an agent framework remain L12 orchestration, and when does it become an L16 application?
- How should domain expertise, evaluation, and human review be represented without hiding lower-layer dependencies?
- Are "copilots" a product pattern, a domain pattern, or a bundle of many lower layers?

## Signals to watch

- Domain-specific AI products developing their own evaluation and governance expectations.
- Application UX making lower-layer decisions visible through citations, approvals, memory controls, and tool traces.
- Organizations asking for stack-level transparency behind AI product behavior.

## Links

- [Previous layer: L15 Governance, Safety & Schema](l15-governance-safety-schema.md)
- [Back to the primer layer](../proposals/AILIS_Primer.md#l16-application-domain-logic)
- [Return to the Layer Atlas](../)
