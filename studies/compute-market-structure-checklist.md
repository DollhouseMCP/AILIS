---
title: Compute Capacity Contract and Benchmark Checklist
description: Draft checklist for evaluating compute-market contracts, benchmarks, and risk-transfer instruments through AILIS.
---

<!-- markdownlint-disable MD013 -->

# Compute Capacity Contract and Benchmark Checklist

This checklist is a draft. It is meant to help AILIS readers evaluate compute-capacity contracts, forward curves, swaps, insurance products, and benchmark claims without flattening compute into a single unit.

The premise is simple: before compute can become commodity-like, market participants need to know what is being delivered, measured, substituted, insured, and settled.

## Why A Checklist Is Needed

The Enron bandwidth analogy is useful because it is uncomfortable. Bandwidth had real supply, real demand expectations, and real financial interest. It also had standardization problems: delivery locations, quality of service, provisioning, billing, industry cooperation, and contract terms. A Berkeley working paper on Enron's bandwidth effort emphasized that spot and forward markets depended on delivery confidence and a master services agreement with shared terms.

Compute may be different in important ways. Cloud APIs, accelerator telemetry, data center finance, and benchmark infrastructure are more mature than bandwidth trading was in 2000. But the contract problem still rhymes. A "GPU-hour" might not specify enough to support institutional settlement.

## Contract Checklist

| Area | Questions |
| --- | --- |
| Deliverable unit | Is the unit GPU-hour, rack-hour, token throughput, power-backed rack, reserved instance, capacity block, or workload outcome? |
| Hardware | Which accelerator SKU, memory size, HBM generation, topology, CPU pairing, storage, and network fabric are included? |
| Performance | Is performance measured by FLOPs, tokens/sec, latency percentiles, job completion, benchmark score, or workload-specific output? |
| Duration | Is the term spot, interruptible, monthly, forward-starting, take-or-pay, multi-year, or perpetual hardware ownership? |
| Location | What region, availability zone, data center, grid node, or sovereign boundary applies? |
| Power and cooling | Is the contract exposed to power price, curtailment, interconnection delay, peak events, PUE, cooling type, or water constraints? |
| Software stack | Are drivers, runtime, compiler, serving engine, container image, firmware, and orchestration commitments specified? |
| Tenancy and security | Is capacity shared, dedicated, isolated, air-gapped, on-prem, sovereign, or classified? |
| Data movement | Who pays for ingress, egress, storage, retrieval, cache, replication, and data-locality constraints? |
| Governance | Which audit, safety, privacy, data residency, model governance, and regulatory obligations attach? |
| Reliability | What uptime, maintenance, interruption, restart, checkpointing, and service-credit terms apply? |
| Substitution | Can the provider substitute SKU, region, topology, software stack, or cloud vendor? What adjustment follows? |
| Measurement | Who measures delivery, how often, using what telemetry, and with what dispute process? |
| Settlement | Is settlement physical, financial, parametric, or hybrid? What happens if delivery and index price diverge? |
| Index linkage | Which benchmark or curve is referenced? What is its methodology, data source, governance, and revision process? |
| Credit and collateral | How are vendor default, buyer non-payment, GPU residual value, lender rights, and collateral depreciation handled? |
| Outage and loss | Do remedies match actual business loss, or only a small service credit? Is insurance available? |
| Change control | How are methodology, hardware, software, precision, and policy changes versioned and noticed? |

## Benchmark Checklist

Financial benchmark governance becomes central if compute contracts settle against indices. IOSCO's principles point to governance, benchmark quality, methodology quality, and accountability. CFTC material on contract listings emphasizes contracts not readily susceptible to manipulation and position accountability where needed.

For a compute benchmark, ask:

- Is the benchmark based on real transactions, firm bids/offers, posted prices, surveys, or modeled values?
- Are the data sources broad enough to represent the claimed market?
- Which providers, regions, SKUs, terms, and tenancy types are included or excluded?
- How are outliers, stale prices, failed transactions, and private discounts handled?
- Is the methodology public, versioned, and auditable?
- Who governs conflicts of interest?
- Can market participants manipulate the benchmark by posting non-executable offers?
- Is the benchmark useful for physical delivery, financial settlement, or only budgeting?
- Does it publish confidence, coverage, or data sufficiency indicators?
- Does it disclose AILIS layer coverage?

## Instrument Types

| Instrument | Possible use | Main residual risk |
| --- | --- | --- |
| Spot GPU rental index | Procurement benchmark and budget reference. | SKU, region, term, and workload mismatch. |
| Forward curve | Budgeting, underwriting, OTC swaps, contract negotiation. | Methodology and liquidity risk; curve may not imply deliverable capacity. |
| Fixed-for-floating compute swap | Hedge rental-rate exposure. | Index basis, credit, collateral, and settlement governance. |
| Physical forward | Reserve future capacity. | Delivery failure, substitution, power delay, and counterparty risk. |
| Outage insurance | Cover business interruption beyond service credits. | Loss measurement, exclusions, and dependency mapping. |
| GPU residual value insurance | Support GPU-backed lending or fleet finance. | Technology obsolescence, secondary-market depth, export controls, and benchmark fit. |
| Power-compute spread hedge | Link energy cost to compute revenue or capacity. | Regional basis, grid constraints, and curtailment rules. |

