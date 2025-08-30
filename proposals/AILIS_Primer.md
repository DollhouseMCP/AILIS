# The AILIS Primer: A Proposed Layer Model for AI Systems

_Version 0.1 - Draft for Discussion • August 2025_

> __Proposal:__ Could an OSI-style mental model help us better understand and discuss AI systems? This document explores
a possible 16+ layer framework for organizing our thinking about the AI stack.

---

## 0) Why explore a layered "AI stack" model?

Most diagrams compress AI into 4–7 broad boxes (infra → model → orchestration → app). This might hide what we're calling
the __under-served middle__ where real interoperability challenges exist: __registry, routing, transport semantics,
session/identity, and governance__. The __AILIS__ proposal explores whether more granular layers could help identify
these gaps.

- __Clarity:__ Common vocabulary for planning and architectural reviews.
- __Interoperability:__ Clear layer boundaries invite specs and conformance tests.
- __Strategy:__ Spot duplication (crowded layers) and white space (under‑served layers).


---

## 1) The Layers (L0–L16)

We keep L0 for facility concerns and extend through L16 (Application). Cross‑cutting planes (Control,
Management/Observability, Security) apply across layers.

__L0 – Facilities & Power__ — Datacenters, power/cooling, physical security.  
__L1 – Compute Fabric__ — GPUs/TPUs/NPUs/CPUs, memory, interconnects.  
__L2 – System & Driver Runtime__ — CUDA/ROCm/Metal; device memory management.  
__L3 – ML Graph & Compilation__ — XLA/TVM/TensorRT‑LLM/ONNX Runtime.  
__L4 – Numeric & Quantization__ — FP16/FP8/INT4, sparsity, calibration.  
__L5 – Tokenization & Encoders__ — BPE tokenizers, CLIP, audio patchifiers.  
__L6 – Model Parameters & Architecture__ — Base/foundation weights, MoE, diffusion.  
__L7 – Inference Engine & Decoding__ — Serving runtimes, caching, speculative decoding.  
__L8 – Context Construction & Prompting__ — System prompts, templates, few‑shot.  
__L9 – Knowledge & Retrieval__ — Vector/graph indexes, rerankers, grounding, citations.  
__L10 – Tool & Function Invocation__ — Typed tool I/O (MCP), function calling, API bindings.  
__L11 – Addressing & Registry__ — Signed manifests, discovery, capability vectors, fingerprints.  
__L12 – Routing, Planning & Policy__ — Rule DSL + bandits; budgets, privacy, fallback/parallel.  
__L13 – Transport & Flow Semantics__ — Idempotent runs, streaming, CANCEL/RESUME, multiplex.  
__L14 – Session, Identity & Memory__ — Portable session envelope, capability tokens, budgets; memory tiers
(episodic/semantic/scratch).
__L15 – Governance, Safety & Schema__ — Redaction, validation/repair, schema change control, audit.  
__L16 – Application & Domain Logic__ — Product UX, workflows, agent frameworks.

__Planes:__ Control (policy/config), Management/Observability (telemetry/evals), Security (mTLS, keys, PII).

---

## 2) Where the market is crowded vs. empty

- __Crowded:__ L1–L7 (compute, models, inference) and L9 (vector DBs).  
- __Under‑served:__ __L11–L15__ (registry, routing, transport semantics, session, governance). This is where
multi‑provider, privacy‑aware, cost‑aware AI breaks down today.


---

## 3) What good looks like at the middle layers

### L11 — Addressing & Registry

__Objective:__ a portable, signed catalog for models, tools, indices, and __ensembles__.  
__Artifacts:__ manifests, capability vectors, immutable fingerprints (benchmarks + environment descriptors).  
__APIs:__ search/filter, publish/update, signature verification, evidence links.

### L12 — Routing, Planning & Policy

__Objective:__ pick the __best plan__ (single model/tool or __ensemble__) under cost/latency/privacy budgets.  
__Mechanics:__ declarative rules + __bandit learning__; cascade/parallel/reducer; canary & rollback; evaluator feedback
loop.

### L13 — Transport & Flow Semantics

__Objective:__ make AI calls __resumable, cancellable, multiplexed__, and stream‑aware across providers/hosts.  
__Verbs:__ `OPEN`, `DATA`, `YIELD`, `NEGOTIATE_GRAMMAR`, `CANCEL`, `PAUSE`, `RESUME`, `CLOSE` + idempotency keys and
resume tokens.

### L14 — Session, Identity & Memory

__Objective:__ continuity and __ownership__ of context across providers.  
__Artifacts:__ __Portable Session Envelope__ (identity, budgets, privacy class, ensemble stack, memory refs) +
__capability tokens__.
__Memory tiers:__ episodic (per thread), semantic (indices), scratch (structured workspaces).

### L15 — Governance, Safety & Schema

__Objective:__ reduce risk without blocking productivity.  
__Mechanics:__ input redaction; output validation/auto‑repair; __schema diffing__ and deprecation windows; approvals &
audit.

---

## 4) Ensembles: composition as a first‑class citizen

Real systems compose __personas, prompts, templates, and skills__. Ensembles are __measured__ (capability vectors) and
__selected__ (routing policies) like any other capability. Evaluation must consider __interaction effects__—small
changes can have large behavioral consequences.

---

## 5) Evidence over hype: fingerprints & capability vectors

- __Fingerprint__ = immutable record of (subject × platform × model‑version × env) performance: behavioral, performance,
robustness, safety, compatibility.
- __Capability vector__ = compact features for routing decisions (reasoning, factuality, structure adherence,
latency/cost bands).
- __Loop:__ route → score → action → outcome → update priors.


---

## 6) Security & privacy by design

- Privacy classes & residency in manifests; __privacy‑aware routing__.  
- Content‑free telemetry option; on‑device redaction in clients; short‑lived capability tokens.  
- For premium IP: attested runs, watermark/provenance, rights metering.


---

## 7) How might AILIS be used in your organization?

1. __Map products__ to layers (primary/secondary).  
2. __Identify gaps__ in L11–L15; pick standards to adopt/publish.  
3. __Instrument evaluation__ and publish fingerprints to your registry.  
4. __Write routing policy__ (start rules → evolve to bandits).  
5. __Govern schemas__ and introduce a firewall before tool/model calls.


---

## 8) FAQ

- __Is AILIS meant to replace existing frameworks?__ No. It's a __proposed map and a set of ideas for discussion__, not
a framework.
- __Why not fewer layers?__ The missing interoperability happens precisely in the “extra” layers (L11–L15).  
- __Does it handle multi‑modal?__ Yes—modalities live in manifests/fingerprints; layers remain the same.


---

## 9) What’s next

- Publish spec drafts for __L11–L15__ and the __Portable Session Envelope__.  
- Provide __reference implementations__ (registry server, router DSL engine, transport shim, session libraries).  
- Invite vendors and users to __contribute fingerprints__ and __manifests__.


_Feedback welcome._
