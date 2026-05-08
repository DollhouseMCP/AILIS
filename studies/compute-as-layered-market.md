---
title: Compute as a Layered Market
description: Exploratory AILIS analysis of compute financialization, infrastructure scarcity, and layer-aware basis risk.
---

<!-- markdownlint-disable MD013 -->

# Compute as a Layered Market

This note is a draft research paper for discussion. It is not financial advice, a market forecast, or a claim that AILIS has solved compute-market design. The narrower claim is that AILIS might help explain why "compute" is becoming financially interesting precisely because it is not one simple commodity.

## Trigger

On May 5, 2026, Bloomberg reported that BlackRock CEO Larry Fink told the Milken Institute Global Conference that demand for computing power could support a future market for compute futures, while also pointing to shortages in compute capacity, chips, and memory. That comment landed in a broader conversation that was already forming around GPU forward curves, compute swaps, AI infrastructure finance, data center power, HBM supply, and the limits of treating a GPU-hour as if it were as simple as a barrel of oil.

The social discussion around the quote surfaced the right tension. Compute can look commodity-like from far away, but in practice it is assembled from layers: power, cooling, chips, memory, interconnect, runtime software, model architecture, quantization, routing, policy, jurisdiction, and workload economics. A change at one layer might reprice compute in ways that are not obvious to people watching only the headline layer.

## Thesis

Compute might become tradable only where enough of its layers can be standardized, measured, and settled. The remaining non-standardized layers become the source of basis risk, contract disputes, operational exposure, and perhaps arbitrage.

AILIS provides a vocabulary for that decomposition. It does not tell us whether a compute futures market should exist. It does help ask better questions:

- Which layer is scarce?
- Which layer is being priced?
- Which layer is being ignored?
- What compute does the buyer actually need?
- What compute does the hedge, index, or contract actually deliver?

## What Is Current

