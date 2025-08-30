# AILIS Cheat Sheet (One-Pager)

__Purpose:__ A crisp reference for the AI stack’s middle layers so teams can design, build, and talk about interoperable
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

__Under‑served (biggest opportunities):__ __L11–L15__.  
__Crowded:__ L1–L7, L9.

- __L11 Registry:__ signed manifests (models, tools, indices, __ensembles__), capability vectors, fingerprints.  
- __L12 Routing:__ policy DSL + bandits; cascade/fan‑out/reducer; budgets & privacy classes.  
- __L13 Transport:__ idempotent runs, streaming, __CANCEL/RESUME__, multiplex, mid‑stream grammar negotiation.  
- __L14 Session:__ __Portable Session Envelope__ (identity, budgets, memory refs, ensemble stack) + capability tokens.  
- __L15 Governance:__ redaction, validation/repair; schema change control; approvals & audit.


__Core artifacts:__ manifests • capability vectors • fingerprints • routing policies • session envelopes • audit logs.

__Design pattern:__ route → execute → evaluate → adapt (closed loop).
