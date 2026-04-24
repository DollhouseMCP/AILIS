---
title: Home
hide:
  - navigation
  - toc
---

<!-- markdownlint-disable MD013 MD033 MD046 -->

<div class="ailis-home">

<section class="ailis-hero">
  <div>
    <div class="ailis-brand-lockup" aria-label="Dollhouse Research and AILIS">
      <span class="ailis-brand-logo is-org" aria-hidden="true"></span>
      <span class="ailis-brand-logo is-ailis" aria-hidden="true"></span>
      <strong>Dollhouse Research Project: AILIS</strong>
    </div>
    <span class="ailis-eyebrow">A Dollhouse Research Project</span>
    <h1>A research map for the AI ecosystem.</h1>
    <p class="ailis-lead">
      AILIS (AI Layer Interface Specification) is a Dollhouse Research white
      paper exploring a 16+ layer vocabulary for AI systems, from physical
      compute up through orchestration, governance, protocols, products, and
      domain behavior.
    </p>
    <div class="ailis-actions">
      <a class="ailis-button ailis-button-primary" href="proposals/AILIS_Primer/">Read the Primer</a>
      <a class="ailis-button ailis-button-secondary" href="proposals/AILIS_Cheat_Sheet/">Open the Cheat Sheet</a>
      <a class="ailis-button ailis-button-secondary" href="https://github.com/DollhouseMCP/AILIS/discussions">Join the Discussion</a>
    </div>
  </div>

  <aside class="ailis-layer-overview" aria-label="AILIS layer model overview">
    <span class="ailis-card-kicker">Layer Model</span>
    <h2>The AILIS 16+ Proposal</h2>
    <p>
      A draft map for locating architecture concerns across the AI stack.
      The boundaries are intentionally open to critique.
    </p>

    <div class="ailis-hero-layer-map" aria-label="Expandable AILIS layer groups">
      <details class="ailis-layer-group">
        <summary><strong>L0-L2</strong><span>Infrastructure foundation</span></summary>
        <ul>
          <li><a href="layers/l0-facilities-power/">L0 Facilities & Power</a></li>
          <li><a href="layers/l1-compute-fabric/">L1 Compute Fabric</a></li>
          <li><a href="layers/l2-system-driver-runtime/">L2 System & Driver Runtime</a></li>
        </ul>
      </details>
      <details class="ailis-layer-group">
        <summary><strong>L3-L7</strong><span>Model and inference stack</span></summary>
        <ul>
          <li><a href="layers/l3-ml-graph-compilation/">L3 ML Graph & Compilation</a></li>
          <li><a href="layers/l4-numeric-quantization/">L4 Numeric & Quantization</a></li>
          <li><a href="layers/l5-tokenization-encoders/">L5 Tokenization & Encoders</a></li>
          <li><a href="layers/l6-model-parameters-architecture/">L6 Model Parameters & Architecture</a></li>
          <li><a href="layers/l7-inference-engine-decoding/">L7 Inference Engine & Decoding</a></li>
        </ul>
      </details>
      <details class="ailis-layer-group">
        <summary><strong>L8-L10</strong><span>AI application interface</span></summary>
        <ul>
          <li><a href="layers/l8-context-construction-prompting/">L8 Context Construction & Prompting</a></li>
          <li><a href="layers/l9-knowledge-retrieval/">L9 Knowledge & Retrieval</a></li>
          <li><a href="layers/l10-tool-function-invocation/">L10 Tool & Function Invocation</a></li>
        </ul>
      </details>
      <details class="ailis-layer-group">
        <summary><strong>L11-L15</strong><span>Orchestration layers</span></summary>
        <ul>
          <li><a href="layers/l11-addressing-registry/">L11 Addressing & Registry</a></li>
          <li><a href="layers/l12-routing-planning-policy/">L12 Routing, Planning & Policy</a></li>
          <li><a href="layers/l13-transport-flow-semantics/">L13 Transport & Flow Semantics</a></li>
          <li><a href="layers/l14-session-identity-memory/">L14 Session, Identity & Memory</a></li>
          <li><a href="layers/l15-governance-safety-schema/">L15 Governance, Safety & Schema</a></li>
        </ul>
      </details>
      <details class="ailis-layer-group">
        <summary><strong>L16+</strong><span>Application and domain logic</span></summary>
        <ul>
          <li><a href="layers/l16-application-domain-logic/">L16 Application & Domain Logic</a></li>
        </ul>
      </details>
    </div>
  </aside>
