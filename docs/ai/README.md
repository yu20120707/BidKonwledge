# docs/ai

This directory stores durable AI context for the 投标智能知识库能力验证版 Demo.

Read these files before implementation work:

1. `00-project-brief.md` - product goal and current phase.
2. `01-scope-boundary.md` - in-scope, out-of-scope, and Phase 1 limits.
3. `02-architecture.md` - future backend module and adapter boundaries.
4. `03-data-model.md` - domain entities and JSON result shapes.
5. `04-api-contract.md` - expected API surface across phases.
6. `05-dev-rules.md` - project-specific engineering rules.
7. `06-verification.md` - MVP and phase verification criteria.
8. `07-source-materials.md` - external source material paths.
9. `08-tech-selection.md` - selected stack and rejected alternatives.
10. `09-phase-roadmap.md` - staged delivery plan.
11. `10-phase1-dev-spec.md` - exact Phase 1 implementation boundary.
12. `11-local-dev-env.md` - local runtime, paths, and script expectations.
13. `12-phase1-api-persistence.md` - upload API and SQLite details.
14. `13-phase1-verification-checklist.md` - required checks before completion.
15. `14-reference-reuse-strategy.md` - direct二开 decision and reference-repo rules.
16. `15-target-architecture.md` - target architecture and phase data flow.
17. `16-phase1-test-cases.md` - detailed Phase 1 test-case specification.
18. `17-lightweight-prd-completion-plan.md` - supplemental plan for closing the lightweight PRD gap, including OCR.
19. `18-phase6-knowledge-cards-dev-spec.md` - Phase 6 knowledge-card implementation contract.
20. `19-phase6-test-cases.md` - Phase 6 knowledge-card test-case specification.
21. `20-phase6-demo-runbook.md` - Phase 6 server demo runbook.
22. `21-phase7-tender-analysis-dev-spec.md` - Phase 7 tender-analysis implementation contract.
23. `22-phase7-test-cases.md` - Phase 7 tender-analysis test-case specification.
24. `23-phase7-demo-runbook.md` - Phase 7 server demo runbook.
25. `24-phase8a-word-conversion-dev-spec.md` - Phase 8A legacy/mislabeled Word conversion contract.
26. `25-phase8a-test-cases.md` - Phase 8A conversion test-case specification.
27. `26-phase8a-demo-runbook.md` - Phase 8A real-sample smoke runbook.
28. `27-phase8b-ocr-adapter-dev-spec.md` - Phase 8B OCR adapter implementation contract.
29. `28-phase8b-test-cases.md` - Phase 8B OCR adapter test-case specification.
30. `29-phase8b-demo-runbook.md` - Phase 8B OCR smoke runbook.
31. `30-phase9-real-ocr-smoke-dev-spec.md` - Phase 9 real PaddleOCR runtime and scanned-PDF smoke contract.
32. `31-phase9-test-cases.md` - Phase 9 real OCR smoke test-case specification.
33. `32-phase9-demo-runbook.md` - Phase 9 real OCR smoke runbook.

Python backend profile files from Auto_AICoding_Harness are also present:

- `python.md`
- `frameworks.md`
- `dependency.md`
- `security.md`
- `testing.md`
- `typing.md`
- `data.md`
- `async.md`
- `packaging.md`
- `observability.md`
- `performance.md`
- `verification-matrix.md`

Source documents and sample-material indexes live under `docs/source-materials/`.

Task runtime state belongs in `.ai/`, not in this directory.
