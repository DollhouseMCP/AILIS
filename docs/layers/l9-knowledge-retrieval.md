---
title: L9 - Knowledge & Retrieval
---

<!-- markdownlint-disable MD013 MD033 -->

# L9 - Knowledge & Retrieval

L9 covers knowledge stores, vector indexes, graph retrieval, embeddings for search, reranking, grounding, citations, and data freshness. It is where systems decide what external knowledge should become available to the model.

<div class="ailis-layer-infographic lane-protocol" aria-label="L9 knowledge and retrieval infographic">
  <div><strong>L9</strong><span>Knowledge & Retrieval</span></div>
  <ol>
    <li>Indexes</li>
    <li>Embeddings</li>
    <li>Reranking</li>
    <li>Citations</li>
  </ol>
</div>

## What belongs here

L9 is broader than vector databases. It includes ingestion, retrieval strategy, citation policy, freshness, data permissions, and the bridge between knowledge systems and prompt construction.

## Representative projects

| Project | Why it might fit | Adjacent layers |
| --- | --- | --- |
| [Pinecone](https://docs.pinecone.io/) | Managed vector database for semantic retrieval. | L9 retrieval, L15 governance |
| [Milvus](https://github.com/milvus-io/milvus) | Open-source vector database and similarity search engine. | L9 retrieval, L11 registry |
| [Weaviate](https://weaviate.io/developers/weaviate) | Vector database with schema, hybrid search, and integrations. | L9 retrieval, L15 schema |
| [Qdrant](https://qdrant.tech/documentation/) | Vector search engine and database for embeddings. | L9 retrieval, L16 applications |
| [Chroma](https://docs.trychroma.com/) | Embedding database often used in local and developer RAG workflows. | L9 retrieval, L8 context |
| [Elasticsearch vector search](https://www.elastic.co/docs/solutions/search/vector) | Search platform adding vector and hybrid retrieval patterns. | L9 retrieval, L16 search products |

## Boundary questions

- Are embedding models part of L5, L6, or L9 when their main purpose is retrieval?
- Should document access control be modeled in L9, L14 identity, or L15 governance?
- Does citation generation belong to retrieval, prompting, or application UX?

## Signals to watch

- Hybrid lexical/vector retrieval becoming the default.
- Retrieval systems carrying provenance, freshness, and permissions as first-class metadata.
- More evaluation pressure on whether RAG answers are grounded, complete, and citation-faithful.

## Links

- [Previous layer: L8 Context Construction & Prompting](l8-context-construction-prompting.md)
- [Back to the primer layer](../proposals/AILIS_Primer.md#l9-knowledge-retrieval)
- [Next layer: L10 Tool & Function Invocation](l10-tool-function-invocation.md)
