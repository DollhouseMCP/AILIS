---
title: L15 - Governance, Safety & Schema
---

<!-- markdownlint-disable MD013 MD033 MD046 -->

# L15 - Governance, Safety & Schema

L15 covers validation, policy controls, safety filters, redaction, auditability, schema conformance, repair, approvals, provenance, and change management. It is where systems try to make AI behavior inspectable enough to use responsibly.

<div class="ailis-layer-infographic lane-research" aria-label="L15 governance safety and schema infographic">
  <div><strong>L15</strong><span>Governance, Safety & Schema</span></div>
  <ol>
    <li>Validation</li>
    <li>Redaction</li>
    <li>Safety checks</li>
    <li>Audit trails</li>
  </ol>
</div>

## What belongs here

L15 is not only moderation. It includes structured output validation, schema evolution, policy audit, privacy controls, guardrails, and evaluation loops that constrain or measure AI behavior.

## Representative projects

| Project | Why it might fit | Adjacent layers |
| --- | --- | --- |
| [NVIDIA NeMo Guardrails](https://docs.nvidia.com/nemo/guardrails/latest/) | Guardrail framework for conversational AI applications. | L15 safety, L16 applications |
| [Guardrails AI](https://www.guardrailsai.com/docs/) | Validation and guardrail framework for LLM outputs. | L15 schema, L8 prompting |
| [Lakera Guard](https://www.lakera.ai/lakera-guard) | Security and safety product for prompt injection and AI risk checks. | L15 safety, L10 tools |
| [Llama Guard](https://www.llama.com/docs/model-cards-and-prompt-formats/llama-guard-4/) | Safety model family for classifying AI inputs and outputs. | L6 models, L15 safety |
| [OpenAI Moderation](https://platform.openai.com/docs/guides/moderation) | Moderation API and guidance for safety classification. | L15 safety, L16 products |
| [Microsoft Presidio](https://microsoft.github.io/presidio/) | PII detection and anonymization framework. | L15 redaction, L14 identity |
| [JSON Schema](https://json-schema.org/) | Schema vocabulary used for validating structured data. | L10 tool schemas, L15 validation |
| [Great Expectations](https://docs.greatexpectations.io/) | Data validation framework relevant to pipeline governance and quality. | L9 knowledge, L15 governance |

## Boundary questions

- Does a safety model belong in L6 as a model, L15 as a control, or both?
- Should schema validation be attached to tools, outputs, stored memories, or all of them?
- How can governance be strong enough for trust without becoming a vague umbrella for every risk?

## Signals to watch

- Guardrails moving from app-level patches into shared infrastructure.
- Structured output and schema enforcement becoming standard provider features.
- AI audit logs needing to connect prompts, tools, identities, model versions, and outputs.

## Links

- [Previous layer: L14 Session, Identity & Memory](l14-session-identity-memory.md)
- [Back to the primer layer](../proposals/AILIS_Primer.md#l15-governance-safety-schema)
- [Next layer: L16 Application & Domain Logic](l16-application-domain-logic.md)
