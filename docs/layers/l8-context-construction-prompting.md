---
title: L8 - Context Construction & Prompting
---

# L8 - Context Construction & Prompting

L8 covers system prompts, prompt templates, few-shot examples, context packing, instruction hierarchy, prompt evaluation, and runtime context assembly. It is where a task becomes a model-facing conversation or request.

<div class="ailis-layer-infographic lane-research" aria-label="L8 context construction and prompting infographic">
  <div><strong>L8</strong><span>Context Construction & Prompting</span></div>
  <ol>
    <li>Instructions</li>
    <li>Examples</li>
    <li>Context packing</li>
    <li>Prompt tests</li>
  </ol>
</div>

## What belongs here

L8 sits above inference and below retrieval, tool calls, and planning. It describes how the system shapes the immediate input to a model, including instructions, examples, retrieved snippets, tool schemas, and conversation state.

## Representative projects

| Project | Why it might fit | Adjacent layers |
| --- | --- | --- |
| [LangChain prompt templates](https://python.langchain.com/docs/concepts/prompt_templates/) | Common abstraction for constructing model inputs from variables and templates. | L8 prompting, L12 orchestration |
| [LlamaIndex](https://docs.llamaindex.ai/) | Data and context orchestration tooling that often constructs prompts from indexed knowledge. | L8 context, L9 retrieval |
| [DSPy](https://dspy.ai/) | Programming model for optimizing prompts and language model pipelines. | L8 prompting, L12 planning |
| [promptfoo](https://www.promptfoo.dev/docs/) | Evaluation and testing workflows for prompts and model behavior. | L8 prompting, L15 governance |
| [Guidance](https://github.com/guidance-ai/guidance) | Structured generation and prompting library for controlling model output. | L8 prompting, L15 schema |
| [Microsoft Prompt Flow](https://microsoft.github.io/promptflow/) | Tooling for prompt and LLM workflow development and evaluation. | L8 prompting, L12 orchestration |

## Boundary questions

- If retrieved content is assembled into a prompt, is the system doing L8 work, L9 work, or both?
- Do tool schemas included in a prompt belong to L8 context or L10 tool invocation?
- Should prompt testing be L8 quality assurance or L15 governance?

## Signals to watch

- Prompt construction shifting from hand-written templates to optimized programs.
- More explicit instruction hierarchy and context provenance.
- Evaluations becoming part of every prompt change.

## Links

- [Previous layer: L7 Inference Engine & Decoding](../l7-inference-engine-decoding/)
- [Back to the primer layer](../../proposals/AILIS_Primer/#l8-context-construction-prompting)
- [Next layer: L9 Knowledge & Retrieval](../l9-knowledge-retrieval/)
