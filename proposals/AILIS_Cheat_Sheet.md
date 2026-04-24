# AILIS Cheat Sheet

<!-- markdownlint-disable MD013 -->

_A scannable field guide for the AI Layer Interface Specification._

AILIS is a proposed map for discussing AI systems. Use this page when you need to orient quickly, map a product, or ask
which layer a concern belongs to. For details and examples, open the [Layer Atlas](../layers/index.md).

## The stack in five regions

- [<span class="ailis-cheat-code">L0-L2</span><span>Infrastructure Foundation</span><span class="ailis-cheat-note">Facilities, compute fabric, driver/runtime substrate.</span>](../layers/index.md#infrastructure-foundation){ .lane-core }
  {: .ailis-cheat-region-item }
- [<span class="ailis-cheat-code">L3-L7</span><span>Model and Inference Stack</span><span class="ailis-cheat-note">Graphs, numbers, encoders, weights, serving.</span>](../layers/index.md#model-and-inference-stack){ .lane-research }
  {: .ailis-cheat-region-item }
- [<span class="ailis-cheat-code">L8-L10</span><span>AI Application Interface</span><span class="ailis-cheat-note">Prompts, retrieval, tools, typed invocation.</span>](../layers/index.md#ai-application-interface){ .lane-protocol }
  {: .ailis-cheat-region-item }
- [<span class="ailis-cheat-code">L11-L15</span><span>Orchestration Layers</span><span class="ailis-cheat-note">Registry, routing, flow, session, governance.</span>](../layers/index.md#orchestration-layers){ .lane-protocol }
  {: .ailis-cheat-region-item }
- [<span class="ailis-cheat-code">L16+</span><span>Application and Domain Logic</span><span class="ailis-cheat-note">Product workflow, domain behavior, user experience.</span>](../layers/index.md#application-and-domain-logic){ .lane-research }
  {: .ailis-cheat-region-item }

## Layer field card

- [<span class="ailis-cheat-code">L16</span><span>Application & Domain Logic</span><span class="ailis-cheat-note">Product UX, workflows, domain rules.</span>](../layers/l16-application-domain-logic.md){ .lane-research }
  {: .ailis-cheat-layer-item }
- [<span class="ailis-cheat-code">L15</span><span>Governance, Safety & Schema</span><span class="ailis-cheat-note">Validation, redaction, guardrails, audit.</span>](../layers/l15-governance-safety-schema.md){ .lane-protocol }
  {: .ailis-cheat-layer-item }
- [<span class="ailis-cheat-code">L14</span><span>Session, Identity & Memory</span><span class="ailis-cheat-note">Portable sessions, consent, capability tokens.</span>](../layers/l14-session-identity-memory.md){ .lane-protocol }
  {: .ailis-cheat-layer-item }
- [<span class="ailis-cheat-code">L13</span><span>Transport & Flow Semantics</span><span class="ailis-cheat-note">Streaming, cancel/resume, idempotency.</span>](../layers/l13-transport-flow-semantics.md){ .lane-protocol }
  {: .ailis-cheat-layer-item }
- [<span class="ailis-cheat-code">L12</span><span>Routing, Planning & Policy</span><span class="ailis-cheat-note">Provider choice, ensembles, budgets, privacy rules.</span>](../layers/l12-routing-planning-policy.md){ .lane-protocol }
  {: .ailis-cheat-layer-item }
- [<span class="ailis-cheat-code">L11</span><span>Addressing & Registry</span><span class="ailis-cheat-note">Discovery, manifests, fingerprints, capability metadata.</span>](../layers/l11-addressing-registry.md){ .lane-protocol }
  {: .ailis-cheat-layer-item }
- [<span class="ailis-cheat-code">L10</span><span>Tool & Function Invocation</span><span class="ailis-cheat-note">MCP, function calling, APIs, tool schemas.</span>](../layers/l10-tool-function-invocation.md){ .lane-protocol }
  {: .ailis-cheat-layer-item }
- [<span class="ailis-cheat-code">L9</span><span>Knowledge & Retrieval</span><span class="ailis-cheat-note">Vector and graph indexes, reranking, citations.</span>](../layers/l9-knowledge-retrieval.md){ .lane-protocol }
  {: .ailis-cheat-layer-item }
- [<span class="ailis-cheat-code">L8</span><span>Context Construction & Prompting</span><span class="ailis-cheat-note">System prompts, templates, context packing.</span>](../layers/l8-context-construction-prompting.md){ .lane-protocol }
  {: .ailis-cheat-layer-item }
- [<span class="ailis-cheat-code">L7</span><span>Inference Engine & Decoding</span><span class="ailis-cheat-note">Serving, batching, KV cache, token streaming.</span>](../layers/l7-inference-engine-decoding.md){ .lane-research }
  {: .ailis-cheat-layer-item }
- [<span class="ailis-cheat-code">L6</span><span>Model Parameters & Architecture</span><span class="ailis-cheat-note">Weights, adapters, model families.</span>](../layers/l6-model-parameters-architecture.md){ .lane-research }
  {: .ailis-cheat-layer-item }
- [<span class="ailis-cheat-code">L5</span><span>Tokenization & Encoders</span><span class="ailis-cheat-note">Text tokens, image/audio encoders, embeddings.</span>](../layers/l5-tokenization-encoders.md){ .lane-research }
  {: .ailis-cheat-layer-item }
- [<span class="ailis-cheat-code">L4</span><span>Numeric & Quantization</span><span class="ailis-cheat-note">Precision, sparsity, compression, calibration.</span>](../layers/l4-numeric-quantization.md){ .lane-research }
  {: .ailis-cheat-layer-item }
- [<span class="ailis-cheat-code">L3</span><span>ML Graph & Compilation</span><span class="ailis-cheat-note">IR, lowering, optimization, execution targets.</span>](../layers/l3-ml-graph-compilation.md){ .lane-research }
  {: .ailis-cheat-layer-item }
- [<span class="ailis-cheat-code">L2</span><span>System & Driver Runtime</span><span class="ailis-cheat-note">CUDA, ROCm, Metal, device memory.</span>](../layers/l2-system-driver-runtime.md){ .lane-core }
  {: .ailis-cheat-layer-item }
- [<span class="ailis-cheat-code">L1</span><span>Compute Fabric</span><span class="ailis-cheat-note">GPUs, TPUs, NPUs, CPUs, memory, interconnect.</span>](../layers/l1-compute-fabric.md){ .lane-core }
  {: .ailis-cheat-layer-item }
- [<span class="ailis-cheat-code">L0</span><span>Facilities & Power</span><span class="ailis-cheat-note">Datacenters, power, cooling, physical security.</span>](../layers/l0-facilities-power.md){ .lane-core }
  {: .ailis-cheat-layer-item }

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

- [AILIS Primer](AILIS_Primer.md)
- [Layer Atlas](../layers/index.md)
- [GitHub discussions](https://github.com/DollhouseMCP/AILIS/discussions)
