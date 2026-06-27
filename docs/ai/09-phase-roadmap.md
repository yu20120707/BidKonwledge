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

Goal: retrieve historical chunks by tag and query.

Scope:

1. Qdrant adapter.
2. Haystack query pipeline wrapper.
3. Dense retrieval first.
4. Metadata-preserving result format.
5. Retrieval tests with fake or small local chunks.

## Phase 4 - Generation, Citations, And Risks

Goal: generate candidate content from retrieval context.

Scope:

1. OpenAI-compatible LLM adapter.
2. Prompt builder.
3. Answer formatter.
4. Citation formatter.
5. Rule-based risk checker.
6. `need_human_review = true` always.

## Phase 5 - Demo Page And Script

Goal: present the full capability chain to a stakeholder.

Scope:

1. Minimal upload/query/result page.
2. Demo script using selected sample files.
3. Raw JSON display.
4. Manual verification notes for citations and risk hints.
