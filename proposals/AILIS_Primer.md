# The AILIS Primer: A Proposed Layer Model for AI Systems

_Version 0.2 - Draft for Discussion - April 2026_

> **Proposal:** Could a shared layer vocabulary make AI systems easier to discuss, compare, evaluate, and improve?
> AILIS explores one possible 16+ layer map for the AI ecosystem. It is a research proposal and conversation starter,
> not a compliance standard.

AILIS is a Dollhouse Research project. It grew out of practical work with model providers, MCP tools, agent workflows,
retrieval systems, governance checks, and multi-step AI applications where the same words often mean different things to
different teams.

The short version: many AI diagrams compress everything into a few broad boxes: infrastructure, model, orchestration,
application. That can be useful, but it also hides the messy middle where interoperability problems show up. AILIS asks
whether a more granular map might help us notice those boundaries sooner.

## How this primer fits with the Atlas

This primer explains the proposal and the reasoning behind it. The
[AILIS Layer Atlas](../layers/index.md) gives each layer its own page with representative projects, boundary questions,
and links into the current ecosystem.

If you are new to AILIS, a good path might be:

1. Read this primer for the model and vocabulary.
2. Open the [Layer Atlas](../layers/index.md) when you want examples.
3. Keep the [Cheat Sheet](AILIS_Cheat_Sheet.md) nearby when mapping a product, protocol, or architecture.
4. Bring disagreements to the [GitHub discussion](https://github.com/DollhouseMCP/AILIS/discussions), especially when a
   layer feels blurry or incorrectly scoped.

## Why explore a layered AI stack?

AI systems are no longer just "a model plus an app." Even a relatively ordinary assistant can involve:

- accelerators and runtime stacks;
- model weights, quantization choices, and inference engines;
- prompt construction and retrieval;
- tool invocation protocols;
- provider routing and policy;
- streaming transport and cancellation;
- identity, memory, consent, and session continuity;
- governance, schema validation, redaction, and audit trails;
- a product workflow that users actually experience.

The AILIS proposal is not that every team must care about every layer. Instead, it suggests that teams might benefit
from naming the layer they are discussing before they argue about architecture, risk, cost, or standards.

## What a layer model is for

AILIS is most useful when it helps people separate concerns that are otherwise blended together. It is less useful if it
becomes a labeling exercise for its own sake.

A layer model can help ask:

- What is the system actually responsible for?
- Which concern is being hidden behind a product name or provider name?
- Where does data cross a boundary?
- Where does control move from one actor, tool, model, or service to another?
- Which part could be swapped out, standardized, audited, or governed independently?

AILIS is not trying to say that every project belongs in exactly one place. Most real projects span layers. The useful
move is to name the primary layer, the secondary layers, and the handoffs between them.

## How to read an AILIS layer

Each layer can be read through four questions:

| Question | What it reveals |
| --- | --- |
| What artifact lives here? | The tangible thing being produced, stored, invoked, routed, or governed. |
| What boundary does it expose? | The interface where another layer depends on it. |
| What evidence would prove it works? | Tests, benchmarks, traces, manifests, evaluations, audits, or examples. |
| What happens if it is missing? | The failure mode that gets pushed into application code or user experience. |

This is why the [Layer Atlas](../layers/index.md) contains examples and boundary questions rather than just definitions.
A layer becomes meaningful only when it helps explain a real system.

## The stack at a glance

AILIS currently groups the stack into five practical regions. The names and boundaries are open to revision.

| Region | Layers | What it helps separate |
| --- | --- | --- |
| Infrastructure foundation | [L0-L2](../layers/index.md#infrastructure-foundation) | Physical sites, compute fabric, driver/runtime substrate. |
| Model and inference stack | [L3-L7](../layers/index.md#model-and-inference-stack) | Graph compilation, numeric representation, encoders, model artifacts, serving. |
| AI application interface | [L8-L10](../layers/index.md#ai-application-interface) | Prompt/context construction, retrieval, tools, typed invocation. |
| Orchestration layers | [L11-L15](../layers/index.md#orchestration-layers) | Discovery, routing, transport, session, identity, memory, governance, schemas. |
| Application and domain logic | [L16+](../layers/index.md#application-and-domain-logic) | User-facing products, workflows, domain rules, review paths. |

## The layers

The layer summaries below are intentionally brief. Use the Atlas links for the richer version of each layer.

### L0 - Facilities & Power

Datacenters, power, cooling, physical security, and site-level resilience.

[Explore L0 in the Layer Atlas](../layers/l0-facilities-power.md)

### L1 - Compute Fabric

GPUs, TPUs, NPUs, CPUs, memory hierarchy, interconnects, and accelerator topology.

[Explore L1 in the Layer Atlas](../layers/l1-compute-fabric.md)

### L2 - System & Driver Runtime

CUDA, ROCm, Metal, device memory management, runtime libraries, and scheduling hooks.

[Explore L2 in the Layer Atlas](../layers/l2-system-driver-runtime.md)

### L3 - ML Graph & Compilation

Graph representation, compilation, lowering, optimization, and execution targets.

[Explore L3 in the Layer Atlas](../layers/l3-ml-graph-compilation.md)

### L4 - Numeric & Quantization

Precision choices, FP8/FP16/INT4, quantization, sparsity, calibration, and compression.

[Explore L4 in the Layer Atlas](../layers/l4-numeric-quantization.md)

### L5 - Tokenization & Encoders

Text tokenizers, image encoders, audio encoders, patching, embeddings, and modality conversion.

[Explore L5 in the Layer Atlas](../layers/l5-tokenization-encoders.md)

### L6 - Model Parameters & Architecture

Model weights, architectures, adapters, model families, release artifacts, and model metadata.

[Explore L6 in the Layer Atlas](../layers/l6-model-parameters-architecture.md)

### L7 - Inference Engine & Decoding

Serving runtimes, batching, KV cache, speculative decoding, streaming, and local or hosted inference.

[Explore L7 in the Layer Atlas](../layers/l7-inference-engine-decoding.md)

### L8 - Context Construction & Prompting

System prompts, templates, examples, context packing, instruction hierarchy, and prompt tests.

[Explore L8 in the Layer Atlas](../layers/l8-context-construction-prompting.md)

### L9 - Knowledge & Retrieval

Vector and graph indexes, hybrid retrieval, reranking, grounding, freshness, permissions, and citations.

[Explore L9 in the Layer Atlas](../layers/l9-knowledge-retrieval.md)

### L10 - Tool & Function Invocation

Typed tool calls, function calling, MCP-style capabilities, API bindings, and result handling.

[Explore L10 in the Layer Atlas](../layers/l10-tool-function-invocation.md)

### L11 - Addressing & Registry

Discovery, manifests, capability metadata, signatures, provenance, fingerprints, and registries.

[Explore L11 in the Layer Atlas](../layers/l11-addressing-registry.md)

### L12 - Routing, Planning & Policy

Provider routing, agent planning, ensemble selection, budgets, privacy rules, fallback, and evaluator feedback.

[Explore L12 in the Layer Atlas](../layers/l12-routing-planning-policy.md)

### L13 - Transport & Flow Semantics

Streaming, cancellation, resume tokens, idempotency, multiplexing, retries, and backpressure.

[Explore L13 in the Layer Atlas](../layers/l13-transport-flow-semantics.md)

### L14 - Session, Identity & Memory

Portable session state, identity, capability tokens, memory tiers, consent, continuity, and ownership.

[Explore L14 in the Layer Atlas](../layers/l14-session-identity-memory.md)

### L15 - Governance, Safety & Schema

Validation, redaction, schema conformance, guardrails, approvals, audit trails, and repair loops.

[Explore L15 in the Layer Atlas](../layers/l15-governance-safety-schema.md)

### L16 - Application & Domain Logic

Product UX, workflows, domain rules, agent frameworks, review paths, and the user's actual experience.

[Explore L16 in the Layer Atlas](../layers/l16-application-domain-logic.md)

## Cross-cutting planes

AILIS also uses three cross-cutting planes. These do not sit above or below the stack; they pass through it.

| Plane | What it asks |
| --- | --- |
| Control | What configuration, policy, budget, capability, or routing decision is being applied? |
| Management and observability | What telemetry, evaluation, trace, cost, quality, and outcome evidence is available? |
| Security | What trust boundary, authorization, privacy class, key, residency rule, or audit requirement applies? |

## Where the proposal sees pressure

The lower and middle model stack is crowded and fast-moving. L1-L7 and L9 have many strong projects, providers, and
frameworks. That does not make them solved, but they are visible and heavily funded.

The AILIS proposal pays special attention to L11-L15 because these layers often appear as ad hoc product code:

- registries that cannot describe tools, models, prompts, indices, and ensembles in one vocabulary;
- routers that select providers without enough evidence, budget, privacy, or outcome feedback;
- transports that stream tokens but do not always handle cancellation, resumability, or long-running tool work cleanly;
- sessions and memories that are difficult for users to inspect, move, consent to, or revoke;
- governance checks that are bolted onto applications instead of treated as shared infrastructure.

That middle may be where shared protocols and public research could be especially useful.

## A worked mapping example

Consider a research assistant that answers questions from private documents and can call approved tools.

| Concern | Likely AILIS layers |
| --- | --- |
| The hosted model and serving endpoint | L6-L7 |
| Prompt template and conversation instructions | L8 |
| Private document index, embeddings, reranker, citations | L9 |
| Approved calendar, file, and search tools | L10 |
| Catalog of which tools and document indices exist | L11 |
| Decision about local model vs. hosted model vs. specialist tool | L12 |
| Streaming answer with cancellable tool progress | L13 |
| User identity, memory policy, and session continuity | L14 |
| Redaction, output schema checks, audit trail, approval gates | L15 |
| The final assistant workflow and user experience | L16 |

The point is not that this mapping is final. The point is that the map lets a team discuss where a concern belongs. If
memory access fails, the team can ask whether the problem is retrieval, session ownership, identity, consent,
governance, or product UX instead of treating "memory" as one undifferentiated feature.

## What good might look like

AILIS is not prescribing one architecture. It is collecting questions that good architectures might answer.

### L11 - Addressing & Registry

Could models, tools, prompts, datasets, indices, and ensembles publish signed manifests with capability claims, evidence
links, version constraints, privacy classes, and deprecation state?

### L12 - Routing, Planning & Policy

Could routing decisions consider cost, latency, privacy, capability evidence, region, failure modes, and evaluator
feedback instead of only provider name and model ID?

### L13 - Transport & Flow Semantics

Could AI calls become resumable, cancellable, multiplexed, and stream-aware across providers, hosts, local tools, and
human approval pauses?

### L14 - Session, Identity & Memory

Could users and organizations carry session state, memory references, permissions, and privacy budgets across tools
without handing every application a private copy of everything?

### L15 - Governance, Safety & Schema

Could redaction, schema validation, output repair, policy checks, audit logs, and approvals become reusable parts of the
stack rather than application-by-application patches?

## How AILIS might be used

AILIS can be used lightly. A team does not need to adopt the whole model to get value from it.

1. **Map a system.** Identify the primary and secondary layers a project touches.
2. **Name the handoffs.** Ask where data, control, identity, policy, and responsibility cross boundaries.
3. **Spot duplication.** Notice when two tools solve the same layer while another layer is missing.
4. **Find risk.** Look for places where memory, tool access, schema validation, or routing policy is implicit.
5. **Invite critique.** Use unclear cases to improve the model rather than forcing the project to fit.

## FAQ

### Is AILIS trying to become a standard?

Not currently. It is a proposed map for discussion. Some layers might eventually inspire specifications, tests, or
reference implementations, but the first goal is shared language.

### Why so many layers?

Because many real interoperability problems disappear when the stack is compressed too far. AILIS may still have too
many, too few, or poorly named layers. The point of the proposal is to make those disagreements easier to discuss.

### Does this handle multimodal AI?

It tries to. Modalities show up most visibly in L5 encoders, L6 architectures, L8 context construction, L9 retrieval,
and L16 product behavior. The Atlas is a good place to test whether that treatment is strong enough.

### Is a project allowed to span layers?

Yes. Most real projects do. AILIS is more useful when it names primary and secondary layers than when it tries to force
everything into exactly one box.

## What is next?

- Keep expanding the [Layer Atlas](../layers/index.md) with examples, critiques, and competing placements.
- Draft deeper proposals for L11-L15, especially addressing, routing, transport, session, and governance.
- Explore a portable session envelope, capability manifests, and evidence-backed fingerprints.
- Invite vendors, researchers, builders, and skeptical users to test the model against real systems.

_Feedback welcome. The most useful critique is often a project that does not fit cleanly._
