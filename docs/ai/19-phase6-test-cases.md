# Phase 6 Test Cases

## Purpose

Define expected test coverage before implementing Phase 6 knowledge cards.

Status: implemented on 2026-06-28 in
`backend/tests/test_knowledge_cards_api.py` and
`backend/tests/test_phase6_boundaries.py`.

## P0 Tests

### TC-KC-001 Build Cards From Parsed Historical Bid

Setup:

- Upload a historical bid file.
- Inject a parser returning sections/chunks with `运维`, `应急`, and `质量`.

Action:

- Call `POST /api/knowledge/build`.

Expected:

- HTTP 200.
- `cards_count > 0`.
- Response tags include PRD-style tags.
- Database contains cards for the document.

### TC-KC-002 List Cards By Document

Setup:

- Build cards for a parsed historical bid.

Action:

- Call `GET /api/documents/{document_id}/knowledge-cards`.

Expected:

- HTTP 200.
- Cards contain `card_id`, `source_chunk_id`, `tag`, `content`,
  `source_filename`, `source_section_title`, `source_section_path`,
  `confidence`, and `metadata`.

### TC-KC-003 Rebuild Replaces Existing Cards

Setup:

- Build cards once.
- Build cards again for the same document.

Expected:

- Card count is stable.
- No duplicate cards remain from the prior build.
- Card ordering is deterministic.

### TC-KC-004 Document Not Found

Action:

- Call `POST /api/knowledge/build` with a missing document id.

Expected:

- Structured error with `error_code = DOCUMENT_NOT_FOUND`.

### TC-KC-005 Document Not Parsed

Setup:

- Upload a historical bid but do not parse it.

Action:

- Call `POST /api/knowledge/build`.

Expected:

- Structured error with `error_code = DOCUMENT_NOT_PARSED`.

### TC-KC-006 Boundary Dependencies

Setup:

- Remove `OPENAI_API_KEY`, `QDRANT_URL`, `HAYSTACK_API_KEY`, and OCR-related env
  variables.

Action:

- Build cards from injected parsed chunks.

Expected:

- Tests pass without OCR, Qdrant, Haystack, embeddings, or LLM.

## P1 Tests

### TC-KC-007 Unsupported Role

Setup:

- Upload and parse a tender document.

Action:

- Call `POST /api/knowledge/build`.

Expected:

- Either reject with `UNSUPPORTED_DOCUMENT_ROLE` or explicitly document that
  Phase 6 builds cards only for `historical_bid`.

### TC-KC-008 Unclassified Content

Setup:

- Parsed chunk contains generic text with no matching keywords.

Expected:

- Card is still created with `tag = 未分类`.
- Metadata shows deterministic fallback.

### TC-KC-009 Source Page Fields

Setup:

- Parsed chunk includes `page_start` and `page_end`.

Expected:

- Knowledge card response preserves page fields.

## Required Commands

Targeted:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_knowledge_cards_api.py backend/tests/test_phase6_boundaries.py
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
