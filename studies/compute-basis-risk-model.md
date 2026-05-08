---
title: A Layered Basis Risk Model for Compute Capacity
description: Draft analytical model for quality-adjusted compute exposure using AILIS layers.
---

<!-- markdownlint-disable MD013 -->

# A Layered Basis Risk Model for Compute Capacity

This draft proposes a modeling frame for compute exposure. It is intentionally simple enough to be criticized. The goal is not to define the correct compute unit, but to show how a layered model might expose mismatches that a raw GPU-hour view can hide.

## Working Definition

Compute basis risk is the mismatch between the compute exposure a buyer, lender, insurer, or operator actually has and the compute exposure represented by a contract, index, hedge, budget, or headline.

A buyer might hedge H100 rental rates and still remain exposed to HBM supply, power delays, region-specific latency, software compatibility, or a model-efficiency shock. The hedge might be economically useful, but it is not the whole exposure.

## Quality-Adjusted Compute Unit

A possible starting abstraction:

```text
QACU =
  raw_gpu_hours
  * utilization_factor
  * performance_factor
  * availability_factor
  * locality_factor
  * policy_factor
  * settlement_factor
```

Where:

| Factor | AILIS anchors | What it captures |
| --- | --- | --- |
| `raw_gpu_hours` | L1 | Quantity of accelerator time before adjustment. |
| `utilization_factor` | L2-L3, L10-L12 | Scheduler efficiency, batch shape, prefill/decode split, orchestration. |
| `performance_factor` | L1-L4 | SKU, memory, interconnect, compiler, kernels, precision, quantization. |
| `availability_factor` | L0-L2, L13 | Uptime, interruptibility, maintenance windows, delivery confidence. |
| `locality_factor` | L0, L9, L13-L15 | Region, data gravity, latency, data movement, sovereignty. |
| `policy_factor` | L15 | Compliance, tenancy, auditability, safety and governance constraints. |
| `settlement_factor` | L11, L15 | Index fit, measurement quality, delivery verification, counterparty credit. |

This is not a pricing model by itself. It is a scaffold for asking which adjustments matter for a given exposure.

## Layer Shock Matrix

| Shock | Entry layer | Possible market effect | Who might misread it |
| --- | --- | --- | --- |
| Grid interconnection delay | L0 | Reserved capacity slips, bridge power cost rises, flexible-load value increases. | Traders watching only GPU spot rates. |
| HBM shortage or allocation change | L1 | High-memory workloads reprice; long-context inference becomes capacity-constrained. | Buyers hedged with generic GPU-hour curves. |
| New GPU generation ramps | L1 | Older fleets may fall in price, unless software support or availability keeps them valuable. | Buyers assuming all new-generation capacity substitutes one-for-one. |
| TensorRT/vLLM-style serving gain | L3 | Effective inference capacity rises on installed hardware. | Infrastructure investors modeling only physical supply. |
| Quantization breakthrough | L4 | Some workloads shift to cheaper devices; others expand demand because costs fall. | Commentators assuming efficiency always lowers aggregate demand. |
| Larger context windows become standard | L8-L9 | KV-cache and memory pressure can dominate raw FLOPs. | Contract designers ignoring memory and storage layers. |
| Sovereign/disconnected requirement | L15 | Public-cloud capacity becomes non-substitutable for some regulated workloads. | Index users applying a global cloud price to local obligations. |
| Benchmark methodology change | L11/L15 | Settlement value changes without any physical supply change. | Risk managers treating index governance as a back-office detail. |

## Scenario Sketches

### Scenario 1: Power-Constrained Contango

If data center projects are delayed by grid interconnection queues, short-term delivered compute may become more valuable even if chip supply improves. The forward curve could steepen for regions where power and substations are binding. The arbitrage question is not "more GPUs or fewer GPUs?" but "which regions have deliverable powered racks?"

Relevant evidence: IEA projects data center electricity consumption roughly doubling from 485 TWh in 2025 to 950 TWh in 2030, while DOE/LBNL estimated U.S. data centers could rise from 4.4% of U.S. electricity in 2023 to 6.7-12% by 2028.

### Scenario 2: Memory-Constrained Compute

If HBM and high-value server memory remain constrained, raw GPU capacity could be a misleading proxy. A model with larger context or memory bandwidth needs may price against HBM availability, not just accelerator count.

Relevant evidence: Micron described memory as a strategic asset in its fiscal Q2 2026 results, and Samsung's Q1 2026 update pointed to continued AI infrastructure demand, HBM4 sales, HBM4E sampling plans, and strong server-memory demand.

### Scenario 3: Efficiency Shock

Software and numeric improvements can increase effective compute supply. vLLM reported 2-4x throughput improvements at similar latency in its evaluated serving workloads. AWQ reported strong 4-bit deployment performance and more than 3x TinyChat speedup versus Hugging Face FP16 on tested desktop and mobile GPUs. NVIDIA reported up to 2.8x per-GPU Blackwell throughput gains over three months from TensorRT-LLM optimizations in early 2026.

