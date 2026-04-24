---
title: L1 - Compute Fabric
---

<!-- markdownlint-disable MD013 MD033 MD046 -->

# L1 - Compute Fabric

L1 covers the hardware substrate exposed to system software: GPUs, TPUs, NPUs, CPUs, memory hierarchy, accelerators, interconnects, and cluster topology. It is where AI capability becomes a physical allocation problem.

<div class="ailis-layer-infographic lane-core" aria-label="L1 compute fabric infographic">
  <div><strong>L1</strong><span>Compute Fabric</span></div>
  <ol>
    <li>Accelerators</li>
    <li>Memory</li>
    <li>Interconnect</li>
    <li>Topology</li>
  </ol>
</div>

## What belongs here

L1 is concerned with the compute resources themselves. It does not decide how a model is compiled, quantized, routed, or governed, but it strongly shapes what those upper layers can achieve.

## Representative projects and platforms

| Project or platform | Why it might fit | Adjacent layers |
| --- | --- | --- |
| [NVIDIA Blackwell](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/) | GPU architecture for large-scale training and inference systems. | L2 drivers, L3 compilation |
| [AMD Instinct](https://www.amd.com/en/products/accelerators/instinct.html) | Accelerator hardware used in AI and HPC deployments. | L2 ROCm, L7 serving |
| [Google Cloud TPU](https://cloud.google.com/tpu) | Tensor processing hardware exposed through Google Cloud. | L2 runtime, L3 XLA |
| [AWS Trainium and Inferentia](https://aws.amazon.com/machine-learning/trainium/) | Purpose-built AWS chips for model training and inference. | L2 runtime, L7 inference |
| [Cerebras Wafer-Scale Engine](https://www.cerebras.ai/chip/) | Wafer-scale AI compute that challenges typical cluster assumptions. | L1 compute, L3 compilation |
| [Groq LPU](https://groq.com/technology/) | Inference-oriented processing architecture with distinct latency tradeoffs. | L7 decoding, L12 routing |

## Boundary questions

- Should interconnect protocols such as NVLink or InfiniBand be modeled inside L1, or as part of L13 transport when they affect distributed inference semantics?
- When a cloud exposes "instances" rather than chips, should the layer describe the underlying fabric or the purchasable unit?
- How much model-specific acceleration belongs in hardware before it becomes an L3 or L7 concern?

## Signals to watch

- Specialized inference chips changing routing economics.
- Memory bandwidth becoming a stronger limiting factor than raw FLOPS.
- Compute providers exposing topology-aware placement APIs to application teams.

## Links

- [Previous layer: L0 Facilities & Power](l0-facilities-power.md)
- [Back to the primer layer](../proposals/AILIS_Primer.md#l1-compute-fabric)
- [Next layer: L2 System & Driver Runtime](l2-system-driver-runtime.md)
