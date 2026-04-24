---
title: L5 - Tokenization & Encoders
---

<!-- markdownlint-disable MD013 MD033 MD046 -->

# L5 - Tokenization & Encoders

L5 covers the conversion of raw inputs into model-facing representations: tokenization, image encoders, audio encoders, patchification, embeddings, and modality-specific preprocessing. It is where the world becomes model input.

<div class="ailis-layer-infographic lane-research" aria-label="L5 tokenization and encoders infographic">
  <div><strong>L5</strong><span>Tokenization & Encoders</span></div>
  <ol>
    <li>Text tokens</li>
    <li>Vision patches</li>
    <li>Audio frames</li>
    <li>Embedding spaces</li>
  </ol>
</div>

## What belongs here

L5 is lower than prompt construction. It does not decide what context is selected, but it does define how selected context is represented and how much of it can fit.

## Representative projects

| Project | Why it might fit | Adjacent layers |
| --- | --- | --- |
| [Hugging Face Tokenizers](https://huggingface.co/docs/tokenizers/) | Fast tokenization library used across transformer workflows. | L5 tokenization, L6 model compatibility |
| [OpenAI tiktoken](https://github.com/openai/tiktoken) | Tokenizer library used for OpenAI model token accounting and encoding. | L5 tokenization, L8 prompting |
| [SentencePiece](https://github.com/google/sentencepiece) | Unsupervised text tokenizer and detokenizer commonly used in NLP models. | L5 tokenization, L6 models |
| [CLIP](https://github.com/openai/CLIP) | Vision-text representation model that illustrates multimodal encoding boundaries. | L5 encoders, L6 architecture |
| [Whisper](https://github.com/openai/whisper) | Speech recognition model with audio preprocessing and encoding concerns. | L5 audio, L16 applications |
| [SigLIP](https://huggingface.co/docs/transformers/en/model_doc/siglip) | Vision-language encoder family useful for multimodal retrieval and classification. | L5 encoders, L9 retrieval |

## Boundary questions

- Does an embedding model belong here, in L6 model architecture, or in L9 retrieval when it is used for search?
- Should token counting be modeled as L5 mechanics or L8 context budgeting?
- How should AILIS represent multimodal systems where each modality has a different encoder stack?

## Signals to watch

- Longer-context models making tokenization less visible but still economically important.
- Multimodal encoders becoming more composable across products.
- Tokenizer mismatch causing retrieval, evaluation, or governance failures.

## Links

- [Previous layer: L4 Numeric & Quantization](l4-numeric-quantization.md)
- [Back to the primer layer](../proposals/AILIS_Primer.md#l5-tokenization-encoders)
- [Next layer: L6 Model Parameters & Architecture](l6-model-parameters-architecture.md)
