# Phase 10 PRD Demo Flow Dev Spec

## Purpose

Phase 10 upgrades `/demo` from a raw endpoint control panel into a PRD-shaped
single-page walkthrough. The page must let a stakeholder follow the intended
story:

1. historical bid upload and parse
2. knowledge card build and display
3. tender upload, parse, and analysis
4. PRD tag selection
5. retrieval evidence display
6. candidate content generation
7. citations, risks, human review, and raw JSON
8. OCR capability status shown only from Phase 9 smoke evidence

## Execution Level

Use harness `large` mode because the repository requires it after Phase 0.
Classify the implementation work itself as Level 2 / medium because the task is
one bounded demo workflow and should not require API/schema changes.

Escalate if:

1. the page cannot express the flow without changing shared API contracts
2. retrieval must accept new PRD tags at the backend contract level
3. database/schema changes become necessary

## In Scope

1. Restructure `backend/app/static/demo.html` into a PRD-shaped narrative flow.
2. Keep the page static and FastAPI-hosted.
3. Add separate historical and tender flow sections.
4. Display knowledge cards, tender analysis, retrieval evidence, candidate
   content, citations, risks, human-review state, and raw JSON.
5. Add PRD-facing tag selection controls.
6. Show OCR capability status from Phase 9 smoke evidence only.
7. Update targeted demo tests and `.ai` runtime evidence.
8. Add Phase 10 durable docs and runbook.

## Out Of Scope

1. No Qdrant, Haystack, embeddings, dense retrieval, or semantic retrieval.
2. No table reconstruction.
3. No image batch ingestion.
4. No certificate or qualification-material validation.
5. No login or user system.
6. No final Word/PDF bidding document export.
7. No PyMuPDF project dependency addition.
8. No new frontend framework or SPA build step.

## Key Design Decision

The page presents PRD labels, but the backend retrieval/generation contract
still uses the current deterministic retrieval tags.

Phase 10 therefore uses a page-layer mapping:

- `运维服务实施方案` -> `运维服务`
- `突发应急方案和措施` -> `应急响应`
- `网络和数据安全防护保障措施` -> `安全保障`
- `服务质量保障和考核评估方案` -> `项目管理`
- `团队人员` / `资格材料` -> `人员资质`
- `商务报价` -> `商务报价`

This keeps the change scoped to the demo layer and avoids silently changing
public API behavior.

## Acceptance Criteria

1. `GET /demo` returns a PRD-shaped page instead of a simple button stack.
2. A stakeholder can see the historical-bid path and tender path separately.
3. The page can call the existing upload, parse, knowledge, tender-analysis,
   retrieval, and generation APIs without changing their request/response
   contracts.
4. Knowledge cards are displayed with source-aware context.
5. Tender analysis displays requirements and disqualification risks.
6. Retrieval evidence displays score, source file, tags, and snippet.
7. Generation output still shows citations, risks, and
   `need_human_review = true`.
8. OCR copy is limited to Phase 9 smoke evidence and does not imply production
   readiness.

## Verification

Required:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_demo_page.py backend/tests/test_phase5_demo_workflow.py
.\scripts\ai_check.ps1
git diff --check
```

Also attempt:

```powershell
bash ./scripts/ai_check.sh
```

If WSL/Linux distro is unavailable on this Windows machine, record the blocker
and do not claim bash verification passed.