| Signal | Source | Why it matters |
| --- | --- | --- |
| Compute futures entered mainstream finance discourse in May 2026. | [Bloomberg Law, May 5, 2026](https://news.bloomberglaw.com/private-equity/larry-fink-predicts-birth-of-futures-market-for-computing-power) | A top asset manager is publicly framing compute as a possible tradable exposure. |
| GPU forward curves are now being marketed as a pricing primitive. | [Silicon Data GPU Forward Curve](https://www.silicondata.com/products/forward-curve) and [May 1, 2026 methodology blog](https://www.silicondata.com/blog/the-gpu-forward-curve-pricing-the-curve-not-just-the-spot) | Market infrastructure is appearing before exchange-traded liquidity. |
| Compute-specific risk-transfer firms are positioning around swaps, forwards, insurance, and indices. | [Forward Compute](https://www.forwardcompute.ai/) | Compute finance may begin with OTC risk transfer and insurance before public futures. |
| Data center electricity demand remains a binding infrastructure concern. | [IEA Key Questions on Energy and AI](https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary), [DOE/LBNL summary](https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers) | L0 power and siting can constrain L1 compute availability. |
| Memory is being reframed as a strategic AI input. | [Micron fiscal Q2 2026 results](https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-results-second-quarter-fiscal-2026), [Samsung Q1 2026 results](https://news.samsung.com/global/samsung-electronics-announces-first-quarter-2026-results) | A GPU contract may not hedge HBM, DRAM, or KV-cache pressure. |
| Software and numeric efficiency can change effective capacity without adding physical GPUs. | [vLLM PagedAttention paper](https://arxiv.org/abs/2309.06180), [AWQ paper](https://arxiv.org/abs/2306.00978), [NVIDIA Blackwell inference update](https://developer.nvidia.com/blog/delivering-massive-performance-leaps-for-mixture-of-experts-inference-on-nvidia-blackwell/) | L3/L4 changes can reduce or increase demand for L0/L1 capacity. |
| Sovereign and disconnected AI infrastructure is becoming a product category. | [Microsoft Sovereign Cloud, Feb. 24, 2026](https://blogs.microsoft.com/blog/2026/02/24/microsoft-sovereign-cloud-adds-governance-productivity-and-support-for-large-ai-models-securely-running-even-when-completely-disconnected/), [EU AI Factories](https://digital-strategy.ec.europa.eu/en/policies/ai-factories) | Some compute cannot freely substitute into cloud capacity markets. |

## Layer Map

| AILIS area | Compute-market interpretation | Example market question |
| --- | --- | --- |
| L0 Facilities and Power | Power, land, cooling, interconnection, substations, water, carbon, bridge power. | If a grid queue slips, which capacity contracts become late or more expensive? |
| L1 Compute Fabric | GPU SKU, HBM, VRAM, interconnect, rack topology, spare parts, fleet age. | Is an H100 index a useful hedge for B200, GB200, MI300X, or ASIC exposure? |
| L2 System Runtime | CUDA, ROCm, drivers, firmware, orchestration, virtualization. | Can the buyer actually run the workload on the contracted fleet? |
| L3 Graph and Compilation | Kernel quality, compiler support, serving engine, graph optimization. | Does a software update change effective capacity before any new hardware arrives? |
| L4 Numeric and Quantization | FP8, FP4, AWQ, sparsity, distillation, precision/accuracy tradeoffs. | Does an efficiency gain reduce demand, or unlock enough use cases to increase total demand? |
| L5-L9 Data and Context | Data location, tokenization, context windows, retrieval, cacheability, data rights. | Is the bottleneck compute, or the right to move and use data near compute? |
| L10-L14 Orchestration and Flow | Routing, scheduling, transport semantics, identity, session state, memory. | Can workloads be moved to cheaper capacity without breaking latency or state assumptions? |
| L15 Governance and Schema | Benchmark definitions, auditability, safety, compliance, sovereignty, contract schema. | Can the market settle on a unit that is auditable and hard to manipulate? |
| L16 Domain Logic | Revenue per token, training objective, inference SLA, business workflow. | Does a cheaper GPU-hour lower cost per business outcome? |

## Why the Mental Model Breaks

A commodity mental model works best when the unit is standardized enough that one unit can replace another. Compute is often quoted that way, but production AI rarely consumes abstract compute. It consumes specific capacity under specific constraints.

Several examples show the problem:

- A power-market shock enters at L0, but it may show up as longer delivery lead times for racks, higher colocation costs, or more demand for flexible-load contracts.
- An HBM shortage enters at L1, but it may affect model size, context length, batch economics, and the relative value of quantization.
- A serving-engine improvement enters at L3, but it can change the effective supply of inference capacity on the same installed fleet.
- A quantization breakthrough enters at L4, but it may reduce raw compute demand for some workloads while making new edge or on-device workloads feasible.
- A sovereignty requirement enters at L15, but it can make low-cost public-cloud capacity non-substitutable for regulated buyers.

This is where the arbitrage intuition becomes interesting. Market participants might overreact to the headline layer and underreact to the layer that actually binds the workload.

## Basis Risk

The early compute market seems likely to create multiple forms of basis risk:

| Basis type | Mismatch |
| --- | --- |
| SKU basis | Index tracks one accelerator while exposure depends on another. |
| Topology basis | Index prices single GPU-hours while workload needs tightly coupled racks. |
| Memory basis | GPU rental price is hedged while HBM, DRAM, or KV-cache capacity drives real constraints. |
| Power basis | Compute contract ignores regional power, interconnection, or curtailment risk. |
| Region basis | Global capacity cannot substitute for latency-bound or sovereign capacity. |
| Duration basis | Spot or monthly price does not match a multi-year product roadmap or financing term. |
| Reliability basis | SLA credits do not match the buyer's actual business interruption loss. |
| Workload basis | Training capacity and inference capacity have different economic drivers. |
| Policy basis | Tradable cloud compute cannot replace on-prem, disconnected, classified, or regulated environments. |

## What AILIS Might Add

AILIS could be useful here in four ways:

1. It can name where scarcity enters the stack.
2. It can identify which attributes a contract or benchmark includes.
3. It can show where a hedge fails to match the real workload.
4. It can help non-financial engineers and non-technical finance teams discuss the same exposure without flattening it into "more GPUs."

The fourth point might be the most practical. The compute market is becoming a meeting point for infrastructure finance, energy markets, semiconductor supply chains, cloud procurement, AI engineering, and governance. A layered map gives those communities a shared surface for disagreement.

## Counterarguments

There are serious reasons to be cautious.

First, the Enron bandwidth analogy is not superficial. A Berkeley working paper on Enron's bandwidth trading effort argued that bandwidth needed standardized contracts, delivery mechanisms, market cooperation, and neutral oversight. It also documented why technical non-fungibility, provisioning complexity, and industry resistance made the market hard to launch. Compute markets may face similar issues, even if cloud APIs, telemetry, and mature infrastructure finance make the environment different.

Second, efficiency gains can cut both ways. vLLM, AWQ, and vendor software optimizations can increase effective capacity. That might reduce scarcity for some workloads. It might also expand total demand by making more AI products economical.

Third, a forward curve is not the same thing as a liquid futures market. It may support budgeting, underwriting, OTC swaps, insurance, or internal transfer pricing long before it supports cleared exchange trading.

Fourth, benchmark governance matters. IOSCO's financial benchmark principles emphasize governance, benchmark quality, methodology quality, and accountability. CFTC rules for futures and swaps emphasize contracts not readily susceptible to manipulation, position accountability, market integrity, and surveillance. A compute index would need to earn trust on those dimensions.

## Open Questions

- What is the smallest useful standard compute unit: GPU-hour, rack-hour, token-throughput-hour, power-backed rack, or workload-specific capacity?
- Should financial settlement begin with narrow GPU rental indices, or with broader quality-adjusted capacity baskets?
- How much of the market will remain bilateral because of region, tenancy, sovereignty, or custom topology?
- Could benchmark administrators publish layer coverage alongside price methodology?
- Would a compute index need separate curves for training, inference, sovereign compute, and interruptible capacity?
- Where could AILIS become a checklist for compute contracts rather than just a conceptual model?

## Sources

- Bloomberg Law, [Larry Fink Predicts Birth of Futures Market for Computing Power](https://news.bloomberglaw.com/private-equity/larry-fink-predicts-birth-of-futures-market-for-computing-power), May 5, 2026.
- Silicon Data, [GPU Forward Curve](https://www.silicondata.com/products/forward-curve), accessed May 7, 2026.
- Silicon Data, [The GPU Forward Curve: Pricing the Curve, Not Just the Spot](https://www.silicondata.com/blog/the-gpu-forward-curve-pricing-the-curve-not-just-the-spot), May 1, 2026.
- Forward Compute, [Insurance and financial derivatives for compute](https://www.forwardcompute.ai/), accessed May 7, 2026.
- IEA, [Key Questions on Energy and AI](https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary), accessed May 7, 2026.
- U.S. Department of Energy, [DOE Releases New Report Evaluating Increase in Electricity Demand from Data Centers](https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers), Dec. 20, 2024.
- Micron, [Fiscal Q2 2026 results](https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-results-second-quarter-fiscal-2026), Mar. 18, 2026.
- Samsung, [First Quarter 2026 Results](https://news.samsung.com/global/samsung-electronics-announces-first-quarter-2026-results), Apr. 30, 2026.
- NVIDIA, [Flexible AI Factories as Grid Assets](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Emerald-AI-Join-Leading-Energy-Companies-to-Pioneer-Flexible-AI-Factories-as-Grid-Assets/default.aspx), Mar. 23, 2026.
- Microsoft, [Sovereign Cloud adds disconnected large-model support](https://blogs.microsoft.com/blog/2026/02/24/microsoft-sovereign-cloud-adds-governance-productivity-and-support-for-large-ai-models-securely-running-even-when-completely-disconnected/), Feb. 24, 2026.
- European Commission, [AI Factories](https://digital-strategy.ec.europa.eu/en/policies/ai-factories), accessed May 7, 2026.
- Andrew Schwartz, [Enron's Missed Opportunity](https://brie.berkeley.edu/sites/default/files/wp152.pdf), Berkeley Roundtable on the International Economy, 2002/2003.
- Financial Stability Board, [IOSCO Principles for Financial Benchmarks](https://www.fsb.org/2013/07/cos_130717/), July 17, 2013.
- CFTC, [Economic Requirements](https://www.cftc.gov/IndustryOversight/ContractsProducts/EconomicRequirements/index.htm), accessed May 7, 2026.
