# The AILIS Primer: A Proposed Layer Model for AI Systems

_Version 0.1 - Draft for Discussion • August 2025_

> **Proposal:** Could an OSI-style mental model help us better understand and discuss AI systems? This document explores
a possible 16+ layer framework for organizing our thinking about the AI stack.

---

## 0) Why explore a layered "AI stack" model?

Most diagrams compress AI into 4–7 broad boxes (infra → model → orchestration → app). This might hide what we're calling
the **under-served middle** where real interoperability challenges exist: **registry, routing, transport semantics,
session/identity, and governance**. The **AILIS** proposal explores whether more granular layers could help identify
these gaps.

- **Clarity:** Common vocabulary for planning and architectural reviews.
- **Interoperability:** Clear layer boundaries invite specs and conformance tests.
- **Strategy:** Spot duplication (crowded layers) and white space (under‑served layers).


---

## 1) The Layers (L0–L16)

We keep L0 for facility concerns and extend through L16 (Application). Cross‑cutting planes (Control,
Management/Observability, Security) apply across layers.

**L0 – Facilities & Power** — Datacenters, power/cooling, physical security.  
**L1 – Compute Fabric** — GPUs/TPUs/NPUs/CPUs, memory, interconnects.  
**L2 – System & Driver Runtime** — CUDA/ROCm/Metal; device memory management.  
**L3 – ML Graph & Compilation** — XLA/TVM/TensorRT‑LLM/ONNX Runtime.  
**L4 – Numeric & Quantization** — FP16/FP8/INT4, sparsity, calibration.  
**L5 – Tokenization & Encoders** — BPE tokenizers, CLIP, audio patchifiers.  
**L6 – Model Parameters & Architecture** — Base/foundation weights, MoE, diffusion.  
**L7 – Inference Engine & Decoding** — Serving runtimes, caching, speculative decoding.  
**L8 – Context Construction & Prompting** — System prompts, templates, few‑shot.  
**L9 – Knowledge & Retrieval** — Vector/graph indexes, rerankers, grounding, citations.  
**L10 – Tool & Function Invocation** — Typed tool I/O (MCP), function calling, API bindings.  
**L11 – Addressing & Registry** — Signed manifests, discovery, capability vectors, fingerprints.  
**L12 – Routing, Planning & Policy** — Rule DSL + bandits; budgets, privacy, fallback/parallel.  
**L13 – Transport & Flow Semantics** — Idempotent runs, streaming, CANCEL/RESUME, multiplex.  
**L14 – Session, Identity & Memory** — Portable session envelope, capability tokens, budgets; memory tiers.  
**L15 – Governance, Safety & Schema** — Redaction, validation/repair, schema change control, audit.  
**L16 – Application & Domain Logic** — Product UX, workflows, agent frameworks.

**Planes:** Control (policy/config), Management/Observability (telemetry/evals), Security (mTLS, keys, PII).

---

## 2) Where the market is crowded vs. empty

- **Crowded:** L1–L7 (compute, models, inference) and L9 (vector DBs).  
- **Under‑served:** **L11–L15** (registry, routing, transport semantics, session, governance). This is where


multi‑provider, privacy‑aware, cost‑aware AI breaks down today.

---

## 3) What good looks like at the middle layers

### L11 — Addressing & Registry

**Objective:** a portable, signed catalog for models, tools, indices, and **ensembles**.  
**Artifacts:** manifests, capability vectors, immutable fingerprints (benchmarks + environment descriptors).  
**APIs:** search/filter, publish/update, signature verification, evidence links.

### L12 — Routing, Planning & Policy

**Objective:** pick the **best plan** (single model/tool or **ensemble**) under cost/latency/privacy budgets.  
**Mechanics:** declarative rules + **bandit learning**; cascade/parallel/reducer; canary & rollback; evaluator feedback
loop.

### L13 — Transport & Flow Semantics

**Objective:** make AI calls **resumable, cancellable, multiplexed**, and stream‑aware across providers/hosts.  
**Verbs:** `OPEN`, `DATA`, `YIELD`, `NEGOTIATE*GRAMMAR`, `CANCEL`, `PAUSE`, `RESUME`, `CLOSE` + idempotency keys and
resume tokens.

### L14 — Session, Identity & Memory

**Objective:** continuity and **ownership** of context across providers.  
**Artifacts:** **Portable Session Envelope** (identity, budgets, privacy class, ensemble stack, memory refs) +
**capability tokens**.
**Memory tiers:** episodic (per thread), semantic (indices), scratch (structured workspaces).

### L15 — Governance, Safety & Schema

**Objective:** reduce risk without blocking productivity.  
**Mechanics:** input redaction; output validation/auto‑repair; **schema diffing** and deprecation windows; approvals &
audit.

---

## 4) Ensembles: composition as a first‑class citizen

Real systems compose **personas, prompts, templates, and skills**. Ensembles are **measured** (capability vectors) and
**selected** (routing policies) like any other capability. Evaluation must consider **interaction effects**—small
changes can have large behavioral consequences.

---

## 5) Evidence over hype: fingerprints & capability vectors

- **Fingerprint** = immutable record of (subject × platform × model‑version × env) performance: behavioral, performance,


robustness, safety, compatibility.

- **Capability vector** = compact features for routing decisions (reasoning, factuality, structure adherence,


latency/cost bands).

- **Loop:** route → score → action → outcome → update priors.


---

## 6) Security & privacy by design

- Privacy classes & residency in manifests; **privacy‑aware routing**.  
- Content‑free telemetry option; on‑device redaction in clients; short‑lived capability tokens.  
- For premium IP: attested runs, watermark/provenance, rights metering.


---

## 7) How might AILIS be used in your organization?

1. **Map products** to layers (primary/secondary).  
2. **Identify gaps** in L11–L15; pick standards to adopt/publish.  
3. **Instrument evaluation** and publish fingerprints to your registry.  
4. **Write routing policy** (start rules → evolve to bandits).  
5. **Govern schemas** and introduce a firewall before tool/model calls.


---

## 8) FAQ

- **Is AILIS meant to replace existing frameworks?** No. It's a **proposed map and a set of ideas for discussion**, not


a framework.

- **Why not fewer layers?** The missing interoperability happens precisely in the “extra” layers (L11–L15).  
- **Does it handle multi‑modal?** Yes—modalities live in manifests/fingerprints; layers remain the same.


---

## 9) What’s next

- Publish spec drafts for **L11–L15** and the **Portable Session Envelope**.  
- Provide **reference implementations** (registry server, router DSL engine, transport shim, session libraries).  
- Invite vendors and users to **contribute fingerprints** and **manifests**.


*Feedback welcome._
