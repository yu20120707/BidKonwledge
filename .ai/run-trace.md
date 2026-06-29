# Run Trace

Keep a short execution log for large-mode work.

## Phase 12 - Semantic Retrieval Adapter Spike

- command: context confirmation
- output: `git status --short --branch` reported `## main...origin/main`;
  `ai-status` confirmed `mode: large`, `status: DONE`, `current_gate: none`;
  `ai-doctor` passed and reported a clean working tree before Phase 12 edits.

- command: required reading
- output: read `AGENTS.md`, `docs/ai/README.md`,
  `docs/ai/workflow.md`, `docs/ai/09-phase-roadmap.md`,
  `docs/ai/17-lightweight-prd-completion-plan.md`,
  `docs/ai/36-phase11-sample-outputs-dev-spec.md`,
  `docs/ai/37-phase11-test-cases.md`,
  `docs/ai/38-phase11-repeatable-demo-runbook.md`,
  `docs/ai/sample-outputs/phase11/manifest.json`,
  `docs/ai/sample-outputs/phase11/retrieval-evidence.json`, and active
  `.ai` files.

- command: retrieval source inspection
- output: read current deterministic retrieval route, service, tests, schemas,
  config, and database retrieval helper. Confirmed `/api/retrieve` uses local
  SQLite chunks and does not require Qdrant, Haystack, embeddings, LLMs, or
  network access.

- command: task contract
- output: classified Phase 12 as harness `large`, task Level 2 / medium for
  the planning slice. Target is technical plan and evaluation boundary first;
  backend code remains deferred until a separate decision gate.

- command: official docs refresh
- output: checked Qdrant, Haystack, and BGE-M3 official docs for current
  integration facts. Used them to shape the optional adapter plan.

- command: Phase 12 docs
- output: added Phase 12 dev spec, test cases, and initial evaluation report.
  The docs keep deterministic retrieval as default and recommend fake adapter
  tests before real Qdrant/Haystack/embedding integration.

- mid-task review
- output: scope stayed inside planned docs and `.ai` runtime artifacts. Backend
  code, schema, dependencies, and API contracts remained untouched. Decision:
  keep Level 2 plan and stop this slice at planning/evaluation.

- command: targeted pytest
- output: `backend/tests/test_phase11_sample_outputs.py` passed with
  `3 passed, 1 warning`.

- command: Windows project check
- output: `.\scripts\ai_check.ps1` passed. Compile check passed and backend
  pytest passed with `114 passed, 1 warning`.

- command: diff hygiene
- output: `git diff --check` passed with CRLF normalization warnings only.

- command: bash project check
- output: `bash ./scripts/ai_check.sh` failed because no usable WSL/Linux
  distro is available on this Windows machine.

- command: Phase 13 check
- output: searched `AGENTS.md`, `README.md`, `docs/`, and `.ai/` for
  `Phase 13` / `phase13`; no Phase 13 definition was found.

- command: Phase 12 closeout
- output: marked Phase 12 as planning/evaluation slice complete and recorded
  that the next step is either explicitly defining Phase 13 or continuing
  Phase 12 into the adapter skeleton code slice.

## Resumed Closeout - PRD Demo Loop And Subagent Review

- command: multi-subagent orchestration
- output: restarted subagent orchestration after earlier capacity/tooling
  issues. Architect and backend review subagents completed, then were closed.
  Two new read-only reviewers were spawned: one for current diff/test gaps and
  one for docs/.ai Phase 12 closeout consistency.

- command: docs/.ai reviewer result
- output: confirmed no Phase 13 definition exists. Reviewer identified small
  consistency gaps in bash blocker wording and `.ai/handoff.md` affected-file
  coverage.

- command: backend/retrieval closeout edits
- output: kept `/api/retrieve` deterministic by default. Added historical-only
  retrieval corpus filtering, PRD knowledge-card tag retrieval over source
  chunks, and equal-score preference for knowledge-card-backed rows.

- command: demo closeout edits
- output: kept public API contracts unchanged. Demo now first retrieves by PRD
  tag, then falls back to the mapped chunk tag only when the PRD tag returns no
  evidence. Raw JSON records requested/effective/fallback tags and whether the
  fallback was used.

- command: targeted pytest
- output: refreshed
  `backend/tests/test_retrieval_api.py`,
  `backend/tests/test_generation_api.py`,
  `backend/tests/test_demo_page.py`, and
  `backend/tests/test_phase5_demo_workflow.py`; earlier checkpoint result was
  `23 passed, 1 warning`.

## Loop Engineering Pass - Demo Polish And Evidence Boundary

- command: subagent challenge
- output: spawned read-only PRD/demo completion and architect/backend reviewers.
  Reviewers identified that query-only retrieval could drift after knowledge
  card build, generation prompts did not expose the PRD knowledge-card bridge,
  and the demo page still lacked browser-level polish evidence.

- command: retrieval boundary hardening
- output: limited knowledge-card-backed retrieval candidates to requests whose
  tag exactly matches the knowledge-card tag. Query-only and ordinary chunk-tag
  retrieval now stay stable before and after knowledge-card build.

- command: generation prompt bridge
- output: added optional `knowledge_card_tag`, `knowledge_card_title`, and
  `knowledge_card_confidence` lines to generation prompt context without
  changing public response schemas.

- command: demo polish
- output: tightened `/demo` into a product-workbench style: neutral background,
  8px panel radius, system UI typography, focus-visible states, reduced-motion
  handling, favicon, and button loading/error wrappers. Demo generation now
  appends the first analyzed tender requirement to the generation query and
  records `tender_requirement_used` plus `generation_query` in Raw JSON.

- command: browser validation
- output: used local Chrome via Playwright against `http://127.0.0.1:8000/demo`.
  Desktop 1440x1000 and mobile 390x844 both loaded with no console errors, no
  horizontal overflow, two sample guides, favicon present, and correct initial
  button gating.

- command: historical evidence pool
- output: added a visible historical evidence pool to the demo page so the two
  Phase 11 historical samples do not appear as a single-slot flow. Backend API
  tests now prove retrieval can return evidence from multiple historical
  documents while excluding tender documents.

- command: real fixed-sample replay
- output: ran the Phase 11 fixed sample set through the API with a temporary
  upload root and SQLite DB outside Git. The primary historical sample parsed
  into `43` sections / `88` chunks and built `88` cards; the qualification
  historical sample parsed into `8` sections / `15` chunks and built `15`
  cards; the tender sample parsed into `10` sections / `142` chunks and
  produced `26` requirements, `34` scoring items, and `52` disqualification
  risks. PRD tag retrieval returned `5` card-backed evidence results.

- command: refreshed verification
- output: targeted closeout pytest passed with `26 passed, 1 warning`;
  `.\scripts\ai_check.ps1` passed with `121 passed, 1 warning`;
  `git diff --check` passed with CRLF normalization warnings only;
  `bash ./scripts/ai_check.sh` still failed because no usable WSL/Linux distro
  is available.
