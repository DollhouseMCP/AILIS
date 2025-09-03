# AILIS (AI Layer Interface Specification)

{{ project_description }}

## 📊 Project Status

{{ workflow_badges }}

{{ project_stats }}

<!-- TOC_START -->
<!-- TOC_END -->

## 📋 Current Proposals

{{ proposal_listing }}

## 🤝 Contributing

{{ contributing_info }}

## 📚 Documentation

{{ documentation_links }}

## 🎯 Project Goals

AILIS aims to provide a shared mental model for the AI ecosystem, similar to how the OSI model helps us understand networking. Our goals:

- **Clarity**: Common vocabulary for planning and architectural reviews
- **Interoperability**: Clear layer boundaries invite specs and conformance tests  
- **Strategy**: Spot duplication (crowded layers) and white space (under-served layers)
- **Community**: Foster collaboration and discussion around AI system architecture

## 🏗️ The AILIS 16+ Layer Model

We're proposing a 16-layer model (plus cross-cutting concerns) that attempts to map the AI stack from physical infrastructure up through application logic:

### Infrastructure Foundation (L0-L2)
- **L0 – Facilities & Power**: Datacenters, power/cooling, physical security
- **L1 – Compute Fabric**: GPUs/TPUs/NPUs/CPUs, memory, interconnects  
- **L2 – System & Driver Runtime**: CUDA/ROCm/Metal, device memory management

### Model & Inference Stack (L3-L7)
- **L3 – ML Graph & Compilation**: XLA/TVM/TensorRT-LLM/ONNX Runtime
- **L4 – Numeric & Quantization**: FP16/FP8/INT4, sparsity, calibration
- **L5 – Tokenization & Encoders**: BPE tokenizers, CLIP, audio patchifiers
- **L6 – Model Parameters & Architecture**: Base/foundation weights, MoE, diffusion
- **L7 – Inference Engine & Decoding**: Serving runtimes, caching, speculative decoding

### AI Application Interface (L8-L10)
- **L8 – Context Construction & Prompting**: System prompts, templates, few-shot
- **L9 – Knowledge & Retrieval**: Vector/graph indexes, rerankers, grounding, citations
- **L10 – Tool & Function Invocation**: Typed tool I/O (MCP), function calling, API bindings

### The "Missing Middle" (L8, L11-L15) - *Underserved Today*
- **L8 – Context Construction & Prompting**: System prompts, templates, few-shot *(haphazard for enterprises)*
- **L11 – Addressing & Registry**: Signed manifests, discovery, capability vectors, fingerprints
- **L12 – Routing, Planning & Policy**: Rule DSL + bandits, budgets, privacy, fallback/parallel
- **L13 – Transport & Flow Semantics**: Idempotent runs, streaming, CANCEL/RESUME, multiplex
- **L14 – Session, Identity & Memory**: Portable session envelope, capability tokens, memory tiers
- **L15 – Governance, Safety & Schema**: Redaction, validation/repair, schema change control, audit

### Application Layer (L16)
- **L16 – Application & Domain Logic**: Product UX, workflows, agent frameworks

### Cross-Cutting Planes
- **Control**: Policy/configuration management
- **Management/Observability**: Telemetry, evaluations, monitoring
- **Security**: mTLS, key management, PII protection

The proposal suggests that **layers L8 and L11-L15 are particularly underserved** in today's ecosystem. L8 (Context Construction & Prompting) is handled haphazardly by most organizations, while L11-L15 create friction when building multi-provider, privacy-aware, cost-conscious AI systems.

For additional details, see the [AILIS Primer](proposals/AILIS_Primer.md).

---

{{ footer }}