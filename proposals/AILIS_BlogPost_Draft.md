
# The AILIS Proposal: Could We Use a Network-Style Map for the AI Stack?

_By Mick Darling — Early draft for feedback_

---

## 1. Why We Need a Layer Model for AI

The AI space is exploding with tools, platforms, and frameworks. Everyone is building “AI agents,” “orchestration
layers,” or “foundational models,” but there's no shared mental map of **what sits where**, **what functions are
duplicated**, and **where the gaps and opportunities lie**.

Computer networking solved this decades ago with the **OSI model**: seven layers, each with clear boundaries, standard
interfaces, and protocols. If you say "Layer 3," everyone knows you're talking about IP addressing and routing—not about
transport reliability or application logic.

Could AI benefit from something similar? We're proposing **AILIS**, a granular, network-inspired way to think about the
AI ecosystem. This is a conversation starter, not a definitive answer.

---

## 2. The AILIS Proposal

The AILIS proposal suggests breaking down AI systems into **16 functional layers**, plus three **cross-cutting planes**
for control, management, and security. This framework might help clarify where a given product, tool, or protocol lives,
where standards could be useful, and where innovation opportunities exist.

### **L0 – Facilities & Power**

Physical datacenter infrastructure: power delivery, cooling, EMI shielding, physical security. _Think: data center
operators, colocation facilities, power management systems._

### **L1 – Compute Fabric**

GPUs, NPUs, TPUs, CPUs, memory hierarchies, network interconnects (PCIe, NVLink, InfiniBand). _Think: NVIDIA H100, AMD
MI300, Intel Gaudi._

### **L2 – System & Driver Runtime**

Vendor-specific runtime stacks for launching compute kernels and managing device memory. _Examples: CUDA, ROCm, Metal._

### **L3 – ML Graph & Compilation**

Compilers and runtimes that transform a model graph into efficient kernels. _Examples: PyTorch, TensorRT, XLA, ONNX
Runtime._

### **L4 – Numeric Representation & Quantization**

Data types (FP32, FP16, FP8, INT4), quantization and calibration pipelines, sparsity patterns. _Examples: INT4
quantization toolchains, SmoothQuant, AWQ._

### **L5 – Tokenization & Encoding**

Mapping bytes or multimodal inputs into token sequences. _Examples: BPE tokenizers, CLIP image encoders, speech
patchifiers._

### **L6 – Model Parameters & Architecture**

The trained model weights and architecture definitions. _Examples: GPT-4 weights, Llama models, Mixtral, Mistral,
Command R+._

### **L7 – Inference Engine & Decoding**

Running a forward pass on the model, speculative decoding, caching, beam search, streaming tokens. _Examples: vLLM,
Fireworks.ai, TensorRT-LLM._

### **L8 – Context Construction & Prompting**

Prompt templates, system instructions, few-shot examples, scratchpads. _Examples: LangChain prompt templates, Semantic
Kernel planners._

### **L9 – Knowledge Access & Retrieval**

Embedding stores, vector search, rerankers, grounding documents, citations. _Examples: Pinecone, Weaviate,
Elasticsearch, RAG pipelines._

### **L10 – Tool & Function Invocation**

Calling external capabilities—databases, APIs, code execution, calculators—via structured I/O. _Examples: MCP servers,
function calling APIs, ReAct tool frameworks._

### **L11 – Addressing & Service Discovery**

How models, tools, and services are named and found. _Analogy: DNS for AI._ Currently fragmented—each provider has its
own catalog.

### **L12 – Routing & Policy Forwarding**

Deciding **which model/tool route** to call given cost, latency, privacy, region, and evaluation feedback. _Think:
multi-provider routers, policy engines, orchestration planners._

### **L13 – Transport, Flow & Streaming**

The wire protocols that carry requests/responses, handle streaming tokens, retries, cancellations, multiplexed
sub-streams. _Examples: HTTP, gRPC, WebSockets—but lacking AI-specific semantics today._

### **L14 – Session, Identity & State**

Conversation state, memory layers (episodic, semantic, scratch), identity, tenancy isolation, scoped permissions,
per-session budgets.

### **L15 – Presentation, Safety & Schema Governance**

Output structuring (JSON, DSL), schema validation, input/output redaction, policy firewalls, jailbreak protection.

### **L16 – Application & Domain Logic**

User-facing apps, workflows, agent frameworks, product logic, human-in-the-loop reviews. _Examples: ChatGPT UI,
Perplexity, GitHub Copilot, Notion AI._

---

### Cross-Cutting Planes

- **Control Plane:** Configuration, policy, budgets, AB/canaries, capability catalogs.
- **Management & Observability Plane:** Telemetry, evaluation corpora, route→score→action→outcome logs, dashboards.
- **Security Plane:** mTLS, key management, data residency, PII classification.


---

## 3. Why This Model Matters

### 3.1 Clarifies Scope

AI vendors often claim to provide an "end-to-end platform." In reality, most products sit in **one or two layers**,
sometimes spanning adjacent layers. This model makes scope **explicit**.

### 3.2 Highlights Duplication

Layers **L6–L7** (foundation models and inference) are heavily duplicated: many players build yet another LLM host or
incremental model variant. Similarly, **L9 vector search** is crowded.

### 3.3 Exposes Gaps

Layers **L11–L14** are underdeveloped:

- No standard **addressing/discovery** (DNS for AI)
- Weak **multi-provider routers** (policy-aware, evaluation-aware)
- No open **transport semantics** for multiplexed streaming
- Fragmented **session, memory, and identity** handling


### 3.4 Guides Innovation

Entrepreneurs and architects can identify **white space**:

- Cross-provider **AIOS layers** that route, compose, and evaluate capabilities across models and tools.
- **Safety firewalls** that enforce schemas and policy across toolchains.
- **Portable capability tokens** for scoped, least-privilege access to models and tools.


---

## 4. How Might AILIS Be Used?

1. **Map your product or idea** to AILIS layers. What's primary, what's secondary?  
2. **Check duplication density**: is this layer crowded with competition?  
3. **Identify adjacent layers** you can connect to add differentiated value.  
4. **Communicate clearly** with teams, investors, customers: "We're a Layer 12–14 product, we don't build Layer 6
models."
5. **Contribute to open standards** where layers lack protocols (L11–L13 especially).


---

## 5. Closing Thoughts

AI is following the trajectory of networking: from monolithic, opaque stacks to modular, layered architectures with
**interoperability standards**. Today, boundaries are blurred, hype conflates layers, and duplication hides where real
innovation is needed.

The **AILIS proposal** is offered as a potential step toward shared language. It's intentionally imperfect and
incomplete, but it might help frame:

- **What is infrastructure vs. application logic**
- **What's vendor-specific vs. what should be standardized**
- **Where composable orchestration can deliver AGI-like behavior** without owning a frontier model.


Use it to ask better questions, design clearer systems, and build the missing protocols and layers that will define the
next era of AI.

---

_Feedback welcome: this draft is open for comments before publication._
