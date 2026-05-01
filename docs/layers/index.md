---
title: Layer Atlas
---

<!-- markdownlint-disable MD013 MD033 -->

# AILIS Layer Atlas

The atlas is a working map of projects, protocols, services, and research areas that fit within the AILIS layer model. It is intentionally incomplete: each page is meant to help contributors test whether the layer boundaries are useful, too broad, too narrow, or missing important vocabulary.

The primer keeps the model short. These pages give each layer enough room for examples, adjacent concerns, open questions, and source links. The atlas below follows the same bands used on the home page, but presents them vertically so the stack reads from physical foundations up through products and domain behavior.

<div class="ailis-atlas-stack" aria-label="AILIS layer atlas grouped by stack region">
  <section id="infrastructure-foundation" class="ailis-atlas-group lane-core">
    <div class="ailis-atlas-group-context">
      <strong>L0-L2</strong>
      <h2>Infrastructure Foundation</h2>
      <p>Where the AI system becomes physical: facilities, accelerators, drivers, runtimes, and the operational substrate that upper layers assume is available. The current public Dollhouse Research portfolio has little visible differentiation here.</p>
    </div>
    <ol>
      <li><a href="l0-facilities-power/"><strong>L0</strong><span>Facilities & Power</span><em>Datacenters, power, cooling, site resilience.</em></a></li>
      <li><a href="l1-compute-fabric/"><strong>L1</strong><span>Compute Fabric</span><em>GPUs, TPUs, NPUs, CPUs, memory, interconnect.</em></a></li>
      <li><a href="l2-system-driver-runtime/"><strong>L2</strong><span>System & Driver Runtime</span><em>CUDA, ROCm, Metal, device memory, scheduling hooks.</em></a></li>
    </ol>
  </section>

  <section id="model-and-inference-stack" class="ailis-atlas-group lane-research">
    <div class="ailis-atlas-group-context">
      <strong>L3-L7</strong>
      <h2>Model and Inference Stack</h2>
      <p>Where learned capability is represented, transformed, optimized, and served. This is one of the most mature and heavily populated areas of the ecosystem, and it is mostly upstream of the current public Dollhouse Research portfolio.</p>
    </div>
    <ol>
      <li><a href="l3-ml-graph-compilation/"><strong>L3</strong><span>ML Graph & Compilation</span><em>XLA, TVM, TensorRT-LLM, ONNX Runtime.</em></a></li>
      <li><a href="l4-numeric-quantization/"><strong>L4</strong><span>Numeric & Quantization</span><em>Precision, compression, sparsity, calibration.</em></a></li>
      <li><a href="l5-tokenization-encoders/"><strong>L5</strong><span>Tokenization & Encoders</span><em>Text tokens, image encoders, audio representations.</em></a></li>
      <li><a href="l6-model-parameters-architecture/"><strong>L6</strong><span>Model Parameters & Architecture</span><em>Weights, model families, adapters, release artifacts.</em></a></li>
      <li><a href="l7-inference-engine-decoding/"><strong>L7</strong><span>Inference Engine & Decoding</span><em>Serving, batching, KV cache, streaming outputs.</em></a></li>
    </ol>
  </section>

  <section id="ai-application-interface" class="ailis-atlas-group lane-protocol">
    <div class="ailis-atlas-group-context">
      <strong>L8-L10</strong>
      <h2>AI Application Interface</h2>
      <p>Where model capability meets application context: prompts, retrieved knowledge, tool schemas, and the typed boundary between generated text and outside action. This is where the public Dollhouse Research portfolio starts to become visibly opinionated, through examples such as DollhouseMCP personas and skills, Dollhouse Collection discovery, and MCP-AQL tool semantics.</p>
    </div>
    <ol>
      <li><a href="l8-context-construction-prompting/"><strong>L8</strong><span>Context Construction & Prompting</span><em>System prompts, templates, examples, context packing.</em></a></li>
      <li><a href="l9-knowledge-retrieval/"><strong>L9</strong><span>Knowledge & Retrieval</span><em>Vector indexes, grounding, rerankers, citations.</em></a></li>
      <li><a href="l10-tool-function-invocation/"><strong>L10</strong><span>Tool & Function Invocation</span><em>MCP, function calling, APIs, tool result handling.</em></a></li>
    </ol>
  </section>

  <section id="orchestration-layers" class="ailis-atlas-group lane-protocol">
    <div class="ailis-atlas-group-context">
      <strong>L11-L15</strong>
      <h2>Orchestration Layers</h2>
      <p>The under-served middle of the proposal: registries, routing, transport, session continuity, identity, memory, governance, and schema controls. The current public Dollhouse Research portfolio is especially useful here because several of its strongest differentiators live in this band, including MCP-AQL introspection and routing work, DollhouseMCP approvals and memory, and generator validation.</p>
    </div>
    <ol>
      <li><a href="l11-addressing-registry/"><strong>L11</strong><span>Addressing & Registry</span><em>Manifests, discovery, fingerprints, capability metadata.</em></a></li>
      <li><a href="l12-routing-planning-policy/"><strong>L12</strong><span>Routing, Planning & Policy</span><em>Provider routing, ensemble selection, budgets, fallback.</em></a></li>
      <li><a href="l13-transport-flow-semantics/"><strong>L13</strong><span>Transport & Flow Semantics</span><em>Streaming, cancellation, resume, idempotency, flow control.</em></a></li>
      <li><a href="l14-session-identity-memory/"><strong>L14</strong><span>Session, Identity & Memory</span><em>Portable sessions, capability tokens, memory tiers, consent.</em></a></li>
      <li><a href="l15-governance-safety-schema/"><strong>L15</strong><span>Governance, Safety & Schema</span><em>Validation, redaction, guardrails, audit, schema repair.</em></a></li>
    </ol>
  </section>

  <section id="application-and-domain-logic" class="ailis-atlas-group lane-research">
    <div class="ailis-atlas-group-context">
      <strong>L16+</strong>
      <h2>Application and Domain Logic</h2>
      <p>Where the stack becomes useful to people: products, workflows, domain rules, review paths, and the actual experience of the system. Many public Dollhouse Research projects are most legible here because this is where people actually touch them, especially Dollhouse Collection, Elemental Surveys, Merview, and the user-facing surface of DollhouseMCP.</p>
    </div>
    <ol>
      <li><a href="l16-application-domain-logic/"><strong>L16</strong><span>Application & Domain Logic</span><em>Product UX, workflows, agent frameworks, domain behavior.</em></a></li>
    </ol>
  </section>
</div>

## How to read these pages

- **Representative projects** are not endorsements or definitive placement decisions. They are examples that make the layer concrete, including the public Dollhouse Research portfolio where it contributes real signal.
- **Adjacent layers** show where boundaries are blurry. Many real systems span multiple layers.
- **Boundary questions** are prompts for contributors: if a project does not fit cleanly, the model may need revision.
- **Signals to watch** are ecosystem changes that might make the layer more important, less useful, or differently shaped.

## Starting points

- [Return to the AILIS Primer](../proposals/AILIS_Primer.md)
- [Open the AILIS Cheat Sheet](../proposals/AILIS_Cheat_Sheet.md)
- [Join the GitHub discussion](https://github.com/DollhouseMCP/AILIS/discussions)
