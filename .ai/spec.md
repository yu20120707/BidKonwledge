# Spec - Phase 11 Sample Outputs And Repeatable Runbook

## Objective

Make the PRD-shaped server demo repeatable by another engineer or agent.

Phase 11 produces a fixed demo replay package:

1. selected sample files from `docs/source-materials/sample-catalog.md`
2. selected PRD tags and their deterministic retrieval-tag mappings
3. representative JSON outputs under `docs/ai/sample-outputs/phase11/`
4. expected success and failure behavior
5. a repeatable runbook for `/demo` and direct API comparison

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

1. Add Phase 11 docs:
   - `docs/ai/36-phase11-sample-outputs-dev-spec.md`
   - `docs/ai/37-phase11-test-cases.md`
   - `docs/ai/38-phase11-repeatable-demo-runbook.md`
2. Add representative JSON under `docs/ai/sample-outputs/phase11/`.
3. Add lightweight pytest coverage for sample JSON validity and boundaries.
4. Update roadmap, docs index, and active `.ai` runtime artifacts.

## Out Of Scope

1. No backend API/schema changes.
2. No customer source files or runtime artifacts committed.
3. No Qdrant, Haystack, embeddings, dense retrieval, or semantic retrieval.
4. No table reconstruction.
5. No image batch ingestion.
6. No certificate or qualification-material authenticity validation.
7. No login/user system.
8. No final Word/PDF export.
9. No PyMuPDF project dependency addition.

## Acceptance Criteria

1. A fixed sample manifest exists and identifies two historical bid files, one
   tender file, one OCR smoke sample, and selected tags.
2. Representative sample JSON files exist and parse successfully.
3. JSON samples avoid secrets, local runtime paths, and committed customer
   content dumps.
4. The runbook explains success, no-LLM fallback, OCR dependency failure,
   text-PDF behavior, scanned-PDF OCR fallback, and large-file deferral.
5. Project verification passes, except for the known bash/WSL blocker if still
   unavailable.
