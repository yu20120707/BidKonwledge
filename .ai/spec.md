# Spec - Phase 10 PRD-shaped Demo Page Flow

## Objective

Upgrade `/demo` from a raw endpoint-control page into a PRD-shaped narrative
demo flow.

The page must show:

1. historical bid upload and parse
2. knowledge card build and display
3. tender upload, parse, and analysis
4. PRD tag selection
5. retrieval evidence display
6. candidate content generation
7. citations, risks, human review, and raw JSON
8. OCR capability status based only on Phase 9 smoke evidence

## Required Execution Mode

This task runs under Auto_AICoding_Harness `large` mode with the
`python-backend-service` profile.

Current harness state remains:

- `mode: large`
- `status: DONE`
- `current_gate: none`

Do not claim a new harness gate transition unless the matching harness command
succeeds.

## In Scope

1. Rework `backend/app/static/demo.html`.
2. Update targeted demo tests.
3. Add Phase 10 durable docs.
4. Update `.ai` runtime artifacts for the active task.

## Out Of Scope

1. No Qdrant, Haystack, embeddings, dense retrieval, or semantic retrieval.
2. No table reconstruction.
3. No image batch ingestion.
4. No certificate or qualification-material validation.
5. No login/user system.
6. No final Word/PDF export.
7. No PyMuPDF project dependency addition.
8. No backend API/schema change unless strictly required to keep the page
   functional.

## Acceptance Criteria

1. `/demo` becomes a PRD-shaped single-page flow.
2. The page reuses existing upload, parse, knowledge, tender-analysis,
   retrieval, and generation APIs.
3. PRD-facing labels are visible without silently changing backend retrieval tag
   semantics.
4. OCR text is limited to Phase 9 smoke evidence and does not imply
   production readiness.
