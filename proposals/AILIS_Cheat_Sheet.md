# AILIS Cheat Sheet

_A scannable field guide for the AI Layer Interface Specification._

AILIS is a proposed map for discussing AI systems. Use this page when you need to orient quickly, map a product, or ask
which layer a concern belongs to. For details and examples, open the [Layer Atlas](../../layers/).

## The stack in five regions

<div class="ailis-cheat-regions" aria-label="AILIS stack regions">
  <a class="lane-core" href="../../layers/#infrastructure-foundation"><strong>L0-L2</strong><span>Infrastructure Foundation</span><em>Facilities, compute fabric, driver/runtime substrate.</em></a>
  <a class="lane-research" href="../../layers/#model-and-inference-stack"><strong>L3-L7</strong><span>Model and Inference Stack</span><em>Graphs, numbers, encoders, weights, serving.</em></a>
  <a class="lane-protocol" href="../../layers/#ai-application-interface"><strong>L8-L10</strong><span>AI Application Interface</span><em>Prompts, retrieval, tools, typed invocation.</em></a>
  <a class="lane-protocol" href="../../layers/#orchestration-layers"><strong>L11-L15</strong><span>Orchestration Layers</span><em>Registry, routing, flow, session, governance.</em></a>
  <a class="lane-research" href="../../layers/#application-and-domain-logic"><strong>L16+</strong><span>Application and Domain Logic</span><em>Product workflow, domain behavior, user experience.</em></a>
</div>

## Layer field card

<div class="ailis-cheat-layer-list" aria-label="AILIS layer field card">
  <a href="../../layers/l16-application-domain-logic/"><strong>L16</strong><span>Application & Domain Logic</span><em>Product UX, workflows, domain rules.</em></a>
  <a href="../../layers/l15-governance-safety-schema/"><strong>L15</strong><span>Governance, Safety & Schema</span><em>Validation, redaction, guardrails, audit.</em></a>
  <a href="../../layers/l14-session-identity-memory/"><strong>L14</strong><span>Session, Identity & Memory</span><em>Portable sessions, consent, capability tokens.</em></a>
  <a href="../../layers/l13-transport-flow-semantics/"><strong>L13</strong><span>Transport & Flow Semantics</span><em>Streaming, cancel/resume, idempotency.</em></a>
  <a href="../../layers/l12-routing-planning-policy/"><strong>L12</strong><span>Routing, Planning & Policy</span><em>Provider choice, ensembles, budgets, privacy rules.</em></a>
  <a href="../../layers/l11-addressing-registry/"><strong>L11</strong><span>Addressing & Registry</span><em>Discovery, manifests, fingerprints, capability metadata.</em></a>
  <a href="../../layers/l10-tool-function-invocation/"><strong>L10</strong><span>Tool & Function Invocation</span><em>MCP, function calling, APIs, tool schemas.</em></a>
  <a href="../../layers/l9-knowledge-retrieval/"><strong>L9</strong><span>Knowledge & Retrieval</span><em>Vector and graph indexes, reranking, citations.</em></a>
  <a href="../../layers/l8-context-construction-prompting/"><strong>L8</strong><span>Context Construction & Prompting</span><em>System prompts, templates, context packing.</em></a>
  <a href="../../layers/l7-inference-engine-decoding/"><strong>L7</strong><span>Inference Engine & Decoding</span><em>Serving, batching, KV cache, token streaming.</em></a>
  <a href="../../layers/l6-model-parameters-architecture/"><strong>L6</strong><span>Model Parameters & Architecture</span><em>Weights, adapters, model families.</em></a>
  <a href="../../layers/l5-tokenization-encoders/"><strong>L5</strong><span>Tokenization & Encoders</span><em>Text tokens, image/audio encoders, embeddings.</em></a>
  <a href="../../layers/l4-numeric-quantization/"><strong>L4</strong><span>Numeric & Quantization</span><em>Precision, sparsity, compression, calibration.</em></a>
  <a href="../../layers/l3-ml-graph-compilation/"><strong>L3</strong><span>ML Graph & Compilation</span><em>IR, lowering, optimization, execution targets.</em></a>
  <a href="../../layers/l2-system-driver-runtime/"><strong>L2</strong><span>System & Driver Runtime</span><em>CUDA, ROCm, Metal, device memory.</em></a>
  <a href="../../layers/l1-compute-fabric/"><strong>L1</strong><span>Compute Fabric</span><em>GPUs, TPUs, NPUs, CPUs, memory, interconnect.</em></a>
  <a href="../../layers/l0-facilities-power/"><strong>L0</strong><span>Facilities & Power</span><em>Datacenters, power, cooling, physical security.</em></a>
</div>

## Fast mapping questions

When evaluating a project, ask:

| Question | Why it matters |
| --- | --- |
| What is the primary layer? | Prevents "platform" or "agent" from hiding the real function. |
| Which adjacent layers does it include? | Finds bundled assumptions and integration risk. |
| What handoff does it define? | Clarifies data, control, identity, policy, or trust boundaries. |
| What would break if this layer were swapped out? | Reveals lock-in and missing interfaces. |
| Is this solving a layer problem or a product problem? | Keeps infrastructure research distinct from application UX. |

## Under-served middle

AILIS currently treats **L11-L15** as the most important open area:

| Layer | Core question |
| --- | --- |
| L11 Addressing & Registry | What exists, which version is it, and what evidence supports its claims? |
| L12 Routing, Planning & Policy | Which model, tool, provider, or ensemble should run under the current constraints? |
| L13 Transport & Flow Semantics | Can work stream, pause, cancel, resume, retry, and report progress reliably? |
| L14 Session, Identity & Memory | Who is acting, what context is portable, and what memory may be used? |
| L15 Governance, Safety & Schema | What must be redacted, validated, repaired, approved, logged, or blocked? |

## Core artifacts

| Artifact | Likely layer |
| --- | --- |
| Signed model, tool, prompt, or index manifest | L11 |
| Capability vector or fingerprint | L11-L12 |
| Routing policy or planner graph | L12 |
| Resume token or idempotency key | L13 |
| Portable session envelope | L14 |
| Memory reference with consent metadata | L14-L15 |
| Output schema, validator, or repair loop | L15 |
| Audit log tying prompt, model, tool, identity, and output together | L14-L15 |

## Useful links

- [AILIS Primer](../AILIS_Primer/)
- [Layer Atlas](../../layers/)
- [GitHub discussions](https://github.com/DollhouseMCP/AILIS/discussions)
