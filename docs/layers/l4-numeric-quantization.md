---
title: L4 - Numeric & Quantization
---

# L4 - Numeric & Quantization

L4 covers numeric formats, quantization, sparsity, calibration, precision tradeoffs, and compression strategies. This layer often determines whether a model is feasible to run in a given cost, memory, latency, or device envelope.

<div class="ailis-layer-infographic lane-core" aria-label="L4 numeric and quantization infographic">
  <div><strong>L4</strong><span>Numeric & Quantization</span></div>
  <ol>
    <li>Precision</li>
    <li>Compression</li>
    <li>Calibration</li>
    <li>Quality tradeoffs</li>
  </ol>
</div>

## What belongs here

L4 is where architecture becomes arithmetic. It describes how tensors are represented and transformed, and how those choices affect quality, speed, cost, memory, and compatibility.

## Representative projects

| Project | Why it might fit | Adjacent layers |
| --- | --- | --- |
| [bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) | Quantization and optimizer tooling commonly used in transformer workflows. | L4 numeric, L6 models |
| [llama.cpp GGUF](https://github.com/ggml-org/llama.cpp) | Local inference ecosystem with quantized model formats and CPU/GPU execution paths. | L4 quantization, L7 inference |
| [AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ) | GPTQ quantization tooling for transformer models. | L4 quantization, L6 weights |
| [AutoAWQ](https://github.com/casper-hansen/AutoAWQ) | Activation-aware quantization tooling for LLM deployment. | L4 quantization, L7 serving |
| [NVIDIA TensorRT quantization](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html#working-with-quantized-types) | Production optimization path for lower-precision inference on NVIDIA platforms. | L3 compilation, L7 inference |
| [vLLM quantization support](https://docs.vllm.ai/en/latest/features/quantization/) | Serving-time support for quantized model variants. | L4 numeric, L7 serving |

## Boundary questions

- Should quantized model files be treated as L4 artifacts, L6 model artifacts, or both?
- When quantization is integrated into a serving engine, is the concern still separable?
- How should AILIS represent accuracy, safety, and governance changes caused by numeric choices?

## Signals to watch

- Wider use of FP8, INT4, and mixed-precision inference.
- Quantization becoming part of model release metadata.
- Evaluation suites that treat quantization as a behavioral change rather than a pure optimization.

## Links

- [Previous layer: L3 ML Graph & Compilation](../l3-ml-graph-compilation/)
- [Back to the primer layer](../../proposals/AILIS_Primer/#l4-numeric-quantization)
- [Next layer: L5 Tokenization & Encoders](../l5-tokenization-encoders/)
