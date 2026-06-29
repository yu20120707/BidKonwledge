# Implementation Plan - Phase 12 Semantic Retrieval Adapter Spike

## Execution Classification

- Harness mode: `large`
- Task level: started as Level 2 / medium for the documentation spike, then
  escalated to Level 3 for the resumed closeout because multi-subagent review,
  retrieval boundary hardening, demo-flow behavior, and docs/runtime artifacts
  had to stay aligned.
- Reason: the current closeout touches the retrieval evidence boundary and the
  stakeholder demo workflow, but still preserves public API contracts, schema,
  dependencies, and deterministic `/api/retrieve` as default.

## Target Outcome

Produce a technical plan and evaluation decision for optional semantic
retrieval.

The first slice should answer:

1. where Qdrant, Haystack, and embeddings would fit
2. how they stay optional
3. how to compare them against Phase 11 fixed samples
4. what minimum code boundary should exist before real external integrations

The resumed closeout should also make the existing deterministic demo path
consistent with PRD tags before any semantic adapter work begins.

## Plan

1. Confirm clean repo and large-mode harness state.
2. Read Phase 11 baseline docs, sample outputs, active `.ai` files, and current
   deterministic retrieval source/tests.
3. Check current official Qdrant, Haystack, and BGE-M3 documentation for
   integration facts.
4. Add Phase 12 dev spec, test cases, and initial evaluation report.
5. Update roadmap, docs index, lightweight PRD plan, and active `.ai` runtime
   artifacts.
6. Run targeted verification:
   - `backend/tests/test_phase11_sample_outputs.py`
   - `.\scripts\ai_check.ps1`
   - `git diff --check`
7. Attempt `bash ./scripts/ai_check.sh` only to record the known WSL blocker if
   still unavailable.

## Resumed Closeout Plan

1. Restart multi-subagent orchestration with disjoint read-only reviewers.
2. Integrate backend/code-review findings in the main workspace only.
3. Keep code changes limited to deterministic retrieval and demo-page behavior:
   - historical-only retrieval corpus
   - PRD knowledge-card tag lookup for source chunks
   - equal-score preference for knowledge-card-backed evidence
   - real demo fallback from PRD tag to chunk tag
4. Add targeted regression tests for PRD tag retrieval, tag-collision metadata,
   tender exclusion, multi-historical retrieval, PRD-label generation, and demo
   fallback evidence.
5. Update `.ai` and durable docs to distinguish Phase 12 planning/evaluation
   from the deterministic demo-flow closeout.
6. Run targeted pytest, project check, diff check, and record bash/WSL blocker.

## Mid-Task Review

Checkpoint after the initial documentation implementation:

- Status versus plan: context confirmation, official docs refresh, Phase 12
  docs, `.ai` runtime updates, and verification were completed.
- Scope changes at that checkpoint: none; backend code, schema, API contracts,
  and dependencies remained untouched until the later resumed closeout.
- Newly discovered risks: `.ai/context-pack.md` and `.ai/tech-design.md` still
  contain older baseline context, but the requested current runtime handoff is
  being kept in `.ai/handoff.md`, `.ai/spec.md`, `.ai/implementation-plan.md`,
  `.ai/run-trace.md`, `.ai/verification.md`, and `.ai/evaluation.md`.
- Side effects outside expected area: none observed beyond planned docs and
  `.ai` file updates.
- Verification sufficiency: sufficient for a documentation/planning slice; not
  sufficient for claiming semantic retrieval runtime behavior.
- Decision: keep Level 2 plan. Do not write backend code in this slice.

## Resumed Closeout Review

- Status versus plan: subagent orchestration was restored; read-only architect,
  backend, docs, and diff reviewers were used; the main agent integrated the
  smallest deterministic retrieval/demo fixes and then a loop-engineering
  polish pass.
- Scope changes: backend retrieval and demo tests were added after review
  findings showed the PRD tag bridge and fallback behavior were incomplete.
- Newly discovered risks: semantic adapter work should still wait until the
  evidence boundary is more explicit; multi-history demo and table-aware
  evidence remained the main product/demo gaps. Multi-history visibility was
  addressed with a historical evidence pool; table-aware evidence remains
  deferred.
- Side effects outside expected area: no schema, dependency, public API, or
  semantic runtime changes.
- Verification sufficiency: targeted pytest, Windows project checks, diff
  hygiene, and browser smoke were refreshed. Bash verification remains blocked
  by missing WSL/Linux distro.
- Decision: keep Level 3 for closeout, do not escalate into semantic runtime
  implementation or Phase 13.

## Code Decision Gate

Proceed to backend code only if the user accepts the adapter-boundary plan or
explicitly asks to continue from planning into implementation.

The lowest-risk code slice would be:

1. semantic retrieval record/match models or dataclasses
2. mapper from current SQLite retrievable chunk rows
3. fake deterministic semantic adapter
4. tests proving `/api/retrieve` remains dependency-free
5. tests proving source metadata is preserved

Real Qdrant/Haystack/embedding integration should remain manual/optional after
the fake boundary exists.
