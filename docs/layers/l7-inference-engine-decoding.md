---
title: L7 - Inference Engine & Decoding
---

<!-- markdownlint-disable MD013 MD033 MD046 -->

# L7 - Inference Engine & Decoding

L7 covers model serving, batching, KV cache management, decoding algorithms, speculative execution, streaming output, and deployment runtime choices. This layer turns model artifacts into live responses.

<div class="ailis-layer-infographic lane-research" aria-label="L7 inference engine and decoding infographic">
  <div><strong>L7</strong><span>Inference Engine & Decoding</span></div>
  <ol>
    <li>Serving</li>
    <li>Batching</li>
    <li>KV cache</li>
    <li>Decoding</li>
  </ol>
</div>

## What belongs here

L7 is not the model itself and not the application policy that chooses among providers. It is the runtime that executes the model and shapes latency, throughput, cost, and response mechanics.

## Representative projects

| Project | Why it might fit | Adjacent layers |
| --- | --- | --- |
| [vLLM](https://docs.vllm.ai/) | LLM serving engine focused on efficient inference and memory management. | L7 serving, L4 quantization |
| [SGLang](https://docs.sglang.ai/) | Serving and programming system for language model applications. | L7 inference, L8 prompting |
| [Text Generation Inference](https://huggingface.co/docs/text-generation-inference/) | Hugging Face serving stack for text generation models. | L7 serving, L6 models |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local inference runtime with broad model and quantization support. | L4 quantization, L7 inference |
| [Ollama](https://ollama.com/) | Local model runner and packaging workflow for developer-facing inference. | L7 inference, L16 applications |
| [Ray Serve](https://docs.ray.io/en/latest/serve/) | Scalable serving framework for ML models and Python applications. | L7 serving, L12 routing |

## Boundary questions

- When a serving layer exposes OpenAI-compatible APIs, is that L7 execution or L13 transport semantics?
- Should decoding policies such as temperature, top-p, and speculative decoding be modeled here or in L8 context construction?
- How should AILIS classify local-first runtimes that include model discovery and application UX?

## Signals to watch

- KV cache reuse becoming a core optimization primitive.
- Speculative decoding and multi-model inference affecting routing economics.
- Local inference becoming good enough to influence privacy and governance architecture.

## Links

- [Previous layer: L6 Model Parameters & Architecture](l6-model-parameters-architecture.md)
- [Back to the primer layer](../proposals/AILIS_Primer.md#l7-inference-engine-decoding)
- [Next layer: L8 Context Construction & Prompting](l8-context-construction-prompting.md)
