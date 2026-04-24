---
title: L3 - ML Graph & Compilation
---

<!-- markdownlint-disable MD013 MD033 -->

# L3 - ML Graph & Compilation

L3 covers graph representation, lowering, optimization, and compilation. This layer transforms model programs into forms that can execute efficiently on specific runtimes and hardware.

<div class="ailis-layer-infographic lane-core" aria-label="L3 graph and compilation infographic">
  <div><strong>L3</strong><span>ML Graph & Compilation</span></div>
  <ol>
    <li>Graph IR</li>
    <li>Operator fusion</li>
    <li>Lowering</li>
    <li>Runtime targets</li>
  </ol>
</div>

## What belongs here

L3 is not the model weights themselves, and it is not the serving engine. It is the translation layer that decides how a model computation graph can be represented, optimized, and mapped to execution backends.

## Representative projects

| Project | Why it might fit | Adjacent layers |
| --- | --- | --- |
| [ONNX Runtime](https://onnxruntime.ai/) | Runtime and tooling around the ONNX model representation and execution providers. | L3 graph, L7 inference |
| [OpenXLA XLA](https://openxla.org/xla) | Compiler technology for optimizing ML workloads across backends. | L2 runtime, L3 compilation |
| [Apache TVM](https://tvm.apache.org/) | Compiler stack for deep learning models across hardware targets. | L1 hardware, L3 compilation |
| [MLIR](https://mlir.llvm.org/) | Compiler infrastructure useful for representing and lowering domain-specific computations. | L3 graph, L4 numeric |
| [TensorRT-LLM](https://nvidia.github.io/TensorRT-LLM/) | Optimization and runtime path for LLM inference on NVIDIA platforms. | L3 compilation, L7 serving |
| [OpenVINO](https://docs.openvino.ai/) | Toolkit for optimizing and deploying AI inference across Intel hardware. | L3 optimization, L7 inference |

## Boundary questions

- Does an inference framework belong in L3 when its main value is compilation, and L7 when its main value is serving?
- Should model exchange formats be separated from compiler execution backends?
- How should the layer handle dynamic agent graphs that are not pure tensor graphs?

## Signals to watch

- More attention to portable intermediate representations for AI workloads.
- Compiler support for speculative decoding, mixture-of-experts routing, and sparse computation.
- Cross-vendor pressure for optimization paths that do not lock models to one accelerator family.

## Links

- [Previous layer: L2 System & Driver Runtime](l2-system-driver-runtime.md)
- [Back to the primer layer](../proposals/AILIS_Primer.md#l3-ml-graph-compilation)
- [Next layer: L4 Numeric & Quantization](l4-numeric-quantization.md)
