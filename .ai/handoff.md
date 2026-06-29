# Handoff

## Current State - Phase 12 Semantic Retrieval Adapter Spike

Phase 12 planning/evaluation slice is complete. A resumed deterministic
demo-flow closeout has also been applied.

Current harness state:

- mode: `large`
- profile: `python-backend-service`
- state status: `DONE`
- current gate: none

Important harness note:

- `.ai/state.json` still reflects `DONE/current_gate: none`.
- Do not claim a new gate has opened unless the matching harness command
  succeeds.

Current Phase 12 artifacts:

1. `docs/ai/39-phase12-semantic-retrieval-spike-dev-spec.md`
2. `docs/ai/40-phase12-test-cases.md`
3. `docs/ai/41-phase12-evaluation-report.md`

Resumed closeout implementation:

1. Deterministic retrieval now limits evidence candidates to parsed
   `historical_bid` documents.
2. PRD knowledge-card tags can retrieve their historical source chunks without
   changing the public `/api/retrieve` contract.
3. Knowledge-card-backed rows are preferred on equal-score ties so evidence
   metadata remains visible.
4. The demo page now performs a real PRD-tag-first, chunk-tag-fallback retrieve
   and records `requested_tag`, `effective_tag`, `fallback_chunk_tag`, and
   `used_fallback` in raw JSON.
5. The loop-engineering polish pass prevents query-only retrieval drift after
   knowledge-card build, adds PRD knowledge-card bridge metadata to generation
   prompts, folds the first tender requirement into the demo generation query,
   and tightens `/demo` visual/interaction details.
6. `/demo` now includes a historical evidence pool so multiple Phase 11
   historical files can be shown as evidence sources instead of disappearing
   behind a single active document slot.

Updated context:

1. `docs/ai/README.md`
2. `docs/ai/09-phase-roadmap.md`
3. `docs/ai/17-lightweight-prd-completion-plan.md`
4. `.ai/spec.md`
5. `.ai/implementation-plan.md`
6. `.ai/affected-files.md`
7. `.ai/run-trace.md`
8. `.ai/verification.md`
9. `.ai/evaluation.md`
10. `.ai/handoff.md`
11. `backend/app/storage/database.py`
12. `backend/app/services/retrieval.py`
13. `backend/app/services/prompt_builder.py`
14. `backend/app/static/demo.html`
15. `backend/tests/test_retrieval_api.py`
16. `backend/tests/test_generation_api.py`
17. `backend/tests/test_demo_page.py`
18. `backend/tests/test_phase5_demo_workflow.py`

Key decision:

- Keep deterministic `/api/retrieve` as the default.
- Do not add Qdrant, Haystack, embeddings, model downloads, API keys, network
  access, or vector services to normal tests.
- If implementation proceeds, start with a fake-testable semantic adapter
  boundary and metadata-preservation tests before any real Qdrant/Haystack
  integration.

Phase 13 check:

- No `Phase 13` / `phase13` definition exists in the repository at this handoff.
- Do not start Phase 13 without an explicit roadmap entry, scope, non-goals,
  and verification plan.

Phase 11 baseline inputs:

1. `docs/ai/sample-outputs/phase11/manifest.json`
2. `docs/ai/sample-outputs/phase11/retrieval-evidence.json`
3. `docs/ai/38-phase11-repeatable-demo-runbook.md`
4. `backend/tests/test_phase11_sample_outputs.py`

Known blocker:

1. Bash verification may remain unavailable on this Windows machine because
   WSL / Linux distro is not installed.

Latest verification:

- `ai-status`: passed.
- `ai-doctor`: passed.
- targeted pytest after resumed closeout:
  `backend/tests/test_retrieval_api.py`
  `backend/tests/test_generation_api.py`
  `backend/tests/test_demo_page.py`
  `backend/tests/test_phase5_demo_workflow.py`
  -> `26 passed, 1 warning`
- `.\scripts\ai_check.ps1`: passed after resumed closeout with
  `121 passed, 1 warning`
- `git diff --check`: passed with line-ending normalization warnings only
- `bash ./scripts/ai_check.sh`: attempted and failed because no usable
  WSL/Linux distro is available; not passed
- browser smoke: local Chrome via Playwright loaded `/demo` at 1440x1000 and
  390x844 with no console errors, no horizontal overflow, favicon present, and
  correct initial button gating
- real Phase 11 fixed-sample API replay: passed with temporary runtime storage;
  historical samples parsed to `43/88` and `8/15` section/chunk counts, built
  `88 + 15` knowledge cards, tender analysis produced `26/34/52`
  requirement/scoring/risk counts, and PRD tag retrieval returned `5`
  card-backed evidence results

Next safe step:

1. Either explicitly define Phase 13, or continue Phase 12 into the adapter
   skeleton code slice.
2. If continuing Phase 12, keep deterministic `/api/retrieve` as default and
   start with fake-testable adapter boundary tests.
