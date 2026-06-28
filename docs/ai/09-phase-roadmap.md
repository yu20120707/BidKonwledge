# Phase Roadmap

## Phase 0 - Repository And Context Initialization

Status: complete.

Done:

1. Initialized Git repository.
2. Applied Auto_AICoding_Harness in medium mode with `python-backend-service` profile.
3. Created durable project context under `docs/ai/`.
4. Copied lightweight source documents into `docs/source-materials/originals/`.
5. Indexed large external sample materials without copying them into Git.

## Phase 1 - Minimal Backend Foundation

Goal: create a runnable backend base without RAG features.

Harness requirement: all Phase 1 development must run in `large` mode and must execute project scripts before completion.

Scope:

1. FastAPI app startup.
2. `GET /health`.
3. `POST /api/files/upload`.
4. Local file saving under `data/uploads`.
5. Document metadata schema.
6. SQLite initialization.
7. Basic configuration management.
8. Minimal smoke tests.
9. README startup commands.

Explicitly excluded:

- OCR
- LLM calls
- embeddings
- vector store
- knowledge cards
- tender analysis
- demo page
- user system
- Word/PDF export

## Phase 2 - Document Parsing And Chunking

Goal: parse sample docx/text-based pdf files into normalized chunks.

Scope:

1. Docling adapter.
2. Unified chunk schema.
3. Section splitting.
4. Initial deterministic tag rules.
5. Parse-status and error handling.
6. Tests with 1-2 small representative files.

## Phase 3 - Retrieval

Status: complete.

Goal: retrieve historical chunks by tag and query.

Scope:

1. `POST /api/retrieve`.
2. Local deterministic retrieval over Phase 2 SQLite chunks.
3. Exact tag filtering.
4. Simple query keyword matching.
5. Metadata-preserving chunk result format.
6. Retrieval tests with temporary upload roots and SQLite DBs.

Implementation decision:

- The original roadmap considered Qdrant, Haystack, and dense retrieval for
  Phase 3. The implemented Phase 3 intentionally uses deterministic local
  retrieval first because the accepted scope was the smallest backend closure
  over already-persisted chunks.

Deferred:

- Qdrant adapter.
- Haystack runtime pipeline.
- Embeddings and dense retrieval.
- Hybrid retrieval.

## Phase 4 - Generation, Citations, And Risks

Status: complete.

Goal: generate candidate content from retrieval context.

Scope:

1. `POST /api/generate`.
2. OpenAI-compatible LLM adapter boundary.
3. Fake-LLM injection seam for automated tests.
4. Prompt builder over Phase 3 retrieval context.
5. Citation-preserving answer formatter.
6. Rule-based risk checker for empty generation and missing citations.
7. `need_human_review = true` always.

Deferred:

- Live external LLM provider smoke with real credentials.
- Full tender deep analysis.
- Final human-approved bidding document output.

## Phase 5 - Demo Page And Script

Status: complete.

Goal: present the full capability chain to a stakeholder.

Input baseline:

1. Phase 1 upload and SQLite metadata are available.
2. Phase 2 parsing/chunking is available for small `.docx` and text-based
   `.pdf`; OCR/scanned PDFs remain out of scope.
3. Phase 3 local retrieval is available through `POST /api/retrieve`.
4. Phase 4 candidate generation is available through `POST /api/generate`.
5. Automated tests pass with fake parsers/fake LLM where appropriate; a real
   external LLM key is optional for manual demo smoke.
6. All generated content remains candidate content and must show
   `need_human_review = true`.

Scope:

1. Minimal upload/query/result page.
2. Demo script using selected sample files.
3. Raw JSON display.
4. Manual verification notes for citations and risk hints.

Implemented:

1. `GET /demo`.
2. FastAPI-hosted static demo page.
3. Page controls for upload, parse, retrieve, and generate.
4. Raw JSON display.
5. Citations, risks, and `need_human_review` display areas.
6. Pytest coverage for route availability, expected API hooks, and Phase 5
   boundary constraints.

Out of scope:

- OCR/PaddleOCR.
- Qdrant/Haystack/dense retrieval.
- Production authentication or user management.
- Word/PDF export.
- Treating generated text as final approved bidding content.
