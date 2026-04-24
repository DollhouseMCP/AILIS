---
title: L0 - Facilities & Power
---

# L0 - Facilities & Power

L0 covers the physical substrate that makes AI systems possible: datacenters, power, cooling, physical security, network access, and site-level resilience. It may seem distant from model behavior, but large-scale AI architecture is increasingly constrained by energy, cooling, rack density, and regional availability.

<div class="ailis-layer-infographic lane-core" aria-label="L0 facilities and power infographic">
  <div><strong>L0</strong><span>Facilities & Power</span></div>
  <ol>
    <li>Power capacity</li>
    <li>Cooling and density</li>
    <li>Physical security</li>
    <li>Regional resilience</li>
  </ol>
</div>

## What belongs here

L0 is about conditions below the compute fabric. A GPU cluster, TPU pod, or inference appliance sits above this layer. The facility layer asks whether the site can physically supply, cool, secure, and connect the hardware that higher layers assume exists.

## Representative projects and organizations

| Project or organization | Why it might fit | Adjacent layers |
| --- | --- | --- |
| [Equinix AI-ready data centers](https://www.equinix.com/solutions/ai) | Colocation and interconnection infrastructure for AI deployments. | L1 compute fabric, L13 transport |
| [Vertiv liquid cooling](https://www.vertiv.com/en-us/solutions/liquid-cooling/) | Cooling systems that make dense accelerated compute practical. | L1 compute fabric |
| [Schneider Electric data center infrastructure](https://www.se.com/us/en/work/solutions/data-centers-and-networks/) | Power management, electrical infrastructure, and datacenter operations. | L0 facilities, L1 compute |
| [Crusoe Cloud](https://crusoe.ai/cloud/) | AI cloud infrastructure tied to energy-aware compute deployment. | L0 facilities, L1 compute |
| [Google data centers](https://www.google.com/about/datacenters/) | Large-scale facilities, energy, and sustainability work for AI and cloud services. | L0 facilities, L16 products |

## Boundary questions

- Does a project manage hardware resources, or does it manage the building and site-level infrastructure around them?
- Should carbon accounting and grid-aware scheduling remain in L0, or should they become a cross-cutting management plane?
- When a cloud provider abstracts facilities away, does AILIS still need to name this layer for architectural honesty?

## Signals to watch

- Rising rack density and liquid cooling adoption.
- Regional power constraints that affect model deployment.
- Energy-aware scheduling and carbon-sensitive placement becoming part of AI procurement.

## Links

- [Back to the primer layer](../../proposals/AILIS_Primer/#l0-facilities-power)
- [Next layer: L1 Compute Fabric](../l1-compute-fabric/)
