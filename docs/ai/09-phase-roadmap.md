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

## Phase 6 - Knowledge Cards And PRD Tags

Status: complete.

See `docs/ai/17-lightweight-prd-completion-plan.md`.

Goal: turn parsed historical bid chunks into source-traceable knowledge cards
with deterministic PRD-aligned tags.

Implemented:

1. SQLite `knowledge_cards` table.
2. Deterministic card builder over parsed `historical_bid` chunks.
3. PRD-aligned keyword tags.
4. `POST /api/knowledge/build`.
5. `GET /api/documents/{document_id}/knowledge-cards`.
6. Source traceability fields for later citations and demo display.

Phase 6 documents:

- `docs/ai/18-phase6-knowledge-cards-dev-spec.md`
- `docs/ai/19-phase6-test-cases.md`
- `docs/ai/20-phase6-demo-runbook.md`

## Phase 7 - Tender Analysis

Status: complete.

Goal: make the new tender-file side of the PRD visible through deterministic
requirements, scoring item, and disqualification risk extraction.

Implemented:

1. Add `tender_analyses` persistence.
2. Add deterministic analyzer over parsed `tender` chunks.
3. Add `POST /api/tender/analyze`.
4. Add `GET /api/documents/{document_id}/tender-analysis`.
5. Preserve evidence traceability and always require human review.

Phase 7 documents:

- `docs/ai/21-phase7-tender-analysis-dev-spec.md`
- `docs/ai/22-phase7-test-cases.md`
- `docs/ai/23-phase7-demo-runbook.md`

## Phase 8A - Legacy / Mislabeled Word Conversion Adapter

Status: complete.

Goal: remove the real tender-sample blocker where a file has a `.docx`
extension but legacy OLE `.doc` content.

Implemented:

1. Parse-time content format detection.
2. Detection for true `.docx` ZIP content, PDF content, text content, and legacy
   OLE Word content.
3. Optional Word converter adapter with fake-testable interface.
4. Windows Word COM implementation for local manual smoke.
5. Internal derived `.docx` conversion path.
6. Parse metadata for detection and conversion evidence.
7. Tests that do not require real Word COM, OCR, vector services, or LLMs.

Phase 8A documents:

- `docs/ai/24-phase8a-word-conversion-dev-spec.md`
- `docs/ai/25-phase8a-test-cases.md`
- `docs/ai/26-phase8a-demo-runbook.md`

## Phase 8B - OCR Adapter For Scanned PDFs

Status: complete.

Goal: support lightweight OCR for scanned PDFs without making OCR a default
dependency.

Implemented:

1. Fake-testable OCR adapter interface.
2. Optional PaddleOCR-backed adapter with lazy import.
3. `parse_mode = auto | text | ocr`.
4. Default `auto` remains backward-compatible.
5. PDF OCR fallback when text parsing fails or produces no chunks.
6. OCR page text converted into normal sections/chunks.
7. OCR evidence recorded in parse and chunk metadata.
8. Tests that do not require PaddleOCR, vector services, or LLMs.

Phase 8B documents:

- `docs/ai/27-phase8b-ocr-adapter-dev-spec.md`
- `docs/ai/28-phase8b-test-cases.md`
- `docs/ai/29-phase8b-demo-runbook.md`

## Phase 9 - Real PaddleOCR Runtime And Scanned PDF Smoke

Status: planned.

Goal: verify the optional PaddleOCR-backed OCR adapter against the local real
runtime before the demo page presents OCR as a demonstrated capability.

Scope:

1. Install the optional OCR dependency group in the local development runtime.
2. Verify `paddleocr` import and lazy adapter construction.
3. Select one small scanned PDF or image-derived PDF sample from the indexed
   source materials.
4. Run upload plus forced `parse_mode=ocr` smoke through the existing API.
5. Run upload plus `parse_mode=auto` smoke when the text parser fails or
   produces no chunks.
6. Record model download behavior, cold-start cost, parse metadata, chunk
   metadata, and sanitized failure behavior.
7. Keep automated test coverage fake-OCR based; real PaddleOCR remains a manual
   smoke dependency.

Non-goals:

- No table reconstruction.
- No large image batch ingestion.
- No certificate or qualification-material validation.
- No default dependency change that makes PaddleOCR required for normal tests.
- No Qdrant, Haystack, embeddings, or semantic retrieval.

Phase 9 documents:

- `docs/ai/30-phase9-real-ocr-smoke-dev-spec.md`
- `docs/ai/31-phase9-test-cases.md`
- `docs/ai/32-phase9-demo-runbook.md`

## Phase 10 - PRD Demo Flow Page

Status: planned.

Goal: make the demo page match the PRD story, not only expose raw endpoints.

Scope:

1. Split the page into historical bid ingestion, tender upload and analysis,
   target tag selection, retrieval evidence, candidate generation, citations,
   risks, human review, and raw JSON.
2. Add target-tag controls with PRD-like labels.
3. Add demo status panels for parsed historical files, generated knowledge
   cards, tender analysis result, and retrieval result count.
4. Keep it a single FastAPI-hosted static page.
5. Show OCR capability/status only from the Phase 9 smoke evidence; do not
   imply OCR is production-ready.

Non-goals:

- No formal frontend app.
- No login.
- No project/file-management system.
- No final bidding document editor.
- No semantic retrieval or vector-store migration.

## Phase 11 - Sample Outputs And Repeatable Runbook

Status: planned.

Goal: make the server demo repeatable by another engineer or agent.

Scope:

1. Create a fixed runbook for two historical bid files, one tender file, one
   selected OCR sample when available, and selected target tags.
2. Add sample JSON output files under docs, not generated runtime artifacts.
3. Record expected success and failure behavior for no LLM key, OCR dependency
   unavailable, text PDF, scanned PDF requiring OCR, and intentionally deferred
   large files.
4. Keep generated bidding content clearly marked as candidate content requiring
   human review.

## Phase 12 - Semantic Retrieval Adapter Spike

Status: planned.

Goal: evaluate Qdrant, Haystack, and embeddings as an optional semantic
retrieval path after the deterministic demo baseline is stable.

Scope:

1. Add a replaceable semantic retrieval adapter boundary.
2. Evaluate a local or provider-backed embedding strategy.
3. Evaluate Qdrant collection creation and indexing for existing chunks or
   knowledge cards.
4. Evaluate Haystack query pipeline integration without replacing the current
   deterministic retrieval default.
5. Compare deterministic retrieval and semantic retrieval on the fixed Phase 11
   sample set.

Non-goals:

- No mandatory vector service for normal tests.
- No migration that invalidates existing SQLite chunk/card storage.
- No production-ranking claim before an evaluation set exists.