The market question is ambiguous. Efficiency could reduce demand for raw GPU-hours in a fixed workload. It could also increase demand by making AI features cheap enough to embed everywhere.

### Scenario 4: Sovereign Non-Substitution

If a buyer needs disconnected, on-prem, or sovereign infrastructure, a global public-cloud GPU index might be a poor hedge. The contractual unit might need to include operational boundary, control plane location, identity/data residency, and local hardware rights.

Relevant evidence: Microsoft's February 2026 Sovereign Cloud announcement emphasized fully disconnected local operations and large-model support within customer-controlled boundaries. The EU AI Factories initiative similarly ties compute capacity to regional industrial, research, public-sector, and sovereignty goals.

## Data Schema For Analysis

The following schema could support an internal research notebook, spreadsheet, or agent memory:

```yaml
compute_exposure:
  workload:
    type: training | inference | evaluation | batch | edge | sovereign
    model_family: string
    sequence_profile: input_tokens/output_tokens/context_window
    latency_requirement: p50/p95/p99
  capacity:
    accelerator: sku
    memory_gb: number
    interconnect: topology
    region: string
    tenancy: shared | dedicated | on_prem | sovereign
    duration: spot | monthly | reserved | multi_year
  layer_constraints:
    l0_power: grid | colocated | bridge | flexible
    l1_memory: hbm | dram | kv_cache | storage
    l2_runtime: cuda | rocm | custom
    l3_engine: vllm | tensorrt_llm | other
    l4_precision: fp16 | fp8 | fp4 | int4 | mixed
    l15_policy: public_cloud | regulated | disconnected | classified
  hedge_or_index:
    reference_name: string
    settlement_type: financial | physical | parametric | hybrid
    methodology_url: string
    coverage_layers: [L0, L1, L2, L3, L4, L15]
  residual_basis_risks:
    - type: sku_basis
      severity: low | medium | high
      note: string
```

## Layer-Aware Arbitrage Questions

The word arbitrage should be used carefully. Some opportunities will be true arbitrage; many will be information advantages, procurement advantages, operational flexibility, or better hedging. AILIS can still help identify where the gap lives.

| If the market reacts to... | But the binding layer is... | Possible analytical edge |
| --- | --- | --- |
| GPU spot prices | L0 power | Model power-backed capacity spreads by region. |
| H100 rental curve | L1 memory/topology | Compare memory-rich versus compute-rich capacity. |
| Chip shipments | L2-L3 software readiness | Track usable capacity, not shipped silicon. |
| Quantization news | L16 workload economics | Separate workloads where quality loss is acceptable from those where it is not. |
| Sovereign AI announcements | L15 governance | Estimate non-substitutable local demand versus global cloud oversupply. |
| Forward-curve publication | L11/L15 benchmark governance | Analyze methodology, data sufficiency, and manipulation risk before trusting settlement. |

## How To Use The Model

1. Start with the real exposure, not the available hedge.
2. Map the exposure to layers.
3. Map the index or contract to layers.
4. Compare included and excluded attributes.
5. Stress the excluded attributes.
6. Describe the residual basis risk in plain language.

## Open Questions

- Should AILIS define a "Layer Coverage Statement" for compute benchmarks?
- Could compute contracts expose both a raw unit and a quality-adjusted unit?
- How should model-efficiency improvements be represented in market data?
- Should power-flexible AI factories receive a different capacity category from static loads?
- What empirical data would make QACU less speculative?

## Sources

- IEA, [Key Questions on Energy and AI](https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary), accessed May 7, 2026.
- U.S. Department of Energy, [DOE Releases New Report Evaluating Increase in Electricity Demand from Data Centers](https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers), Dec. 20, 2024.
- Micron, [Fiscal Q2 2026 results](https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-results-second-quarter-fiscal-2026), Mar. 18, 2026.
- Samsung, [First Quarter 2026 Results](https://news.samsung.com/global/samsung-electronics-announces-first-quarter-2026-results), Apr. 30, 2026.
- vLLM, [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180), 2023.
- AWQ, [Activation-aware Weight Quantization for LLM Compression and Acceleration](https://arxiv.org/abs/2306.00978), 2023.
- NVIDIA, [Delivering Massive Performance Leaps for Mixture of Experts Inference on NVIDIA Blackwell](https://developer.nvidia.com/blog/delivering-massive-performance-leaps-for-mixture-of-experts-inference-on-nvidia-blackwell/), Jan. 8, 2026.
- Microsoft, [Sovereign Cloud adds disconnected large-model support](https://blogs.microsoft.com/blog/2026/02/24/microsoft-sovereign-cloud-adds-governance-productivity-and-support-for-large-ai-models-securely-running-even-when-completely-disconnected/), Feb. 24, 2026.
- European Commission, [AI Factories](https://digital-strategy.ec.europa.eu/en/policies/ai-factories), accessed May 7, 2026.
