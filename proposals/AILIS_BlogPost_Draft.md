# AILIS: A Map for Talking About the AI Stack

_Draft for feedback - April 2026_

AI systems are becoming easier to demo and harder to explain.

One product might include a frontier model, a local model, a vector database, prompt templates, tool calls, memory,
provider routing, safety checks, schema validation, identity rules, and a user-facing workflow. Another product might
use similar words for a very different stack. "Agent," "orchestration," "memory," "tool," and "platform" can mean almost
anything until someone draws the boundaries.

AILIS, the AI Layer Interface Specification, is a Dollhouse Research proposal for drawing those boundaries more
carefully. It asks a simple question:

> Could AI benefit from a shared layer map, not as a rigid standard, but as a better way to discuss architecture?

## The problem with four boxes

Many AI diagrams use a familiar shape:

```text
Infrastructure -> Model -> Orchestration -> Application
```

That is useful for a slide. It is less useful when a team needs to decide where identity lives, how tool permissions are
scoped, whether memory belongs to the app or the user, why a cancellation cannot resume, or which provider should handle
a request under cost, latency, privacy, and quality constraints.

The important problems often live between the obvious boxes.

AILIS proposes a more granular map: L0 through L16, with cross-cutting planes for control, observability, and security.
The goal is not to make the diagram bigger for its own sake. The goal is to make hidden handoffs visible.

## A first pass at the stack

At the highest level, AILIS groups the AI ecosystem into five regions:

| Region | Layers | What it describes |
| --- | --- | --- |
| Infrastructure foundation | L0-L2 | Facilities, compute fabric, and system runtimes. |
| Model and inference stack | L3-L7 | Graph compilation, quantization, encoders, model artifacts, and serving. |
| AI application interface | L8-L10 | Prompting, retrieval, and tool/function invocation. |
| Orchestration layers | L11-L15 | Registry, routing, transport, session, memory, governance, and schema controls. |
| Application and domain logic | L16+ | Products, workflows, domain rules, and user experience. |

The full [AILIS Layer Atlas](../../layers/) gives each layer a page with examples and open questions. The Atlas matters
because real systems rarely fit neatly into a single row. The interesting part is often where a project crosses layers.

## Why the middle deserves attention

The model and inference layers are crowded. There is intense activity around chips, runtimes, model families, serving
engines, quantization, and retrieval.

That work is important, but it is not the whole stack.

AILIS highlights L11-L15 because many teams are already rebuilding those layers inside their own products:

- **Addressing and registry:** How do we discover models, tools, prompts, indices, and agent capabilities in a way that
  includes versions, evidence, signatures, and constraints?
- **Routing, planning, and policy:** How do we choose among providers, tools, local models, remote models, and ensembles
  under cost, latency, privacy, quality, and failure constraints?
- **Transport and flow semantics:** How do AI calls stream, cancel, pause, resume, multiplex, and recover?
- **Session, identity, and memory:** Who is acting, what context is portable, what memory can be used, and what did the
  user consent to?
- **Governance, safety, and schema:** What must be redacted, validated, repaired, approved, audited, or blocked before
  the system takes action?

These are not edge cases. They are becoming ordinary engineering concerns.

## A map, not a mandate

AILIS is intentionally a proposal. It is not claiming that L11 must be exactly here forever, or that every project needs
to present itself in AILIS terminology. The model is useful only if it helps people ask better questions.

For example:

- Is this tool primarily a retrieval product, a tool invocation protocol, or an application workflow?
- Is this "memory" a vector index, a user-owned session object, a product feature, or all three?
- Is a routing layer choosing providers based on evidence, or only hiding API differences?
- Where does consent live when an agent calls a tool using long-term memory?
- Which layer owns cancellation when a model stream triggers a long-running action?

If the map makes those questions easier to ask, it is doing useful work. If a real system does not fit, that is not a
failure. It is feedback.

## What this could unlock

A shared layer vocabulary could help different groups without forcing them into the same architecture.

For builders, it could make product boundaries clearer. A team might say, "We are mostly L12-L14. We route across
providers, maintain session continuity, and manage consented memory. We do not train models."

For researchers, it could expose under-studied problems. Instead of another broad claim about "agents," a paper might
focus on transport resumability, registry evidence, or memory governance.

For users and organizations, it could make AI systems more inspectable. If a product claims to have memory, routing,
tools, and governance, the AILIS map gives people a way to ask where those things live and how they interact.

For protocol designers, it could point toward missing interfaces. MCP, tool calling, vector stores, model registries,
guardrails, and agent frameworks all touch pieces of the stack. AILIS asks how those pieces might be described together.

## What happens next

The next step is not to declare the model finished. The next step is to test it.

That means mapping real systems, adding examples to the [Layer Atlas](../../layers/), arguing about blurry boundaries,
and drafting deeper proposals where the gaps are clearest. L11-L15 are obvious candidates, especially addressing,
routing, flow semantics, portable session envelopes, memory consent, and governance schemas.

AILIS may change shape as better examples arrive. That is the point.

The AI ecosystem does not need another diagram that pretends everything is settled. It might need a shared workbench for
the questions that are still open.

*Feedback welcome. Especially the kind that breaks the model in useful ways.*
