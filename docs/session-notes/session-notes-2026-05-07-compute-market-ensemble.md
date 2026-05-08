# Session Notes: Compute Market Ensemble and AILIS Drafts

**Date:** 2026-05-07

## Session Overview

Built a DollhouseMCP analyst ensemble for studying AI compute as a layered
financial and technology market, then used the research frame to draft AILIS
study material around compute financialization, basis risk, contracts, and
benchmarks.

## Goals

- Create a reusable DollhouseMCP ensemble that can independently research,
  model, and write about compute markets.
- Research current industry discussion rather than relying on prior model
  knowledge.
- Draft AILIS-facing analysis papers that explain why a layered model is useful
  for compute-market interpretation.
- Fix the Case Studies index feature-card layout so project names and
  descriptions render as separate lines and the featured title wraps cleanly.

## DollhouseMCP Elements Created

- `layered-compute-market-strategist` persona
- `ailis-compute-layer-mapping` skill
- `compute-basis-risk-modeling` skill
- `compute-market-structure-research` skill
- `compute-market-writing` skill
- `ailis-compute-market-brief` template
- `compute-market-research-agent` agent
- `compute-market-research-ledger` memory
- `layered-compute-market-analyst` ensemble

The ensemble was validated and activated. The research ledger was seeded with
the initial source set and working hypothesis.

## AILIS Drafts Created

- `studies/compute-as-layered-market.md`
- `studies/compute-basis-risk-model.md`
- `studies/compute-market-structure-checklist.md`

`studies/index.md` was updated to link the new research drafts.

## Website Fixes

- Reworked the Case Studies index feature area from mixed Markdown-in-HTML to
  explicit HTML, making the intended list and card classes stable.
- Scoped the featured card call-to-action styling to `.ailis-case-study-cta`
  so it no longer affects the title link.
- Added a three-card Compute Market Research section for the new drafts.

## Research Sources Used

Current-source research covered:

- Larry Fink's May 2026 compute-futures remarks reported by Bloomberg Law.
- Silicon Data GPU forward curve and methodology discussion.
- Forward Compute's compute insurance, swaps, forwards, and index framing.
- IEA 2026 and DOE/LBNL data center electricity demand material.
- Micron and Samsung 2026 memory/HBM statements.
- NVIDIA and Emerald AI's power-flexible AI factory announcement.
- Microsoft Sovereign Cloud and EU AI Factories material.
- CFTC and IOSCO market-structure and benchmark-governance references.
- Berkeley's Enron bandwidth trading analysis as a cautionary analogy.

## Key Decisions

- Frame compute as a quality-adjusted, layered capacity bundle rather than a
  single commodity.
- Treat AILIS as an exploratory vocabulary for surfacing basis risk, not as a
  prescriptive market standard.
- Draft research material under `studies/` as reviewable papers rather than
  accepted proposals.

## Validation

- Dollhouse element validation passed for the agent, ensemble, memory, persona,
  skills, and template, with only non-blocking usability suggestions.
- `mkdocs build` passed using a temporary Python 3.11 virtual environment.
- Browser checks were run against the local MkDocs server for the Case Studies
  index at desktop and mobile widths.
- `mkdocs build --strict` initially failed because new uncommitted pages had no
  git revision history yet; this is expected for newly added files under the
  git revision date plugin.
- `git diff --check` and trailing-whitespace checks passed.

## Next Steps

- Review the three drafts for tone, claims, and publication readiness.
- Consider turning the contract checklist into a reference artifact if the
  community finds it useful.
- Consider a LinkedIn post that introduces the compute-as-layers framing before
  linking to the AILIS drafts.
