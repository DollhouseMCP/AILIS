---
title: L12 - Routing, Planning & Policy
---

<!-- markdownlint-disable MD013 MD033 -->

# L12 - Routing, Planning & Policy

L12 covers model routing, agent planning, policy enforcement, budget constraints, fallback paths, privacy rules, ensemble selection, and evaluator feedback loops. It is where the system decides what to do next and under what constraints.

<div class="ailis-layer-infographic lane-protocol" aria-label="L12 routing planning and policy infographic">
  <div><strong>L12</strong><span>Routing, Planning & Policy</span></div>
  <ol>
    <li>Routing</li>
    <li>Planning</li>
    <li>Budgets</li>
    <li>Policy checks</li>
  </ol>
</div>

## What belongs here

L12 sits above individual model and tool capabilities. It may choose between providers, split work across ensembles, enforce cost limits, apply privacy policy, or select a planner strategy.

## Representative projects

| Project | Why it might fit | Adjacent layers |
| --- | --- | --- |
| [LiteLLM](https://docs.litellm.ai/) | Proxy and routing layer across model providers with budgets and access controls. | L12 routing, L13 transport |
| [OpenRouter](https://openrouter.ai/docs) | Model routing and provider abstraction for many model endpoints. | L12 routing, L7 inference |
| [LangGraph](https://langchain-ai.github.io/langgraph/) | Graph-based orchestration for controllable agent workflows. | L12 planning, L14 memory |
| [Microsoft AutoGen](https://microsoft.github.io/autogen/) | Multi-agent framework for planning and collaboration patterns. | L12 planning, L16 applications |
| [CrewAI](https://docs.crewai.com/) | Agent orchestration framework centered on roles, tasks, and crews. | L12 planning, L16 applications |
| [Open Policy Agent](https://www.openpolicyagent.org/docs/latest/) | General policy engine that can inform AI routing and authorization decisions. | L12 policy, L15 governance |

## Boundary questions

- Does routing belong in L12 when it is implemented inside an inference gateway?
- Should agent planning be modeled separately from application logic, or is that distinction too artificial?
- How should policy decisions reference identity, memory, governance, and provider constraints without collapsing layers?

## Signals to watch

- Provider routing becoming a normal architectural layer rather than a helper library.
- Planner frameworks converging around durable graph execution.
- Privacy, cost, and latency policies becoming explicit inputs to routing decisions.

## Links

- [Previous layer: L11 Addressing & Registry](l11-addressing-registry.md)
- [Back to the primer layer](../proposals/AILIS_Primer.md#l12-routing-planning-policy)
- [Next layer: L13 Transport & Flow Semantics](l13-transport-flow-semantics.md)
