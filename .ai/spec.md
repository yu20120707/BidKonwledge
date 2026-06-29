# Spec - Phase 12 Semantic Retrieval Adapter Spike

## Objective

Evaluate Qdrant, Haystack, and embeddings as an optional semantic retrieval
path for BidKnowledge.

Phase 12 is a spike and evaluation phase. It must not replace the current
deterministic retrieval default.

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

Documentation/planning slice:

1. Add Phase 12 docs:
   - `docs/ai/39-phase12-semantic-retrieval-spike-dev-spec.md`
   - `docs/ai/40-phase12-test-cases.md`
   - `docs/ai/41-phase12-evaluation-report.md`
2. Update roadmap, docs index, lightweight PRD plan, and active `.ai` runtime
   artifacts.
3. Define a minimum adapter boundary and decision gate before writing backend
   code.
4. Use the Phase 11 fixed sample set as the comparison baseline.

Deterministic demo-flow closeout slice:

1. Keep deterministic `/api/retrieve` as the default retrieval path.
2. Allow PRD knowledge-card tags to retrieve their historical source chunks.
3. Exclude tender documents from the retrieval evidence pool.
4. Make the demo page's chunk-tag fallback an actual secondary request, not
   only display text.
5. Preserve existing public API request and response contracts.

Loop-engineering polish slice:

1. Keep query-only retrieval stable before and after knowledge-card build.
2. Preserve PRD knowledge-card bridge metadata inside generation prompts.
3. Include tender-analysis requirement context in demo generation without
   changing the backend generation schema.
4. Improve `/demo` visual hierarchy, focus/loading states, and responsive
   behavior.
5. Show a historical evidence pool for multiple Phase 11 historical sample
   sources.
6. Verify `/demo` with real browser smoke evidence.

Potential follow-up implementation slice:

1. Add fake-testable semantic retrieval records and adapter boundary.
2. Preserve current `RetrievalResponse` source metadata.
3. Keep default `POST /api/retrieve` deterministic.
4. Keep Qdrant/Haystack/embedding dependencies optional and lazily imported.

## Out Of Scope

1. No replacement of deterministic retrieval.
2. No mandatory Qdrant, Haystack, embedding model, API key, network service, or
   vector store for normal tests.
3. No public API contract change.
4. No SQLite schema migration.
5. No production ranking or semantic retrieval quality claim.
6. No table reconstruction.
7. No image batch ingestion.
8. No certificate or qualification-material authenticity validation.
9. No login/user system.
10. No final Word/PDF export.
11. No PyMuPDF project dependency addition.

## Acceptance Criteria

1. Phase 12 docs identify the optional semantic retrieval boundary and
   comparison method.
2. The Phase 11 sample set remains the baseline.
3. The docs state when to proceed to code and when to defer.
4. PRD-tag deterministic retrieval is covered by tests.
5. Demo fallback/effective-tag evidence is visible in raw JSON.
6. Demo generation records the tender requirement used and generation query.
7. Multiple historical documents can contribute retrieval evidence while tender
   documents remain excluded from retrieval evidence.
8. Browser validation shows no console errors or horizontal overflow at desktop
   and mobile widths.
9. `.ai` runtime artifacts accurately reflect Phase 12 status without claiming
   a new harness gate.
10. Project verification is run or blockers are recorded honestly.
