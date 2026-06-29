# Evaluation

## Phase 12 Semantic Retrieval Adapter Spike Evaluation

Status: planning/evaluation slice implemented locally; deterministic demo-flow
closeout implemented and targeted tests passed.

Implemented in the planning/evaluation slice:

1. Created Phase 12 semantic retrieval spike dev spec.
2. Created Phase 12 test cases for documentation, adapter skeleton, and
   optional/manual Qdrant/Haystack/embedding smokes.
3. Created initial Phase 12 evaluation report.
4. Updated roadmap, docs index, lightweight PRD plan, and active `.ai`
   runtime artifacts.

Implemented in the resumed deterministic demo-flow closeout:

1. Restricted retrieval evidence candidates to parsed `historical_bid`
   documents.
2. Added PRD knowledge-card tag retrieval over source chunks without changing
   the public `/api/retrieve` response contract.
3. Preferred knowledge-card-backed rows when an original chunk row and card row
   tie on score, preserving `chunk_metadata.knowledge_card` evidence.
4. Made the demo page perform a real fallback from PRD tag to mapped chunk tag
   only when the PRD tag returns no evidence.
5. Added regression coverage for PRD tag retrieval, tag-collision metadata,
   tender exclusion, PRD-label generation, and demo fallback/effective-tag
   evidence.

Implemented in the loop-engineering polish pass:

1. Prevented knowledge-card-backed rows from changing query-only retrieval
   results after knowledge-card build.
2. Added mixed historical+tender retrieval coverage to prove tender chunks stay
   out of the evidence pool.
3. Added generation prompt bridge metadata for PRD knowledge-card evidence
   without changing public schemas.
4. Made the demo generation request include analyzed tender requirement context
   by folding it into the existing `query` field.
5. Polished `/demo` into a product workbench style and verified it in local
   Chrome at desktop and mobile viewports.
6. Added a visible historical evidence pool so the two Phase 11 historical
   samples can be represented as multiple evidence sources rather than a
   single hidden slot.

Scope control:

1. No public API contract changed.
2. No SQLite schema changed.
3. No dependency changed.
4. No Qdrant, Haystack, embedding model, API key, or network service became
   required for normal tests.
5. Deterministic `/api/retrieve` remains the default and only implemented
   retrieval path.

Most important decision:

Do not start with real Qdrant/Haystack code. If Phase 12 proceeds to
implementation, first add a fake-testable semantic retrieval adapter boundary
and metadata-preservation tests. Real Qdrant/Haystack/embedding integration
should remain optional/manual until that boundary is proven.

Phase 13 check:

- No `Phase 13` / `phase13` definition was found in `AGENTS.md`, `README.md`,
  `docs/`, or `.ai/`.
- Do not start Phase 13 without first defining its roadmap entry, scope,
  non-goals, and verification plan.

Verification summary:

- `ai-status`: passed, `mode: large`, status `DONE`, `current_gate: none`.
- `ai-doctor`: passed.
- targeted pytest after PRD demo-loop closeout edits:
  `26 passed, 1 warning`.
- `.\scripts\ai_check.ps1`: passed after resumed closeout with
  `121 passed, 1 warning`.
- `git diff --check`: passed with line-ending normalization warnings only.
- `bash ./scripts/ai_check.sh`: attempted and failed because no usable
  WSL/Linux distro is available; not passed.
- Browser validation: local Chrome via Playwright loaded `/demo` at
  1440x1000 and 390x844 with no console errors, no horizontal overflow,
  favicon present, and correct initial button gating.
- Real Phase 11 fixed-sample API replay: passed using temporary runtime
  storage outside Git. The two historical samples parsed and built `88 + 15`
  knowledge cards; the tender sample parsed and produced `26` requirements,
  `34` scoring items, and `52` disqualification risks; PRD tag retrieval
  returned `5` card-backed evidence results.

Residual risk:

1. This is not a retrieval-quality benchmark yet.
2. Official Qdrant/Haystack/BGE-M3 docs were used to shape the plan, but no
   local semantic runtime smoke has run yet.
3. Bash verification remains blocked by missing or unusable WSL/Linux distro on
   this Windows machine.
4. Phase 13 remains undefined; the next implementation path must be chosen
   explicitly.
5. Real fixed-sample replay covered upload, parse, knowledge build, tender
   analysis, and retrieval. It did not call a real external LLM or OCR replay.
