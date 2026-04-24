---
title: L2 - System & Driver Runtime
---

# L2 - System & Driver Runtime

L2 covers the runtime bridge between hardware and ML frameworks: drivers, kernel APIs, device memory management, container integration, scheduling hooks, and low-level libraries. It is where hardware becomes programmable by the rest of the stack.

<div class="ailis-layer-infographic lane-core" aria-label="L2 system and driver runtime infographic">
  <div><strong>L2</strong><span>System & Driver Runtime</span></div>
  <ol>
    <li>Drivers</li>
    <li>Kernel APIs</li>
    <li>Memory management</li>
    <li>Cluster scheduling hooks</li>
  </ol>
</div>

## What belongs here

L2 is lower than model graph compilation. It asks whether accelerated hardware can be addressed, scheduled, isolated, monitored, and shared safely by higher layers.

## Representative projects

| Project | Why it might fit | Adjacent layers |
| --- | --- | --- |
| [NVIDIA CUDA](https://docs.nvidia.com/cuda/) | Programming model, libraries, and runtime for NVIDIA GPU computing. | L1 GPUs, L3 compilation |
| [AMD ROCm](https://rocm.docs.amd.com/) | Open software stack for AMD GPU acceleration. | L1 accelerators, L3 frameworks |
| [Apple Metal](https://developer.apple.com/metal/) | Low-level graphics and compute API used by Apple silicon workloads. | L1 devices, L7 local inference |
| [Intel oneAPI](https://www.intel.com/content/www/us/en/developer/tools/oneapi/overview.html) | Cross-architecture programming model and toolkits. | L1 CPU/GPU, L3 compilation |
| [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html) | Kubernetes integration for GPU drivers, runtime components, and monitoring. | L2 runtime, L12 policy |

## Boundary questions

- Are scheduler plugins part of L2 because they expose devices, or L12 because they enforce placement policy?
- When a runtime library performs graph optimization, should it move up to L3?
- How should AILIS represent local-device inference where L1 and L2 are hidden inside the operating system?

## Signals to watch

- Better accelerator virtualization and multi-tenant isolation.
- Runtime support for confidential or attested AI workloads.
- Scheduling APIs that expose power, memory, and accelerator topology to higher layers.

## Links

- [Previous layer: L1 Compute Fabric](../l1-compute-fabric/)
- [Back to the primer layer](../../proposals/AILIS_Primer/#l2-system-driver-runtime)
- [Next layer: L3 ML Graph & Compilation](../l3-ml-graph-compilation/)
