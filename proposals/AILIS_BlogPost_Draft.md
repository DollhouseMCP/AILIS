
# The AILIS Proposal: Could We Use a Network-Style Map for the AI Stack?

_By Mick Darling — Early draft for feedback_

---

## 1. Why We Need a Layer Model for AI

The AI space is exploding with tools, platforms, and frameworks. Everyone is building “AI agents,” “orchestration
layers,” or “foundational models,” but there’s no shared mental map of __what sits where__, __what functions are
duplicated__, and __where the gaps and opportunities lie__.

Computer networking solved this decades ago with the __OSI model__: seven layers, each with clear boundaries, standard
interfaces, and protocols. If you say “Layer 3,” everyone knows you’re talking about IP addressing and routing—not about
transport reliability or application logic.

Could AI benefit from something similar? We're proposing __AILIS__, a granular, network-inspired way to think about the
AI ecosystem. This is a conversation starter, not a definitive answer.

---

## 2. The AILIS Proposal

The AILIS proposal suggests breaking down AI systems into __16 functional layers__, plus three __cross-cutting planes__
for control, management, and security. This framework might help clarify where a given product, tool, or protocol lives,
where standards could be useful, and where innovation opportunities exist.

### __L0 – Facilities & Power__

Physical datacenter infrastructure: power delivery, cooling, EMI shielding, physical security. _Think: data center
operators, colocation facilities, power management systems._

### __L1 – Compute Fabric__

GPUs, NPUs, TPUs, CPUs, memory hierarchies, network interconnects (PCIe, NVLink, InfiniBand). _Think: NVIDIA H100, AMD
MI300, Intel Gaudi._

### __L2 – System & Driver Runtime__

Vendor-specific runtime stacks for launching compute kernels and managing device memory. _Examples: CUDA, ROCm, Metal._

### __L3 – ML Graph & Compilation__

Compilers and runtimes that transform a model graph into efficient kernels. _Examples: PyTorch, TensorRT, XLA, ONNX
Runtime._

### __L4 – Numeric Representation & Quantization__

Data types (FP32, FP16, FP8, INT4), quantization and calibration pipelines, sparsity patterns. _Examples: INT4
quantization toolchains, SmoothQuant, AWQ._

### __L5 – Tokenization & Encoding__

Mapping bytes or multimodal inputs into token sequences. _Examples: BPE tokenizers, CLIP image encoders, speech
patchifiers._

### __L6 – Model Parameters & Architecture__

The trained model weights and architecture definitions. _Examples: GPT-4 weights, Llama models, Mixtral, Mistral,
Command R+._

### __L7 – Inference Engine & Decoding__

Running a forward pass on the model, speculative decoding, caching, beam search, streaming tokens. _Examples: vLLM,
Fireworks.ai, TensorRT-LLM._

### __L8 – Context Construction & Prompting__

Prompt templates, system instructions, few-shot examples, scratchpads. _Examples: LangChain prompt templates, Semantic
Kernel planners._

### __L9 – Knowledge Access & Retrieval__

Embedding stores, vector search, rerankers, grounding documents, citations. _Examples: Pinecone, Weaviate,
Elasticsearch, RAG pipelines._

### __L10 – Tool & Function Invocation__

Calling external capabilities—databases, APIs, code execution, calculators—via structured I/O. _Examples: MCP servers,
function calling APIs, ReAct tool frameworks._

### __L11 – Addressing & Service Discovery__

How models, tools, and services are named and found. _Analogy: DNS for AI._ Currently fragmented—each provider has its
own catalog.

### __L12 – Routing & Policy Forwarding__

Deciding __which model/tool route__ to call given cost, latency, privacy, region, and evaluation feedback. _Think:
multi-provider routers, policy engines, orchestration planners._

### __L13 – Transport, Flow & Streaming__

The wire protocols that carry requests/responses, handle streaming tokens, retries, cancellations, multiplexed
sub-streams. _Examples: HTTP, gRPC, WebSockets—but lacking AI-specific semantics today._

### __L14 – Session, Identity & State__

Conversation state, memory layers (episodic, semantic, scratch), identity, tenancy isolation, scoped permissions,
per-session budgets.

### __L15 – Presentation, Safety & Schema Governance__

Output structuring (JSON, DSL), schema validation, input/output redaction, policy firewalls, jailbreak protection.

### __L16 – Application & Domain Logic__

User-facing apps, workflows, agent frameworks, product logic, human-in-the-loop reviews. _Examples: ChatGPT UI,
Perplexity, GitHub Copilot, Notion AI._

---

### Cross-Cutting Planes

- __Control Plane:__ Configuration, policy, budgets, AB/canaries, capability catalogs.
- __Management & Observability Plane:__ Telemetry, evaluation corpora, route→score→action→outcome logs, dashboards.
- __Security Plane:__ mTLS, key management, data residency, PII classification.


---

## 3. Why This Model Matters

### 3.1 Clarifies Scope

AI vendors often claim to provide an “end-to-end platform.” In reality, most products sit in __one or two layers__,
sometimes spanning adjacent layers. This model makes scope __explicit__.

### 3.2 Highlights Duplication

Layers __L6–L7__ (foundation models and inference) are heavily duplicated: many players build yet another LLM host or
incremental model variant. Similarly, __L9 vector search__ is crowded.

### 3.3 Exposes Gaps

Layers __L11–L14__ are underdeveloped:

- No standard __addressing/discovery__ (DNS for AI)
- Weak __multi-provider routers__ (policy-aware, evaluation-aware)
- No open __transport semantics__ for multiplexed streaming
- Fragmented __session, memory, and identity__ handling


### 3.4 Guides Innovation

Entrepreneurs and architects can identify __white space__:

- Cross-provider __AIOS layers__ that route, compose, and evaluate capabilities across models and tools.
- __Safety firewalls__ that enforce schemas and policy across toolchains.
- __Portable capability tokens__ for scoped, least-privilege access to models and tools.


---

## 4. How Might AILIS Be Used?

1. __Map your product or idea__ to AILIS layers. What's primary, what's secondary?  
2. __Check duplication density__: is this layer crowded with competition?  
3. __Identify adjacent layers__ you can connect to add differentiated value.  
4. __Communicate clearly__ with teams, investors, customers: “We’re a Layer 12–14 product, we don’t build Layer 6
models.”
5. __Contribute to open standards__ where layers lack protocols (L11–L13 especially).


---

## 5. Closing Thoughts

AI is following the trajectory of networking: from monolithic, opaque stacks to modular, layered architectures with
__interoperability standards__. Today, boundaries are blurred, hype conflates layers, and duplication hides where real
innovation is needed.

The __AILIS proposal__ is offered as a potential step toward shared language. It's intentionally imperfect and
incomplete, but it might help frame:

- __What is infrastructure vs. application logic__
- __What’s vendor-specific vs. what should be standardized__
- __Where composable orchestration can deliver AGI-like behavior__ without owning a frontier model.


Use it to ask better questions, design clearer systems, and build the missing protocols and layers that will define the
next era of AI.

---

_Feedback welcome: this draft is open for comments before publication._
