# Phase 9 Test Cases

## Purpose

These cases verify the real PaddleOCR smoke without turning OCR into a default
test dependency. Automated tests still use fake OCR. Real PaddleOCR checks are
manual smoke checks with recorded evidence.

## P0 - Required

### TC-P9-001 Optional Dependency Install

Steps:

1. Use the project Python runtime.
2. Run `pip install -e ".[ocr]"`.
3. Run `python -c "import paddleocr; print(paddleocr.__version__)"`.

Expected:

1. Install completes, or the failure is recorded with the exact package/runtime
   blocker.
2. `paddleocr` import succeeds when install succeeds.
3. Normal non-OCR tests remain runnable without adding OCR to default
   dependencies.

### TC-P9-002 Adapter Construction Smoke

Steps:

1. Import the OCR adapter module.
2. Construct the PaddleOCR-backed adapter.

Expected:

1. Construction succeeds after optional dependencies are installed, or a
   sanitized OCR dependency error is raised.
2. No OCR model path or local absolute customer path is leaked in API-facing
   errors.

### TC-P9-003 Forced OCR Parse On Scanned PDF

Steps:

1. Select one small scanned PDF or image-derived PDF from
   `docs/source-materials/sample-catalog.md`.
2. Upload it as `doc_role=historical_bid` or `doc_role=tender`.
3. Call `POST /api/documents/{document_id}/parse` with
   `{"parse_mode":"ocr"}`.
4. Inspect the parse response and chunks.

Expected:

1. Success path: parse response is `parsed`, sections/chunks are created, and
   OCR metadata is present.
2. Failure path: parse response is `failed` with a sanitized error and the
   blocker is recorded.
3. Customer file contents are not committed to Git.

### TC-P9-004 Auto Fallback Behavior

Steps:

1. Use the same scanned PDF.
2. Call parse with `{"parse_mode":"auto"}`.
3. Inspect whether text parsing failed or produced no chunks before OCR.

Expected:

1. Auto mode keeps text parsing first.
2. OCR is attempted only when the parser fails or produces no chunks.
3. Parse metadata shows enough evidence to explain the route.

### TC-P9-005 Regression: Text PDF Stays OCR-Free

Steps:

1. Use a known text-layer PDF.
2. Call parse with `{"parse_mode":"auto"}`.

Expected:

1. Text parser succeeds.
2. OCR is not attempted.
3. Existing chunks and metadata remain compatible with prior phases.

## P1 - Important

### TC-P9-006 Cold Start And Model Download Notes

Steps:

1. Record first-run install and model-download behavior.
2. Record approximate cold-start duration if available.

Expected:

1. Runbook states whether the first OCR run downloads models.
2. Any proxy, cache, disk, or permission blocker is documented.

### TC-P9-007 Normal Verification Still Passes

Steps:

1. Run targeted fake-OCR tests.
2. Run `scripts/ai_check.ps1`.

Expected:

1. Fake-OCR automated tests pass.
2. Project verification passes without requiring live OCR models.

## P2 - Deferred

1. Table reconstruction from OCR layout.
2. OCR for large image batches.
3. OCR confidence threshold tuning.
4. Seal, certificate, or qualification-material validation.
5. Semantic retrieval over OCR-derived chunks.
