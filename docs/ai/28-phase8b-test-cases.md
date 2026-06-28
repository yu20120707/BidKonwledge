# Phase 8B Test Cases

## Purpose

Define OCR adapter coverage for scanned PDF parsing.

Status: implemented on 2026-06-28 in:

- `backend/tests/test_ocr_adapter_parse.py`
- `backend/tests/test_phase8b_boundaries.py`

## P0 Tests

### TC-OCR-001 Auto Keeps Text PDF Path

No request body. Parser succeeds.

Expected:

- parse succeeds
- OCR is not called
- `parse_mode = auto`

### TC-OCR-002 Text Mode Never Calls OCR

`parse_mode = text`. Parser fails.

Expected:

- parse fails
- OCR is not called
- local paths are sanitized

### TC-OCR-003 OCR Mode Uses OCR Directly

`parse_mode = ocr`. Fake OCR returns page text.

Expected:

- parser is not called
- OCR pages become sections/chunks
- metadata includes OCR engine, page count, confidence

### TC-OCR-004 Auto Fallback On Parser Failure

No request body. Parser fails for PDF.

Expected:

- OCR fallback runs
- parse succeeds
- fallback reason is recorded safely

### TC-OCR-005 Auto Fallback On No Chunks

Parser returns no chunkable content.

Expected:

- OCR fallback runs
- parse succeeds

### TC-OCR-006 OCR Failure Is Sanitized

Fake OCR raises an error containing local paths.

Expected:

- parse fails
- error message is sanitized
- sections/chunks are empty

## Required Commands

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_ocr_adapter_parse.py backend/tests/test_phase8b_boundaries.py
.\scripts\ai_check.ps1
python -m pytest backend/tests
```
