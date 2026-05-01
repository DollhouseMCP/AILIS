---
title: Case Study - Public Dollhouse Research Portfolio Mapping
---

<!-- markdownlint-disable MD013 MD033 -->

# Case Study: Mapping the public Dollhouse Research portfolio into AILIS

This case study maps the current public Dollhouse Research portfolio into the AILIS layer model. The placements are editorial rather than official, but they are concrete enough to show how one research organization spans multiple layers of the stack.

<div class="ailis-case-study-feature">
  <article id="dollhouse-research" class="ailis-case-study-lead lane-research">
    <span class="ailis-card-kicker">Research home</span>
    <h2>Dollhouse Research</h2>
    <p>
      The public projects in this case study share one research home, but they
      do not all live at the same layer. Some are platform, some are protocol,
      and some are user-facing applications.
    </p>
  </article>

  <aside class="ailis-case-study-side">
    <span class="ailis-card-kicker">Projects included</span>
    <ul class="ailis-case-study-list">
      <li><strong>DollhouseMCP</strong><span>Core platform and runtime surface</span></li>
      <li><strong>Dollhouse Collection</strong><span>Catalog and activation product</span></li>
      <li><strong>MCP-AQL spec</strong><span>Protocol semantics and introspection</span></li>
      <li><strong>MCP-AQL adapters</strong><span>Reference runtime surface</span></li>
      <li><strong>MCP-AQL generator</strong><span>Generation and validation tooling</span></li>
      <li><strong>Elemental Surveys</strong><span>Applied research workflow</span></li>
      <li><strong>Merview</strong><span>Companion review utility</span></li>
    </ul>
  </aside>
</div>

<div class="ailis-layer-infographic lane-protocol" aria-label="Observed pattern in the public Dollhouse Research portfolio">
  <div>
    <strong>Observed pattern</strong>
    <span>Most public Dollhouse Research work begins around L8 and stretches upward through L16.</span>
  </div>
  <ol>
    <li>L0-L7 mostly depend on external model and infrastructure ecosystems.</li>
    <li>DollhouseMCP appears to span the widest range of AILIS layers.</li>
    <li>MCP-AQL clusters most strongly in L10-L15.</li>
    <li>Applied products surface at L16 but lean on lower shared layers.</li>
  </ol>
</div>

## Portfolio view

The first read is by project rather than by layer. That makes it easier to see that the public Dollhouse Research portfolio is not one thing. Some pieces are platform, some are protocol, some are generators and adapters, and some are applications sitting on top.

