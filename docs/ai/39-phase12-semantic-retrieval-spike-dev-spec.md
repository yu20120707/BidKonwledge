# Phase 12 Semantic Retrieval Adapter Spike Dev Spec

## Purpose

Phase 12 evaluates whether Qdrant, Haystack, and embeddings should become an
optional semantic retrieval path for the BidKnowledge demo.

This phase is a spike and evaluation track. It must not replace the current
deterministic retrieval default.

## Execution Level

- Harness mode: `large`
- Task level: Level 2 / medium
- Reason: the first slice is documentation and evaluation planning across
  several docs and `.ai` runtime files. The possible follow-up code path is
  bounded to a replaceable adapter boundary and fake-testable tests.

Escalate to Level 3 if Phase 12 changes any of these:

1. public `/api/retrieve` request or response contract
2. SQLite schema or persisted chunk/card contract
3. default runtime dependencies
4. normal test requirements
5. production retrieval behavior

## Baseline

The Phase 11 fixed sample set is the comparison baseline:

- `docs/ai/sample-outputs/phase11/manifest.json`
- `docs/ai/sample-outputs/phase11/retrieval-evidence.json`
- `docs/ai/38-phase11-repeatable-demo-runbook.md`

The current retrieval path is deterministic:

```text
POST /api/retrieve
-> backend.app.api.retrieval.retrieve()
-> backend.app.services.retrieval.retrieve_chunks()
-> backend.app.storage.database.list_retrievable_chunks()
-> SQLite document_chunks joined with documents
```

Current behavior:

1. requires at least one of `query` or `tag`
2. filters by exact deterministic tag when provided
3. scores by simple query term occurrences
4. returns the existing `RetrievalResponse`
5. does not require Qdrant, Haystack, embeddings, LLMs, or network access

## External Component Findings

These are integration facts for the spike, not default project dependencies.

### Qdrant

Qdrant is a candidate optional vector store. Official documentation supports:

1. local Docker startup for development
2. Python client local mode for quick local use
3. collections of vectors plus payload metadata
4. named dense and sparse vectors for later hybrid retrieval
5. payload indexes for faster filtering on real datasets

Useful Phase 12 boundary:

```text
BidKnowledge chunks/cards
-> semantic payload mapper
-> optional Qdrant collection
-> semantic query
-> BidKnowledge retrieval-like evidence rows
```

Do not write customer source files, runtime uploads, model caches, or Qdrant
storage into Git.

### Haystack

Haystack is a candidate optional pipeline wrapper around indexing and query
components. Official documentation provides:

1. `QdrantDocumentStore` through the separate `qdrant-haystack` integration
2. dense `QdrantEmbeddingRetriever`
3. sparse and hybrid Qdrant retrievers
4. document and text embedders, including Sentence Transformers and OpenAI
   embedding components

Useful Phase 12 boundary:

```text
payload mapper
-> Haystack Document objects
-> DocumentEmbedder
-> QdrantDocumentStore / DocumentWriter
-> TextEmbedder
-> Qdrant retriever
```

Haystack should be treated as adapter implementation detail. It must not leak
into the existing API response contract during the spike.

### Embeddings

Candidate embedding strategies:

1. local model: BGE-M3 or another Chinese/multilingual sentence-transformer
   model
2. provider-backed embeddings through an OpenAI-compatible or vendor-specific
   embedder
3. fake deterministic vectors for automated adapter tests only

BGE-M3 is attractive for this domain because its model card describes
multilingual support, different input granularities, and dense/sparse/multi-
vector retrieval functions. It is still optional and should not be downloaded
by normal tests.

Provider-backed embeddings require secrets and network access, so they belong
only in manual smoke or explicitly skipped integration checks.

## Proposed Adapter Boundary

If Phase 12 proceeds to code, introduce a boundary that can be tested without
Qdrant, Haystack, or real embeddings:

```text
SemanticRetrievalAdapter
  index(records: list[SemanticRetrievalRecord]) -> SemanticIndexResult
  query(query: str | None, tag: str | None, top_k: int) -> list[SemanticMatch]
```

Suggested record fields:

