# Phase 8A Test Cases

## Purpose

Define Phase 8A coverage for legacy Word and mislabeled `.docx` conversion.

Status: implemented on 2026-06-28 in:

- `backend/tests/test_document_format.py`
- `backend/tests/test_word_conversion_parse.py`
- `backend/tests/test_phase8a_boundaries.py`

## P0 Tests

### TC-WC-001 Detect True DOCX

Input has `.docx` extension and `PK` header.

Expected:

- `detected_format = docx_zip`
- no conversion required

### TC-WC-002 Detect Legacy DOC

Input has `.doc` extension and `D0 CF 11 E0` header.

Expected:

- `detected_format = legacy_ole_word`
- conversion required

### TC-WC-003 Detect Mislabeled DOCX

Input has `.docx` extension and `D0 CF 11 E0` header.

Expected:

- `detected_format = legacy_ole_word`
- `is_mislabeled = true`
- conversion required

### TC-WC-004 Parse Uses Converted File

Use fake converter and fake parser.

Expected:

- converter is called once
- parser receives derived `.converted.docx`
- parse succeeds
- parse metadata records safe relative converted path

### TC-WC-005 Converter Failure

Fake converter raises an error containing local paths.

Expected:

- parse status is `failed`
- sections/chunks are cleared
- error message is sanitized
- parser is not called

### TC-WC-006 Boundary Dependencies

Automated tests run without OCR, PaddleOCR, Qdrant, Haystack, embeddings, LLM
credentials, or real Word COM.

## Required Commands

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_document_format.py backend/tests/test_word_conversion_parse.py backend/tests/test_phase8a_boundaries.py
.\scripts\ai_check.ps1
python -m pytest backend/tests
```