<div class="ailis-dollhouse-project-grid">
  <article id="dollhousemcp" class="ailis-dollhouse-project lane-core">
    <span class="ailis-card-kicker">Core platform</span>
    <h3>DollhouseMCP server</h3>
    <p>The broadest public stack component: MCP capability exposure, agent tooling, memory, approvals, safety controls, and end-user product behavior.</p>
    <ul class="ailis-dollhouse-layer-tags">
      <li>L8</li>
      <li>L10</li>
      <li>L11</li>
      <li>L12</li>
      <li>L13</li>
      <li>L14</li>
      <li>L15</li>
      <li>L16</li>
    </ul>
    <p class="ailis-dollhouse-note"><strong>Strongest anchors:</strong> tool invocation, discovery, routing and policy, memory, governance, application UX.</p>
  </article>

  <article id="dollhouse-collection" class="ailis-dollhouse-project lane-research">
    <span class="ailis-card-kicker">Catalog product</span>
    <h3>Dollhouse Collection</h3>
    <p>A public catalog and activation surface for personas, tools, and artifacts. It reads as a product at L16, but it likely depends on retrieval, manifests, and capability metadata underneath.</p>
    <ul class="ailis-dollhouse-layer-tags">
      <li>L9</li>
      <li>L11</li>
      <li>L16</li>
    </ul>
    <p class="ailis-dollhouse-note"><strong>Strongest anchors:</strong> discovery, metadata, catalog UX, installation and activation flows.</p>
  </article>

  <article id="mcp-aql-spec" class="ailis-dollhouse-project lane-protocol">
    <span class="ailis-card-kicker">Protocol layer</span>
    <h3>MCP-AQL spec</h3>
    <p>The clearest protocol-centered piece in the portfolio. It looks less like an application and more like a proposal for semantic operations, introspection, routing signals, and transport-aware behavior on top of MCP.</p>
    <ul class="ailis-dollhouse-layer-tags">
      <li>L10</li>
      <li>L11</li>
      <li>L12</li>
      <li>L13</li>
      <li>L15</li>
    </ul>
    <p class="ailis-dollhouse-note"><strong>Strongest anchors:</strong> operation semantics, registry and introspection, routing cues, protocol control, conformance.</p>
  </article>

  <article id="mcp-aql-adapters" class="ailis-dollhouse-project lane-protocol">
    <span class="ailis-card-kicker">Reference runtime</span>
    <h3>MCP-AQL adapters and reference implementations</h3>
    <p>The adapter and example layer is where the spec becomes executable. These pieces seem especially useful for testing the boundary between invocation, discovery, transport, and policy.</p>
    <ul class="ailis-dollhouse-layer-tags">
      <li>L10</li>
      <li>L11</li>
      <li>L12</li>
      <li>L13</li>
      <li>L15</li>
    </ul>
    <p class="ailis-dollhouse-note"><strong>Strongest anchors:</strong> CRUDE-style operations, runtime introspection, transport contracts, enforcement edges.</p>
  </article>

  <article id="mcp-aql-generator" class="ailis-dollhouse-project lane-protocol">
    <span class="ailis-card-kicker">Generator tooling</span>
    <h3>MCP-AQL generator and validator-style tooling</h3>
    <p>Generation and validation tooling might sit slightly differently from the reference adapters. They look less like end-user applications and more like infrastructure for producing, checking, and governing protocol artifacts.</p>
    <ul class="ailis-dollhouse-layer-tags">
      <li>L11</li>
      <li>L12</li>
      <li>L13</li>
      <li>L15</li>
    </ul>
    <p class="ailis-dollhouse-note"><strong>Strongest anchors:</strong> manifest generation, policy shaping, conformance checking, schema and transport expectations.</p>
  </article>

  <article id="elemental-surveys" class="ailis-dollhouse-project lane-research">
    <span class="ailis-card-kicker">Applied workflow</span>
    <h3>Elemental Surveys and other research applications</h3>
    <p>Public applied systems from Dollhouse Research likely show up as L16-first products, but they also reveal what is happening in context construction, orchestration, memory, and governance under the surface.</p>
    <ul class="ailis-dollhouse-layer-tags">
      <li>L8</li>
      <li>L12</li>
      <li>L14</li>
      <li>L15</li>
      <li>L16</li>
    </ul>
    <p class="ailis-dollhouse-note"><strong>Strongest anchors:</strong> workflow design, prompt assembly, human review paths, stateful sessions, application logic.</p>
  </article>

  <article id="merview" class="ailis-dollhouse-project lane-research">
    <span class="ailis-card-kicker">Companion app</span>
    <h3>Merview and adjacent public utilities</h3>
    <p>These are less about protocol invention and more about what people actually do with artifacts, reviews, drafts, or outputs once the lower layers have done their job.</p>
    <ul class="ailis-dollhouse-layer-tags">
      <li>L15</li>
      <li>L16</li>
    </ul>
    <p class="ailis-dollhouse-note"><strong>Strongest anchors:</strong> reviewability, rendering, artifact handling, end-user workflow surfaces.</p>
  </article>
</div>

## Layer view

The second read turns the same portfolio back into the layer model. This view makes it easier to see where the strongest Dollhouse Research examples cluster across the stack.

