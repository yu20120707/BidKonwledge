# Scope Boundary

## In Scope For Capability Demo

The lightweight demo is responsible for:

1. File upload.
2. Historical bid file parsing.
3. Tender file parsing.
4. Section splitting.
5. Initial tag recognition.
6. Knowledge card generation.
7. Vector indexing.
8. Tag plus semantic retrieval.
9. Calling an external LLM to generate candidate content.
10. Returning source citations.
11. Returning risk hints.
12. Returning structured JSON.
13. Providing a minimal demo page.

## Out Of Scope

The current validation demo must not become:

1. A complete bidding system.
2. A formal frontend system.
3. A Word or PDF layout/export system.
4. A cover, table-of-contents, header, footer, logo, or document-formatting engine.
5. An automatic quotation-file generator.
6. An automatic qualification-material generator.
7. A CA signing, bid bond, social security, tax certificate, software copyright, or vendor authorization workflow.
8. A user login or permission system.
9. A project management system.
10. A complete file management system.
11. A formal human review workflow.
12. A guarantee that AI output can be used directly for final bidding.

## Phase 0 Scope

Phase 0 only initializes the repository and AI context:

1. Initialize the empty folder as a Git repository.
2. Copy the Auto_AICoding_Harness baseline workflow files.
3. Write durable project context under `docs/ai/`.
4. Generate current task files under `.ai/`.

## Phase 1 Scope

Phase 1 should implement only:

1. FastAPI application startup.
2. `GET /health`.
3. `POST /api/files/upload`.
4. Local file saving to `data/uploads`.
5. Document metadata schema.
6. SQLite initialization.
7. Basic configuration management.
8. Minimal smoke test.
9. README local startup commands.

## Phase 1 Non-Goals

Phase 1 must not implement:

1. OCR.
2. LLM calls.
3. Embeddings.
4. Vector store.
5. Knowledge card generation.
6. Tender analysis.
7. Demo page.
8. User system.
9. Word/PDF export.

## Safety Rule

All generated content must return:

- `citations`
- `risks`
- `need_human_review = true`

Any generated content without a source citation must be marked high risk.
