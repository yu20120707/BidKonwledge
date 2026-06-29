# Phase 10 Test Cases

## Goal

Verify that the PRD-shaped demo page exposes the intended narrative flow
without expanding backend scope or overstating OCR support.

## Automated

### P0 Page Availability

1. `GET /demo` returns HTTP `200`.
2. Response content type includes `text/html`.
3. Page title and main Phase 10 headline are present.

### P0 Required Flow Sections

Assert the page includes:

1. historical bid section
2. knowledge card section
3. tender section
4. PRD tag selection section
5. retrieval evidence section
6. candidate generation section
7. review / raw JSON section
8. OCR status section

### P0 Required API Hooks

Assert the page still calls:

1. `POST /api/files/upload`
2. `POST /api/documents/{document_id}/parse`
3. `POST /api/knowledge/build`
4. `GET /api/documents/{document_id}/knowledge-cards`
5. `POST /api/tender/analyze`
6. `POST /api/retrieve`
7. `POST /api/generate`

### P0 PRD Tag Mapping Boundary

Assert the page source includes PRD label options and explicit page-layer
mapping to current deterministic retrieval tags.

### P0 OCR Copy Boundary

Assert the page source:

1. mentions `paddleocr 2.10.0 / paddlepaddle 2.6.2`
2. mentions `1 section / 1 chunk`
3. mentions PyMuPDF as local smoke-only
4. states OCR is smoke evidence only and not production-ready

### P0 No-LLM UI Fallback

Assert the page source still preserves the structured
`LLM_NOT_CONFIGURED` fallback path and keeps `need_human_review` visible.

### P0 Demo Workflow API Chain

Use fake parser and fake LLM injection to verify:

1. upload historical bid
2. parse historical bid
3. build knowledge cards
4. upload tender
5. parse tender
6. analyze tender
7. retrieve evidence
8. generate candidate content

And assert:

1. knowledge cards are created
2. tender analysis returns requirements and risks
3. retrieval returns historical evidence
4. generation returns citations and `need_human_review = true`

## Manual

1. Start the backend server locally.
2. Open `/demo`.
3. Upload one historical bid file and parse it.
4. Build knowledge cards and confirm card list updates.
5. Upload one tender file, parse it, and analyze it.
6. Change PRD tag selection and confirm mapped retrieval tag text updates.
7. Retrieve evidence and confirm the list shows file name, tags, and score.
8. Generate candidate content with either:
   - server env LLM config
   - request-scoped page LLM config
9. Confirm citations, risks, and `need_human_review` are visible.
10. Confirm OCR section reads as smoke evidence only.

## Non-Goals

These tests do not require:

1. Qdrant or Haystack
2. embeddings
3. table reconstruction
4. batch image OCR
5. login/user system
6. final Word/PDF export