1. `chunk_id`
2. `document_id`
3. `section_id`
4. `section_title`
5. `section_path`
6. `text`
7. `tags`
8. `source_filename`
9. `doc_role`
10. `file_ext`
11. `page_start`
12. `page_end`
13. `metadata`

Suggested implementations:

1. `DeterministicSemanticRetrievalAdapter` or fake adapter for tests
2. optional Qdrant/Haystack adapter behind lazy imports
3. optional embedding provider interface behind lazy imports

Default retrieval must keep using `backend.app.services.retrieval.retrieve_chunks`.

## API Boundary

Do not change `/api/retrieve` during the first spike.

Preferred Phase 12 code path, if approved:

1. add internal adapter classes and tests
2. add an evaluation-only script or service function that compares deterministic
   and semantic results on Phase 11 sample records
3. keep all Qdrant/Haystack paths opt-in through explicit function calls,
   environment variables, or manual smoke commands

Avoid adding a public endpoint until the evaluation report shows a concrete
demo benefit.

## Minimal Spike Plan

### Stage 1 - Documentation And Decision Plan

Status: complete.

Deliver:

1. this dev spec
2. Phase 12 test cases
3. initial evaluation report
4. updated `.ai` runtime artifacts

Decision:

- proceed to adapter skeleton only if the boundary is accepted
- otherwise stop with a documented deferral
- do not invent Phase 13; no Phase 13 scope is defined in the repository yet

### Stage 2 - Adapter Skeleton With Fake Tests

Potential follow-up code.

Deliver:

1. semantic retrieval record/match dataclasses or Pydantic models
2. fake deterministic semantic adapter
3. mapper from existing SQLite chunk rows to semantic records
4. tests proving deterministic `/api/retrieve` does not require semantic deps
5. tests proving fake semantic adapter returns source metadata

No Qdrant, Haystack, model download, or network access required.

### Stage 3 - Optional Local Qdrant Smoke

Manual or skipped integration path.

Deliver:

1. local Qdrant setup notes
2. collection naming and payload schema
3. index a tiny Phase 11-derived redacted sample set
4. query the three fixed Phase 11 tags
5. record dependency setup, latency, observed matches, and cleanup

Do not add Qdrant as a normal test dependency.

### Stage 4 - Optional Haystack Pipeline Smoke

Manual or skipped integration path.

Deliver:

1. minimal Haystack indexing pipeline shape
2. minimal query pipeline shape
3. comparison with direct Qdrant client complexity
4. decision on whether Haystack adds enough value for this demo

Do not expose Haystack types in API schemas.

### Stage 5 - Evaluation Decision

Update `docs/ai/41-phase12-evaluation-report.md` with one of:

1. keep semantic retrieval optional and continue toward a controlled prototype
2. defer semantic retrieval because deterministic retrieval is sufficient for
   the demo
3. promote a narrow optional semantic path, still keeping deterministic as the
   default

## Acceptance Criteria

1. Phase 12 clearly separates deterministic default retrieval from optional
   semantic retrieval.
2. The Phase 11 sample set is the comparison baseline.
3. Qdrant, Haystack, and embeddings remain optional and lazily integrated.
4. Normal tests do not require Qdrant, Haystack, model downloads, API keys, or
   network access.
5. Any code follow-up has an adapter boundary before real external components.
6. The evaluation report states the next implementation decision explicitly.

## References

- Qdrant local quickstart: https://qdrant.tech/documentation/quickstart/
- Qdrant collections and vector schema: https://qdrant.tech/documentation/manage-data/collections/
- Qdrant security: https://qdrant.tech/documentation/security/
- Haystack QdrantDocumentStore: https://docs.haystack.deepset.ai/docs/qdrant-document-store
- Haystack Qdrant integration reference: https://docs.haystack.deepset.ai/reference/integrations-qdrant
- Haystack embedders: https://docs.haystack.deepset.ai/docs/embedders
- Haystack SentenceTransformersDocumentEmbedder: https://docs.haystack.deepset.ai/docs/sentencetransformersdocumentembedder
- Haystack OpenAIDocumentEmbedder: https://docs.haystack.deepset.ai/docs/openaidocumentembedder
- BGE-M3 model card: https://huggingface.co/BAAI/bge-m3
