---
title: L6 - Model Parameters & Architecture
---

<!-- markdownlint-disable MD013 MD033 MD046 -->

# L6 - Model Parameters & Architecture

L6 covers model weights, architectures, model families, adapter strategies, and release artifacts. It is where a system's learned capability is packaged before serving, routing, prompting, retrieval, or application logic comes into play.

<div class="ailis-layer-infographic lane-research" aria-label="L6 model parameters and architecture infographic">
  <div><strong>L6</strong><span>Model Parameters & Architecture</span></div>
  <ol>
    <li>Weights</li>
    <li>Architecture</li>
    <li>Adapters</li>
    <li>Model cards</li>
  </ol>
</div>

## What belongs here

L6 asks what model is being used and how it is structured. The same L6 artifact may be served by many L7 engines, quantized through L4 choices, and governed by L15 controls.

## Representative projects and families

| Project or family | Why it might fit | Adjacent layers |
| --- | --- | --- |
| [Hugging Face Transformers](https://huggingface.co/docs/transformers/en/index) | Common library and model interface for transformer architectures. | L5 tokenization, L6 models |
| [Meta Llama](https://www.llama.com/) | Public model family with architecture, weights, model cards, and deployment ecosystem. | L6 models, L15 safety |
| [Mistral AI models](https://docs.mistral.ai/) | Model family and API/provider ecosystem with multiple deployment paths. | L6 models, L7 serving |
| [Qwen](https://qwenlm.github.io/) | Open model family with language and multimodal variants. | L6 models, L5 encoders |
| [Hugging Face Diffusers](https://huggingface.co/docs/diffusers/) | Model and pipeline ecosystem for diffusion architectures. | L6 architecture, L16 applications |
| [LoRA in PEFT](https://huggingface.co/docs/peft/index) | Adapter-based model customization that may change capability without replacing a base model. | L6 adapters, L15 governance |

## Boundary questions

- Should model cards and release metadata live in L6, L11 registry, or L15 governance?
- When a model is only available through an API, how much of L6 can consumers actually inspect?
- Are adapters separate L6 artifacts, or policy-controlled overlays in L12/L15?

## Signals to watch

- Model releases shipping with richer capability, safety, and deployment metadata.
- Small specialized models becoming more important in routing strategies.
- Adapter composition making "the model" less singular.

## Links

- [Previous layer: L5 Tokenization & Encoders](l5-tokenization-encoders.md)
- [Back to the primer layer](../proposals/AILIS_Primer.md#l6-model-parameters-architecture)
- [Next layer: L7 Inference Engine & Decoding](l7-inference-engine-decoding.md)