<div class="ailis-atlas-stack" aria-label="Mock-up mapping of public Dollhouse Research projects into AILIS layers">
  <section class="ailis-atlas-group lane-core">
    <div class="ailis-atlas-group-context">
      <strong>L0-L7</strong>
      <h2>Mostly external substrate</h2>
      <p>The current public Dollhouse Research portfolio does not differentiate itself primarily at the facilities, runtime, model compilation, quantization, or inference-engine layers. That is useful signal in itself.</p>
    </div>
    <ol>
      <li><a href="../../layers/l0-facilities-power/"><strong>L0-L2</strong><span>Infrastructure foundation</span><em>No strong public-first Dollhouse footprint today; these layers are mostly inherited from providers, devices, and external runtimes.</em></a></li>
      <li><a href="../../layers/l3-ml-graph-compilation/"><strong>L3-L7</strong><span>Model and inference stack</span><em>Possible indirect influence through model choice, adapters, and serving assumptions, but not where the public portfolio seems to lead.</em></a></li>
    </ol>
  </section>

  <section class="ailis-atlas-group lane-protocol">
    <div class="ailis-atlas-group-context">
      <strong>L8-L10</strong>
      <h2>Where public stack behavior starts to become visible</h2>
      <p>This band is where Dollhouse systems stop looking like generic AI consumption and start looking like opinionated application interfaces.</p>
    </div>
    <ol>
      <li><a href="../../layers/l8-context-construction-prompting/"><strong>L8</strong><span>Context Construction & Prompting</span><em>DollhouseMCP personas, skills, activation patterns, and research workflows such as Elemental Surveys likely express themselves here.</em></a></li>
      <li><a href="../../layers/l9-knowledge-retrieval/"><strong>L9</strong><span>Knowledge & Retrieval</span><em>Dollhouse Collection and related portfolio surfaces fit here where search, artifact lookup, grounding context, and installation metadata become useful.</em></a></li>
      <li><a href="../../layers/l10-tool-function-invocation/"><strong>L10</strong><span>Tool & Function Invocation</span><em>DollhouseMCP server capabilities, MCP-AQL semantic operations, and adapter runtimes look like especially strong examples at this boundary.</em></a></li>
    </ol>
  </section>

  <section class="ailis-atlas-group lane-protocol">
    <div class="ailis-atlas-group-context">
      <strong>L11-L15</strong>
      <h2>Where the portfolio may be most differentiated</h2>
      <p>A large share of the visible Dollhouse Research distinctiveness lives here rather than in model weights or generic application chrome.</p>
    </div>
    <ol>
      <li><a href="../../layers/l11-addressing-registry/"><strong>L11</strong><span>Addressing & Registry</span><em>Dollhouse Collection metadata, MCP-AQL introspection, adapter manifests, and capability discovery are strong examples at this layer.</em></a></li>
      <li><a href="../../layers/l12-routing-planning-policy/"><strong>L12</strong><span>Routing, Planning & Policy</span><em>MCP-AQL semantic routing, DollhouseMCP approval paths, and workflow selection logic appear to cluster in this layer.</em></a></li>
      <li><a href="../../layers/l13-transport-flow-semantics/"><strong>L13</strong><span>Transport & Flow Semantics</span><em>MCP-AQL transport rules, reference adapters, streaming behavior, and execution lifecycle semantics make this layer more concrete.</em></a></li>
      <li><a href="../../layers/l14-session-identity-memory/"><strong>L14</strong><span>Session, Identity & Memory</span><em>DollhouseMCP memory features, session continuity, user-scoped behavior, and stateful applied workflows seem like natural examples here.</em></a></li>
      <li><a href="../../layers/l15-governance-safety-schema/"><strong>L15</strong><span>Governance, Safety & Schema</span><em>Danger-zone controls, review and approval logic, generator validation, and schema or conformance tooling are strong portfolio-specific examples.</em></a></li>
    </ol>
  </section>

  <section class="ailis-atlas-group lane-research">
    <div class="ailis-atlas-group-context">
      <strong>L16+</strong>
      <h2>Where people experience the portfolio directly</h2>
      <p>This is the layer most visible to outside users: sites, workflows, utilities, and research applications that make the lower layers legible through an actual product surface.</p>
    </div>
    <ol>
      <li><a href="../../layers/l16-application-domain-logic/"><strong>L16</strong><span>Application & Domain Logic</span><em>Dollhouse Collection, Elemental Surveys, Merview, and the user-facing surface of DollhouseMCP all look like natural examples in this layer.</em></a></li>
    </ol>
  </section>
</div>

## Implications for the atlas

This case study suggests a simple editorial rule for the layer pages: only add named Dollhouse Research examples where the public portfolio contributes real signal.

- It shows that a real portfolio can span many layers without collapsing the model.
- It highlights that the current public Dollhouse Research work is strongest in the application-interface and orchestration bands.
- It might give the AILIS layer pages more concrete examples without turning them into branded marketing pages.
- It creates a path for future case studies from other ecosystems, which is probably the healthier long-term move.

That would make L10, L11, L12, L14, L15, and L16 the strongest candidate pages for brief named examples, while leaving L0-L7 mostly grounded in broader ecosystem references.