</section>

<section class="ailis-section ailis-layer-detail">
  <span class="ailis-pill">Layer Model</span>
  <h2>The first thing to see is the stack.</h2>
  <p class="ailis-subtle">
    The draft groups the AI ecosystem into practical zones. It is asking
    whether this kind of map could make architecture discussions clearer,
    especially where infrastructure, model behavior, protocols, orchestration,
    governance, and products blur together.
  </p>

  <div class="ailis-callout">
    AILIS is not trying to enforce a compliance model, and it is expected to
    change as people test it against real systems.
  </div>
</section>

<section class="ailis-band ailis-research-position">
  <div class="ailis-band-inner">
    <span class="ailis-pill">Research Context</span>
    <h2>AILIS is one research project from Dollhouse Research.</h2>
    <p class="ailis-subtle">
      This site is focused on AILIS: a public white-paper effort for describing
      AI system layers. DollhouseMCP and MCP-AQL are related public projects
      from the same research home, shown here as portfolio context rather than
      dependencies of AILIS.
    </p>

    <div class="ailis-portfolio-context" aria-label="Dollhouse Research portfolio context">
      <div class="ailis-portfolio-home lane-org">
        <span class="ailis-portfolio-logo is-org" aria-hidden="true"></span>
        <span class="ailis-card-kicker">Research Home</span>
        <h3>Dollhouse Research</h3>
        <p>
          An applied AI systems research home for public papers, protocols,
          infrastructure work, and experiments as they become ready to share.
        </p>
        <a href="https://dollhouseresearch.com">Open Dollhouse Research</a>
      </div>

      <div class="ailis-portfolio-list" aria-label="Public Dollhouse Research work">
        <article class="ailis-portfolio-item is-current lane-research">
          <span class="ailis-logo-pair" aria-hidden="true">
            <span class="ailis-portfolio-logo is-org"></span>
            <span class="ailis-portfolio-logo is-ailis"></span>
          </span>
          <span class="ailis-card-kicker">Current project</span>
          <h3>AILIS</h3>
          <p>White paper and vocabulary for understanding AI system layers.</p>
          <a href="proposals/AILIS_Primer/">Read the Primer</a>
        </article>
        <article class="ailis-portfolio-item lane-core">
          <span class="ailis-portfolio-logo is-core" aria-hidden="true"></span>
          <span class="ailis-card-kicker">Peer project</span>
          <h3>DollhouseMCP</h3>
          <p>Distributable MCP server with broad capability and safety controls.</p>
          <a href="https://dollhousemcp.com">Open DollhouseMCP</a>
        </article>
        <article class="ailis-portfolio-item lane-protocol">
          <span class="ailis-logo-pair" aria-hidden="true">
            <span class="ailis-portfolio-logo is-protocol"></span>
            <span class="ailis-mcpaql-frame">
              <span class="ailis-mcpaql-mark"></span>
            </span>
          </span>
          <span class="ailis-card-kicker">Peer project</span>
          <h3>MCP-AQL</h3>
          <p>Protocol layer on top of MCP for semantic routing and introspection.</p>
          <a href="https://mcpaql.com">Open MCP-AQL</a>
        </article>
      </div>
    </div>
  </div>
</section>

