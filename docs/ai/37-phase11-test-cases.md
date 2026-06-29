# Phase 11 Test Cases

## Goal

Verify that the Phase 11 repeatable demo package is usable and stays inside the
documentation/sample-output boundary.

## Automated

### P0 JSON Validity

Parse every `*.json` file under `docs/ai/sample-outputs/phase11/`.

Expected:

1. all files parse successfully
2. each file has `sample_kind`
3. each file has either `stage`, `phase`, or `title`

### P0 Manifest Completeness

Read `docs/ai/sample-outputs/phase11/manifest.json`.

Expected:

1. every path listed in `sample_outputs` exists
2. fixed sample files include two `historical_bid` entries
3. fixed sample files include one `tender` entry
4. fixed sample files include one OCR smoke entry
5. selected tags include PRD labels and mapped deterministic retrieval tags

### P0 Secret Boundary

Scan sample JSON text.

Expected:

1. no `api_key` field
2. no `bearer ` token text
3. no committed `OPENAI_API_KEY`
4. no committed `%TEMP%` or `C:\Users\...` local runtime path

### P0 Scope Boundary

Expected:

1. no sample JSON claims generated content is final
2. OCR output is described as smoke evidence only
3. PyMuPDF is described as local-smoke-only
4. large files are explicitly deferred

## Manual

### Demo Replay

1. Start the backend.
2. Open `/demo`.
3. Use the fixed sample set from `manifest.json`.
4. Run historical upload/parse.
5. Build knowledge cards.
6. Run tender upload/parse/analyze.
7. Select a PRD tag from the fixed list.
8. Retrieve evidence.
9. Generate candidate content or confirm the no-LLM fallback.
10. Compare the page shape with the sample JSON files.

### Failure Replay

1. Clear LLM environment variables and leave page key empty.
2. Confirm `LLM_NOT_CONFIGURED`.
3. Run text PDF parse and confirm OCR is not attempted.
4. Run OCR sample only where optional OCR runtime is available.
5. Confirm large files are deferred from the baseline.

## Non-Goals

The Phase 11 tests do not verify:

1. live external LLM quality
2. legal truth of qualification material
3. semantic retrieval ranking
4. production OCR reliability
5. final document export
