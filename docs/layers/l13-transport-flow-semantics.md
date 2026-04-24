---
title: L13 - Transport & Flow Semantics
---

# L13 - Transport & Flow Semantics

L13 covers the mechanics of AI calls as flows: streaming, cancellation, resume tokens, multiplexing, idempotency, retries, backpressure, and transport negotiation. It is where AI interaction becomes a durable protocol conversation rather than a single request-response call.

<div class="ailis-layer-infographic lane-protocol" aria-label="L13 transport and flow semantics infographic">
  <div><strong>L13</strong><span>Transport & Flow Semantics</span></div>
  <ol>
    <li>Streaming</li>
    <li>Cancel and resume</li>
    <li>Backpressure</li>
    <li>Multiplexing</li>
  </ol>
</div>

## What belongs here

L13 is not simply "HTTP." It describes flow behavior that AI systems increasingly need: partial results, tool progress, long-running actions, resumable conversations, and reliable cancellation across provider and host boundaries.

## Representative projects and protocols

| Project or protocol | Why it might fit | Adjacent layers |
| --- | --- | --- |
| [MCP transports](https://modelcontextprotocol.io/docs/concepts/transports) | Transport choices and message flow for Model Context Protocol clients and servers. | L10 tools, L13 transport |
| [A2A protocol](https://a2aproject.github.io/A2A/latest/) | Agent-to-agent protocol work that raises flow, task, and interaction semantics. | L13 transport, L12 planning |
| [gRPC](https://grpc.io/docs/) | RPC framework with streaming patterns useful for service-to-service AI systems. | L13 transport, L16 services |
| [NATS](https://docs.nats.io/) | Messaging system for distributed systems and event-driven coordination. | L13 transport, L12 orchestration |
| [Server-Sent Events](https://html.spec.whatwg.org/multipage/server-sent-events.html) | Common browser-facing streaming primitive used by AI APIs and apps. | L13 streaming, L16 UX |
| [Temporal](https://docs.temporal.io/) | Durable execution framework relevant to long-running AI workflows. | L13 durability, L12 planning |

## Boundary questions

- What semantics are AI-specific, and what should remain generic distributed-systems plumbing?
- Should resumability be modeled in L13 transport, L14 session, or both?
- How should tool progress, model streaming, and human approval pauses share one flow vocabulary?

## Signals to watch

- More AI protocols adding cancellation, resume, and progress semantics.
- Browser and local-app AI clients needing richer streaming and session recovery.
- Durable agent workflows making "request-response" insufficient as the main mental model.

## Links

- [Previous layer: L12 Routing, Planning & Policy](../l12-routing-planning-policy/)
- [Back to the primer layer](../../proposals/AILIS_Primer/#l13-transport-flow-semantics)
- [Next layer: L14 Session, Identity & Memory](../l14-session-identity-memory/)
