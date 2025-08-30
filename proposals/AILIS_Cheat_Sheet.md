# AILIS Cheat Sheet (One-Pager)

**Purpose:** A crisp reference for the AI stack’s middle layers so teams can design, build, and talk about interoperable
systems.

```text
L16  Application & Domain Logic
L15  Governance, Safety & Schema
L14  Session, Identity & Memory
L13  Transport & Flow Semantics
L12  Routing, Planning & Policy
L11  Addressing & Registry
L10  Tool & Function Invocation
L9   Knowledge & Retrieval
L8   Context Construction & Prompting
L7   Inference Engine & Decoding
L6   Model Parameters & Architecture
L5   Tokenization & Encoders
L4   Numeric & Quantization
L3   ML Graph & Compilation
L2   System & Driver Runtime
L1   Compute Fabric
L0   Facilities & Power
```text

**Under‑served (biggest opportunities):** **L11–L15**.  
**Crowded:** L1–L7, L9.

- **L11 Registry:** signed manifests (models, tools, indices, **ensembles**), capability vectors, fingerprints.  
- **L12 Routing:** policy DSL + bandits; cascade/fan‑out/reducer; budgets & privacy classes.  
- **L13 Transport:** idempotent runs, streaming, **CANCEL/RESUME**, multiplex, mid‑stream grammar negotiation.  
- **L14 Session:** **Portable Session Envelope** (identity, budgets, memory refs, ensemble stack) + capability tokens.  
- **L15 Governance:** redaction, validation/repair; schema change control; approvals & audit.


**Core artifacts:** manifests • capability vectors • fingerprints • routing policies • session envelopes • audit logs.

**Design pattern:** route → execute → evaluate → adapt (closed loop).
