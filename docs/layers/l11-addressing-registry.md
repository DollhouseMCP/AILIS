---
title: L11 - Addressing & Registry
---

<!-- markdownlint-disable MD013 MD033 MD046 -->

# L11 - Addressing & Registry

L11 covers discovery, naming, manifests, capability metadata, signed artifacts, provenance, versioning, fingerprints, and registries for models, tools, datasets, prompts, adapters, indices, and ensembles.

<div class="ailis-layer-infographic lane-protocol" aria-label="L11 addressing and registry infographic">
  <div><strong>L11</strong><span>Addressing & Registry</span></div>
  <ol>
    <li>Discovery</li>
    <li>Manifests</li>
    <li>Signatures</li>
    <li>Capability metadata</li>
  </ol>
</div>

## What belongs here

L11 asks how a system knows what exists, what version it is, what capabilities it claims, what evidence supports those claims, and whether the artifact can be trusted. AILIS currently treats this as one of the more under-served middle layers.

## Representative projects

| Project | Why it might fit | Adjacent layers |
| --- | --- | --- |
| [Hugging Face Hub](https://huggingface.co/docs/hub/) | Registry and collaboration platform for models, datasets, and spaces. | L6 models, L11 registry |
| [Docker Hub and OCI registries](https://docs.docker.com/docker-hub/) | Image naming, versioning, and distribution patterns that may inspire AI artifact registries. | L2 runtime, L11 registry |
| [MLflow Model Registry](https://mlflow.org/docs/latest/ml/model-registry/) | Model versioning, lifecycle, and registry workflow. | L6 models, L15 governance |
| [Sigstore](https://docs.sigstore.dev/) | Signing and provenance infrastructure relevant to artifact trust. | L11 addressing, L15 governance |
| [OpenAPI descriptions](https://spec.openapis.org/oas/latest.html) | Machine-readable API descriptions that can be registered and discovered. | L10 tools, L11 registry |
| [Model Context Protocol server ecosystem](https://modelcontextprotocol.io/) | MCP servers raise registry and capability-discovery questions for AI tools. | L10 tools, L13 transport |

## Boundary questions

- What is the minimum useful manifest for a model, tool, index, prompt, or ensemble?
- Should capability vectors be registered claims, measured evidence, or both?
- How should registries represent incompatible versions, deprecations, and security advisories?

## Signals to watch

- Signed AI artifacts becoming a default expectation.
- Capability metadata moving from marketing claims into machine-readable evidence.
- Tool and model discovery becoming provider-neutral rather than application-specific.

## Links

- [Previous layer: L10 Tool & Function Invocation](l10-tool-function-invocation.md)
- [Back to the primer layer](../proposals/AILIS_Primer.md#l11-addressing-registry)
- [Next layer: L12 Routing, Planning & Policy](l12-routing-planning-policy.md)
