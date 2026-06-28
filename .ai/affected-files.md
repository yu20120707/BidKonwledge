# Affected Files - Phase 2 Document Parsing And Chunking

## Expected Added Files

- `backend/app/api/documents.py`
- `backend/app/adapters/__init__.py`
- `backend/app/adapters/docling_parser.py`
- `backend/app/services/__init__.py`
- `backend/app/services/document_parsing.py`
- `backend/app/services/section_chunker.py`
- `backend/app/services/tagger.py`
- `backend/tests/test_document_parse_api.py`
- `backend/tests/test_document_chunks.py`
- `backend/tests/test_phase2_boundaries.py`

## Expected Updated Files

- `pyproject.toml`
- `backend/app/main.py`
- `backend/app/schemas/document.py`
- `backend/app/storage/database.py`
- `backend/tests/conftest.py`
- `README.md`
- `docs/ai/03-data-model.md`
- `docs/ai/04-api-contract.md`
- `.ai/spec.md`
- `.ai/implementation-plan.md`
- `.ai/affected-files.md`
- `.ai/run-trace.md`
- `.ai/verification.md`
- `.ai/evaluation.md`
- `.ai/handoff.md`

## Forbidden Areas

- Do not vendor `F:\BidKonwledge_refs\ragflow`.
- Do not vendor `F:\BidKonwledge_refs\haystack-demos`.
- Do not copy large customer sample files into the repository.
- Do not implement OCR, embeddings, vector store, Haystack execution, LLM
  generation, full knowledge cards, tender deep analysis, frontend Demo, user
  system, or Word/PDF export.