## AILIS Layer Coverage Statement

A compute contract or benchmark could include a short layer coverage statement:

| Layer | Covered? | Notes |
| --- | --- | --- |
| L0 Facilities and Power | Yes/No/Partial | Region, power source, bridge power, interconnection, cooling. |
| L1 Compute Fabric | Yes/No/Partial | SKU, memory, interconnect, topology. |
| L2 Runtime | Yes/No/Partial | Driver, firmware, virtualization, container. |
| L3 Graph and Compilation | Yes/No/Partial | Compiler/runtime expectations, optimized kernels. |
| L4 Numeric | Yes/No/Partial | Supported precisions and quantization assumptions. |
| L5-L9 Data and Context | Yes/No/Partial | Data locality, context, retrieval, cache/storage. |
| L10-L14 Flow and State | Yes/No/Partial | Routing, transport, identity, session continuity. |
| L15 Governance and Schema | Yes/No/Partial | Compliance, audit, benchmark governance, sovereignty. |
| L16 Domain Logic | Yes/No/Partial | Workload outcome or application SLA. |

This would not make the contract perfect. It would make hidden exclusions easier to discuss.

## Example Reads

### GPU Forward Curve

Silicon Data describes a GPU forward curve built from rental term structures and no-arbitrage forward derivation. This appears useful for pricing expectations, procurement timing, and financial products. The AILIS question is what layer coverage the curve has: SKU and term may be covered; power, topology, software stack, sovereignty, and workload outcome may remain outside the curve unless separately specified.

### Compute Risk Transfer

Forward Compute describes insurance, swaps, forwards, and purpose-built indices for compute. This maps naturally to L15 governance and L11 addressing/registry questions: what is the settlement reference, what data supports it, and what exactly is insured or hedged?

### Power-Flexible AI Factories

NVIDIA and Emerald AI's March 2026 announcement reframes some AI factories as flexible grid assets rather than passive loads. That suggests a contract category where L0 flexibility is not a side issue; it is part of the economic unit.

### Sovereign Private Cloud

Microsoft's February 2026 sovereign cloud announcement shows why some compute cannot simply be replaced by cheaper public cloud supply. The deliverable includes operational boundary, local control, governance, and disconnected operation.

## Questions For Review

- Should AILIS publish a formal "Compute Capacity Contract Checklist" as a reference artifact?
- Would benchmark administrators be willing to state layer coverage?
- Which attributes are essential for a minimal compute forward contract?
- Are token-throughput contracts more economically meaningful than GPU-hour contracts, or too workload-specific?
- How should outage insurance map dependencies across L0-L16?
- What role could open-source telemetry play in settlement verification?

## Sources

- Andrew Schwartz, [Enron's Missed Opportunity](https://brie.berkeley.edu/sites/default/files/wp152.pdf), Berkeley Roundtable on the International Economy, 2002/2003.
- Silicon Data, [GPU Forward Curve](https://www.silicondata.com/products/forward-curve), accessed May 7, 2026.
- Silicon Data, [The GPU Forward Curve: Pricing the Curve, Not Just the Spot](https://www.silicondata.com/blog/the-gpu-forward-curve-pricing-the-curve-not-just-the-spot), May 1, 2026.
- Forward Compute, [Insurance and financial derivatives for compute](https://www.forwardcompute.ai/), accessed May 7, 2026.
- Financial Stability Board, [IOSCO Principles for Financial Benchmarks](https://www.fsb.org/2013/07/cos_130717/), July 17, 2013.
- CFTC, [Designated Contract Markets](https://www.cftc.gov/IndustryOversight/TradingOrganizations/DCMs/index.htm), accessed May 7, 2026.
- CFTC, [Economic Requirements](https://www.cftc.gov/IndustryOversight/ContractsProducts/EconomicRequirements/index.htm), accessed May 7, 2026.
- NVIDIA, [Flexible AI Factories as Grid Assets](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Emerald-AI-Join-Leading-Energy-Companies-to-Pioneer-Flexible-AI-Factories-as-Grid-Assets/default.aspx), Mar. 23, 2026.
- Microsoft, [Sovereign Cloud adds disconnected large-model support](https://blogs.microsoft.com/blog/2026/02/24/microsoft-sovereign-cloud-adds-governance-productivity-and-support-for-large-ai-models-securely-running-even-when-completely-disconnected/), Feb. 24, 2026.