<section class="ailis-band">
  <div class="ailis-band-inner">
    <span class="ailis-pill">Related Example</span>
    <h2>Semantic routing as a layer-boundary example.</h2>
    <p class="ailis-subtle">
      MCP-AQL is useful context for AILIS because it shows how protocol semantics,
      safety classification, runtime discovery, and token economics can be
      separated from application behavior.
    </p>

    <div class="md-typeset__table ailis-mcpaql-routing-table">
      <table>
        <thead>
          <tr>
            <th>MCP-AQL concern</th>
            <th>AILIS lens</th>
            <th>Why it matters</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>CRUDE endpoints</td>
            <td>L10-L13 tool, routing, and transport semantics</td>
            <td>Operation intent is explicit before a client acts.</td>
          </tr>
          <tr>
            <td>Runtime introspection</td>
            <td>L11 registry and capability discovery</td>
            <td>Clients can discover valid operations on demand.</td>
          </tr>
          <tr>
            <td>Permission classification</td>
            <td>L12-L15 policy, safety, and governance</td>
            <td>Read, delete, and execute paths can receive different controls.</td>
          </tr>
          <tr>
            <td>Token reduction</td>
            <td>L8-L10 context construction and tool exposure</td>
            <td>Large tool menus do not have to be loaded up front.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="ailis-section">
  <span class="ailis-pill">Quick Path</span>
  <h2>Start here if you are new to AILIS.</h2>
  <div class="ailis-card-grid">
    <article class="ailis-card">
      <span class="ailis-card-kicker">10 minutes</span>
      <h3>Read the Primer</h3>
      <p>Get the full layer model, motivation, and open questions.</p>
      <a href="proposals/AILIS_Primer/">Open Primer</a>
    </article>
    <article class="ailis-card">
      <span class="ailis-card-kicker">2 minutes</span>
      <h3>Use the Cheat Sheet</h3>
      <p>Scan the layer definitions and cross-cutting control planes.</p>
      <a href="proposals/AILIS_Cheat_Sheet/">Open Cheat Sheet</a>
    </article>
    <article class="ailis-card">
      <span class="ailis-card-kicker">Contribute</span>
      <h3>Share critique</h3>
      <p>Challenge the model, submit a use case, or propose a different framing.</p>
      <a href="FEEDBACK/">Review feedback areas</a>
    </article>
    <article class="ailis-card">
      <span class="ailis-card-kicker">Build locally</span>
      <h3>Preview the site</h3>
      <p>Use MkDocs to run the documentation site and validate changes.</p>
      <a href="website-workflows/">Open website workflow</a>
    </article>
  </div>
</section>

<section class="ailis-band">
  <div class="ailis-band-inner">
    <span class="ailis-pill">Open Questions</span>
    <h2>What we are asking the community.</h2>
    <ul class="ailis-timeline">
      <li>
        <strong>Resonance</strong>
        <p>Does this framing make AI architecture easier to discuss, or does it feel forced?</p>
      </li>
      <li>
        <strong>Boundaries</strong>
        <p>Which layers are missing, overloaded, or miscategorized?</p>
      </li>
      <li>
        <strong>Alternatives</strong>
        <p>Are there better ways to describe these interfaces and control planes?</p>
      </li>
      <li>
        <strong>Evidence</strong>
        <p>Which real-world systems should be mapped first to test whether AILIS holds up?</p>
      </li>
    </ul>
    <div class="ailis-callout">
      Critical feedback is especially valuable. The goal is a useful conversation,
      not a polished diagram that hides uncertainty.
    </div>
  </div>
</section>

<section class="ailis-section">
  <span class="ailis-pill">Explore</span>
  <h2>Proposal resources</h2>
  <div class="ailis-card-grid">
    <article class="ailis-card">
      <h3>All Proposals</h3>
      <p>Browse current and upcoming proposal material.</p>
      <a href="proposals/">Open proposals</a>
    </article>
    <article class="ailis-card">
      <h3>Reference Code</h3>
      <p>Review examples and implementation sketches.</p>
      <a href="reference/">Open reference</a>
    </article>
    <article class="ailis-card">
      <h3>Case Studies</h3>
      <p>Use real systems to pressure-test the layer model.</p>
      <a href="studies/">Open studies</a>
    </article>
    <article class="ailis-card">
      <h3>GitHub Discussions</h3>
      <p>Join open conversation about alternatives and critiques.</p>
      <a href="https://github.com/DollhouseMCP/AILIS/discussions">Open discussions</a>
    </article>
  </div>
</section>

</div>
