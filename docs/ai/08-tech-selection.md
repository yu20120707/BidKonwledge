# Tech Selection

## Source

This file summarizes `docs/source-materials/originals/deep-research-report.md`.

## Main Decision

Use a thin FastAPI service as the project shell.

For later RAG phases, the recommended implementation stack is:

- Haystack for Python-native retrieval/generation pipeline orchestration.
- Docling as the primary structured document parser.
- PaddleOCR as the later OCR adapter for scanned PDF and image pages.
- Qdrant as the later vector store.
- RAGFlow as the product-reference benchmark, not the codebase to fork.

## Why Not Fork A Full Platform First

Do not start by heavy-forking RAGFlow, Dify, AnythingLLM, or MinerU.

Reasons:

1. The current project is a capability-validation demo, not a general AI platform.
2. Full platforms bring UI, workflow, team, plugin, and deployment surfaces that are outside the PRD.
3. Dify and MinerU have custom licenses that need legal review before any deep reuse.
4. Heavy platform adoption would make two-week demo delivery harder to control.

## Practical Stack By Phase

Phase 1:

- FastAPI
- Pydantic
- SQLite
- local file storage
- pytest smoke tests

Phase 2:

- Docling adapter for docx and text-based pdf parsing.
- Unified chunk schema.
- Deterministic section splitting and tag rules.

Phase 3:

- Qdrant adapter.
- Haystack retrieval pipeline.
- Dense retrieval first, hybrid retrieval as an interface-compatible extension.

Phase 4:

- OpenAI-compatible LLM adapter.
- Prompt builder.
- Citation-preserving answer formatter.
- Rule-based risk checker.

Phase 5:

- Minimal FastAPI-hosted demo page.
- Demo script using 2-3 historical bid files and 1 tender file.

## Dependency Guardrails

1. Prefer MIT or Apache-2.0 dependencies.
2. Treat Dify and MinerU as reference-only unless license review approves deeper reuse.
3. Avoid introducing AGPL dependencies into the main path without explicit approval.
4. Keep external services behind adapters so parser, vector store, embedding, and LLM providers can be replaced.
5. No generated answer can be returned without citations, risks, and `need_human_review = true`.
