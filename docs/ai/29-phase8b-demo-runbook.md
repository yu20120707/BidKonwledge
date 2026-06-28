# Phase 8B OCR Demo Runbook

## Purpose

Verify OCR adapter behavior for scanned PDFs.

## Setup

Automated tests do not require PaddleOCR. For real OCR smoke:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pip install -e ".[ocr]"
```

Real PaddleOCR may download models and should be smoke-tested separately from
normal project verification.

## API Flow

Upload a scanned PDF, then force OCR:

```powershell
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/documents/<document_id>/parse" `
  -H "Content-Type: application/json" `
  -d "{\"parse_mode\":\"ocr\"}"
```

Or use automatic fallback:

```powershell
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/documents/<document_id>/parse" `
  -H "Content-Type: application/json" `
  -d "{\"parse_mode\":\"auto\"}"
```

## Expected Output

Parse response includes safe metadata:

```json
{
  "parse_status": "parsed",
  "parse_metadata": {
    "parse_mode": "ocr",
    "ocr_attempted": true,
    "ocr_engine": "paddleocr",
    "ocr_pages_count": 1
  }
}
```

## Boundaries

Phase 8B does not reconstruct tables, validate certificates, or guarantee legal
reliability of OCR text. Downstream generated content must still require human
review.
