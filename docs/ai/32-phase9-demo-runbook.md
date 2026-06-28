# Phase 9 Real OCR Smoke Runbook

## Purpose

Run one real PaddleOCR smoke against the existing Phase 8B OCR adapter. This is
an operator runbook, not a default CI path.

## Setup

Use the bundled project Python when available:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pip install -e ".[ocr]"
& $py -c "import paddleocr; print(paddleocr.__version__)"
```

If install or import fails, record the exact error in `.ai/verification.md` and
do not claim real OCR smoke passed.

PDF input note:

```powershell
& $py -m pip install PyMuPDF
& $py -c "import fitz; print('fitz_available=True')"
```

Use this only as a local smoke dependency unless license review approves it for
the project. `PyMuPDF` reports dual `GNU AFFERO GPL 3.0 or Artifex Commercial
License`, so it must not be added to `pyproject.toml` by default.

## Sample Selection

Use one small scanned PDF or image-derived PDF from the indexed source
materials. Do not copy the sample into Git.

Candidate indexed paths:

1. `宁波运维项目\九州拓新\批量输出为图片\...`
2. `宁波运维项目\浙江速微科技有限公司\批量输出为图片\...`

If these are image folders rather than PDFs, create a temporary local PDF only
under a runtime/temp directory and do not commit it.

## Start Server

```powershell
$env:BIDKNOWLEDGE_DATABASE_URL='sqlite:///./data/bidknowledge.db'
$env:BIDKNOWLEDGE_UPLOAD_ROOT='./data/uploads'
& $py -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
```

Use `curl.exe --noproxy "*"` for localhost calls when proxy variables may
interfere.

## Upload Sample

```powershell
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/files/upload" `
  -F "doc_role=historical_bid" `
  -F "file=@<absolute-path-to-scanned-sample.pdf>"
```

Record the returned `document_id`.

## Forced OCR Parse

```powershell
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/documents/<document_id>/parse" `
  -H "Content-Type: application/json" `
  -d "{\"parse_mode\":\"ocr\"}"
```

Expected success evidence:

```json
{
  "parse_status": "parsed",
  "parse_metadata": {
    "parse_mode": "ocr",
    "ocr_attempted": true,
    "ocr_engine": "paddleocr"
  }
}
```

Failure is acceptable only when the sanitized error and dependency/runtime
blocker are recorded.

## Auto Fallback Parse

Use a fresh upload of the same sample or clear previous parse output before
re-running if needed.

```powershell
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/documents/<document_id>/parse" `
  -H "Content-Type: application/json" `
  -d "{\"parse_mode\":\"auto\"}"
```

Expected:

1. Text parser is tried first.
2. OCR is attempted only if text parsing fails or produces no chunks.
3. Metadata explains the route.

## Inspect Chunks

```powershell
curl.exe --noproxy "*" "http://127.0.0.1:8000/api/documents/<document_id>/chunks"
```

Check that OCR-derived chunks keep source metadata and enough OCR evidence for
later risk display.

## Required Closure Notes

Record in `.ai/verification.md`:

1. Python runtime path.
2. `paddleocr` version or import failure.
3. Sample catalog path used.
4. Whether first run downloaded models.
5. Forced OCR result.
6. Auto fallback result.
7. Chunk count and OCR metadata summary.
8. Whether `scripts/ai_check.ps1` passed after the smoke.

Record in `.ai/evaluation.md`:

1. Real OCR status: passed, failed, or blocked.
2. Remaining operational risks.
3. Whether Phase 10 may show OCR as smoke-verified.

## Boundaries

Phase 9 does not make OCR production-ready. It does not reconstruct tables,
validate certificates, process large image batches, or add semantic retrieval.
Downstream generated content must still require human review.
