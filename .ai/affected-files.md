# Affected Files - Phase 8B OCR Adapter For Scanned PDFs

This is the expected Phase 8B edit surface.

## Added Files

Implementation:

- `backend/app/adapters/ocr_adapter.py`

Tests:

- `backend/tests/test_ocr_adapter_parse.py`
- `backend/tests/test_phase8b_boundaries.py`

Durable docs:

- `docs/ai/27-phase8b-ocr-adapter-dev-spec.md`
- `docs/ai/28-phase8b-test-cases.md`
- `docs/ai/29-phase8b-demo-runbook.md`

## Updated Files

Backend:

- `backend/app/api/documents.py`
- `backend/app/services/document_parsing.py`
- `backend/app/services/section_chunker.py`
- `backend/app/schemas/document.py`
- `pyproject.toml`

Docs and evidence:

- `README.md`
- `docs/ai/03-data-model.md`
- `docs/ai/04-api-contract.md`
- `docs/ai/09-phase-roadmap.md`
- `docs/ai/17-lightweight-prd-completion-plan.md`
- `docs/ai/README.md`
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
- Do not copy customer scanned files into the repository.
- Do not commit generated OCR output.
- Do not make PaddleOCR a required default or test dependency.
- Do not add Qdrant, Haystack, embeddings, dense retrieval, hybrid retrieval,
  LLM parsing, user system, export, or final approved bidding output.
- Do not implement certificate validation or qualification evidence validation.

## Watch List

- `backend/app/services/document_parsing.py`: keep OCR fallback limited and
  preserve existing text parsing behavior.
- `backend/app/adapters/ocr_adapter.py`: PaddleOCR imports must be lazy.
- `backend/app/api/documents.py`: parse body must remain backward compatible
  with no-body requests.
- `backend/app/services/section_chunker.py`: OCR metadata should stay attached
  to chunks without disrupting existing deterministic tags.
- Tests must use fake OCR adapters and isolated temp resources.
