---
title: L10 - Tool & Function Invocation
---

# L10 - Tool & Function Invocation

L10 covers typed tool calls, function calling, tool schemas, API bindings, plugin interfaces, and capability exposure. It is where a model or agent system can request action outside its own generated text.

<div class="ailis-layer-infographic lane-protocol" aria-label="L10 tool and function invocation infographic">
  <div><strong>L10</strong><span>Tool & Function Invocation</span></div>
  <ol>
    <li>Tool schemas</li>
    <li>Function calls</li>
    <li>API bindings</li>
    <li>Result handling</li>
  </ol>
</div>

## What belongs here

L10 is about the contract between the model-facing system and callable capabilities. It does not necessarily decide which tool to use, whether the user is authorized, or how the call is transported, but it defines the shape of invocation.

## Representative projects and protocols

| Project or protocol | Why it might fit | Adjacent layers |
| --- | --- | --- |
| [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) | Protocol for connecting AI applications to tools, resources, and prompts. | L10 tools, L13 transport |
| [OpenAI function calling](https://platform.openai.com/docs/guides/function-calling) | Model-facing tool/function call interface with structured arguments. | L10 invocation, L15 schema |
| [Anthropic tool use](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview) | Tool-use interface for Claude applications and agents. | L10 tools, L8 context |
| [Semantic Kernel plugins](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/) | Plugin abstraction for functions callable by AI orchestration. | L10 tools, L12 planning |
| [OpenAPI](https://www.openapis.org/) | API description format that can become a source for tool schemas. | L10 invocation, L11 registry |
| [LangChain tools](https://python.langchain.com/docs/concepts/tools/) | Tool abstraction used in agent and chain workflows. | L10 tools, L12 orchestration |

## Boundary questions

- Is tool discovery part of L10, or does discovery require L11 registry semantics?
- Should function-call JSON schemas be governed in L10 or L15?
- When a tool call streams progress, does the invocation belong in L10 while flow control belongs in L13?

## Signals to watch

- Tool schemas becoming portable across providers.
- More attention to tool permissions, consent, and audit trails.
- Protocols such as MCP making tool invocation a shared interoperability concern.

## Links

- [Previous layer: L9 Knowledge & Retrieval](../l9-knowledge-retrieval/)
- [Back to the primer layer](../../proposals/AILIS_Primer/#l10-tool-function-invocation)
- [Next layer: L11 Addressing & Registry](../l11-addressing-registry/)
