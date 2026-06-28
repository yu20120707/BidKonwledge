# Phase 7 Test Cases

## Purpose

Define expected test coverage before implementing Phase 7 tender analysis.

Status: implemented on 2026-06-28 in
`backend/tests/test_tender_analysis_api.py` and
`backend/tests/test_phase7_boundaries.py`.

## P0 Tests

### TC-TA-001 Analyze Parsed Tender

Setup:

- Upload a document with `doc_role = tender`.
- Inject parsed chunks containing requirements, scoring wording, and risk
  wording.

Action:

- Call `POST /api/tender/analyze`.

Expected:

- HTTP 200.
- `need_human_review = true`.
- Response includes at least one project requirement.
- Response includes at least one scoring item.
- Response includes at least one disqualification risk.
- Items include source chunk and section evidence.

### TC-TA-002 Get Existing Tender Analysis

Setup:

- Analyze a parsed tender.

Action:

- Call `GET /api/documents/{document_id}/tender-analysis`.

Expected:

- HTTP 200.
- Response matches the latest stored analysis.

### TC-TA-003 Re-Analyze Replaces Existing Analysis

Setup:

- Analyze the same tender twice.

Expected:

- Item counts are stable.
- No duplicate stale analysis remains.
- Item ordering is deterministic.

### TC-TA-004 Document Not Found

Action:

- Call analyze with a missing document id.

Expected:

- Structured error with `error_code = DOCUMENT_NOT_FOUND`.

### TC-TA-005 Document Not Parsed

Setup:

- Upload a tender but do not parse it.

Action:

- Call analyze.

Expected:

- Structured error with `error_code = DOCUMENT_NOT_PARSED`.

### TC-TA-006 Unsupported Role

Setup:

- Upload and parse a `historical_bid`.

Action:

- Call analyze.

Expected:

- Structured error with `error_code = UNSUPPORTED_DOCUMENT_ROLE`.

### TC-TA-007 Boundary Dependencies

Setup:

- Remove LLM/vector/OCR environment variables.
- Use injected parsed chunks.

Expected:

- Analysis passes without OCR, Qdrant, Haystack, embeddings, or LLM.

## P1 Tests

### TC-TA-008 Empty Or Low-Signal Tender

Setup:

- Parsed tender text contains no matching rules.

Expected:

- HTTP 200.
- Lists may be empty.
- `need_human_review = true`.
- Metadata explains deterministic no-match behavior.

### TC-TA-009 Get Missing Analysis

Setup:

- Parsed tender exists but analysis has not been run.

Action:

- Call get analysis.

Expected:

- Structured error with `error_code = TENDER_ANALYSIS_NOT_FOUND`.

## Required Commands

Targeted:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_tender_analysis_api.py backend/tests/test_phase7_boundaries.py
```

Full:

```powershell
.\scripts\ai_check.ps1
python -m pytest backend/tests
```

Shell:

```powershell
bash ./scripts/ai_check.sh
```

If WSL/bash is unavailable, record the blocker and do not claim shell
verification passed.
