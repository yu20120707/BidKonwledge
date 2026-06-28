# Affected Files - Phase 9 Real OCR Smoke

## Updated Files

Implementation/config:

- `backend/app/adapters/ocr_adapter.py`
- `backend/tests/test_ocr_adapter_parse.py`
- `pyproject.toml`

Runtime evidence:

- `.ai/spec.md`
- `.ai/implementation-plan.md`
- `.ai/affected-files.md`
- `.ai/run-trace.md`
- `.ai/verification.md`
- `.ai/evaluation.md`
- `.ai/handoff.md`

## Runtime-Only Artifacts

Do not commit:

- temporary scanned PDF generated under `%TEMP%`
- uploaded smoke files under temporary upload roots
- temporary SQLite smoke databases
- PaddleOCR model cache under `C:\Users\26561\.paddleocr`
- customer source images or PDFs

## Dependency Boundary

Committed OCR optional dependencies:

- `paddleocr>=2.8,<3.0`
- `paddlepaddle>=2.6,<3.0`

Local smoke-only dependency:

- `PyMuPDF 1.27.2.3`, installed only in the local Python runtime because
  PaddleOCR PDF input imports `fitz`. It is not added to `pyproject.toml`
  because the package reports dual `GNU AFFERO GPL 3.0 or Artifex Commercial`
  licensing and needs explicit license review before becoming project
  dependency.

## Forbidden Areas

- Do not add Qdrant, Haystack, embeddings, dense retrieval, or hybrid retrieval.
- Do not add table reconstruction.
- Do not add image batch ingestion.
- Do not validate certificates, seals, or qualification evidence.
- Do not commit customer samples or generated OCR output.
