# Verification

## MVP Acceptance Criteria

The MVP must eventually support:

1. Upload 2-3 historical bid files.
2. Upload 1 tender file.
3. Parse files into sections.
4. Build knowledge cards from historical bid files.
5. Apply initial tags to knowledge cards.
6. Retrieve knowledge cards by tag and query.
7. Analyze tender file for project requirements, scoring items, and disqualification risks.
8. Generate candidate content with an external LLM API.
9. Return source citations.
10. Return risk hints.
11. Mark `need_human_review = true`.
12. Show results in a simple demo page.
13. Provide raw JSON response.

## Smoke Test For Future MVP

A minimal successful demo should prove:

1. Historical bid file uploaded successfully.
2. At least one section is parsed.
3. At least one knowledge card is created.
4. A target tag can retrieve relevant cards.
5. Generate API returns content.
6. The response includes citations.
7. The response includes risks.
8. The response includes `need_human_review = true`.

## Phase 0 Verification

Phase 0 is complete when:

1. The folder is a Git repository.
2. Harness baseline files exist.
3. `docs/ai/` contains project brief, scope, architecture, data model, API contract, dev rules, and verification notes.
4. `.ai/` contains spec, implementation plan, verification, evaluation, and handoff files.
5. No business code was implemented.

## Phase 1 Verification

Phase 1 should be verified with:

1. Unit or API tests for `GET /health`.
2. Upload smoke test for `POST /api/files/upload`.
3. SQLite metadata persistence check.
4. Local saved-file existence check.
5. README startup command check.
