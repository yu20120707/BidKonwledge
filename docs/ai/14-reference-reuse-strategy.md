# Reference Reuse Strategy

## Decision

Do not directly fork a full RAG platform as the main business repository.

Use this repository as the business codebase, and use selected external repositories as reference material outside Git:

```text
F:\BidKonwledge              # business repository
F:\BidKonwledge_refs         # external reference repositories, not committed
├── ragflow
└── haystack-demos
```

## Repositories Pulled For Reference

| Repository | Local Path | Commit | Use |
| --- | --- | --- | --- |
| `https://github.com/infiniflow/ragflow.git` | `F:\BidKonwledge_refs\ragflow` | `f90be41` | Product reference: document ingestion UX, citation display, RAG workflow shape, deployment complexity. |
| `https://github.com/deepset-ai/haystack-demos.git` | `F:\BidKonwledge_refs\haystack-demos` | `17e6103` | Engineering reference: Haystack pipeline wrappers, Qdrant indexing/query demo, upload-to-index flow. |

Both were cloned shallowly outside the main repository.

## Can We Directly Build On Someone Else's Project?

Yes, but only under a narrow condition: if the delivery goal changes from "投标智能知识库能力验证 Demo" to "ship or customize an existing RAG platform".

For the current PRD, direct platform forking is not the best default.

## Option Assessment

### Option A - Directly Fork RAGFlow

Pros:

- Already has a full RAG product shape.
- Has document ingestion, chunking, retrieval, citations, UI, Docker deployment.
- Apache-2.0 license is acceptable for reference and possible reuse.

Cons:

- Heavy full-stack platform, not a thin FastAPI demo.
- Uses Flask/Quart backend, React frontend, Docker services, MySQL, Redis, MinIO, and search/vector infrastructure.
- Requires more environment work before we can show a small custom bidding workflow.
- Customizing the product down to our narrow PRD may be slower than building the thin vertical slice.

Verdict:

Use as product reference. Do not make it the main repo unless we intentionally pivot to a RAGFlow customization project.

### Option B - Directly Fork Haystack Demos

Pros:

- Small examples of indexing/query pipelines.
- The `qdrant_indexing` demo directly shows upload -> embed -> write to Qdrant and query -> retrieve from Qdrant.
- Good fit for later Phase 3 retrieval implementation.

Cons:

- It is a demo collection, not a bidding-product backend.
- It uses Hayhooks deployment patterns that may be more than we need in Phase 1.

Verdict:

Use as code reference for pipeline shape. Do not make it the main repo.

### Option C - Use Libraries And Build A Thin Business Shell

Pros:

- Not from zero: FastAPI, Haystack, Docling, Qdrant, and PaddleOCR provide most heavy capability.
- Keeps PRD scope narrow.
- Lets us implement the exact upload/API/metadata/citation/risk contract we need.
- Easier for Codex to work in bounded phases.

Cons:

- We must write the glue code ourselves.
- We need to design our own minimal data model and demo UI.

Verdict:

Recommended path.

## Reuse Rules

1. Do not copy external repository source into `F:\BidKonwledge` unless a later task explicitly approves it.
2. Prefer dependency usage over source vendoring.
3. If copying a small snippet becomes necessary, record source file, commit, license, and adaptation notes in the implementing PR/task.
4. Keep RAGFlow as a product and UX reference.
5. Keep Haystack demos as an engineering reference.
6. Treat direct RAGFlow customization as a separate spike, not as the default mainline.

## Not From Zero Means

The project should not hand-roll:

- document parsing engines
- vector database internals
- embedding pipelines
- RAG orchestration primitives
- OCR engines

The project should own:

- bidding-domain API contract
- document metadata model
- tag taxonomy and risk rules
- source citation response format
- minimal demo flow
- integration tests and smoke scripts
