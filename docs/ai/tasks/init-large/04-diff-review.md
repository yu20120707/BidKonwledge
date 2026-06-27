# Diff Review

## Status

WAITING_HUMAN_DIFF_APPROVAL

## Git Status

```text
 A .ai/.gitkeep
 A .ai/affected-files.md
 A .ai/approvals/README.md
 A .ai/approvals/plan-approval.md
 A .ai/approvals/spec-approval.md
 A .ai/backups/20260627-214154/.ai/state.json
 A .ai/backups/20260627-214154/.ai/template-hashes.json
 A .ai/backups/20260627-214154/manifest.json
 A .ai/backups/20260628-004821/.ai/state.json
 A .ai/backups/20260628-004821/manifest.json
 A .ai/backups/20260628-005022/.ai/state.json
 A .ai/backups/20260628-005022/manifest.json
 A .ai/backups/20260628-005118/.ai/reviews/spec-review.md
 A .ai/backups/20260628-005118/.ai/state.json
 A .ai/backups/20260628-005118/docs/ai/tasks/README.md
 A .ai/backups/20260628-005118/docs/ai/tasks/init-large/00-prd.md
 A .ai/backups/20260628-005118/docs/ai/tasks/init-large/01-spec.md
 A .ai/backups/20260628-005118/docs/ai/tasks/init-large/02-tech-design.md
 A .ai/backups/20260628-005118/docs/ai/tasks/init-large/03-implementation-plan.md
 A .ai/backups/20260628-005118/docs/ai/tasks/init-large/04-diff-review.md
 A .ai/backups/20260628-005118/docs/ai/tasks/init-large/05-verification.md
 A .ai/backups/20260628-005118/docs/ai/tasks/init-large/06-risk-and-rollback.md
 A .ai/backups/20260628-005118/docs/ai/tasks/init-large/07-handoff.md
 A .ai/backups/20260628-005118/manifest.json
 A .ai/backups/20260628-005307/.ai/approvals/spec-approval.md
 A .ai/backups/20260628-005307/.ai/state.json
 A .ai/backups/20260628-005307/manifest.json
 A .ai/backups/20260628-005615/.ai/state.json
 A .ai/backups/20260628-005615/docs/ai/tasks/README.md
 A .ai/backups/20260628-005615/docs/ai/tasks/init-large/00-prd.md
 A .ai/backups/20260628-005615/docs/ai/tasks/init-large/01-spec.md
 A .ai/backups/20260628-005615/docs/ai/tasks/init-large/02-tech-design.md
 A .ai/backups/20260628-005615/docs/ai/tasks/init-large/03-implementation-plan.md
 A .ai/backups/20260628-005615/docs/ai/tasks/init-large/04-diff-review.md
 A .ai/backups/20260628-005615/docs/ai/tasks/init-large/05-verification.md
 A .ai/backups/20260628-005615/docs/ai/tasks/init-large/06-risk-and-rollback.md
 A .ai/backups/20260628-005615/docs/ai/tasks/init-large/07-handoff.md
 A .ai/backups/20260628-005615/manifest.json
 A .ai/backups/20260628-005751/.ai/state.json
 A .ai/backups/20260628-005751/manifest.json
 A .ai/context-pack.md
 A .ai/epic.md
 A .ai/evaluation.md
 A .ai/handoff.md
 A .ai/implementation-plan.md
 A .ai/reviews/README.md
 A .ai/reviews/plan-review.md
 A .ai/reviews/spec-review.md
 A .ai/risk-and-rollback.md
 A .ai/run-trace.md
 A .ai/scope.md
 A .ai/spec.md
 A .ai/state.json
 A .ai/subagent-packets/README.md
 A .ai/subagent-packets/evaluator.md
 A .ai/subagent-packets/explorer.md
 A .ai/subagent-packets/implementer.md
 A .ai/subagent-packets/planner.md
 A .ai/subagent-packets/reviewer.md
 A .ai/tasks/init-large/approval.json
 A .ai/tasks/init-large/context.jsonl
 A .ai/tasks/init-large/rca.md
 A .ai/tech-design.md
 A .ai/template-hashes.json
 A .ai/templates/README.md
 A .ai/verification.md
 A .codex/agents/README.md
 A .codex/agents/evaluator.md
 A .codex/agents/explorer.md
 A .codex/agents/implementer.md
 A .codex/agents/planner.md
 A .codex/agents/reviewer.md
 A .github/copilot-instructions.md
 A .gitignore
 A AGENTS.md
 A CLAUDE.md
 A README.md
 A backend/__init__.py
 A backend/app/.gitkeep
 A backend/app/__init__.py
 A backend/app/api/__init__.py
 A backend/app/api/files.py
 A backend/app/api/health.py
 A backend/app/config.py
 A backend/app/main.py
 A backend/app/schemas/__init__.py
 A backend/app/schemas/document.py
 A backend/app/storage/__init__.py
 A backend/app/storage/database.py
 A backend/app/storage/file_storage.py
 A backend/tests/.gitkeep
 A backend/tests/conftest.py
 A backend/tests/test_database.py
 A backend/tests/test_health.py
 A backend/tests/test_phase1_boundaries.py
 A backend/tests/test_storage.py
 A backend/tests/test_upload_contract.py
 A backend/tests/test_upload_validation.py
 A data/samples/.gitkeep
 A data/uploads/.gitkeep
 A docs/ai/00-project-brief.md
 A docs/ai/01-scope-boundary.md
 A docs/ai/02-architecture.md
 A docs/ai/03-data-model.md
 A docs/ai/04-api-contract.md
 A docs/ai/05-dev-rules.md
 A docs/ai/06-verification.md
 A docs/ai/07-source-materials.md
 A docs/ai/08-tech-selection.md
 A docs/ai/09-phase-roadmap.md
 A docs/ai/10-phase1-dev-spec.md
 A docs/ai/11-local-dev-env.md
 A docs/ai/12-phase1-api-persistence.md
 A docs/ai/13-phase1-verification-checklist.md
 A docs/ai/14-reference-reuse-strategy.md
 A docs/ai/15-target-architecture.md
 A docs/ai/16-phase1-test-cases.md
 A docs/ai/README.md
 A docs/ai/async.md
 A docs/ai/check-rules/drafts/init-large-spec.md
 A docs/ai/check-rules/index.md
 A docs/ai/data.md
 A docs/ai/dependency.md
 A docs/ai/frameworks.md
 A docs/ai/migrations/index.md
 A docs/ai/observability.md
 A docs/ai/packaging.md
 A docs/ai/performance.md
 A docs/ai/python.md
 A docs/ai/security.md
 A docs/ai/tasks/README.md
 A docs/ai/tasks/init-large/00-prd.md
 A docs/ai/tasks/init-large/01-spec.md
 A docs/ai/tasks/init-large/02-tech-design.md
 A docs/ai/tasks/init-large/03-implementation-plan.md
 A docs/ai/tasks/init-large/04-diff-review.md
 A docs/ai/tasks/init-large/05-verification.md
 A docs/ai/tasks/init-large/06-risk-and-rollback.md
 A docs/ai/tasks/init-large/07-handoff.md
 A docs/ai/testing.md
 A docs/ai/typing.md
 A docs/ai/verification-matrix.md
 A docs/ai/workflow.md
 A docs/source-materials/README.md
 A docs/source-materials/originals/deep-research-report.md
 A "docs/source-materials/originals/\346\212\225\346\240\207\346\231\272\350\203\275\347\237\245\350\257\206\345\272\223\350\203\275\345\212\233\351\252\214\350\257\201\347\211\210-PRD-v0.1.pdf"
 A docs/source-materials/reference-repos.md
 A docs/source-materials/sample-catalog.md
 A frontend/.gitkeep
 A pyproject.toml
 A scripts/ai_build.sh
 A scripts/ai_check.ps1
 A scripts/ai_check.sh
 A scripts/ai_test.sh
```

## Diff Stat

```text
 .ai/.gitkeep                                       |   1 +
 .ai/affected-files.md                              |  47 +++
 .ai/approvals/README.md                            |   3 +
 .ai/approvals/plan-approval.md                     |  21 +
 .ai/approvals/spec-approval.md                     |  21 +
 .ai/backups/20260627-214154/.ai/state.json         |  12 +
 .../20260627-214154/.ai/template-hashes.json       | 106 +++++
 .ai/backups/20260627-214154/manifest.json          |  20 +
 .ai/backups/20260628-004821/.ai/state.json         |  12 +
 .ai/backups/20260628-004821/manifest.json          |  12 +
 .ai/backups/20260628-005022/.ai/state.json         |  12 +
 .ai/backups/20260628-005022/manifest.json          |  12 +
 .../20260628-005118/.ai/reviews/spec-review.md     | 100 +++++
 .ai/backups/20260628-005118/.ai/state.json         |  12 +
 .../20260628-005118/docs/ai/tasks/README.md        |  14 +
 .../docs/ai/tasks/init-large/00-prd.md             |  18 +
 .../docs/ai/tasks/init-large/01-spec.md            |  27 ++
 .../docs/ai/tasks/init-large/02-tech-design.md     |  12 +
 .../ai/tasks/init-large/03-implementation-plan.md  |  11 +
 .../docs/ai/tasks/init-large/04-diff-review.md     |  10 +
 .../docs/ai/tasks/init-large/05-verification.md    |  27 ++
 .../ai/tasks/init-large/06-risk-and-rollback.md    |  14 +
 .../docs/ai/tasks/init-large/07-handoff.md         |  22 ++
 .ai/backups/20260628-005118/manifest.json          |  92 +++++
 .../20260628-005307/.ai/approvals/spec-approval.md |  21 +
 .ai/backups/20260628-005307/.ai/state.json         |  12 +
 .ai/backups/20260628-005307/manifest.json          |  20 +
 .ai/backups/20260628-005615/.ai/state.json         |  14 +
 .../20260628-005615/docs/ai/tasks/README.md        |  14 +
 .../docs/ai/tasks/init-large/00-prd.md             |  22 ++
 .../docs/ai/tasks/init-large/01-spec.md            | 156 ++++++++
 .../docs/ai/tasks/init-large/02-tech-design.md     |  34 ++
 .../ai/tasks/init-large/03-implementation-plan.md  |  90 +++++
 .../docs/ai/tasks/init-large/04-diff-review.md     |   3 +
 .../docs/ai/tasks/init-large/05-verification.md    | 162 ++++++++
 .../ai/tasks/init-large/06-risk-and-rollback.md    |  22 ++
 .../docs/ai/tasks/init-large/07-handoff.md         |  96 +++++
 .ai/backups/20260628-005615/manifest.json          |  84 ++++
 .ai/backups/20260628-005751/.ai/state.json         |  14 +
 .ai/backups/20260628-005751/manifest.json          |  12 +
 .ai/context-pack.md                                |  86 ++++
 .ai/epic.md                                        |  22 ++
 .ai/evaluation.md                                  | 146 +++++++
 .ai/handoff.md                                     | 191 +++++++++
 .ai/implementation-plan.md                         | 173 +++++++++
 .ai/reviews/README.md                              |   3 +
 .ai/reviews/plan-review.md                         | 166 ++++++++
 .ai/reviews/spec-review.md                         | 174 +++++++++
 .ai/risk-and-rollback.md                           |  22 ++
 .ai/run-trace.md                                   |  56 +++
 .ai/scope.md                                       |  22 ++
 .ai/spec.md                                        | 156 ++++++++
 .ai/state.json                                     |  15 +
 .ai/subagent-packets/README.md                     |  26 ++
 .ai/subagent-packets/evaluator.md                  |  63 +++
 .ai/subagent-packets/explorer.md                   |  61 +++
 .ai/subagent-packets/implementer.md                |  63 +++
 .ai/subagent-packets/planner.md                    |  66 ++++
 .ai/subagent-packets/reviewer.md                   |  61 +++
 .ai/tasks/init-large/approval.json                 |   8 +
 .ai/tasks/init-large/context.jsonl                 |   9 +
 .ai/tasks/init-large/rca.md                        |  29 ++
 .ai/tech-design.md                                 |  34 ++
 .ai/template-hashes.json                           | 182 +++++++++
 .ai/templates/README.md                            |   6 +
 .ai/verification.md                                | 313 +++++++++++++++
 .codex/agents/README.md                            |  19 +
 .codex/agents/evaluator.md                         |  46 +++
 .codex/agents/explorer.md                          |  45 +++
 .codex/agents/implementer.md                       |  47 +++
 .codex/agents/planner.md                           |  46 +++
 .codex/agents/reviewer.md                          |  44 +++
 .github/copilot-instructions.md                    |  15 +
 .gitignore                                         |  27 ++
 AGENTS.md                                          |  55 +++
 CLAUDE.md                                          |   4 +
 README.md                                          | 107 +++++
 backend/__init__.py                                |   1 +
 backend/app/.gitkeep                               |   1 +
 backend/app/__init__.py                            |   1 +
 backend/app/api/__init__.py                        |   1 +
 backend/app/api/files.py                           | 136 +++++++
 backend/app/api/health.py                          |  10 +
 backend/app/config.py                              |  45 +++
 backend/app/main.py                                |  15 +
 backend/app/schemas/__init__.py                    |   1 +
 backend/app/schemas/document.py                    |  35 ++
 backend/app/storage/__init__.py                    |   1 +
 backend/app/storage/database.py                    |  96 +++++
 backend/app/storage/file_storage.py                |  42 ++
 backend/tests/.gitkeep                             |   1 +
 backend/tests/conftest.py                          |  52 +++
 backend/tests/test_database.py                     |  91 +++++
 backend/tests/test_health.py                       |  21 +
 backend/tests/test_phase1_boundaries.py            |  34 ++
 backend/tests/test_storage.py                      |  93 +++++
 backend/tests/test_upload_contract.py              |  59 +++
 backend/tests/test_upload_validation.py            |  92 +++++
 data/samples/.gitkeep                              |   1 +
 data/uploads/.gitkeep                              |   1 +
 docs/ai/00-project-brief.md                        |  65 ++++
 docs/ai/01-scope-boundary.md                       |  84 ++++
 docs/ai/02-architecture.md                         |  62 +++
 docs/ai/03-data-model.md                           |  81 ++++
 docs/ai/04-api-contract.md                         | 163 ++++++++
 docs/ai/05-dev-rules.md                            |  39 ++
 docs/ai/06-verification.md                         |  53 +++
 docs/ai/07-source-materials.md                     |  38 ++
 docs/ai/08-tech-selection.md                       |  71 ++++
 docs/ai/09-phase-roadmap.md                        |  92 +++++
 docs/ai/10-phase1-dev-spec.md                      | 102 +++++
 docs/ai/11-local-dev-env.md                        | 105 +++++
 docs/ai/12-phase1-api-persistence.md               | 150 +++++++
 docs/ai/13-phase1-verification-checklist.md        |  96 +++++
 docs/ai/14-reference-reuse-strategy.md             | 114 ++++++
 docs/ai/15-target-architecture.md                  | 157 ++++++++
 docs/ai/16-phase1-test-cases.md                    | 431 +++++++++++++++++++++
 docs/ai/README.md                                  |  42 ++
 docs/ai/async.md                                   |  18 +
 docs/ai/check-rules/drafts/init-large-spec.md      |  19 +
 docs/ai/check-rules/index.md                       |   5 +
 docs/ai/data.md                                    |  18 +
 docs/ai/dependency.md                              |  18 +
 docs/ai/frameworks.md                              |  18 +
 docs/ai/migrations/index.md                        |   4 +
 docs/ai/observability.md                           |  18 +
 docs/ai/packaging.md                               |  18 +
 docs/ai/performance.md                             |  18 +
 docs/ai/python.md                                  |  21 +
 docs/ai/security.md                                |  18 +
 docs/ai/tasks/README.md                            |  14 +
 docs/ai/tasks/init-large/00-prd.md                 |  22 ++
 docs/ai/tasks/init-large/01-spec.md                | 156 ++++++++
 docs/ai/tasks/init-large/02-tech-design.md         |  34 ++
 docs/ai/tasks/init-large/03-implementation-plan.md | 173 +++++++++
 docs/ai/tasks/init-large/04-diff-review.md         |   3 +
 docs/ai/tasks/init-large/05-verification.md        | 162 ++++++++
 docs/ai/tasks/init-large/06-risk-and-rollback.md   |  22 ++
 docs/ai/tasks/init-large/07-handoff.md             |  96 +++++
 docs/ai/testing.md                                 |  19 +
 docs/ai/typing.md                                  |  18 +
 docs/ai/verification-matrix.md                     |  16 +
 docs/ai/workflow.md                                |  57 +++
 docs/source-materials/README.md                    |  35 ++
 .../originals/deep-research-report.md              | 312 +++++++++++++++
 ...1\252\214\350\257\201\347\211\210-PRD-v0.1.pdf" | Bin 0 -> 369642 bytes
 docs/source-materials/reference-repos.md           |  22 ++
 docs/source-materials/sample-catalog.md            |  53 +++
 frontend/.gitkeep                                  |   1 +
 pyproject.toml                                     |  28 ++
 scripts/ai_build.sh                                |  18 +
 scripts/ai_check.ps1                               |  24 ++
 scripts/ai_check.sh                                |  18 +
 scripts/ai_test.sh                                 |  17 +
 154 files changed, 8310 insertions(+)
```

## Changed Files

```text
.ai/.gitkeep
.ai/affected-files.md
.ai/approvals/README.md
.ai/approvals/plan-approval.md
.ai/approvals/spec-approval.md
.ai/backups/20260627-214154/.ai/state.json
.ai/backups/20260627-214154/.ai/template-hashes.json
.ai/backups/20260627-214154/manifest.json
.ai/backups/20260628-004821/.ai/state.json
.ai/backups/20260628-004821/manifest.json
.ai/backups/20260628-005022/.ai/state.json
.ai/backups/20260628-005022/manifest.json
.ai/backups/20260628-005118/.ai/reviews/spec-review.md
.ai/backups/20260628-005118/.ai/state.json
.ai/backups/20260628-005118/docs/ai/tasks/README.md
.ai/backups/20260628-005118/docs/ai/tasks/init-large/00-prd.md
.ai/backups/20260628-005118/docs/ai/tasks/init-large/01-spec.md
.ai/backups/20260628-005118/docs/ai/tasks/init-large/02-tech-design.md
.ai/backups/20260628-005118/docs/ai/tasks/init-large/03-implementation-plan.md
.ai/backups/20260628-005118/docs/ai/tasks/init-large/04-diff-review.md
.ai/backups/20260628-005118/docs/ai/tasks/init-large/05-verification.md
.ai/backups/20260628-005118/docs/ai/tasks/init-large/06-risk-and-rollback.md
.ai/backups/20260628-005118/docs/ai/tasks/init-large/07-handoff.md
.ai/backups/20260628-005118/manifest.json
.ai/backups/20260628-005307/.ai/approvals/spec-approval.md
.ai/backups/20260628-005307/.ai/state.json
.ai/backups/20260628-005307/manifest.json
.ai/backups/20260628-005615/.ai/state.json
.ai/backups/20260628-005615/docs/ai/tasks/README.md
.ai/backups/20260628-005615/docs/ai/tasks/init-large/00-prd.md
.ai/backups/20260628-005615/docs/ai/tasks/init-large/01-spec.md
.ai/backups/20260628-005615/docs/ai/tasks/init-large/02-tech-design.md
.ai/backups/20260628-005615/docs/ai/tasks/init-large/03-implementation-plan.md
.ai/backups/20260628-005615/docs/ai/tasks/init-large/04-diff-review.md
.ai/backups/20260628-005615/docs/ai/tasks/init-large/05-verification.md
.ai/backups/20260628-005615/docs/ai/tasks/init-large/06-risk-and-rollback.md
.ai/backups/20260628-005615/docs/ai/tasks/init-large/07-handoff.md
.ai/backups/20260628-005615/manifest.json
.ai/backups/20260628-005751/.ai/state.json
.ai/backups/20260628-005751/manifest.json
.ai/context-pack.md
.ai/epic.md
.ai/evaluation.md
.ai/handoff.md
.ai/implementation-plan.md
.ai/reviews/README.md
.ai/reviews/plan-review.md
.ai/reviews/spec-review.md
.ai/risk-and-rollback.md
.ai/run-trace.md
.ai/scope.md
.ai/spec.md
.ai/state.json
.ai/subagent-packets/README.md
.ai/subagent-packets/evaluator.md
.ai/subagent-packets/explorer.md
.ai/subagent-packets/implementer.md
.ai/subagent-packets/planner.md
.ai/subagent-packets/reviewer.md
.ai/tasks/init-large/approval.json
.ai/tasks/init-large/context.jsonl
.ai/tasks/init-large/rca.md
.ai/tech-design.md
.ai/template-hashes.json
.ai/templates/README.md
.ai/verification.md
.codex/agents/README.md
.codex/agents/evaluator.md
.codex/agents/explorer.md
.codex/agents/implementer.md
.codex/agents/planner.md
.codex/agents/reviewer.md
.github/copilot-instructions.md
.gitignore
AGENTS.md
CLAUDE.md
README.md
backend/__init__.py
backend/app/.gitkeep
backend/app/__init__.py
backend/app/api/__init__.py
backend/app/api/files.py
backend/app/api/health.py
backend/app/config.py
backend/app/main.py
backend/app/schemas/__init__.py
backend/app/schemas/document.py
backend/app/storage/__init__.py
backend/app/storage/database.py
backend/app/storage/file_storage.py
backend/tests/.gitkeep
backend/tests/conftest.py
backend/tests/test_database.py
backend/tests/test_health.py
backend/tests/test_phase1_boundaries.py
backend/tests/test_storage.py
backend/tests/test_upload_contract.py
backend/tests/test_upload_validation.py
data/samples/.gitkeep
data/uploads/.gitkeep
docs/ai/00-project-brief.md
docs/ai/01-scope-boundary.md
docs/ai/02-architecture.md
docs/ai/03-data-model.md
docs/ai/04-api-contract.md
docs/ai/05-dev-rules.md
docs/ai/06-verification.md
docs/ai/07-source-materials.md
docs/ai/08-tech-selection.md
docs/ai/09-phase-roadmap.md
docs/ai/10-phase1-dev-spec.md
docs/ai/11-local-dev-env.md
docs/ai/12-phase1-api-persistence.md
docs/ai/13-phase1-verification-checklist.md
docs/ai/14-reference-reuse-strategy.md
docs/ai/15-target-architecture.md
docs/ai/16-phase1-test-cases.md
docs/ai/README.md
docs/ai/async.md
docs/ai/check-rules/drafts/init-large-spec.md
docs/ai/check-rules/index.md
docs/ai/data.md
docs/ai/dependency.md
docs/ai/frameworks.md
docs/ai/migrations/index.md
docs/ai/observability.md
docs/ai/packaging.md
docs/ai/performance.md
docs/ai/python.md
docs/ai/security.md
docs/ai/tasks/README.md
docs/ai/tasks/init-large/00-prd.md
docs/ai/tasks/init-large/01-spec.md
docs/ai/tasks/init-large/02-tech-design.md
docs/ai/tasks/init-large/03-implementation-plan.md
docs/ai/tasks/init-large/04-diff-review.md
docs/ai/tasks/init-large/05-verification.md
docs/ai/tasks/init-large/06-risk-and-rollback.md
docs/ai/tasks/init-large/07-handoff.md
docs/ai/testing.md
docs/ai/typing.md
docs/ai/verification-matrix.md
docs/ai/workflow.md
docs/source-materials/README.md
docs/source-materials/originals/deep-research-report.md
"docs/source-materials/originals/\346\212\225\346\240\207\346\231\272\350\203\275\347\237\245\350\257\206\345\272\223\350\203\275\345\212\233\351\252\214\350\257\201\347\211\210-PRD-v0.1.pdf"
docs/source-materials/reference-repos.md
docs/source-materials/sample-catalog.md
frontend/.gitkeep
pyproject.toml
scripts/ai_build.sh
scripts/ai_check.ps1
scripts/ai_check.sh
scripts/ai_test.sh
```

## Diff

```diff
diff --git a/.ai/.gitkeep b/.ai/.gitkeep
new file mode 100644
index 0000000..8b13789
--- /dev/null
+++ b/.ai/.gitkeep
@@ -0,0 +1 @@
+
diff --git a/.ai/affected-files.md b/.ai/affected-files.md
new file mode 100644
index 0000000..2ba0154
--- /dev/null
+++ b/.ai/affected-files.md
@@ -0,0 +1,47 @@
+# Affected Files - Phase 1 Backend Foundation
+
+## Expected Added Files
+
+- `pyproject.toml`
+- `backend/app/__init__.py`
+- `backend/app/main.py`
+- `backend/app/config.py`
+- `backend/app/api/__init__.py`
+- `backend/app/api/health.py`
+- `backend/app/api/files.py`
+- `backend/app/schemas/__init__.py`
+- `backend/app/schemas/document.py`
+- `backend/app/storage/__init__.py`
+- `backend/app/storage/database.py`
+- `backend/app/storage/file_storage.py`
+- `backend/tests/conftest.py`
+- `backend/tests/test_health.py`
+- `backend/tests/test_upload_contract.py`
+- `backend/tests/test_upload_validation.py`
+- `backend/tests/test_storage.py`
+- `backend/tests/test_database.py`
+- `backend/tests/test_phase1_boundaries.py`
+
+## Expected Updated Files
+
+- `README.md`
+- `scripts/ai_check.ps1`
+- `scripts/ai_check.sh`
+- `.ai/spec.md`
+- `.ai/implementation-plan.md`
+- `.ai/affected-files.md`
+- `.ai/run-trace.md`
+- `.ai/verification.md`
+- `.ai/evaluation.md`
+- `.ai/handoff.md`
+- `.ai/state.json`
+- `.ai/reviews/spec-review.md`
+- `.ai/approvals/spec-approval.md`
+- large-mode generated files under `docs/ai/tasks/init-large/`
+
+## Forbidden Areas
+
+- Do not vendor `F:\BidKonwledge_refs\ragflow`.
+- Do not vendor `F:\BidKonwledge_refs\haystack-demos`.
+- Do not copy large customer sample files into the repository.
+- Do not implement OCR, LLM, embeddings, vector store, Haystack execution, knowledge cards, tender analysis, frontend Demo, user system, or Word/PDF export.
diff --git a/.ai/approvals/README.md b/.ai/approvals/README.md
new file mode 100644
index 0000000..ab34f96
--- /dev/null
+++ b/.ai/approvals/README.md
@@ -0,0 +1,3 @@
+# Approvals
+
+This directory stores approval records for large-mode tasks.
diff --git a/.ai/approvals/plan-approval.md b/.ai/approvals/plan-approval.md
new file mode 100644
index 0000000..f6cb6c8
--- /dev/null
+++ b/.ai/approvals/plan-approval.md
@@ -0,0 +1,21 @@
+# Plan Approval
+
+## Decision
+
+APPROVED
+
+## Gate
+
+plan
+
+## Previous Status
+
+WAITING_HUMAN_PLAN_APPROVAL
+
+## New Status
+
+PLAN_APPROVED
+
+## Notes
+
+Human approved the plan review gate.
diff --git a/.ai/approvals/spec-approval.md b/.ai/approvals/spec-approval.md
new file mode 100644
index 0000000..15f59b4
--- /dev/null
+++ b/.ai/approvals/spec-approval.md
@@ -0,0 +1,21 @@
+# Spec Approval
+
+## Decision
+
+APPROVED
+
+## Gate
+
+spec
+
+## Previous Status
+
+WAITING_HUMAN_SPEC_APPROVAL
+
+## New Status
+
+SPEC_APPROVED
+
+## Notes
+
+Human approved the spec review gate.
diff --git a/.ai/backups/20260627-214154/.ai/state.json b/.ai/backups/20260627-214154/.ai/state.json
new file mode 100644
index 0000000..d543791
--- /dev/null
+++ b/.ai/backups/20260627-214154/.ai/state.json
@@ -0,0 +1,12 @@
+{
+  "schema_version": 1,
+  "mode": "medium",
+  "profile": "python-backend-service",
+  "status": "INIT",
+  "current_gate": null,
+  "approved_gates": [],
+  "created_by": "Auto_AICoding_Harness",
+  "task_id": "init-medium",
+  "task_title": "Initialize harness in medium mode",
+  "updated_at": "2026-06-27T21:30:16+08:00"
+}
diff --git a/.ai/backups/20260627-214154/.ai/template-hashes.json b/.ai/backups/20260627-214154/.ai/template-hashes.json
new file mode 100644
index 0000000..a1bf6b3
--- /dev/null
+++ b/.ai/backups/20260627-214154/.ai/template-hashes.json
@@ -0,0 +1,106 @@
+{
+  "schema_version": 1,
+  "profile": "python-backend-service",
+  "files": [
+    {
+      "path": ".ai/.gitkeep",
+      "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
+    },
+    {
+      "path": ".ai/implementation-plan.md",
+      "sha256": "796c3297ff371f58999af70ca42e010656aa4abf12d18c6c7665b0e62c836e80"
+    },
+    {
+      "path": ".ai/run-trace.md",
+      "sha256": "533b76f7e8980a8193dd8d145add6cf97819a1bd93a276e545c9a921ff1264cc"
+    },
+    {
+      "path": ".ai/templates/README.md",
+      "sha256": "f0b3ef6c12cc04e0b217bb25f1715b5deb15b367fb0ce633008737682e282fc6"
+    },
+    {
+      "path": ".ai/verification.md",
+      "sha256": "e584acdddc52d448963ffe9925e9a49b6e829b86494ec85d057ff6402eddf700"
+    },
+    {
+      "path": ".github/copilot-instructions.md",
+      "sha256": "c3be6e94afc6ad33748d2818126ebccddce59291e77d057dbd53330bae883071"
+    },
+    {
+      "path": "AGENTS.md",
+      "sha256": "1038e187b4ca584b697563afa5abcd4793ef6765950f6b1f9058abb1156f44cb"
+    },
+    {
+      "path": "CLAUDE.md",
+      "sha256": "de31e5ff3de46ff418e5ea6a2ce068bd0a5d39b2c96b2325558718cacce71bd2"
+    },
+    {
+      "path": "docs/ai/async.md",
+      "sha256": "200430ab399334078195eae030120e67b105b3550b0a60d0b7d5528a137fe1f1"
+    },
+    {
+      "path": "docs/ai/data.md",
+      "sha256": "9e3820043e6d743070de15bc2b0718ec85327e77d62e1448105c27c82c934fb0"
+    },
+    {
+      "path": "docs/ai/dependency.md",
+      "sha256": "b871400bb96e3573dacfb7bec344afe413217870af6aa63556632294e037a461"
+    },
+    {
+      "path": "docs/ai/frameworks.md",
+      "sha256": "c0cd47788a2b75a6696c887fe9c8677494d2ab451c80029640489d6a5e709308"
+    },
+    {
+      "path": "docs/ai/observability.md",
+      "sha256": "41996dda20336d2d479454e542d2d0709b99289dad252f00c7cfe019cf554dcc"
+    },
+    {
+      "path": "docs/ai/packaging.md",
+      "sha256": "5398483725d14b63b12a4b3a27213de70e6e9974932756873faece77173d642e"
+    },
+    {
+      "path": "docs/ai/performance.md",
+      "sha256": "82ac1a2e185840146ac62ea790601c0bc5f7bbf5e9d8cd6b1cf0f1bd97f03e44"
+    },
+    {
+      "path": "docs/ai/python.md",
+      "sha256": "a2854b7272bd8e2c196ce1e29286609ae094490d87fcda7f49c483218c39c882"
+    },
+    {
+      "path": "docs/ai/README.md",
+      "sha256": "442b45633136126ad9b0139ee7bde0fc21850c695dd7b93d5575a2a20337e732"
+    },
+    {
+      "path": "docs/ai/security.md",
+      "sha256": "ec10aa68e4a74813f631224904ab4636e85b848c460ab08c6c68d1360cc5abb8"
+    },
+    {
+      "path": "docs/ai/testing.md",
+      "sha256": "345a31fccfe53eb90cb6ae16e433d79fcccdacacb7e0f08093b8b9b47516fed6"
+    },
+    {
+      "path": "docs/ai/typing.md",
+      "sha256": "4cacc2b57ddfbde6d468086336c8837881bbed3f65f42ec987ea3e973d7f73c7"
+    },
+    {
+      "path": "docs/ai/verification-matrix.md",
+      "sha256": "195ca11079c62c251814f97514d189f3f82a1c0ce6feaa159099bcc73c1e1577"
+    },
+    {
+      "path": "docs/ai/workflow.md",
+      "sha256": "07aa22c1a7a698e8ed3a37a358fe98dfc2c6c6daca022eb63772c1f6536acfbe"
+    },
+    {
+      "path": "scripts/ai_build.sh",
+      "sha256": "9feb6363dd15910756cf19e3399e82ed7a693b4ad3caa7abc234a03547188f00"
+    },
+    {
+      "path": "scripts/ai_check.sh",
+      "sha256": "667ff58541183e4c227e2c2abb15545fc37a25471ad056e3af354e216621a1f2"
+    },
+    {
+      "path": "scripts/ai_test.sh",
+      "sha256": "db25fee3702819854b3d2af7cb74852b4e97d51ab23fa6c587367a815e196986"
+    }
+  ]
+}
diff --git a/.ai/backups/20260627-214154/manifest.json b/.ai/backups/20260627-214154/manifest.json
new file mode 100644
index 0000000..a340cc6
--- /dev/null
+++ b/.ai/backups/20260627-214154/manifest.json
@@ -0,0 +1,20 @@
+{
+  "writes": [
+    {
+      "operation": "force_overwrite",
+      "path": ".ai/template-hashes.json",
+      "action": "OVERWRITTEN",
+      "sha256_before": "a59d921ead1479b4934c5540809c2eb8722b40df65b3024abbd81ac1ff90789c",
+      "sha256_after": "7eeba5f4404a0ff2433dbb1e10de517b0c8b0d9d63ff5ded90d3b49a8077d096",
+      "backup_path": ".ai/backups/20260627-214154/.ai/template-hashes.json"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": ".ai/state.json",
+      "action": "OVERWRITTEN",
+      "sha256_before": "ac6e5f7af6c8dec245e9a03a9902a108ac43cf604a45faef4bf01637e1bf240e",
+      "sha256_after": "7b3f7aa94654f919f22f6bb8f6ef1d41d784d38612d48a6e5962351e88deb4be",
+      "backup_path": ".ai/backups/20260627-214154/.ai/state.json"
+    }
+  ]
+}
diff --git a/.ai/backups/20260628-004821/.ai/state.json b/.ai/backups/20260628-004821/.ai/state.json
new file mode 100644
index 0000000..ae33db0
--- /dev/null
+++ b/.ai/backups/20260628-004821/.ai/state.json
@@ -0,0 +1,12 @@
+{
+  "schema_version": 1,
+  "mode": "large",
+  "profile": "python-backend-service",
+  "status": "INIT",
+  "current_gate": null,
+  "approved_gates": [],
+  "created_by": "Auto_AICoding_Harness",
+  "task_id": "init-large",
+  "task_title": "Initialize harness in large mode",
+  "updated_at": "2026-06-27T21:41:54+08:00"
+}
diff --git a/.ai/backups/20260628-004821/manifest.json b/.ai/backups/20260628-004821/manifest.json
new file mode 100644
index 0000000..e7146ca
--- /dev/null
+++ b/.ai/backups/20260628-004821/manifest.json
@@ -0,0 +1,12 @@
+{
+  "writes": [
+    {
+      "operation": "force_overwrite",
+      "path": ".ai/state.json",
+      "action": "OVERWRITTEN",
+      "sha256_before": "9c2b0aed005a9da331248c1f449414d98d66a6698d3f8f317459723e8df37043",
+      "sha256_after": "15c6a48c3880297a46fe4acdf87ac786a39f3583c20b71162cf1adaa5729e2af",
+      "backup_path": ".ai/backups/20260628-004821/.ai/state.json"
+    }
+  ]
+}
diff --git a/.ai/backups/20260628-005022/.ai/state.json b/.ai/backups/20260628-005022/.ai/state.json
new file mode 100644
index 0000000..c6f3704
--- /dev/null
+++ b/.ai/backups/20260628-005022/.ai/state.json
@@ -0,0 +1,12 @@
+{
+  "schema_version": 1,
+  "mode": "large",
+  "profile": "python-backend-service",
+  "status": "WAITING_HUMAN_SPEC_APPROVAL",
+  "current_gate": "spec",
+  "approved_gates": [],
+  "created_by": "Auto_AICoding_Harness",
+  "task_id": "init-large",
+  "task_title": "Initialize harness in large mode",
+  "updated_at": "2026-06-28T00:48:21+08:00"
+}
diff --git a/.ai/backups/20260628-005022/manifest.json b/.ai/backups/20260628-005022/manifest.json
new file mode 100644
index 0000000..682cb29
--- /dev/null
+++ b/.ai/backups/20260628-005022/manifest.json
@@ -0,0 +1,12 @@
+{
+  "writes": [
+    {
+      "operation": "force_overwrite",
+      "path": ".ai/state.json",
+      "action": "OVERWRITTEN",
+      "sha256_before": "15c6a48c3880297a46fe4acdf87ac786a39f3583c20b71162cf1adaa5729e2af",
+      "sha256_after": "1f65e61742003043bdce0a80210efe03915646a7ba3ac3905f1eca3fce953033",
+      "backup_path": ".ai/backups/20260628-005022/.ai/state.json"
+    }
+  ]
+}
diff --git a/.ai/backups/20260628-005118/.ai/reviews/spec-review.md b/.ai/backups/20260628-005118/.ai/reviews/spec-review.md
new file mode 100644
index 0000000..379ab3c
--- /dev/null
+++ b/.ai/backups/20260628-005118/.ai/reviews/spec-review.md
@@ -0,0 +1,100 @@
+# Spec Review
+
+## Status
+
+WAITING_HUMAN_SPEC_APPROVAL
+
+## Source
+
+.ai/spec.md
+
+## Spec Summary
+
+```text
+# Spec - Phase 0 Repository Initialization
+
+## Objective
+
+Initialize `F:\BidKonwledge` as the business repository for the 投标智能知识库能力验证版 Demo.
+
+## Current Task
+
+Complete 0 阶段初始化:
+
+1. Initialize the empty folder as a Git repository.
+2. Copy the Auto_AICoding_Harness baseline workflow files.
+3. Write project background and durable context under `docs/ai/`.
+4. Generate `.ai/` task files for the next implementation phase.
+
+## Project Understanding
+
+The product is a lightweight capability-validation demo, not a full bidding system.
+
+The demo should eventually validate:
+
+- historical bid ingestion
+- document parsing
+- section and tag based knowledge cards
+- tender analysis
+- retrieval
+- LLM-generated candidate content
+- citations
+- risk hints
+- human review markers
+
+## Hard Boundaries
+
+Do not implement during Phase 0:
+
+- FastAPI business code
+- OCR
+- LLM calls
+- embeddings
+- vector store
+- knowledge card generation
+- tender analysis
+- demo page
+- user system
+- Word/PDF export
+
+## Acceptance Criteria
+
+Phase 0 is accepted when the repository contains:
+
+- harness baseline files
+- `docs/ai/00-project-brief.md`
+- `docs/ai/01-scope-boundary.md`
+- `docs/ai/02-architecture.md`
+- `docs/ai/03-data-model.md`
+- `docs/ai/04-api-contract.md`
+- `docs/ai/05-dev-rules.md`
+- `docs/ai/06-verification.md`
+- `.ai/implementation-plan.md`
+- `.ai/verification.md`
+- `.ai/evaluation.md`
+- `.ai/handoff.md`
+```
+
+## Scope Check
+
+- [ ] Goal is clear
+- [ ] Non-goals are explicit
+- [ ] Allowed files / modules are clear
+- [ ] Forbidden changes are clear
+- [ ] Required validation is defined
+
+## Risk Check
+
+- [ ] API / ABI risk considered
+- [ ] Data / persistence risk considered
+- [ ] Concurrency / IPC / network risk considered
+- [ ] Performance risk considered
+- [ ] Rollback or recovery considered
+
+## Human Decision
+
+- [ ] Approved
+- [ ] Needs replan
+- [ ] Rejected
+
+## Human Notes
diff --git a/.ai/backups/20260628-005118/.ai/state.json b/.ai/backups/20260628-005118/.ai/state.json
new file mode 100644
index 0000000..67c195c
--- /dev/null
+++ b/.ai/backups/20260628-005118/.ai/state.json
@@ -0,0 +1,12 @@
+{
+  "schema_version": 1,
+  "mode": "large",
+  "profile": "python-backend-service",
+  "status": "NEEDS_REPLAN",
+  "current_gate": null,
+  "approved_gates": [],
+  "created_by": "Auto_AICoding_Harness",
+  "task_id": "init-large",
+  "task_title": "Initialize harness in large mode",
+  "updated_at": "2026-06-28T00:50:22+08:00"
+}
diff --git a/.ai/backups/20260628-005118/docs/ai/tasks/README.md b/.ai/backups/20260628-005118/docs/ai/tasks/README.md
new file mode 100644
index 0000000..10af412
--- /dev/null
+++ b/.ai/backups/20260628-005118/docs/ai/tasks/README.md
@@ -0,0 +1,14 @@
+# Task Evidence Chain
+
+Each subdirectory under `docs/ai/tasks/` represents one large-mode task keyed by `.ai/state.json::task_id`.
+
+Expected files:
+
+- `00-prd.md`
+- `01-spec.md`
+- `02-tech-design.md`
+- `03-implementation-plan.md`
+- `04-diff-review.md`
+- `05-verification.md`
+- `06-risk-and-rollback.md`
+- `07-handoff.md`
diff --git a/.ai/backups/20260628-005118/docs/ai/tasks/init-large/00-prd.md b/.ai/backups/20260628-005118/docs/ai/tasks/init-large/00-prd.md
new file mode 100644
index 0000000..3b73021
--- /dev/null
+++ b/.ai/backups/20260628-005118/docs/ai/tasks/init-large/00-prd.md
@@ -0,0 +1,18 @@
+# PRD - Large-Mode Phase 1 Preparation
+
+## User Request
+
+后续开发必须基于 large 模式，并且必须跑脚本。当前任务是补齐开发前还差的文档。
+
+## Required Outcome
+
+1. Upgrade the repository to Auto_AICoding_Harness large mode.
+2. Persist the rule that future development must use large mode.
+3. Persist the rule that development completion requires script execution.
+4. Add missing Phase 1 pre-development documents.
+5. Do not implement business code.
+
+## Acceptance
+
+The task is complete when harness checks pass, scripts are run, and the missing Phase 1 documents are present.
+
diff --git a/.ai/backups/20260628-005118/docs/ai/tasks/init-large/01-spec.md b/.ai/backups/20260628-005118/docs/ai/tasks/init-large/01-spec.md
new file mode 100644
index 0000000..fa5749d
--- /dev/null
+++ b/.ai/backups/20260628-005118/docs/ai/tasks/init-large/01-spec.md
@@ -0,0 +1,27 @@
+# Spec
+
+## Target
+
+Prepare the repository for Phase 1 implementation under large mode.
+
+## Required Documents
+
+- `docs/ai/10-phase1-dev-spec.md`
+- `docs/ai/11-local-dev-env.md`
+- `docs/ai/12-phase1-api-persistence.md`
+- `docs/ai/13-phase1-verification-checklist.md`
+
+## Required Runtime Artifacts
+
+- `.ai/state.json` must report `mode = large`.
+- `.ai/state.json` must report `profile = python-backend-service`.
+- `.ai/verification.md` must record script checks.
+- `.ai/handoff.md` must give the next Phase 1 prompt.
+
+## Non-Goals
+
+- No FastAPI implementation.
+- No SQLite implementation.
+- No upload endpoint implementation.
+- No document parsing, retrieval, OCR, LLM, or UI.
+
diff --git a/.ai/backups/20260628-005118/docs/ai/tasks/init-large/02-tech-design.md b/.ai/backups/20260628-005118/docs/ai/tasks/init-large/02-tech-design.md
new file mode 100644
index 0000000..e43dcc2
--- /dev/null
+++ b/.ai/backups/20260628-005118/docs/ai/tasks/init-large/02-tech-design.md
@@ -0,0 +1,12 @@
+# Tech Design
+
+This is a documentation and workflow configuration task.
+
+The project remains a target repository generated by Auto_AICoding_Harness:
+
+- `docs/ai/` stores durable context.
+- `.ai/` stores runtime task state.
+- `docs/ai/tasks/init-large/` stores this large-mode evidence chain.
+
+Phase 1 will later implement the minimal backend described in `docs/ai/10-phase1-dev-spec.md`.
+
diff --git a/.ai/backups/20260628-005118/docs/ai/tasks/init-large/03-implementation-plan.md b/.ai/backups/20260628-005118/docs/ai/tasks/init-large/03-implementation-plan.md
new file mode 100644
index 0000000..a737c35
--- /dev/null
+++ b/.ai/backups/20260628-005118/docs/ai/tasks/init-large/03-implementation-plan.md
@@ -0,0 +1,11 @@
+# Implementation Plan
+
+1. Upgrade harness to large mode.
+2. Confirm or correct Python backend profile.
+3. Add missing Phase 1 documents.
+4. Update project entrypoint docs.
+5. Update `.ai` runtime artifacts.
+6. Run harness checks.
+7. Run project scripts.
+8. Record verification and evaluation.
+
diff --git a/.ai/backups/20260628-005118/docs/ai/tasks/init-large/04-diff-review.md b/.ai/backups/20260628-005118/docs/ai/tasks/init-large/04-diff-review.md
new file mode 100644
index 0000000..6e23aac
--- /dev/null
+++ b/.ai/backups/20260628-005118/docs/ai/tasks/init-large/04-diff-review.md
@@ -0,0 +1,10 @@
+# Diff Review
+
+Review focus:
+
+1. Does the diff only touch workflow and documentation files?
+2. Does it avoid business implementation?
+3. Does it clearly require large mode for future development?
+4. Does it require scripts before completion?
+5. Does it keep Phase 1 narrow?
+
diff --git a/.ai/backups/20260628-005118/docs/ai/tasks/init-large/05-verification.md b/.ai/backups/20260628-005118/docs/ai/tasks/init-large/05-verification.md
new file mode 100644
index 0000000..210d00f
--- /dev/null
+++ b/.ai/backups/20260628-005118/docs/ai/tasks/init-large/05-verification.md
@@ -0,0 +1,27 @@
+# Verification
+
+Required checks:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
+.\scripts\ai_check.ps1
+bash ./scripts/ai_check.sh
+```
+
+Expected:
+
+- Harness initialized.
+- Mode is large.
+- Profile is python-backend-service.
+- Scripts execute or any blocker is recorded.
+
+Observed:
+
+- Harness checks passed in large mode with `python-backend-service`.
+- `scripts/ai_check.ps1` passed.
+- `bash ./scripts/ai_check.sh` failed because WSL is not installed; use PowerShell script as the Windows-local check path until shell tooling is available.
+- Reference repositories were cloned outside the business repo under `F:\BidKonwledge_refs`.
+- Detailed Phase 1 test cases were documented in `docs/ai/16-phase1-test-cases.md`; pytest implementation remains a Phase 1 task.
+- The Phase 1 upload contract is now fixed as HTTP `201 Created` plus structured error JSON.
diff --git a/.ai/backups/20260628-005118/docs/ai/tasks/init-large/06-risk-and-rollback.md b/.ai/backups/20260628-005118/docs/ai/tasks/init-large/06-risk-and-rollback.md
new file mode 100644
index 0000000..f7e1464
--- /dev/null
+++ b/.ai/backups/20260628-005118/docs/ai/tasks/init-large/06-risk-and-rollback.md
@@ -0,0 +1,14 @@
+# Risk And Rollback
+
+## Risks
+
+- Harness upgrade can default to the wrong profile.
+- Documentation can drift into implementation instructions that are too broad.
+- Placeholder scripts can be mistaken for real tests.
+
+## Rollback
+
+Use Git revert before commit.
+
+If needed, restore harness state backups from `.ai/backups/20260627-214154/`.
+
diff --git a/.ai/backups/20260628-005118/docs/ai/tasks/init-large/07-handoff.md b/.ai/backups/20260628-005118/docs/ai/tasks/init-large/07-handoff.md
new file mode 100644
index 0000000..c54b305
--- /dev/null
+++ b/.ai/backups/20260628-005118/docs/ai/tasks/init-large/07-handoff.md
@@ -0,0 +1,22 @@
+# Handoff
+
+Before Phase 1 implementation:
+
+1. Run `ai-status` and `ai-doctor`.
+2. Confirm large mode.
+3. Read `AGENTS.md`.
+4. Read `docs/ai/10-phase1-dev-spec.md`.
+5. Read `docs/ai/11-local-dev-env.md`.
+6. Read `docs/ai/12-phase1-api-persistence.md`.
+7. Read `docs/ai/13-phase1-verification-checklist.md`.
+8. Read `docs/ai/16-phase1-test-cases.md`.
+
+Phase 1 must implement only the minimal FastAPI/upload/SQLite foundation and must run scripts before completion.
+
+The upload API contract is fixed before implementation:
+
+1. Valid upload returns HTTP `201 Created`.
+2. Success response includes `document_id`, `original_filename`, `doc_role`, `parse_status`, `file_size`, and `created_at`.
+3. Error response includes `error_code`, `message`, and `details`.
+4. SQLite `documents` fields must follow `docs/ai/12-phase1-api-persistence.md`.
+5. Phase 1 is not the customer-facing Demo.
diff --git a/.ai/backups/20260628-005118/manifest.json b/.ai/backups/20260628-005118/manifest.json
new file mode 100644
index 0000000..23903d3
--- /dev/null
+++ b/.ai/backups/20260628-005118/manifest.json
@@ -0,0 +1,92 @@
+{
+  "writes": [
+    {
+      "operation": "force_overwrite",
+      "path": ".ai/reviews/spec-review.md",
+      "action": "OVERWRITTEN",
+      "sha256_before": "f38d92ab39b3e6c681611f5e30ec465b1adca1b1e5bd1da9089fb38c21c65994",
+      "sha256_after": "719853226e63b12699d52d324a117779f1b011d80baf29ab0d35ef07f15cc8ee",
+      "backup_path": ".ai/backups/20260628-005118/.ai/reviews/spec-review.md"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": ".ai/state.json",
+      "action": "OVERWRITTEN",
+      "sha256_before": "1f65e61742003043bdce0a80210efe03915646a7ba3ac3905f1eca3fce953033",
+      "sha256_after": "446d263ed245d8f5b0b0b0ab55cc491f1ed9f14bd8fdd21ae1e90572d7ee6909",
+      "backup_path": ".ai/backups/20260628-005118/.ai/state.json"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": "docs/ai/tasks/README.md",
+      "action": "OVERWRITTEN",
+      "sha256_before": "65851afd96f38cdb389f0b7e3ae40c343def91ba47956bdbbe7356c2cb417582",
+      "sha256_after": "65851afd96f38cdb389f0b7e3ae40c343def91ba47956bdbbe7356c2cb417582",
+      "backup_path": ".ai/backups/20260628-005118/docs/ai/tasks/README.md"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": "docs/ai/tasks/init-large/00-prd.md",
+      "action": "OVERWRITTEN",
+      "sha256_before": "741c48b472955fbde7a69b3455a0af2713f54534748ae2b51059fd34bc5104c5",
+      "sha256_after": "30b914287b0c29c69b2e0165224aad359ee7818aa11db5ea2dd88c9179f300f1",
+      "backup_path": ".ai/backups/20260628-005118/docs/ai/tasks/init-large/00-prd.md"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": "docs/ai/tasks/init-large/01-spec.md",
+      "action": "OVERWRITTEN",
+      "sha256_before": "da70a21d1f4042f9e10219d3f8fefc7f237fa9eb05381c67c541b2cae375b4c0",
+      "sha256_after": "9134a266e0bb595e9cdaad6d22039861a2ebb75c02b278660f63993ff63cc6a6",
+      "backup_path": ".ai/backups/20260628-005118/docs/ai/tasks/init-large/01-spec.md"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": "docs/ai/tasks/init-large/02-tech-design.md",
+      "action": "OVERWRITTEN",
+      "sha256_before": "54094d762d28c06bcebc76adf54dbb1f77741f9b02d8f2cc8a17d158dc3fbeb1",
+      "sha256_after": "fc19144990f313d5225a02fd77cc7166a69e5f46aa71296f018bbf624033a4d8",
+      "backup_path": ".ai/backups/20260628-005118/docs/ai/tasks/init-large/02-tech-design.md"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": "docs/ai/tasks/init-large/03-implementation-plan.md",
+      "action": "OVERWRITTEN",
+      "sha256_before": "8edd0074b8d8703afb6d43918be9dc27e4e43f836dda92dccd3b7506e2ce3ef9",
+      "sha256_after": "bc504f8b471b849b7fd5ad56d278ffbfb095b8f2050fa99232bb7bc111487c4c",
+      "backup_path": ".ai/backups/20260628-005118/docs/ai/tasks/init-large/03-implementation-plan.md"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": "docs/ai/tasks/init-large/04-diff-review.md",
+      "action": "OVERWRITTEN",
+      "sha256_before": "33eefc3e919042513ff79bc84c8b9fa622147046df2cf575f13cdd0faf3ae3fb",
+      "sha256_after": "130aabb0ee983298a4a0ea7e160a2e5d0a5ac6af39b92e22bb8e6f4fab9a6e0d",
+      "backup_path": ".ai/backups/20260628-005118/docs/ai/tasks/init-large/04-diff-review.md"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": "docs/ai/tasks/init-large/05-verification.md",
+      "action": "OVERWRITTEN",
+      "sha256_before": "c23494f7924f61d55dc8c007d6166da854ca303896235ec14001dd329d363be5",
+      "sha256_after": "66920256c5a3ae2a772fe94d8b9bb1788ec2d9e738662f35684174a2fd8107b8",
+      "backup_path": ".ai/backups/20260628-005118/docs/ai/tasks/init-large/05-verification.md"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": "docs/ai/tasks/init-large/06-risk-and-rollback.md",
+      "action": "OVERWRITTEN",
+      "sha256_before": "9a13c6f17ae27b75aa71ea7cda568ff22b5bda27960145170c1c802f8d892ee2",
+      "sha256_after": "238d894d03cb9764e554ae91f6971588526acc2ee393159e1c418c6672500955",
+      "backup_path": ".ai/backups/20260628-005118/docs/ai/tasks/init-large/06-risk-and-rollback.md"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": "docs/ai/tasks/init-large/07-handoff.md",
+      "action": "OVERWRITTEN",
+      "sha256_before": "f0df6bb0aec51748dcda3c0aea729f84da740d308f01dfcfb28a30bfdc2898db",
+      "sha256_after": "2356c3feb4371680d1903e44724303ca8f161e4190ef6e4f7d0fba87f8d88099",
+      "backup_path": ".ai/backups/20260628-005118/docs/ai/tasks/init-large/07-handoff.md"
+    }
+  ]
+}
diff --git a/.ai/backups/20260628-005307/.ai/approvals/spec-approval.md b/.ai/backups/20260628-005307/.ai/approvals/spec-approval.md
new file mode 100644
index 0000000..a9a49d2
--- /dev/null
+++ b/.ai/backups/20260628-005307/.ai/approvals/spec-approval.md
@@ -0,0 +1,21 @@
+# Spec Approval
+
+## Decision
+
+REJECTED
+
+## Gate
+
+spec
+
+## Previous Status
+
+WAITING_HUMAN_SPEC_APPROVAL
+
+## New Status
+
+NEEDS_REPLAN
+
+## Notes
+
+Human rejected the spec review gate. The task requires replanning before continuing.
diff --git a/.ai/backups/20260628-005307/.ai/state.json b/.ai/backups/20260628-005307/.ai/state.json
new file mode 100644
index 0000000..3764cfe
--- /dev/null
+++ b/.ai/backups/20260628-005307/.ai/state.json
@@ -0,0 +1,12 @@
+{
+  "schema_version": 1,
+  "mode": "large",
+  "profile": "python-backend-service",
+  "status": "WAITING_HUMAN_SPEC_APPROVAL",
+  "current_gate": "spec",
+  "approved_gates": [],
+  "created_by": "Auto_AICoding_Harness",
+  "task_id": "init-large",
+  "task_title": "Initialize harness in large mode",
+  "updated_at": "2026-06-28T00:51:18+08:00"
+}
diff --git a/.ai/backups/20260628-005307/manifest.json b/.ai/backups/20260628-005307/manifest.json
new file mode 100644
index 0000000..f809689
--- /dev/null
+++ b/.ai/backups/20260628-005307/manifest.json
@@ -0,0 +1,20 @@
+{
+  "writes": [
+    {
+      "operation": "force_overwrite",
+      "path": ".ai/approvals/spec-approval.md",
+      "action": "OVERWRITTEN",
+      "sha256_before": "c80a468339b80c34d304baf73187f7352dd64f2f93723507cb192a76c4750969",
+      "sha256_after": "bb2dec304597f14015f988da0de8567d2d75c12ba254b52f459fa91ae2ea5853",
+      "backup_path": ".ai/backups/20260628-005307/.ai/approvals/spec-approval.md"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": ".ai/state.json",
+      "action": "OVERWRITTEN",
+      "sha256_before": "446d263ed245d8f5b0b0b0ab55cc491f1ed9f14bd8fdd21ae1e90572d7ee6909",
+      "sha256_after": "472ccaf0f5c838879ebf62a8da5e56069ccac6d2c22c0700d551007017556ff6",
+      "backup_path": ".ai/backups/20260628-005307/.ai/state.json"
+    }
+  ]
+}
diff --git a/.ai/backups/20260628-005615/.ai/state.json b/.ai/backups/20260628-005615/.ai/state.json
new file mode 100644
index 0000000..4c4ece0
--- /dev/null
+++ b/.ai/backups/20260628-005615/.ai/state.json
@@ -0,0 +1,14 @@
+{
+  "schema_version": 1,
+  "mode": "large",
+  "profile": "python-backend-service",
+  "status": "SPEC_APPROVED",
+  "current_gate": null,
+  "approved_gates": [
+    "spec"
+  ],
+  "created_by": "Auto_AICoding_Harness",
+  "task_id": "init-large",
+  "task_title": "Initialize harness in large mode",
+  "updated_at": "2026-06-28T00:53:07+08:00"
+}
diff --git a/.ai/backups/20260628-005615/docs/ai/tasks/README.md b/.ai/backups/20260628-005615/docs/ai/tasks/README.md
new file mode 100644
index 0000000..10af412
--- /dev/null
+++ b/.ai/backups/20260628-005615/docs/ai/tasks/README.md
@@ -0,0 +1,14 @@
+# Task Evidence Chain
+
+Each subdirectory under `docs/ai/tasks/` represents one large-mode task keyed by `.ai/state.json::task_id`.
+
+Expected files:
+
+- `00-prd.md`
+- `01-spec.md`
+- `02-tech-design.md`
+- `03-implementation-plan.md`
+- `04-diff-review.md`
+- `05-verification.md`
+- `06-risk-and-rollback.md`
+- `07-handoff.md`
diff --git a/.ai/backups/20260628-005615/docs/ai/tasks/init-large/00-prd.md b/.ai/backups/20260628-005615/docs/ai/tasks/init-large/00-prd.md
new file mode 100644
index 0000000..e1de3b9
--- /dev/null
+++ b/.ai/backups/20260628-005615/docs/ai/tasks/init-large/00-prd.md
@@ -0,0 +1,22 @@
+# Epic - Large-Mode Phase 1 Preparation
+
+## Objective
+
+Make this repository ready for Phase 1 development under Auto_AICoding_Harness `large` mode.
+
+## Outcome
+
+Before any business code is written, the repository must contain:
+
+1. Large-mode harness state.
+2. Project-level rule that future development must use large mode.
+3. Phase 1 development spec.
+4. Local development environment guide.
+5. Phase 1 API and persistence details.
+6. Phase 1 verification checklist.
+7. Updated `.ai` task artifacts and handoff.
+
+## Non-Goal
+
+This task does not implement FastAPI, upload handling, SQLite code, parsing, retrieval, LLM calls, or UI.
+
diff --git a/.ai/backups/20260628-005615/docs/ai/tasks/init-large/01-spec.md b/.ai/backups/20260628-005615/docs/ai/tasks/init-large/01-spec.md
new file mode 100644
index 0000000..b8d6bcc
--- /dev/null
+++ b/.ai/backups/20260628-005615/docs/ai/tasks/init-large/01-spec.md
@@ -0,0 +1,156 @@
+# Spec - Phase 1 Backend Foundation
+
+## Objective
+
+Implement the smallest runnable FastAPI backend foundation for the 投标智能知识库能力验证版 Demo.
+
+Phase 1 proves that the service can start, accept an uploaded file, save it under a configurable local upload root, and persist document metadata in SQLite.
+
+Phase 1 is a backend foundation milestone. It is not the customer-facing Demo acceptance milestone.
+
+## Required Execution Mode
+
+This task must run under Auto_AICoding_Harness `large` mode with the `python-backend-service` profile.
+
+Before implementation:
+
+1. Run `ai-status` or `ai-doctor`.
+2. Confirm `.ai/state.json` reports `"mode": "large"`.
+3. Use large-mode gates according to `AGENTS.md`.
+4. Use subagent orchestration because the user explicitly requested it.
+
+## In Scope
+
+Implement only:
+
+1. FastAPI application startup.
+2. `GET /health`.
+3. `POST /api/files/upload`.
+4. Upload success response with HTTP `201 Created`.
+5. Upload success fields:
+   - `document_id`
+   - `original_filename`
+   - `doc_role`
+   - `parse_status`
+   - `file_size`
+   - `created_at`
+6. Structured error response fields:
+   - `error_code`
+   - `message`
+   - `details`
+7. Configurable upload root.
+8. Backend-generated stored filenames that do not use raw user filenames.
+9. SQLite `documents` table matching `docs/ai/12-phase1-api-persistence.md`.
+10. Pytest coverage for all P0 cases in `docs/ai/16-phase1-test-cases.md`.
+11. README local startup and test commands.
+12. Updated `.ai/verification.md`, `.ai/evaluation.md`, and `.ai/handoff.md`.
+
+## Out Of Scope
+
+Do not implement:
+
+1. OCR.
+2. LLM calls.
+3. Embeddings.
+4. Vector store or Qdrant.
+5. Haystack pipeline execution.
+6. Knowledge card generation.
+7. Tender file analysis.
+8. Frontend Demo.
+9. User system.
+10. Word or PDF export.
+11. Production deployment.
+
+## Expected File Scope
+
+Allowed implementation scope:
+
+```text
+backend/
+├── app/
+│   ├── __init__.py
+│   ├── main.py
+│   ├── config.py
+│   ├── api/
+│   │   ├── __init__.py
+│   │   ├── health.py
+│   │   └── files.py
+│   ├── schemas/
+│   │   ├── __init__.py
+│   │   └── document.py
+│   └── storage/
+│       ├── __init__.py
+│       ├── database.py
+│       └── file_storage.py
+└── tests/
+    ├── test_health.py
+    ├── test_upload_contract.py
+    ├── test_upload_validation.py
+    ├── test_storage.py
+    ├── test_database.py
+    └── test_phase1_boundaries.py
+```
+
+Repository-level files may be updated only as needed:
+
+- `README.md`
+- `.gitignore`
+- one dependency file, preferably `pyproject.toml`
+- `scripts/ai_check.ps1`
+- `scripts/ai_check.sh`
+- `.ai/implementation-plan.md`
+- `.ai/affected-files.md`
+- `.ai/run-trace.md`
+- `.ai/verification.md`
+- `.ai/evaluation.md`
+- `.ai/handoff.md`
+
+## Reference Repository Rule
+
+Reference repositories must remain outside this repository under:
+
+```text
+F:\BidKonwledge_refs
+```
+
+Use RAGFlow only for product/document ingestion/citation reference and Haystack demos only for later pipeline-shape reference. Do not vendor either repository into `F:\BidKonwledge`.
+
+## Acceptance Criteria
+
+Phase 1 is accepted when:
+
+1. The FastAPI app is importable.
+2. `GET /health` returns HTTP 200 and exactly `{"status": "ok"}`.
+3. `POST /api/files/upload` accepts valid `historical_bid` and `tender` uploads.
+4. Valid upload returns HTTP `201 Created`.
+5. Success responses contain only the documented Phase 1 fields and do not expose absolute local paths.
+6. Invalid upload requests return the documented structured error shape and error codes.
+7. Uploaded bytes are stored under the configured upload root.
+8. Stored filenames are generated by the backend and are distinct from raw original filenames.
+9. SQLite creates and uses a `documents` table with the required Phase 1 fields.
+10. Validation failures do not leave orphan files or metadata rows.
+11. P0 pytest coverage from `docs/ai/16-phase1-test-cases.md` passes.
+12. `scripts/ai_check.ps1` runs real Phase 1 checks.
+13. `scripts/ai_check.sh` is run when available, or the WSL/bash blocker is recorded.
+14. Local uvicorn and `curl.exe --noproxy "*"` smoke checks are run if the app starts locally.
+15. `.ai/verification.md`, `.ai/evaluation.md`, and `.ai/handoff.md` record the actual command evidence and residual risks.
+
+## Required Verification Commands
+
+Run before completion:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
+.\scripts\ai_check.ps1
+python -m pytest backend/tests
+```
+
+When shell tooling is available:
+
+```powershell
+bash ./scripts/ai_check.sh
+```
+
+If WSL/bash is unavailable, record the reason in `.ai/verification.md` and do not claim the bash script passed.
diff --git a/.ai/backups/20260628-005615/docs/ai/tasks/init-large/02-tech-design.md b/.ai/backups/20260628-005615/docs/ai/tasks/init-large/02-tech-design.md
new file mode 100644
index 0000000..02cf8c6
--- /dev/null
+++ b/.ai/backups/20260628-005615/docs/ai/tasks/init-large/02-tech-design.md
@@ -0,0 +1,34 @@
+# Tech Design
+
+## Current Task Design
+
+This task is documentation and workflow configuration only.
+
+The design is to keep the repository as a generated target project for Auto_AICoding_Harness:
+
+- `docs/ai/` stores durable product and engineering context.
+- `.ai/` stores current large-mode task runtime artifacts.
+- `docs/source-materials/` stores source document copies and sample indexes.
+- `backend/` and `frontend/` remain placeholders until Phase 1 implementation begins.
+
+## Phase 1 Design Boundary
+
+Phase 1 will later implement:
+
+- FastAPI app startup.
+- `GET /health`.
+- `POST /api/files/upload`.
+- local file storage.
+- SQLite document metadata.
+- smoke tests.
+
+Phase 1 will not implement parsing, retrieval, generation, OCR, vector storage, or UI.
+
+## Interface Decisions For Future Implementation
+
+1. Upload status starts as `parse_status = pending`.
+2. SQLite table `documents` stores metadata only.
+3. Uploaded files are saved under configurable `data/uploads`.
+4. User-provided filenames are preserved as metadata but must not be trusted as storage paths.
+5. Tests and scripts must be run before completion.
+
diff --git a/.ai/backups/20260628-005615/docs/ai/tasks/init-large/03-implementation-plan.md b/.ai/backups/20260628-005615/docs/ai/tasks/init-large/03-implementation-plan.md
new file mode 100644
index 0000000..1d775eb
--- /dev/null
+++ b/.ai/backups/20260628-005615/docs/ai/tasks/init-large/03-implementation-plan.md
@@ -0,0 +1,90 @@
+# Implementation Plan
+
+## Current Large-Mode Prep Task
+
+1. Upgrade harness state to `large`.
+2. Record project rule: future development requires large mode and script execution.
+3. Add Phase 1 pre-development docs:
+   - `docs/ai/10-phase1-dev-spec.md`
+   - `docs/ai/11-local-dev-env.md`
+   - `docs/ai/12-phase1-api-persistence.md`
+   - `docs/ai/13-phase1-verification-checklist.md`
+   - `docs/ai/16-phase1-test-cases.md`
+4. Update `.ai` large-mode artifacts.
+5. Run harness checks and project scripts.
+6. Record verification, evaluation, and handoff.
+
+## Phase 0 - Initialization
+
+1. Initialize Git repository.
+2. Copy Auto_AICoding_Harness baseline project files.
+3. Create baseline business folders:
+   - `backend/app`
+   - `backend/tests`
+   - `frontend`
+   - `data/uploads`
+   - `data/samples`
+   - `scripts`
+4. Write durable project context under `docs/ai/`.
+5. Write current task artifacts under `.ai/`.
+6. Verify file presence and Git status.
+
+## Phase 1 - Minimal Backend Foundation
+
+Only after this large-mode prep is reviewed, implement:
+
+1. FastAPI app startup.
+2. `GET /health`.
+3. `POST /api/files/upload` with fixed `201 Created` success contract.
+4. Structured upload error responses.
+5. Local file saving to configured upload root with backend-generated stored filenames.
+6. Document metadata schema matching `docs/ai/12-phase1-api-persistence.md`.
+7. SQLite initialization.
+8. Basic configuration management.
+9. Phase 1 P0 pytest coverage from `docs/ai/16-phase1-test-cases.md`.
+10. Minimal manual smoke test.
+11. README local startup commands.
+
+## Recommended Backend Structure For Phase 1
+
+```text
+backend/
+├── app/
+│   ├── __init__.py
+│   ├── main.py
+│   ├── config.py
+│   ├── api/
+│   │   ├── __init__.py
+│   │   ├── health.py
+│   │   └── files.py
+│   ├── schemas/
+│   │   ├── __init__.py
+│   │   └── document.py
+│   └── storage/
+│       ├── __init__.py
+│       ├── database.py
+│       └── file_storage.py
+└── tests/
+    ├── test_health.py
+    ├── test_upload_contract.py
+    ├── test_upload_validation.py
+    ├── test_storage.py
+    ├── test_database.py
+    └── test_phase1_boundaries.py
+```
+
+## Phase 1 Non-Goals
+
+Do not implement OCR, LLM, embeddings, vector store, knowledge card generation, tender analysis, demo page, user system, or Word/PDF export in Phase 1.
+
+## Phase 1 Required Pre-Reads
+
+Before coding Phase 1, read:
+
+1. `AGENTS.md`
+2. `docs/ai/10-phase1-dev-spec.md`
+3. `docs/ai/11-local-dev-env.md`
+4. `docs/ai/12-phase1-api-persistence.md`
+5. `docs/ai/13-phase1-verification-checklist.md`
+6. `docs/ai/16-phase1-test-cases.md`
+7. `.ai/risk-and-rollback.md`
diff --git a/.ai/backups/20260628-005615/docs/ai/tasks/init-large/04-diff-review.md b/.ai/backups/20260628-005615/docs/ai/tasks/init-large/04-diff-review.md
new file mode 100644
index 0000000..6e3f11b
--- /dev/null
+++ b/.ai/backups/20260628-005615/docs/ai/tasks/init-large/04-diff-review.md
@@ -0,0 +1,3 @@
+# Diff Review
+
+Diff review has not been generated yet.
diff --git a/.ai/backups/20260628-005615/docs/ai/tasks/init-large/05-verification.md b/.ai/backups/20260628-005615/docs/ai/tasks/init-large/05-verification.md
new file mode 100644
index 0000000..df3c267
--- /dev/null
+++ b/.ai/backups/20260628-005615/docs/ai/tasks/init-large/05-verification.md
@@ -0,0 +1,162 @@
+# Verification
+
+## Large-Mode Requirement
+
+All future development must run under harness `large` mode and must run the project check scripts before completion.
+
+For this documentation-prep task, verify:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
+.\scripts\ai_check.ps1
+bash ./scripts/ai_check.sh
+```
+
+Observed on 2026-06-27:
+
+- `ai-status`: initialized yes, mode `large`, profile `python-backend-service`, state valid.
+- `ai-doctor`: OK for Git repo, state schema, large-mode files, and task chain; warning only for uncommitted working tree changes.
+- `.\scripts\ai_check.ps1`: passed; script reported Phase 0 has no runnable backend yet and listed future Python checks.
+- `bash ./scripts/ai_check.sh`: not runnable on this machine because no WSL/Linux distribution is installed; PowerShell script is the current Windows check path.
+
+## Reference Repository Checks
+
+Run on 2026-06-27:
+
+```powershell
+git -C F:\BidKonwledge_refs\ragflow rev-parse --short HEAD
+git -C F:\BidKonwledge_refs\haystack-demos rev-parse --short HEAD
+git status --short
+```
+
+Observed:
+
+- RAGFlow reference clone: `f90be41`.
+- Haystack demos reference clone: `17e6103`.
+- Both clones are outside `F:\BidKonwledge`.
+- `git status --short` in the business repository does not include `F:\BidKonwledge_refs`.
+
+## Phase 1 Test-Case Documentation Check
+
+Updated on 2026-06-27:
+
+- `docs/ai/16-phase1-test-cases.md` now defines detailed Phase 1 automated and manual test cases.
+- `docs/ai/16-phase1-test-cases.md` is explicitly an internal backend foundation test spec, not a customer-facing PRD or complete Demo acceptance document.
+- Upload success is now fixed as HTTP `201 Created`.
+- Upload error responses now use the fixed JSON shape `error_code`, `message`, and `details`.
+- SQLite `documents` fields are now fixed in `docs/ai/12-phase1-api-persistence.md`.
+- File safety and atomicity rules now require backend-generated stored filenames and cleanup when validation or persistence fails.
+- Harness commands are documented as delivery command checks, not core business pytest cases.
+- The document is a test-case specification for the next development session, not pytest implementation.
+- Phase 1 pytest files are still expected to be created during backend implementation.
+- `docs/ai/README.md`, `.ai/implementation-plan.md`, and `.ai/handoff.md` now include the detailed test-case document in required Phase 1 context.
+
+Verification commands run after the update:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
+.\scripts\ai_check.ps1
+```
+
+Observed:
+
+- `ai-status`: initialized yes, mode `large`, profile `python-backend-service`, state valid, task chain present.
+- `ai-doctor`: passed required state, mode, profile, large files, and task chain checks; warning only for uncommitted working tree changes.
+- `.\scripts\ai_check.ps1`: exited successfully and reported Phase 0 has no runnable backend yet.
+- `bash ./scripts/ai_check.sh`: not rerun for this documentation-only update; previous blocker remains no WSL/Linux distribution installed.
+
+## Phase 1 Contract-Hardening Check
+
+Updated on 2026-06-27:
+
+- `docs/ai/12-phase1-api-persistence.md` now fixes the Phase 1 upload API contract.
+- `docs/ai/04-api-contract.md` now mirrors the fixed upload success/error response shape.
+- `docs/ai/03-data-model.md` now mirrors the fixed Phase 1 document metadata fields.
+- `docs/ai/16-phase1-test-cases.md` now states that it is an internal backend foundation test spec, not a customer-facing PRD or full Demo acceptance document.
+- `docs/ai/16-phase1-test-cases.md` now separates delivery command checks from business pytest coverage.
+- The current local checkout path remains `F:\BidKonwledge`; `docs/ai/11-local-dev-env.md` records the canonical project name as `BidKnowledge` and warns not to hard-code the absolute path in tests.
+
+Verification commands run after the contract-hardening update:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
+.\scripts\ai_check.ps1
+git diff --check
+```
+
+Observed:
+
+- `ai-status`: initialized yes, mode `large`, profile `python-backend-service`, state valid, task chain present.
+- `ai-doctor`: passed required state, mode, profile, large files, and task chain checks; warning only for uncommitted working tree changes.
+- `.\scripts\ai_check.ps1`: exited successfully and reported Phase 0 has no runnable backend yet.
+- `git diff --check`: passed.
+- `rg` old-contract scan over docs and `.ai`: no matches for the prior loose status-code, old response-field, old DB-field, or pytest/script-mixing wording.
+- Pytest was not run because Phase 1 backend implementation has not started.
+
+## Current Initialization And Documentation Checks
+
+Run on 2026-06-27:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
+git status --short
+Get-ChildItem -Recurse -Force docs\source-materials
+Get-ChildItem -Force docs\ai
+```
+
+Observed:
+
+- `ai-status` now reports initialized large mode with `python-backend-service` profile.
+- `ai-doctor` reports valid state schema and required large files present.
+- `ai-doctor` warns that the working tree has uncommitted changes, which is expected for this newly initialized repository.
+- Source documents copied into `docs/source-materials/originals/`.
+- Large external sample files remain outside Git and are indexed in `docs/source-materials/sample-catalog.md`.
+
+## Phase 0 Checks
+
+Run:
+
+```powershell
+git status --short
+Get-ChildItem -Force
+Get-ChildItem -Force docs/ai
+Get-ChildItem -Force .ai
+```
+
+Expected:
+
+- Git repository exists.
+- Harness files exist.
+- `docs/ai` contains project context files.
+- `.ai` contains current planning files.
+- No business implementation files are present beyond empty scaffold folders and `.gitkeep` files.
+
+## Phase 1 Checks
+
+Future Phase 1 should run:
+
+```powershell
+python -m pytest
+python -m uvicorn app.main:app --reload
+```
+
+The exact Python command may change depending on the selected virtual environment.
+
+Phase 1 acceptance requires:
+
+- `GET /health` returns `{"status":"ok"}`.
+- `POST /api/files/upload` returns HTTP `201 Created` for valid uploads.
+- Upload success response contains `document_id`, `original_filename`, `doc_role`, `parse_status`, `file_size`, and `created_at`.
+- Upload error response contains `error_code`, `message`, and `details`.
+- Upload endpoint saves a file under configured upload root using a backend-generated stored filename.
+- SQLite stores document metadata using the fields in `docs/ai/12-phase1-api-persistence.md`.
+- Invalid uploads do not leave orphan files or metadata rows.
+- Tests cover the P0 cases in `docs/ai/16-phase1-test-cases.md`.
diff --git a/.ai/backups/20260628-005615/docs/ai/tasks/init-large/06-risk-and-rollback.md b/.ai/backups/20260628-005615/docs/ai/tasks/init-large/06-risk-and-rollback.md
new file mode 100644
index 0000000..285fd3a
--- /dev/null
+++ b/.ai/backups/20260628-005615/docs/ai/tasks/init-large/06-risk-and-rollback.md
@@ -0,0 +1,22 @@
+# Risk And Rollback
+
+## Risks
+
+1. Harness profile drift: `ai-upgrade large` defaults to `cpp-linux-backend-system` unless `--profile python-backend-service` is provided.
+2. Scope drift: Phase 1 could accidentally start parsing/RAG work too early.
+3. Large sample files could accidentally enter Git history.
+4. Placeholder scripts could be mistaken for real build/test coverage after Phase 1 implementation.
+
+## Mitigations
+
+1. `.ai/state.json` is set to `mode = large` and `profile = python-backend-service`.
+2. `AGENTS.md`, `README.md`, and Phase 1 docs explicitly require large mode and script execution.
+3. `docs/source-materials/sample-catalog.md` indexes large files without copying them.
+4. `docs/ai/13-phase1-verification-checklist.md` requires real script/test evidence before Phase 1 completion.
+
+## Rollback
+
+This task is documentation-only. Rollback is a normal Git revert before commit.
+
+If harness-generated large-mode files are not wanted, remove the files listed in `.ai/affected-files.md` and restore `.ai/state.json` from `.ai/backups/20260627-214154/.ai/state.json`.
+
diff --git a/.ai/backups/20260628-005615/docs/ai/tasks/init-large/07-handoff.md b/.ai/backups/20260628-005615/docs/ai/tasks/init-large/07-handoff.md
new file mode 100644
index 0000000..733fbb2
--- /dev/null
+++ b/.ai/backups/20260628-005615/docs/ai/tasks/init-large/07-handoff.md
@@ -0,0 +1,96 @@
+# Handoff
+
+## Current State
+
+The repository has been initialized for the 投标智能知识库能力验证版 Demo.
+
+Auto_AICoding_Harness has been upgraded to `large` mode with the `python-backend-service` profile.
+
+Future development in this repository must use large mode and must run the project scripts before completion.
+
+Latest verification:
+
+- `ai-status` and `ai-doctor` pass for large mode.
+- `scripts/ai_check.ps1` runs successfully.
+- `bash ./scripts/ai_check.sh` was attempted but cannot run because WSL is not installed.
+
+## Important Context
+
+Read these first:
+
+1. `docs/ai/00-project-brief.md`
+2. `docs/ai/01-scope-boundary.md`
+3. `docs/ai/05-dev-rules.md`
+4. `docs/ai/08-tech-selection.md`
+5. `docs/ai/09-phase-roadmap.md`
+6. `docs/source-materials/README.md`
+7. `docs/source-materials/sample-catalog.md`
+8. `.ai/spec.md`
+9. `.ai/implementation-plan.md`
+10. `docs/ai/10-phase1-dev-spec.md`
+11. `docs/ai/11-local-dev-env.md`
+12. `docs/ai/12-phase1-api-persistence.md`
+13. `docs/ai/13-phase1-verification-checklist.md`
+14. `docs/ai/14-reference-reuse-strategy.md`
+15. `docs/ai/15-target-architecture.md`
+16. `docs/ai/16-phase1-test-cases.md`
+
+## Next Recommended Prompt
+
+```md
+当前仓库已经完成 0 阶段初始化，并已升级到 Auto_AICoding_Harness large mode。请先运行 ai-status / ai-doctor，确认 .ai/state.json 中 mode=large 且 profile=python-backend-service。
+
+请先阅读：
+- AGENTS.md
+- docs/ai/10-phase1-dev-spec.md
+- docs/ai/11-local-dev-env.md
+- docs/ai/12-phase1-api-persistence.md
+- docs/ai/13-phase1-verification-checklist.md
+- docs/ai/16-phase1-test-cases.md
+- .ai/implementation-plan.md
+- .ai/verification.md
+
+现在开始执行 Phase 1。
+
+只实现以下内容：
+
+1. FastAPI app 启动；
+2. GET /health；
+3. POST /api/files/upload，成功响应固定为 HTTP 201；
+4. 结构化错误响应，字段为 error_code / message / details；
+5. 本地文件保存到配置化 upload root，真实存储名由后端生成；
+6. Document metadata schema，字段按 docs/ai/12-phase1-api-persistence.md；
+7. SQLite 初始化；
+8. 基础配置管理；
+9. docs/ai/16-phase1-test-cases.md 中的 P0 pytest 覆盖；
+10. 最小 smoke test；
+11. README 中补充本地启动命令。
+
+不要实现 OCR、LLM、embedding、vector store、知识卡片生成、招标文件分析、Demo 页面、用户系统、Word/PDF 导出。
+
+注意：Phase 1 只是后端底座，不是甲方 Demo 验收。
+
+实现完成后更新 .ai/evaluation.md 和 .ai/handoff.md，并列出新增文件、修改文件、运行命令、测试命令、验证结果、下一步建议。
+
+必须运行项目脚本，并把结果写入 .ai/verification.md。
+```
+
+## Source Materials
+
+Project materials are under:
+
+`C:\Users\26561\Desktop\模型训练资料`
+
+Copied lightweight source documents:
+
+- `docs/source-materials/originals/投标智能知识库能力验证版-PRD-v0.1.pdf`
+- `docs/source-materials/originals/deep-research-report.md`
+
+Large sample files were not copied into Git. Use `docs/source-materials/sample-catalog.md` to select validation files.
+
+Reference repositories:
+
+- `F:\BidKonwledge_refs\ragflow`
+- `F:\BidKonwledge_refs\haystack-demos`
+
+These are reference-only clones and should not be committed into the business repo.
diff --git a/.ai/backups/20260628-005615/manifest.json b/.ai/backups/20260628-005615/manifest.json
new file mode 100644
index 0000000..74ce94a
--- /dev/null
+++ b/.ai/backups/20260628-005615/manifest.json
@@ -0,0 +1,84 @@
+{
+  "writes": [
+    {
+      "operation": "force_overwrite",
+      "path": ".ai/state.json",
+      "action": "OVERWRITTEN",
+      "sha256_before": "472ccaf0f5c838879ebf62a8da5e56069ccac6d2c22c0700d551007017556ff6",
+      "sha256_after": "74902db3f4d4814245e4a81a381cc5b76495a59201e7fa02a83002805c43db1b",
+      "backup_path": ".ai/backups/20260628-005615/.ai/state.json"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": "docs/ai/tasks/README.md",
+      "action": "OVERWRITTEN",
+      "sha256_before": "65851afd96f38cdb389f0b7e3ae40c343def91ba47956bdbbe7356c2cb417582",
+      "sha256_after": "65851afd96f38cdb389f0b7e3ae40c343def91ba47956bdbbe7356c2cb417582",
+      "backup_path": ".ai/backups/20260628-005615/docs/ai/tasks/README.md"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": "docs/ai/tasks/init-large/00-prd.md",
+      "action": "OVERWRITTEN",
+      "sha256_before": "30b914287b0c29c69b2e0165224aad359ee7818aa11db5ea2dd88c9179f300f1",
+      "sha256_after": "30b914287b0c29c69b2e0165224aad359ee7818aa11db5ea2dd88c9179f300f1",
+      "backup_path": ".ai/backups/20260628-005615/docs/ai/tasks/init-large/00-prd.md"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": "docs/ai/tasks/init-large/01-spec.md",
+      "action": "OVERWRITTEN",
+      "sha256_before": "9134a266e0bb595e9cdaad6d22039861a2ebb75c02b278660f63993ff63cc6a6",
+      "sha256_after": "9134a266e0bb595e9cdaad6d22039861a2ebb75c02b278660f63993ff63cc6a6",
+      "backup_path": ".ai/backups/20260628-005615/docs/ai/tasks/init-large/01-spec.md"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": "docs/ai/tasks/init-large/02-tech-design.md",
+      "action": "OVERWRITTEN",
+      "sha256_before": "fc19144990f313d5225a02fd77cc7166a69e5f46aa71296f018bbf624033a4d8",
+      "sha256_after": "fc19144990f313d5225a02fd77cc7166a69e5f46aa71296f018bbf624033a4d8",
+      "backup_path": ".ai/backups/20260628-005615/docs/ai/tasks/init-large/02-tech-design.md"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": "docs/ai/tasks/init-large/03-implementation-plan.md",
+      "action": "OVERWRITTEN",
+      "sha256_before": "bc504f8b471b849b7fd5ad56d278ffbfb095b8f2050fa99232bb7bc111487c4c",
+      "sha256_after": "5c937acfa4d91a1ae7ba8e3d3e5d21e2979d0f0126c3c058fd86bf5710819e1a",
+      "backup_path": ".ai/backups/20260628-005615/docs/ai/tasks/init-large/03-implementation-plan.md"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": "docs/ai/tasks/init-large/04-diff-review.md",
+      "action": "OVERWRITTEN",
+      "sha256_before": "130aabb0ee983298a4a0ea7e160a2e5d0a5ac6af39b92e22bb8e6f4fab9a6e0d",
+      "sha256_after": "130aabb0ee983298a4a0ea7e160a2e5d0a5ac6af39b92e22bb8e6f4fab9a6e0d",
+      "backup_path": ".ai/backups/20260628-005615/docs/ai/tasks/init-large/04-diff-review.md"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": "docs/ai/tasks/init-large/05-verification.md",
+      "action": "OVERWRITTEN",
+      "sha256_before": "66920256c5a3ae2a772fe94d8b9bb1788ec2d9e738662f35684174a2fd8107b8",
+      "sha256_after": "66920256c5a3ae2a772fe94d8b9bb1788ec2d9e738662f35684174a2fd8107b8",
+      "backup_path": ".ai/backups/20260628-005615/docs/ai/tasks/init-large/05-verification.md"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": "docs/ai/tasks/init-large/06-risk-and-rollback.md",
+      "action": "OVERWRITTEN",
+      "sha256_before": "238d894d03cb9764e554ae91f6971588526acc2ee393159e1c418c6672500955",
+      "sha256_after": "238d894d03cb9764e554ae91f6971588526acc2ee393159e1c418c6672500955",
+      "backup_path": ".ai/backups/20260628-005615/docs/ai/tasks/init-large/06-risk-and-rollback.md"
+    },
+    {
+      "operation": "force_overwrite",
+      "path": "docs/ai/tasks/init-large/07-handoff.md",
+      "action": "OVERWRITTEN",
+      "sha256_before": "2356c3feb4371680d1903e44724303ca8f161e4190ef6e4f7d0fba87f8d88099",
+      "sha256_after": "2356c3feb4371680d1903e44724303ca8f161e4190ef6e4f7d0fba87f8d88099",
+      "backup_path": ".ai/backups/20260628-005615/docs/ai/tasks/init-large/07-handoff.md"
+    }
+  ]
+}
diff --git a/.ai/backups/20260628-005751/.ai/state.json b/.ai/backups/20260628-005751/.ai/state.json
new file mode 100644
index 0000000..c9981b8
--- /dev/null
+++ b/.ai/backups/20260628-005751/.ai/state.json
@@ -0,0 +1,14 @@
+{
+  "schema_version": 1,
+  "mode": "large",
+  "profile": "python-backend-service",
+  "status": "WAITING_HUMAN_PLAN_APPROVAL",
+  "current_gate": "plan",
+  "approved_gates": [
+    "spec"
+  ],
+  "created_by": "Auto_AICoding_Harness",
+  "task_id": "init-large",
+  "task_title": "Initialize harness in large mode",
+  "updated_at": "2026-06-28T00:56:15+08:00"
+}
diff --git a/.ai/backups/20260628-005751/manifest.json b/.ai/backups/20260628-005751/manifest.json
new file mode 100644
index 0000000..8192023
--- /dev/null
+++ b/.ai/backups/20260628-005751/manifest.json
@@ -0,0 +1,12 @@
+{
+  "writes": [
+    {
+      "operation": "force_overwrite",
+      "path": ".ai/state.json",
+      "action": "OVERWRITTEN",
+      "sha256_before": "74902db3f4d4814245e4a81a381cc5b76495a59201e7fa02a83002805c43db1b",
+      "sha256_after": "515e0b7686f383acad4c01897353abff6c2d9a7bcc33fc9c8858fc9671d0d982",
+      "backup_path": ".ai/backups/20260628-005751/.ai/state.json"
+    }
+  ]
+}
diff --git a/.ai/context-pack.md b/.ai/context-pack.md
new file mode 100644
index 0000000..cff255e
--- /dev/null
+++ b/.ai/context-pack.md
@@ -0,0 +1,86 @@
+# Context Pack
+
+## Harness State
+
+- mode: large
+- profile: python-backend-service
+- status: INIT
+- current_gate: none
+- approved_gates: none
+
+## Important Files
+
+- AGENTS.md: present
+- docs/ai/: present
+- task chain: present
+- docs/ai/tasks/init-large/05-verification.md: present
+- scripts/ai_check.sh: present
+- .ai/verification.md: present
+- .ai/reviews/diff-review.md: missing
+- .ai/approvals/diff-approval.md: missing
+
+## Git Summary
+
+```text
+?? .ai/
+?? .codex/
+?? .github/
+?? .gitignore
+?? AGENTS.md
+?? CLAUDE.md
+?? README.md
+?? backend/
+?? data/
+?? docs/
+?? frontend/
+?? scripts/
+```
+
+## Diff Stat
+
+```text
+empty
+```
+
+## Changed Files
+
+```text
+empty
+```
+
+## Recent Review
+
+- unavailable
+
+## Context Manifest
+
+- context manifest: present (.ai/tasks/init-large/context.jsonl)
+- context manifest valid: yes
+- context manifest entries: 9
+  - .ai/spec.md [implement]: Large-mode requirement source
+  - .ai/implementation-plan.md [implement]: Large-mode implementation plan
+  - .ai/tech-design.md [implement]: Large-mode technical design
+  - .ai/risk-and-rollback.md [review]: Rollback and risk guardrails
+  - .ai/verification.md [review]: Verification evidence
+  - .ai/handoff.md [handoff]: Cross-session handoff summary
+  - docs/ai/tasks/init-large/01-spec.md [implement]: Durable task spec evidence
+  - docs/ai/tasks/init-large/03-implementation-plan.md [implement]: Durable task implementation plan evidence
+  - ... 1 more
+
+## Recent Approval
+
+- unavailable
+
+## Plan Snapshot
+
+- spec: # Spec - Phase 0 Repository Initialization ## Objective
+- plan: # Implementation Plan ## Current Large-Mode Prep Task
+- affected-files: # Affected Files ## Updated
+
+## Verification Snapshot
+
+- verification.md: present (0 ran, 0 not-run)
+
+## Next Suggested Action
+
+- Start a task or run `ai-review diff` after changes.
diff --git a/.ai/epic.md b/.ai/epic.md
new file mode 100644
index 0000000..e1de3b9
--- /dev/null
+++ b/.ai/epic.md
@@ -0,0 +1,22 @@
+# Epic - Large-Mode Phase 1 Preparation
+
+## Objective
+
+Make this repository ready for Phase 1 development under Auto_AICoding_Harness `large` mode.
+
+## Outcome
+
+Before any business code is written, the repository must contain:
+
+1. Large-mode harness state.
+2. Project-level rule that future development must use large mode.
+3. Phase 1 development spec.
+4. Local development environment guide.
+5. Phase 1 API and persistence details.
+6. Phase 1 verification checklist.
+7. Updated `.ai` task artifacts and handoff.
+
+## Non-Goal
+
+This task does not implement FastAPI, upload handling, SQLite code, parsing, retrieval, LLM calls, or UI.
+
diff --git a/.ai/evaluation.md b/.ai/evaluation.md
new file mode 100644
index 0000000..ce141e9
--- /dev/null
+++ b/.ai/evaluation.md
@@ -0,0 +1,146 @@
+# Evaluation
+
+## Phase 1 Backend Foundation Evaluation
+
+Status: implemented and locally verified, pending any required human diff/final gate decision.
+
+Implemented:
+
+1. FastAPI app entrypoint at `backend.app.main:app`.
+2. `GET /health` returning exactly `{"status": "ok"}`.
+3. `POST /api/files/upload` returning HTTP `201 Created` for valid uploads.
+4. Fixed success fields: `document_id`, `original_filename`, `doc_role`, `parse_status`, `file_size`, `created_at`.
+5. Fixed error response shape: `error_code`, `message`, `details`.
+6. Configurable upload root and SQLite path through settings.
+7. Backend-generated stored filenames based on server-generated document ids.
+8. SQLite `documents` table with Phase 1 required fields.
+9. Pytest coverage for health, upload contract, validation, storage, database, and Phase 1 boundaries.
+10. Real PowerShell project check script.
+11. README local setup, startup, test, and smoke commands.
+
+Scope control:
+
+- OCR: not implemented.
+- LLM: not implemented.
+- Embeddings: not implemented.
+- Qdrant/vector store: not implemented.
+- Haystack pipeline execution: not implemented.
+- Knowledge cards: not implemented.
+- Tender analysis: not implemented.
+- Frontend Demo: not implemented.
+- User system: not implemented.
+- Word/PDF export: not implemented.
+
+Verification summary:
+
+- `ai-status`: large mode confirmed.
+- `ai-doctor`: large-mode state valid; only active-worktree warning.
+- `compileall backend/app`: passed.
+- `pytest backend/tests`: `37 passed, 1 warning`.
+- `.\scripts\ai_check.ps1`: passed and runs real compile/test checks.
+- `python -m pytest backend/tests`: passed after temporarily placing bundled Python on PATH.
+- `curl.exe --noproxy "*"` health smoke: HTTP 200.
+- `curl.exe --noproxy "*"` upload smoke: HTTP 201.
+- `bash ./scripts/ai_check.sh`: not verified because WSL/bash is unavailable.
+
+Residual risk:
+
+1. Test run has a third-party deprecation warning from FastAPI/Starlette test client and `httpx`; no functional failure observed.
+2. The repository still has many untracked files because it appears to be a newly initialized working tree.
+
+## Phase 0 Evaluation
+
+Status: verified.
+
+Verified on 2026-06-27:
+
+1. `F:\BidKonwledge` is a Git repository.
+2. Auto_AICoding_Harness baseline files are present.
+3. `docs/ai` contains the project brief, scope boundary, architecture, data model, API contract, dev rules, verification notes, and source-material notes.
+4. `.ai` contains spec, implementation plan, verification, evaluation, and handoff files.
+5. Backend and frontend directories contain only scaffold placeholders; no business code was implemented.
+
+## Scope Control
+
+Phase 0 should only initialize repository context and task planning. It must not implement backend business code.
+
+## Review Questions
+
+1. Do `docs/ai` files match the PRD boundary?
+2. Does `.ai/implementation-plan.md` keep Phase 1 narrow?
+3. Are OCR, LLM, embeddings, vector store, and demo page explicitly deferred?
+4. Is the source material path recorded without copying large sample files into the repository?
+
+Current answers: yes to all four.
+
+## Harness Configuration Evaluation
+
+Status: verified.
+
+Verified on 2026-06-27:
+
+1. `Auto_AICoding_Harness` upstream URL is `https://github.com/yu20120707/Auto_AICoding_Harness.git`.
+2. Upstream `HEAD` and local source checkout both resolve to `b961e9171ebdfed7ec39491da821cbe0fbca8912`.
+3. Current project is initialized by harness in `medium` mode with `python-backend-service` profile.
+4. `.ai/state.json` exists and is schema-valid according to `ai-doctor`.
+5. Python backend profile docs were generated under `docs/ai/`.
+
+## Source Material Organization Evaluation
+
+Status: verified.
+
+1. Original PRD PDF and deep research report are stored under `docs/source-materials/originals/`.
+2. Large sample files remain at `C:\Users\26561\Desktop\模型训练资料\甲方提供资料`.
+3. `docs/source-materials/sample-catalog.md` records recommended early samples and deferred large files.
+4. `docs/ai/08-tech-selection.md` captures the technical route from the research report.
+5. `docs/ai/09-phase-roadmap.md` separates Phase 1 from later Docling/Qdrant/Haystack/LLM work.
+
+## Large-Mode Prep Evaluation
+
+Status: verified.
+
+Review criteria:
+
+1. `.ai/state.json` reports `mode = large`.
+2. `.ai/state.json` reports `profile = python-backend-service`.
+3. `AGENTS.md` requires large mode and script execution for future development.
+4. Phase 1 docs cover spec, local environment, API/persistence details, and verification.
+5. No business code was implemented.
+
+Current answers: yes to all five.
+
+## Script Execution Evaluation
+
+Status: partially verified for cross-shell scripts.
+
+1. PowerShell project check script ran successfully.
+2. Bash check script was attempted and failed because WSL is not installed.
+3. Since this is a Windows-local repo and no backend code exists yet, the PowerShell check is the valid current script evidence.
+4. Phase 1 must replace placeholder script output with real Python compile/test commands.
+
+## Reference Reuse Evaluation
+
+Status: verified.
+
+1. Reference repositories were cloned outside the business repo.
+2. RAGFlow is documented as product reference, not mainline fork.
+3. Haystack demos are documented as engineering reference.
+4. Target architecture is documented in `docs/ai/15-target-architecture.md`.
+5. The direct二开 decision is documented in `docs/ai/14-reference-reuse-strategy.md`.
+
+Decision: use our business repo as the mainline, with dependency-based reuse and reference-guided implementation. Direct RAGFlow customization remains a separate spike option, not the default path.
+
+## Phase 1 Test-Case Documentation Evaluation
+
+Status: contract-hardened, implementation pending.
+
+1. `docs/ai/16-phase1-test-cases.md` now provides detailed P0/P1/P2 cases for health, upload success contract, structured error contract, file storage, SQLite persistence, atomicity, configuration, boundary checks, delivery command checks, and manual smoke.
+2. `docs/ai/12-phase1-api-persistence.md` and `docs/ai/04-api-contract.md` now fix the upload success response as HTTP `201 Created`.
+3. Error responses now use a stable JSON shape: `error_code`, `message`, and `details`.
+4. The SQLite `documents` table fields are now fixed for Phase 1.
+5. File safety rules now require backend-generated stored filenames and cleanup on validation or persistence failures.
+6. Harness/script checks are documented as delivery checks, not core business pytest cases.
+7. The test cases intentionally stay inside Phase 1 and do not require OCR, LLM, embeddings, Qdrant, Haystack, frontend Demo, export, or customer sample files.
+8. Actual pytest code is not written yet because Phase 1 implementation has not started.
+
+Decision: the next development session should implement backend code and tests together, using `docs/ai/16-phase1-test-cases.md` as the acceptance source.
diff --git a/.ai/handoff.md b/.ai/handoff.md
new file mode 100644
index 0000000..5bc5c5c
--- /dev/null
+++ b/.ai/handoff.md
@@ -0,0 +1,191 @@
+# Handoff
+
+## Current State - Phase 1 Backend Foundation
+
+Phase 1 backend foundation has been implemented locally.
+
+Current harness state before final gate review:
+
+- mode: `large`
+- profile: `python-backend-service`
+- spec gate: approved by user
+- plan gate: approved by user
+- next harness action after implementation: `ai-review diff`
+
+Implemented backend capabilities:
+
+1. FastAPI app startup through `backend.app.main:app`.
+2. `GET /health`.
+3. `POST /api/files/upload`.
+4. Configurable local upload root.
+5. Backend-generated stored filename.
+6. SQLite `documents` metadata persistence.
+7. Fixed upload success and error response contracts.
+8. P0 pytest coverage for Phase 1 backend foundation.
+
+Important files changed or added:
+
+- `pyproject.toml`
+- `backend/__init__.py`
+- `backend/app/__init__.py`
+- `backend/app/main.py`
+- `backend/app/config.py`
+- `backend/app/api/health.py`
+- `backend/app/api/files.py`
+- `backend/app/schemas/document.py`
+- `backend/app/storage/database.py`
+- `backend/app/storage/file_storage.py`
+- `backend/tests/conftest.py`
+- `backend/tests/test_health.py`
+- `backend/tests/test_upload_contract.py`
+- `backend/tests/test_upload_validation.py`
+- `backend/tests/test_storage.py`
+- `backend/tests/test_database.py`
+- `backend/tests/test_phase1_boundaries.py`
+- `scripts/ai_check.ps1`
+- `scripts/ai_check.sh`
+- `README.md`
+- `.ai/spec.md`
+- `.ai/implementation-plan.md`
+- `.ai/affected-files.md`
+- `.ai/run-trace.md`
+- `.ai/verification.md`
+- `.ai/evaluation.md`
+- `.ai/handoff.md`
+
+Verification run:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py -m pip install -e '.[dev]'
+& $py -m compileall backend/app
+& $py -m pytest backend/tests
+.\scripts\ai_check.ps1
+$env:Path='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python;' + $env:Path
+python -m pytest backend/tests
+curl.exe --noproxy "*" http://127.0.0.1:8000/health
+curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/files/upload" -F "doc_role=historical_bid" -F "file=@.\data\samples\phase1-smoke.txt"
+```
+
+Results:
+
+- `compileall backend/app`: passed.
+- `pytest backend/tests`: `37 passed, 1 warning`.
+- `.\scripts\ai_check.ps1`: passed.
+- `python -m pytest backend/tests`: passed with bundled Python placed on PATH.
+- Health smoke: HTTP 200, `{"status":"ok"}`.
+- Upload smoke: HTTP 201, fixed Phase 1 success fields.
+- `bash ./scripts/ai_check.sh`: attempted and failed because WSL/bash is unavailable; do not claim passed.
+
+Subagents used:
+
+1. Hooke: read-only API/persistence/test-contract scan.
+2. Meitner: read-only scripts/README/verification scan.
+3. Bohr: read-only implementation review after coding.
+
+Residual risks:
+
+- Dedicated forced file-write and metadata-write failure tests are now covered.
+- FastAPI/Starlette test client emits a deprecation warning related to `httpx`; tests still pass.
+- Phase 1 remains backend foundation only; it is not OCR/RAG/LLM/frontend demo completion.
+
+Next recommended action:
+
+```md
+Review the Phase 1 diff. If acceptable, approve the diff gate so the agent can run final gate review and close the Phase 1 backend foundation task.
+```
+
+## Current State
+
+The repository has been initialized for the 投标智能知识库能力验证版 Demo.
+
+Auto_AICoding_Harness has been upgraded to `large` mode with the `python-backend-service` profile.
+
+Future development in this repository must use large mode and must run the project scripts before completion.
+
+Latest verification:
+
+- `ai-status` and `ai-doctor` pass for large mode.
+- `scripts/ai_check.ps1` runs successfully.
+- `bash ./scripts/ai_check.sh` was attempted but cannot run because WSL is not installed.
+
+## Important Context
+
+Read these first:
+
+1. `docs/ai/00-project-brief.md`
+2. `docs/ai/01-scope-boundary.md`
+3. `docs/ai/05-dev-rules.md`
+4. `docs/ai/08-tech-selection.md`
+5. `docs/ai/09-phase-roadmap.md`
+6. `docs/source-materials/README.md`
+7. `docs/source-materials/sample-catalog.md`
+8. `.ai/spec.md`
+9. `.ai/implementation-plan.md`
+10. `docs/ai/10-phase1-dev-spec.md`
+11. `docs/ai/11-local-dev-env.md`
+12. `docs/ai/12-phase1-api-persistence.md`
+13. `docs/ai/13-phase1-verification-checklist.md`
+14. `docs/ai/14-reference-reuse-strategy.md`
+15. `docs/ai/15-target-architecture.md`
+16. `docs/ai/16-phase1-test-cases.md`
+
+## Next Recommended Prompt
+
+```md
+当前仓库已经完成 0 阶段初始化，并已升级到 Auto_AICoding_Harness large mode。请先运行 ai-status / ai-doctor，确认 .ai/state.json 中 mode=large 且 profile=python-backend-service。
+
+请先阅读：
+- AGENTS.md
+- docs/ai/10-phase1-dev-spec.md
+- docs/ai/11-local-dev-env.md
+- docs/ai/12-phase1-api-persistence.md
+- docs/ai/13-phase1-verification-checklist.md
+- docs/ai/16-phase1-test-cases.md
+- .ai/implementation-plan.md
+- .ai/verification.md
+
+现在开始执行 Phase 1。
+
+只实现以下内容：
+
+1. FastAPI app 启动；
+2. GET /health；
+3. POST /api/files/upload，成功响应固定为 HTTP 201；
+4. 结构化错误响应，字段为 error_code / message / details；
+5. 本地文件保存到配置化 upload root，真实存储名由后端生成；
+6. Document metadata schema，字段按 docs/ai/12-phase1-api-persistence.md；
+7. SQLite 初始化；
+8. 基础配置管理；
+9. docs/ai/16-phase1-test-cases.md 中的 P0 pytest 覆盖；
+10. 最小 smoke test；
+11. README 中补充本地启动命令。
+
+不要实现 OCR、LLM、embedding、vector store、知识卡片生成、招标文件分析、Demo 页面、用户系统、Word/PDF 导出。
+
+注意：Phase 1 只是后端底座，不是甲方 Demo 验收。
+
+实现完成后更新 .ai/evaluation.md 和 .ai/handoff.md，并列出新增文件、修改文件、运行命令、测试命令、验证结果、下一步建议。
+
+必须运行项目脚本，并把结果写入 .ai/verification.md。
+```
+
+## Source Materials
+
+Project materials are under:
+
+`C:\Users\26561\Desktop\模型训练资料`
+
+Copied lightweight source documents:
+
+- `docs/source-materials/originals/投标智能知识库能力验证版-PRD-v0.1.pdf`
+- `docs/source-materials/originals/deep-research-report.md`
+
+Large sample files were not copied into Git. Use `docs/source-materials/sample-catalog.md` to select validation files.
+
+Reference repositories:
+
+- `F:\BidKonwledge_refs\ragflow`
+- `F:\BidKonwledge_refs\haystack-demos`
+
+These are reference-only clones and should not be committed into the business repo.
diff --git a/.ai/implementation-plan.md b/.ai/implementation-plan.md
new file mode 100644
index 0000000..77bed23
--- /dev/null
+++ b/.ai/implementation-plan.md
@@ -0,0 +1,173 @@
+# Implementation Plan - Phase 1 Backend Foundation
+
+## Execution Classification
+
+- Harness mode: `large`
+- Task level: Level 3 / complex
+- Reason: this task introduces the backend app entrypoint, upload API contract, local file persistence, SQLite metadata persistence, project scripts, and P0 automated tests for a complete backend workflow.
+- Rollback: normal Git revert before commit; no migrations beyond local SQLite initialization.
+
+## Target Outcome
+
+Implement the Phase 1 backend foundation only:
+
+1. FastAPI app startup.
+2. `GET /health`.
+3. `POST /api/files/upload`.
+4. HTTP `201 Created` upload success contract.
+5. Structured upload error contract.
+6. Configurable local upload root and SQLite database path.
+7. Backend-generated stored filenames.
+8. `documents` SQLite table matching `docs/ai/12-phase1-api-persistence.md`.
+9. P0 pytest coverage from `docs/ai/16-phase1-test-cases.md`.
+10. README and `.ai` evidence updates.
+
+## Non-Goals
+
+Do not implement OCR, LLM calls, embedding, Qdrant/vector store, Haystack pipeline execution, knowledge cards, tender analysis, frontend Demo, user system, or Word/PDF export.
+
+## Expected File Scope
+
+Implementation files:
+
+```text
+backend/app/__init__.py
+backend/app/main.py
+backend/app/config.py
+backend/app/api/__init__.py
+backend/app/api/health.py
+backend/app/api/files.py
+backend/app/schemas/__init__.py
+backend/app/schemas/document.py
+backend/app/storage/__init__.py
+backend/app/storage/database.py
+backend/app/storage/file_storage.py
+```
+
+Test files:
+
+```text
+backend/tests/conftest.py
+backend/tests/test_health.py
+backend/tests/test_upload_contract.py
+backend/tests/test_upload_validation.py
+backend/tests/test_storage.py
+backend/tests/test_database.py
+backend/tests/test_phase1_boundaries.py
+```
+
+Project files:
+
+```text
+pyproject.toml
+README.md
+scripts/ai_check.ps1
+scripts/ai_check.sh
+.ai/affected-files.md
+.ai/run-trace.md
+.ai/verification.md
+.ai/evaluation.md
+.ai/handoff.md
+```
+
+## Subagent Plan
+
+Use subagents for read-only and review work only. Main agent owns all writes to avoid conflicting edits.
+
+1. Explorer Hooke: read-only API/persistence/test-contract scan.
+2. Explorer Meitner: read-only script/README/verification-artifact scan.
+3. After implementation, use reviewer/evaluator subagent only if useful for final contract review.
+
+## Implementation Stages
+
+### Stage 1 - Package And App Skeleton
+
+1. Add a single dependency file, `pyproject.toml`, with FastAPI, Uvicorn, Pydantic, pytest, and HTTPX.
+2. Add FastAPI app factory/import entrypoint in `backend/app/main.py`.
+3. Add `GET /health` router.
+
+Verification:
+
+```powershell
+python -m compileall backend/app
+python -m pytest backend/tests/test_health.py
+```
+
+### Stage 2 - Configuration, SQLite, And File Storage
+
+1. Add settings object with configurable upload root, database path, allowed extensions, and max upload size.
+2. Add SQLite initialization and `documents` insert/query helpers.
+3. Add file-storage helper that generates stored filenames using backend document ids and writes only under upload root.
+
+Verification:
+
+```powershell
+python -m pytest backend/tests/test_storage.py backend/tests/test_database.py
+```
+
+### Stage 3 - Upload API And Error Contract
+
+1. Add `POST /api/files/upload`.
+2. Validate missing file, missing/invalid doc role, empty file, unsafe filename, unsupported extension, and file-too-large.
+3. Save file before metadata insert.
+4. Clean up stored file if metadata insert fails.
+5. Return only documented success fields.
+6. Return fixed error fields: `error_code`, `message`, `details`.
+
+Verification:
+
+```powershell
+python -m pytest backend/tests/test_upload_contract.py backend/tests/test_upload_validation.py
+```
+
+### Stage 4 - Boundary Tests And Scripts
+
+1. Add tests proving Phase 1 does not require OCR, LLM credentials, vector service, or parser output.
+2. Replace PowerShell project check placeholder with real compile and pytest commands.
+3. Replace bash project check placeholder with the same real check sequence for shell environments.
+
+Verification:
+
+```powershell
+.\scripts\ai_check.ps1
+python -m pytest backend/tests
+```
+
+Run `bash ./scripts/ai_check.sh` when available. If WSL/bash is unavailable on this Windows machine, record the blocker in `.ai/verification.md`.
+
+### Stage 5 - README, Evidence, And Smoke
+
+1. Update README with large-mode status, dependency install, local startup, pytest, and curl commands.
+2. Start uvicorn locally if dependencies are available.
+3. Run `curl.exe --noproxy "*"` health and upload smoke checks.
+4. Update `.ai/verification.md`, `.ai/evaluation.md`, and `.ai/handoff.md` with real command evidence.
+
+Verification:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
+.\scripts\ai_check.ps1
+python -m pytest backend/tests
+curl.exe --noproxy "*" http://127.0.0.1:8000/health
+```
+
+## Mid-Task Review Checkpoint
+
+After Stage 3, perform a self-review:
+
+1. Status versus this plan.
+2. Scope changes since start.
+3. Newly discovered risks.
+4. Decision: keep plan, revise plan, or escalate.
+
+## Escalation Triggers
+
+Escalate or pause if:
+
+1. The upload contract conflicts with docs.
+2. Dependencies cannot be installed or imported.
+3. Tests require external services.
+4. File/database atomicity cannot be verified locally.
+5. Harness gate state blocks implementation.
diff --git a/.ai/reviews/README.md b/.ai/reviews/README.md
new file mode 100644
index 0000000..82a9868
--- /dev/null
+++ b/.ai/reviews/README.md
@@ -0,0 +1,3 @@
+# Reviews
+
+This directory stores generated review artifacts for large-mode tasks.
diff --git a/.ai/reviews/plan-review.md b/.ai/reviews/plan-review.md
new file mode 100644
index 0000000..0019305
--- /dev/null
+++ b/.ai/reviews/plan-review.md
@@ -0,0 +1,166 @@
+# Plan Review
+
+## Status
+
+WAITING_HUMAN_PLAN_APPROVAL
+
+## Source
+
+.ai/implementation-plan.md
+
+## Plan Summary
+
+```text
+# Implementation Plan - Phase 1 Backend Foundation
+
+## Execution Classification
+
+- Harness mode: `large`
+- Task level: Level 3 / complex
+- Reason: this task introduces the backend app entrypoint, upload API contract, local file persistence, SQLite metadata persistence, project scripts, and P0 automated tests for a complete backend workflow.
+- Rollback: normal Git revert before commit; no migrations beyond local SQLite initialization.
+
+## Target Outcome
+
+Implement the Phase 1 backend foundation only:
+
+1. FastAPI app startup.
+2. `GET /health`.
+3. `POST /api/files/upload`.
+4. HTTP `201 Created` upload success contract.
+5. Structured upload error contract.
+6. Configurable local upload root and SQLite database path.
+7. Backend-generated stored filenames.
+8. `documents` SQLite table matching `docs/ai/12-phase1-api-persistence.md`.
+9. P0 pytest coverage from `docs/ai/16-phase1-test-cases.md`.
+10. README and `.ai` evidence updates.
+
+## Non-Goals
+
+Do not implement OCR, LLM calls, embedding, Qdrant/vector store, Haystack pipeline execution, knowledge cards, tender analysis, frontend Demo, user system, or Word/PDF export.
+
+## Expected File Scope
+
+Implementation files:
+
+```text
+backend/app/__init__.py
+backend/app/main.py
+backend/app/config.py
+backend/app/api/__init__.py
+backend/app/api/health.py
+backend/app/api/files.py
+backend/app/schemas/__init__.py
+backend/app/schemas/document.py
+backend/app/storage/__init__.py
+backend/app/storage/database.py
+backend/app/storage/file_storage.py
+```
+
+Test files:
+
+```text
+backend/tests/conftest.py
+backend/tests/test_health.py
+backend/tests/test_upload_contract.py
+backend/tests/test_upload_validation.py
+backend/tests/test_storage.py
+backend/tests/test_database.py
+backend/tests/test_phase1_boundaries.py
+```
+
+Project files:
+
+```text
+pyproject.toml
+README.md
+scripts/ai_check.ps1
+scripts/ai_check.sh
+.ai/affected-files.md
+.ai/run-trace.md
+.ai/verification.md
+.ai/evaluation.md
+.ai/handoff.md
+```
+
+## Subagent Plan
+
+Use subagents for read-only and review work only. Main agent owns all writes to avoid conflicting edits.
+
+1. Explorer Hooke: read-only API/persistence/test-contract scan.
+2. Explorer Meitner: read-only script/README/verification-artifact scan.
+3. After implementation, use reviewer/evaluator subagent only if useful for final contract review.
+
+## Implementation Stages
+
+### Stage 1 - Package And App Skeleton
+
+1. Add a single dependency file, `pyproject.toml`, with FastAPI, Uvicorn, Pydantic, pytest, and HTTPX.
+2. Add FastAPI app factory/import entrypoint in `backend/app/main.py`.
+3. Add `GET /health` router.
+
+Verification:
+
+```powershell
+python -m compileall backend/app
+python -m pytest backend/tests/test_health.py
+```
+
+### Stage 2 - Configuration, SQLite, And File Storage
+
+1. Add settings object with configurable upload root, database path, allowed extensions, and max upload size.
+2. Add SQLite initialization and `documents` insert/query helpers.
+3. Add file-storage helper that generates stored filenames using backend document ids and writes only under upload root.
+
+Verification:
+
+```powershell
+python -m pytest backend/tests/test_storage.py backend/tests/test_database.py
+```
+
+### Stage 3 - Upload API And Error Contract
+
+1. Add `POST /api/files/upload`.
+2. Validate missing file, missing/invalid doc role, empty file, unsafe filename, unsupported extension, and file-too-large.
+3. Save file before metadata insert.
+4. Clean up stored file if metadata insert fails.
+5. Return only documented success fields.
+6. Return fixed error fields: `error_code`, `message`, `details`.
+
+Verification:
+
+```powershell
+python -m pytest backend/tests/test_upload_contract.py backend/tests/test_upload_validation.py
+```
+
+### Stage 4 - Boundary Tests And Scripts
+
+1. Add tests proving Phase 1 does not require OCR, LLM credentials, vector service, or parser output.
+2. Replace PowerShell project check placeholder with real compile and pytest commands.
+3. Replace bash project check placeholder with the same real check sequence for shell
+...[truncated]
+```
+
+## Implementation Check
+
+- [ ] Call chain is identified
+- [ ] Affected files are listed
+- [ ] Change scope is minimal
+- [ ] Validation commands are defined
+- [ ] Rollback or fallback is considered
+
+## C++ / System Check
+
+- [ ] Resource lifetime considered
+- [ ] Error propagation considered
+- [ ] Concurrency and locking considered
+- [ ] API / ABI compatibility considered
+- [ ] Performance impact considered
+
+## Human Decision
+
+- [ ] Approved
+- [ ] Needs replan
+- [ ] Rejected
+
+## Human Notes
diff --git a/.ai/reviews/spec-review.md b/.ai/reviews/spec-review.md
new file mode 100644
index 0000000..56e843f
--- /dev/null
+++ b/.ai/reviews/spec-review.md
@@ -0,0 +1,174 @@
+# Spec Review
+
+## Status
+
+WAITING_HUMAN_SPEC_APPROVAL
+
+## Source
+
+.ai/spec.md
+
+## Spec Summary
+
+```text
+# Spec - Phase 1 Backend Foundation
+
+## Objective
+
+Implement the smallest runnable FastAPI backend foundation for the 投标智能知识库能力验证版 Demo.
+
+Phase 1 proves that the service can start, accept an uploaded file, save it under a configurable local upload root, and persist document metadata in SQLite.
+
+Phase 1 is a backend foundation milestone. It is not the customer-facing Demo acceptance milestone.
+
+## Required Execution Mode
+
+This task must run under Auto_AICoding_Harness `large` mode with the `python-backend-service` profile.
+
+Before implementation:
+
+1. Run `ai-status` or `ai-doctor`.
+2. Confirm `.ai/state.json` reports `"mode": "large"`.
+3. Use large-mode gates according to `AGENTS.md`.
+4. Use subagent orchestration because the user explicitly requested it.
+
+## In Scope
+
+Implement only:
+
+1. FastAPI application startup.
+2. `GET /health`.
+3. `POST /api/files/upload`.
+4. Upload success response with HTTP `201 Created`.
+5. Upload success fields:
+   - `document_id`
+   - `original_filename`
+   - `doc_role`
+   - `parse_status`
+   - `file_size`
+   - `created_at`
+6. Structured error response fields:
+   - `error_code`
+   - `message`
+   - `details`
+7. Configurable upload root.
+8. Backend-generated stored filenames that do not use raw user filenames.
+9. SQLite `documents` table matching `docs/ai/12-phase1-api-persistence.md`.
+10. Pytest coverage for all P0 cases in `docs/ai/16-phase1-test-cases.md`.
+11. README local startup and test commands.
+12. Updated `.ai/verification.md`, `.ai/evaluation.md`, and `.ai/handoff.md`.
+
+## Out Of Scope
+
+Do not implement:
+
+1. OCR.
+2. LLM calls.
+3. Embeddings.
+4. Vector store or Qdrant.
+5. Haystack pipeline execution.
+6. Knowledge card generation.
+7. Tender file analysis.
+8. Frontend Demo.
+9. User system.
+10. Word or PDF export.
+11. Production deployment.
+
+## Expected File Scope
+
+Allowed implementation scope:
+
+```text
+backend/
+├── app/
+│   ├── __init__.py
+│   ├── main.py
+│   ├── config.py
+│   ├── api/
+│   │   ├── __init__.py
+│   │   ├── health.py
+│   │   └── files.py
+│   ├── schemas/
+│   │   ├── __init__.py
+│   │   └── document.py
+│   └── storage/
+│       ├── __init__.py
+│       ├── database.py
+│       └── file_storage.py
+└── tests/
+    ├── test_health.py
+    ├── test_upload_contract.py
+    ├── test_upload_validation.py
+    ├── test_storage.py
+    ├── test_database.py
+    └── test_phase1_boundaries.py
+```
+
+Repository-level files may be updated only as needed:
+
+- `README.md`
+- `.gitignore`
+- one dependency file, preferably `pyproject.toml`
+- `scripts/ai_check.ps1`
+- `scripts/ai_check.sh`
+- `.ai/implementation-plan.md`
+- `.ai/affected-files.md`
+- `.ai/run-trace.md`
+- `.ai/verification.md`
+- `.ai/evaluation.md`
+- `.ai/handoff.md`
+
+## Reference Repository Rule
+
+Reference repositories must remain outside this repository under:
+
+```text
+F:\BidKonwledge_refs
+```
+
+Use RAGFlow only for product/document ingestion/citation reference and Haystack demos only for later pipeline-shape reference. Do not vendor either repository into `F:\BidKonwledge`.
+
+## Acceptance Criteria
+
+Phase 1 is accepted when:
+
+1. The FastAPI app is importable.
+2. `GET /health` returns HTTP 200 and exactly `{"status": "ok"}`.
+3. `POST /api/files/upload` accepts valid `historical_bid` and `tender` uploads.
+4. Valid upload returns HTTP `201 Created`.
+5. Success responses contain only the documented Phase 1 fields and do not expose absolute local paths.
+6. Invalid upload requests return the documented structured error shape and error codes.
+7. Uploaded bytes are stored under the configured upload root.
+8. Stored filenames are generated by the backend and are distinct from raw original filenames.
+9. SQLite creates and uses a `documents` table with the required Phase 1 fields.
+10. Validation failures do not leave orphan files or metadata rows.
+11. P0 pytest coverage from `docs/ai/16-phase1-test-cases.md` passes.
+12. `scripts/ai_check.ps1` runs real Phase 1 checks.
+13. `scripts/ai_check.sh` is run when available, or the WSL/bash blocker is recorded.
+14. Loc
+...[truncated]
+```
+
+## Scope Check
+
+- [ ] Goal is clear
+- [ ] Non-goals are explicit
+- [ ] Allowed files / modules are clear
+- [ ] Forbidden changes are clear
+- [ ] Required validation is defined
+
+## Risk Check
+
+- [ ] API / ABI risk considered
+- [ ] Data / persistence risk considered
+- [ ] Concurrency / IPC / network risk considered
+- [ ] Performance risk considered
+- [ ] Rollback or recovery considered
+
+## Human Decision
+
+- [ ] Approved
+- [ ] Needs replan
+- [ ] Rejected
+
+## Human Notes
diff --git a/.ai/risk-and-rollback.md b/.ai/risk-and-rollback.md
new file mode 100644
index 0000000..285fd3a
--- /dev/null
+++ b/.ai/risk-and-rollback.md
@@ -0,0 +1,22 @@
+# Risk And Rollback
+
+## Risks
+
+1. Harness profile drift: `ai-upgrade large` defaults to `cpp-linux-backend-system` unless `--profile python-backend-service` is provided.
+2. Scope drift: Phase 1 could accidentally start parsing/RAG work too early.
+3. Large sample files could accidentally enter Git history.
+4. Placeholder scripts could be mistaken for real build/test coverage after Phase 1 implementation.
+
+## Mitigations
+
+1. `.ai/state.json` is set to `mode = large` and `profile = python-backend-service`.
+2. `AGENTS.md`, `README.md`, and Phase 1 docs explicitly require large mode and script execution.
+3. `docs/source-materials/sample-catalog.md` indexes large files without copying them.
+4. `docs/ai/13-phase1-verification-checklist.md` requires real script/test evidence before Phase 1 completion.
+
+## Rollback
+
+This task is documentation-only. Rollback is a normal Git revert before commit.
+
+If harness-generated large-mode files are not wanted, remove the files listed in `.ai/affected-files.md` and restore `.ai/state.json` from `.ai/backups/20260627-214154/.ai/state.json`.
+
diff --git a/.ai/run-trace.md b/.ai/run-trace.md
new file mode 100644
index 0000000..f7724f5
--- /dev/null
+++ b/.ai/run-trace.md
@@ -0,0 +1,56 @@
+# Run Trace
+
+Keep a short execution log for large-mode work.
+
+## Notes
+
+- command: ai-init medium --profile python-backend-service
+- output: created `.ai/state.json`, `.ai/run-trace.md`, Python backend profile docs, and `.ai/template-hashes.json`; existing project docs were skipped rather than overwritten.
+- follow-up: organized source documents under `docs/source-materials/`, added tech-selection and phase-roadmap docs, and kept large sample files outside Git.
+- command: ai-upgrade large
+- output: large-mode files and task evidence chain created; command defaulted profile to `cpp-linux-backend-system`.
+- follow-up: reran `ai-upgrade large --profile python-backend-service`; existing files were skipped, then `.ai/state.json` was corrected to `python-backend-service` to match project direction.
+- command: documentation prep
+- output: added Phase 1 development spec, local environment guide, API/persistence details, and verification checklist.
+- follow-up: run harness checks and project scripts before final response.
+- command: git clone references
+- output: cloned `infiniflow/ragflow` at `f90be41` and `deepset-ai/haystack-demos` at `17e6103` under `F:\BidKonwledge_refs`, outside the business repository.
+- follow-up: added direct二开/reuse strategy and target architecture documents.
+- command: ai-review spec
+- output: first review used stale Phase 0 spec and entered `WAITING_HUMAN_SPEC_APPROVAL`.
+- follow-up: user instructed rejection and Phase 1 spec rewrite.
+- command: ai-reject spec
+- output: stale Phase 0 spec gate rejected; state moved to `NEEDS_REPLAN`.
+- command: update `.ai/spec.md`
+- output: rewrote spec for Phase 1 backend foundation, fixed scope, non-goals, file scope, reference-repo rule, and verification commands.
+- command: ai-review spec --force
+- output: regenerated spec review from Phase 1 spec; state moved to `WAITING_HUMAN_SPEC_APPROVAL`.
+- command: ai-approve spec --force
+- output: user-approved Phase 1 spec gate; state moved to `SPEC_APPROVED`.
+- subagent: Hooke
+- role: read-only explorer
+- scope: Phase 1 API, persistence, validation, and pytest contract scan.
+- subagent: Meitner
+- role: read-only explorer
+- scope: scripts, README, verification artifact, and handoff scan.
+- command: ai-approve plan
+- output: user-approved Phase 1 plan gate; state moved to `PLAN_APPROVED`.
+- command: implementation
+- output: added FastAPI app, health endpoint, upload endpoint, config, local file storage, SQLite metadata persistence, pytest suite, real project scripts, and README local commands.
+- mid-task review: after upload API and tests, scope remained aligned with Phase 1; no OCR/RAG/LLM/frontend work was added; plan kept without escalation.
+- command: pip install -e '.[dev]'
+- output: first attempt failed because setuptools discovered multiple top-level packages; fixed package discovery and added `backend/__init__.py`; second issue required `python-multipart`; final install passed.
+- command: python -m compileall backend/app
+- output: passed.
+- command: python -m pytest backend/tests
+- output: initially 34 passed, 1 warning; after review fixes, 37 passed, 1 warning.
+- command: .\scripts\ai_check.ps1
+- output: passed; script now runs compileall and pytest.
+- command: bash ./scripts/ai_check.sh
+- output: failed because WSL/bash is unavailable on this Windows machine; recorded as not verified.
+- command: uvicorn + curl smoke
+- output: `GET /health` returned HTTP 200 and upload returned HTTP 201 with Phase 1 response fields.
+- subagent: Bohr
+- role: read-only reviewer
+- scope: implementation review against Phase 1 contract, scripts, README, tests, and boundary rules.
+- review-fix: broadened metadata failure handling, added file-write failure fault injection, metadata-failure cleanup test, and Windows `..\evil.txt` traversal test.
diff --git a/.ai/scope.md b/.ai/scope.md
new file mode 100644
index 0000000..28c5a57
--- /dev/null
+++ b/.ai/scope.md
@@ -0,0 +1,22 @@
+# Scope
+
+## Allowed Write Scope
+
+- `AGENTS.md`
+- `README.md`
+- `docs/ai/*.md`
+- `docs/ai/tasks/init-large/*.md`
+- `.ai/*.md`
+- `.ai/state.json`
+
+## Forbidden Areas
+
+- Do not implement backend business code.
+- Do not add runtime dependencies.
+- Do not copy large customer sample files into Git.
+- Do not start OCR, LLM, embedding, vector-store, retrieval, or demo-page work.
+
+## Harness Requirement
+
+Future development must use `large` mode. Large mode means stronger planning, gate, verification, and handoff discipline. It does not automatically imply multi-agent orchestration unless the user explicitly asks for subagents or delegation.
+
diff --git a/.ai/spec.md b/.ai/spec.md
new file mode 100644
index 0000000..b8d6bcc
--- /dev/null
+++ b/.ai/spec.md
@@ -0,0 +1,156 @@
+# Spec - Phase 1 Backend Foundation
+
+## Objective
+
+Implement the smallest runnable FastAPI backend foundation for the 投标智能知识库能力验证版 Demo.
+
+Phase 1 proves that the service can start, accept an uploaded file, save it under a configurable local upload root, and persist document metadata in SQLite.
+
+Phase 1 is a backend foundation milestone. It is not the customer-facing Demo acceptance milestone.
+
+## Required Execution Mode
+
+This task must run under Auto_AICoding_Harness `large` mode with the `python-backend-service` profile.
+
+Before implementation:
+
+1. Run `ai-status` or `ai-doctor`.
+2. Confirm `.ai/state.json` reports `"mode": "large"`.
+3. Use large-mode gates according to `AGENTS.md`.
+4. Use subagent orchestration because the user explicitly requested it.
+
+## In Scope
+
+Implement only:
+
+1. FastAPI application startup.
+2. `GET /health`.
+3. `POST /api/files/upload`.
+4. Upload success response with HTTP `201 Created`.
+5. Upload success fields:
+   - `document_id`
+   - `original_filename`
+   - `doc_role`
+   - `parse_status`
+   - `file_size`
+   - `created_at`
+6. Structured error response fields:
+   - `error_code`
+   - `message`
+   - `details`
+7. Configurable upload root.
+8. Backend-generated stored filenames that do not use raw user filenames.
+9. SQLite `documents` table matching `docs/ai/12-phase1-api-persistence.md`.
+10. Pytest coverage for all P0 cases in `docs/ai/16-phase1-test-cases.md`.
+11. README local startup and test commands.
+12. Updated `.ai/verification.md`, `.ai/evaluation.md`, and `.ai/handoff.md`.
+
+## Out Of Scope
+
+Do not implement:
+
+1. OCR.
+2. LLM calls.
+3. Embeddings.
+4. Vector store or Qdrant.
+5. Haystack pipeline execution.
+6. Knowledge card generation.
+7. Tender file analysis.
+8. Frontend Demo.
+9. User system.
+10. Word or PDF export.
+11. Production deployment.
+
+## Expected File Scope
+
+Allowed implementation scope:
+
+```text
+backend/
+├── app/
+│   ├── __init__.py
+│   ├── main.py
+│   ├── config.py
+│   ├── api/
+│   │   ├── __init__.py
+│   │   ├── health.py
+│   │   └── files.py
+│   ├── schemas/
+│   │   ├── __init__.py
+│   │   └── document.py
+│   └── storage/
+│       ├── __init__.py
+│       ├── database.py
+│       └── file_storage.py
+└── tests/
+    ├── test_health.py
+    ├── test_upload_contract.py
+    ├── test_upload_validation.py
+    ├── test_storage.py
+    ├── test_database.py
+    └── test_phase1_boundaries.py
+```
+
+Repository-level files may be updated only as needed:
+
+- `README.md`
+- `.gitignore`
+- one dependency file, preferably `pyproject.toml`
+- `scripts/ai_check.ps1`
+- `scripts/ai_check.sh`
+- `.ai/implementation-plan.md`
+- `.ai/affected-files.md`
+- `.ai/run-trace.md`
+- `.ai/verification.md`
+- `.ai/evaluation.md`
+- `.ai/handoff.md`
+
+## Reference Repository Rule
+
+Reference repositories must remain outside this repository under:
+
+```text
+F:\BidKonwledge_refs
+```
+
+Use RAGFlow only for product/document ingestion/citation reference and Haystack demos only for later pipeline-shape reference. Do not vendor either repository into `F:\BidKonwledge`.
+
+## Acceptance Criteria
+
+Phase 1 is accepted when:
+
+1. The FastAPI app is importable.
+2. `GET /health` returns HTTP 200 and exactly `{"status": "ok"}`.
+3. `POST /api/files/upload` accepts valid `historical_bid` and `tender` uploads.
+4. Valid upload returns HTTP `201 Created`.
+5. Success responses contain only the documented Phase 1 fields and do not expose absolute local paths.
+6. Invalid upload requests return the documented structured error shape and error codes.
+7. Uploaded bytes are stored under the configured upload root.
+8. Stored filenames are generated by the backend and are distinct from raw original filenames.
+9. SQLite creates and uses a `documents` table with the required Phase 1 fields.
+10. Validation failures do not leave orphan files or metadata rows.
+11. P0 pytest coverage from `docs/ai/16-phase1-test-cases.md` passes.
+12. `scripts/ai_check.ps1` runs real Phase 1 checks.
+13. `scripts/ai_check.sh` is run when available, or the WSL/bash blocker is recorded.
+14. Local uvicorn and `curl.exe --noproxy "*"` smoke checks are run if the app starts locally.
+15. `.ai/verification.md`, `.ai/evaluation.md`, and `.ai/handoff.md` record the actual command evidence and residual risks.
+
+## Required Verification Commands
+
+Run before completion:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
+.\scripts\ai_check.ps1
+python -m pytest backend/tests
+```
+
+When shell tooling is available:
+
+```powershell
+bash ./scripts/ai_check.sh
+```
+
+If WSL/bash is unavailable, record the reason in `.ai/verification.md` and do not claim the bash script passed.
diff --git a/.ai/state.json b/.ai/state.json
new file mode 100644
index 0000000..245748c
--- /dev/null
+++ b/.ai/state.json
@@ -0,0 +1,15 @@
+{
+  "schema_version": 1,
+  "mode": "large",
+  "profile": "python-backend-service",
+  "status": "PLAN_APPROVED",
+  "current_gate": null,
+  "approved_gates": [
+    "spec",
+    "plan"
+  ],
+  "created_by": "Auto_AICoding_Harness",
+  "task_id": "init-large",
+  "task_title": "Initialize harness in large mode",
+  "updated_at": "2026-06-28T00:57:51+08:00"
+}
diff --git a/.ai/subagent-packets/README.md b/.ai/subagent-packets/README.md
new file mode 100644
index 0000000..e7f075b
--- /dev/null
+++ b/.ai/subagent-packets/README.md
@@ -0,0 +1,26 @@
+# Subagent Packets
+
+These files are large-mode task packet templates.
+Use them when a task benefits from bounded role-specific work by a subagent, another local agent, or the main agent acting in that role.
+
+Packets are not an execution system.
+They do not start subagents, install skills, approve gates, or replace `.ai/state.json`.
+
+## How To Use
+
+1. Pick the role packet that matches the needed work.
+2. Fill in the required context with exact files, docs, diffs, and constraints.
+3. Copy the packet's `Required Skills` and `Optional Skills` explicitly into the real dispatch request.
+4. Record the dispatch in `.ai/run-trace.md` with role, scope, required skills, optional skills, objective, and result location.
+5. Give the packet to the worker agent or use it yourself as the role contract.
+6. Write the returned evidence into `.ai/run-trace.md`, `.ai/reviews/`, `.ai/evaluation.md`, `.ai/context-pack.md`, or `.ai/handoff.md` as appropriate.
+
+## Roles
+
+- `planner.md`: scope, sequencing, gates, and verification strategy.
+- `explorer.md`: read-only repository analysis and affected-file mapping.
+- `implementer.md`: scoped edits only.
+- `reviewer.md`: diff and regression review.
+- `evaluator.md`: verification evidence and residual-risk check.
+
+If subagents are unavailable, the main agent should follow these packet contracts sequentially.
diff --git a/.ai/subagent-packets/evaluator.md b/.ai/subagent-packets/evaluator.md
new file mode 100644
index 0000000..3fb998b
--- /dev/null
+++ b/.ai/subagent-packets/evaluator.md
@@ -0,0 +1,63 @@
+# Evaluator Packet
+
+## Role
+
+Check whether the completed work has enough evidence to claim completion.
+
+## Required Skills
+
+- `methodology/verification-before-completion`
+- `system/performance-analysis`
+
+## Optional Skills
+
+- `methodology/systematic-debugging`
+- `methodology/context-engineering`
+- `methodology/code-review-and-quality`
+- `system/cpp-linux-system-engineering`
+
+## Required Context
+
+- User request and final claimed outcome.
+- Changed files or final diff.
+- Commands run and their output.
+- Relevant `.ai/evaluation.md`, `.ai/run-trace.md`, `.ai/context-pack.md`, or `.ai/handoff.md`.
+- Known unverified items.
+
+## Objective
+
+Validate completion evidence and identify remaining risks before the main agent reports final status.
+
+## Forbidden Actions
+
+- Do not edit implementation files.
+- Do not claim tests passed unless command output proves it.
+- Do not hide failed or skipped verification.
+- Do not convert missing verification into success.
+
+## Expected Output
+
+- Verification status.
+- Commands reviewed.
+- Evidence quality.
+- Unverified items and why they matter.
+- Recommended final claim.
+
+## Stop Conditions
+
+- Verification evidence is unavailable.
+- The changed scope cannot be matched to the request.
+- A critical check failed and no accepted mitigation exists.
+
+## Return Format
+
+```text
+role: evaluator
+status: complete | blocked
+verified:
+commands:
+evidence:
+unverified:
+recommended_final_claim:
+blockers:
+```
diff --git a/.ai/subagent-packets/explorer.md b/.ai/subagent-packets/explorer.md
new file mode 100644
index 0000000..e073c5a
--- /dev/null
+++ b/.ai/subagent-packets/explorer.md
@@ -0,0 +1,61 @@
+# Explorer Packet
+
+## Role
+
+Inspect the repository or subsystem and return evidence-backed context without changing files.
+
+## Required Skills
+
+- `methodology/context-engineering`
+- `methodology/systematic-debugging`
+
+## Optional Skills
+
+- `methodology/source-driven-development`
+- `system/cpp-linux-system-engineering`
+- `system/performance-analysis`
+- `system/security-review`
+
+## Required Context
+
+- User request.
+- Expected subsystem or files, if known.
+- Relevant `docs/ai/*`, `.ai/spec.md`, `.ai/scope.md`, or `.ai/implementation-plan.md`.
+- Current failure, diff, logs, or command output if exploration is for debugging.
+
+## Objective
+
+Map the relevant code, contracts, call chains, and likely affected files.
+
+## Forbidden Actions
+
+- Do not edit files.
+- Do not run destructive commands.
+- Do not create implementation plans that exceed the requested scope.
+- Do not claim behavior without file, command, or log evidence.
+
+## Expected Output
+
+- Relevant entrypoints.
+- Affected files or modules.
+- Important contracts and dependencies.
+- Evidence references.
+- Open questions or risks.
+
+## Stop Conditions
+
+- Required files are missing.
+- The repository state conflicts with the supplied context.
+- The needed evidence requires credentials, services, or data not available to the worker.
+
+## Return Format
+
+```text
+role: explorer
+status: complete | blocked
+entrypoints:
+affected_files:
+evidence:
+risks:
+blockers:
+```
diff --git a/.ai/subagent-packets/implementer.md b/.ai/subagent-packets/implementer.md
new file mode 100644
index 0000000..bf5a782
--- /dev/null
+++ b/.ai/subagent-packets/implementer.md
@@ -0,0 +1,63 @@
+# Implementer Packet
+
+## Role
+
+Make scoped changes that match the approved plan or task contract.
+
+## Required Skills
+
+- `methodology/karpathy-guidelines`
+- `methodology/verification-before-completion`
+- `system/cpp-linux-system-engineering`
+
+## Optional Skills
+
+- `methodology/test-driven-development`
+- `methodology/source-driven-development`
+- `methodology/context-engineering`
+- `system/security-review`
+- `system/performance-analysis`
+
+## Required Context
+
+- User request and non-goals.
+- Approved plan or explicit task contract.
+- Files or modules allowed for editing.
+- Relevant `docs/ai/*` and `.ai/*` artifacts.
+- Verification commands expected after the change.
+
+## Objective
+
+Implement the smallest change that satisfies the task while preserving existing contracts.
+
+## Forbidden Actions
+
+- Do not edit files outside the allowed scope.
+- Do not change public contracts unless the packet explicitly authorizes it.
+- Do not bypass safe-write, review, or verification requirements.
+- Do not install dependencies or modify secrets.
+
+## Expected Output
+
+- Files changed.
+- Rationale for the chosen implementation.
+- Any deviations from the plan.
+- Verification run or verification blocker.
+
+## Stop Conditions
+
+- Required context is stale or contradicts the repo.
+- The fix requires a broader contract, schema, security, or architecture change.
+- The planned verification cannot be run or replaced with an equivalent check.
+
+## Return Format
+
+```text
+role: implementer
+status: complete | blocked
+changed_files:
+summary:
+deviations:
+verification:
+blockers:
+```
diff --git a/.ai/subagent-packets/planner.md b/.ai/subagent-packets/planner.md
new file mode 100644
index 0000000..57005fe
--- /dev/null
+++ b/.ai/subagent-packets/planner.md
@@ -0,0 +1,66 @@
+# Planner Packet
+
+## Role
+
+Convert the user request into a bounded implementation plan, task level, risks, gates, and verification strategy.
+
+## Required Skills
+
+- `methodology/task-contract-and-leveling`
+- `methodology/karpathy-guidelines`
+- `methodology/context-engineering`
+- `methodology/planning-and-task-breakdown`
+
+## Optional Skills
+
+- `methodology/source-driven-development`
+- `system/cpp-linux-system-engineering`
+- `system/performance-analysis`
+- `system/security-review`
+
+## Required Context
+
+- User request and explicit non-goals.
+- Current task level, if already chosen.
+- Relevant `AGENTS.md`, `docs/ai/*`, and `.ai/*` artifacts.
+- Files, modules, or interfaces likely in scope.
+- Known verification commands or constraints.
+
+## Objective
+
+Return a concise plan that controls scope and identifies what must be verified before completion.
+
+## Forbidden Actions
+
+- Do not edit files.
+- Do not approve gates.
+- Do not expand scope beyond the user request.
+- Do not assume missing project facts without labeling them as assumptions.
+
+## Expected Output
+
+- Proposed task level.
+- Target outcome.
+- File or module scope.
+- Sequenced plan.
+- Risks and rollback notes.
+- Verification plan.
+
+## Stop Conditions
+
+- Requirements are materially ambiguous.
+- The task appears to affect a public API, shared schema, security boundary, or production data path without enough context.
+- Verification cannot be defined.
+
+## Return Format
+
+```text
+role: planner
+status: complete | blocked
+task_level:
+scope:
+plan:
+risks:
+verification:
+blockers:
+```
diff --git a/.ai/subagent-packets/reviewer.md b/.ai/subagent-packets/reviewer.md
new file mode 100644
index 0000000..a3e0336
--- /dev/null
+++ b/.ai/subagent-packets/reviewer.md
@@ -0,0 +1,61 @@
+# Reviewer Packet
+
+## Role
+
+Review the proposed diff or artifact for correctness, regressions, contract impact, tests, and maintainability.
+
+## Required Skills
+
+- `methodology/code-review-and-quality`
+- `methodology/verification-before-completion`
+- `system/cpp-linux-system-engineering`
+
+## Optional Skills
+
+- `methodology/source-driven-development`
+- `system/security-review`
+- `system/performance-analysis`
+- `methodology/systematic-debugging`
+
+## Required Context
+
+- User request and non-goals.
+- Current diff or exact changed files.
+- Relevant `docs/ai/*`, `.ai/spec.md`, `.ai/implementation-plan.md`, and `.ai/affected-files.md`.
+- Tests or checks already run.
+
+## Objective
+
+Identify actionable defects, regressions, missing verification, and scope drift before approval.
+
+## Forbidden Actions
+
+- Do not edit files unless explicitly asked.
+- Do not approve the gate by yourself.
+- Do not produce vague quality comments without actionable evidence.
+- Do not ignore missing tests when behavior changed.
+
+## Expected Output
+
+- Findings ordered by severity.
+- File and line references when available.
+- Missing tests or verification gaps.
+- Residual risks and open questions.
+
+## Stop Conditions
+
+- No diff or artifact is provided.
+- Required source files cannot be read.
+- The change scope is materially different from the supplied request.
+
+## Return Format
+
+```text
+role: reviewer
+status: complete | blocked
+findings:
+verification_gaps:
+scope_drift:
+open_questions:
+blockers:
+```
diff --git a/.ai/tasks/init-large/approval.json b/.ai/tasks/init-large/approval.json
new file mode 100644
index 0000000..11063c8
--- /dev/null
+++ b/.ai/tasks/init-large/approval.json
@@ -0,0 +1,8 @@
+{
+  "status": "approved",
+  "review_type": "spec",
+  "created_at": "2026-06-28T00:53:07+08:00",
+  "review_summary": "Human approved the Phase 1 backend foundation spec gate after the stale Phase 0 spec was rejected and replaced.",
+  "risk_level": "medium",
+  "required_action": "run ai-review plan"
+}
diff --git a/.ai/tasks/init-large/context.jsonl b/.ai/tasks/init-large/context.jsonl
new file mode 100644
index 0000000..46adb20
--- /dev/null
+++ b/.ai/tasks/init-large/context.jsonl
@@ -0,0 +1,9 @@
+{"path": ".ai/spec.md", "reason": "Large-mode requirement source", "phase": "implement"}
+{"path": ".ai/implementation-plan.md", "reason": "Large-mode implementation plan", "phase": "implement"}
+{"path": ".ai/tech-design.md", "reason": "Large-mode technical design", "phase": "implement"}
+{"path": ".ai/risk-and-rollback.md", "reason": "Rollback and risk guardrails", "phase": "review"}
+{"path": ".ai/verification.md", "reason": "Verification evidence", "phase": "review"}
+{"path": ".ai/handoff.md", "reason": "Cross-session handoff summary", "phase": "handoff"}
+{"path": "docs/ai/tasks/init-large/01-spec.md", "reason": "Durable task spec evidence", "phase": "implement"}
+{"path": "docs/ai/tasks/init-large/03-implementation-plan.md", "reason": "Durable task implementation plan evidence", "phase": "implement"}
+{"path": "docs/ai/tasks/init-large/05-verification.md", "reason": "Durable task verification evidence", "phase": "review"}
diff --git a/.ai/tasks/init-large/rca.md b/.ai/tasks/init-large/rca.md
new file mode 100644
index 0000000..3d3f82a
--- /dev/null
+++ b/.ai/tasks/init-large/rca.md
@@ -0,0 +1,29 @@
+# RCA Draft
+
+## Status
+
+DRAFT
+
+## Trigger
+
+- gate: spec
+- rejected_status: NEEDS_REPLAN
+- task_id: init-large
+- created_at: 2026-06-28T00:50:22+08:00
+
+## Observed Failure
+
+Human rejected the spec review gate. The task requires replanning before continuing.
+
+## Likely Cause
+
+- To be completed by the implementer or reviewer before retrying the gate.
+
+## Corrective Action
+
+- Address the rejected `spec` gate feedback.
+- Rerun `ai-review spec` after the fix.
+
+## Follow-up Rule Candidate
+
+- See the generated check-rule draft. It is not enforced unless explicitly approved.
diff --git a/.ai/tech-design.md b/.ai/tech-design.md
new file mode 100644
index 0000000..02cf8c6
--- /dev/null
+++ b/.ai/tech-design.md
@@ -0,0 +1,34 @@
+# Tech Design
+
+## Current Task Design
+
+This task is documentation and workflow configuration only.
+
+The design is to keep the repository as a generated target project for Auto_AICoding_Harness:
+
+- `docs/ai/` stores durable product and engineering context.
+- `.ai/` stores current large-mode task runtime artifacts.
+- `docs/source-materials/` stores source document copies and sample indexes.
+- `backend/` and `frontend/` remain placeholders until Phase 1 implementation begins.
+
+## Phase 1 Design Boundary
+
+Phase 1 will later implement:
+
+- FastAPI app startup.
+- `GET /health`.
+- `POST /api/files/upload`.
+- local file storage.
+- SQLite document metadata.
+- smoke tests.
+
+Phase 1 will not implement parsing, retrieval, generation, OCR, vector storage, or UI.
+
+## Interface Decisions For Future Implementation
+
+1. Upload status starts as `parse_status = pending`.
+2. SQLite table `documents` stores metadata only.
+3. Uploaded files are saved under configurable `data/uploads`.
+4. User-provided filenames are preserved as metadata but must not be trusted as storage paths.
+5. Tests and scripts must be run before completion.
+
diff --git a/.ai/template-hashes.json b/.ai/template-hashes.json
new file mode 100644
index 0000000..c58b8e2
--- /dev/null
+++ b/.ai/template-hashes.json
@@ -0,0 +1,182 @@
+{
+  "schema_version": 1,
+  "profile": "cpp-linux-backend-system",
+  "files": [
+    {
+      "path": ".ai/.gitkeep",
+      "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
+    },
+    {
+      "path": ".ai/affected-files.md",
+      "sha256": "c8136bb0a9f634143ea703268806789f95ec3510c506dd7afc2681cf6b11a3bd"
+    },
+    {
+      "path": ".ai/approvals/README.md",
+      "sha256": "46fb131525e709fee6440d07b64cb113556f9a5ba6a63a9c09a026f7fbd04da8"
+    },
+    {
+      "path": ".ai/epic.md",
+      "sha256": "4db8f8972f100afc0f963c2aef182748db71d4a46512fd8030aba213b2156ee3"
+    },
+    {
+      "path": ".ai/implementation-plan.md",
+      "sha256": "796c3297ff371f58999af70ca42e010656aa4abf12d18c6c7665b0e62c836e80"
+    },
+    {
+      "path": ".ai/reviews/README.md",
+      "sha256": "7a0426311283caef2a98b94b2ac29f92ba2314c616f954cf4164b7f0517764a0"
+    },
+    {
+      "path": ".ai/risk-and-rollback.md",
+      "sha256": "f81dc9776184b1212767dd24021232f75a042fbf15b4a1f06dc96bbf20392df1"
+    },
+    {
+      "path": ".ai/run-trace.md",
+      "sha256": "533b76f7e8980a8193dd8d145add6cf97819a1bd93a276e545c9a921ff1264cc"
+    },
+    {
+      "path": ".ai/scope.md",
+      "sha256": "4db107f4286ac3b205cd0c069bdab2defd00931b7825019802469f27b562aeaa"
+    },
+    {
+      "path": ".ai/subagent-packets/README.md",
+      "sha256": "cd3b49455f74a68411162d38f603388151f4d3e7dc45bebe776977747db404bc"
+    },
+    {
+      "path": ".ai/subagent-packets/evaluator.md",
+      "sha256": "4329f21dc0188ee259e2e9963d8b9805b6893593896260872f5619e519a189e5"
+    },
+    {
+      "path": ".ai/subagent-packets/explorer.md",
+      "sha256": "f8d34fa6bb2d9a8987fe0f82acd05972d530358a157ad7757650a3732490d86b"
+    },
+    {
+      "path": ".ai/subagent-packets/implementer.md",
+      "sha256": "7ebf578d6032450ce212852b9cf40b7aa8017d64b0972ee4ac129d1ebb142391"
+    },
+    {
+      "path": ".ai/subagent-packets/planner.md",
+      "sha256": "59a642c0969a093f8593ed486c4d9e7430d0d9a8bbec2bcd015d2c2c596419b8"
+    },
+    {
+      "path": ".ai/subagent-packets/reviewer.md",
+      "sha256": "f068bdd78446b8a619cc5d3ebda389d1a665bafd451bdd4f4363c38a1bd2e8f9"
+    },
+    {
+      "path": ".ai/tech-design.md",
+      "sha256": "79721b80a1ba6ccff2baa2e7fb7f0e9f33ce1e5d8555460c1a26d564d4ec2428"
+    },
+    {
+      "path": ".ai/templates/README.md",
+      "sha256": "f0b3ef6c12cc04e0b217bb25f1715b5deb15b367fb0ce633008737682e282fc6"
+    },
+    {
+      "path": ".ai/verification.md",
+      "sha256": "e584acdddc52d448963ffe9925e9a49b6e829b86494ec85d057ff6402eddf700"
+    },
+    {
+      "path": ".codex/agents/README.md",
+      "sha256": "1fc752d871294f7cd4e1f396e9cfcd2d7060b0680492892538a3e78472330431"
+    },
+    {
+      "path": ".codex/agents/evaluator.md",
+      "sha256": "f89c58d70d504c39c388893fb36a6c88ae1dd78cd15fd377e83cc7f7a240119a"
+    },
+    {
+      "path": ".codex/agents/explorer.md",
+      "sha256": "d1ebe9f449f8fcfd46cbcdd1278078fbdd67721444ab0c497aeded6ec942be27"
+    },
+    {
+      "path": ".codex/agents/implementer.md",
+      "sha256": "71f9e6a6b5c6bf8a89adfa6cd4b34dbe70d2b2d0186eb97d873976ec7826a481"
+    },
+    {
+      "path": ".codex/agents/planner.md",
+      "sha256": "3bbb1b569a77a7e2beb43471fc31c1b996da7ed79e1b8c63e9f6bf25783f7f12"
+    },
+    {
+      "path": ".codex/agents/reviewer.md",
+      "sha256": "d821adcb990f5e9007f817024487a39cddaa41a83ff275817cbefc233ff760d4"
+    },
+    {
+      "path": ".github/copilot-instructions.md",
+      "sha256": "c3be6e94afc6ad33748d2818126ebccddce59291e77d057dbd53330bae883071"
+    },
+    {
+      "path": "AGENTS.md",
+      "sha256": "1038e187b4ca584b697563afa5abcd4793ef6765950f6b1f9058abb1156f44cb"
+    },
+    {
+      "path": "CLAUDE.md",
+      "sha256": "de31e5ff3de46ff418e5ea6a2ce068bd0a5d39b2c96b2325558718cacce71bd2"
+    },
+    {
+      "path": "docs/ai/README.md",
+      "sha256": "442b45633136126ad9b0139ee7bde0fc21850c695dd7b93d5575a2a20337e732"
+    },
+    {
+      "path": "docs/ai/async.md",
+      "sha256": "200430ab399334078195eae030120e67b105b3550b0a60d0b7d5528a137fe1f1"
+    },
+    {
+      "path": "docs/ai/data.md",
+      "sha256": "9e3820043e6d743070de15bc2b0718ec85327e77d62e1448105c27c82c934fb0"
+    },
+    {
+      "path": "docs/ai/dependency.md",
+      "sha256": "b871400bb96e3573dacfb7bec344afe413217870af6aa63556632294e037a461"
+    },
+    {
+      "path": "docs/ai/frameworks.md",
+      "sha256": "c0cd47788a2b75a6696c887fe9c8677494d2ab451c80029640489d6a5e709308"
+    },
+    {
+      "path": "docs/ai/observability.md",
+      "sha256": "41996dda20336d2d479454e542d2d0709b99289dad252f00c7cfe019cf554dcc"
+    },
+    {
+      "path": "docs/ai/packaging.md",
+      "sha256": "5398483725d14b63b12a4b3a27213de70e6e9974932756873faece77173d642e"
+    },
+    {
+      "path": "docs/ai/performance.md",
+      "sha256": "82ac1a2e185840146ac62ea790601c0bc5f7bbf5e9d8cd6b1cf0f1bd97f03e44"
+    },
+    {
+      "path": "docs/ai/python.md",
+      "sha256": "a2854b7272bd8e2c196ce1e29286609ae094490d87fcda7f49c483218c39c882"
+    },
+    {
+      "path": "docs/ai/security.md",
+      "sha256": "ec10aa68e4a74813f631224904ab4636e85b848c460ab08c6c68d1360cc5abb8"
+    },
+    {
+      "path": "docs/ai/testing.md",
+      "sha256": "345a31fccfe53eb90cb6ae16e433d79fcccdacacb7e0f08093b8b9b47516fed6"
+    },
+    {
+      "path": "docs/ai/typing.md",
+      "sha256": "4cacc2b57ddfbde6d468086336c8837881bbed3f65f42ec987ea3e973d7f73c7"
+    },
+    {
+      "path": "docs/ai/verification-matrix.md",
+      "sha256": "195ca11079c62c251814f97514d189f3f82a1c0ce6feaa159099bcc73c1e1577"
+    },
+    {
+      "path": "docs/ai/workflow.md",
+      "sha256": "07aa22c1a7a698e8ed3a37a358fe98dfc2c6c6daca022eb63772c1f6536acfbe"
+    },
+    {
+      "path": "scripts/ai_build.sh",
+      "sha256": "9feb6363dd15910756cf19e3399e82ed7a693b4ad3caa7abc234a03547188f00"
+    },
+    {
+      "path": "scripts/ai_check.sh",
+      "sha256": "667ff58541183e4c227e2c2abb15545fc37a25471ad056e3af354e216621a1f2"
+    },
+    {
+      "path": "scripts/ai_test.sh",
+      "sha256": "db25fee3702819854b3d2af7cb74852b4e97d51ab23fa6c587367a815e196986"
+    }
+  ]
+}
diff --git a/.ai/templates/README.md b/.ai/templates/README.md
new file mode 100644
index 0000000..8a1e34f
--- /dev/null
+++ b/.ai/templates/README.md
@@ -0,0 +1,6 @@
+# .ai templates
+
+This directory is the template source for target-project `.ai/` runtime skeleton files.
+
+`state.json`, reviews, approvals, traces, and backups are runtime outputs.
+They should be generated into the target project, not maintained as live state in the harness repository.
diff --git a/.ai/verification.md b/.ai/verification.md
new file mode 100644
index 0000000..393ea62
--- /dev/null
+++ b/.ai/verification.md
@@ -0,0 +1,313 @@
+# Verification
+
+## Phase 1 Backend Foundation Verification
+
+Updated on 2026-06-28.
+
+### Harness Gate And Status
+
+Commands run:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
+```
+
+Observed:
+
+- `ai-status`: initialized yes, mode `large`, profile `python-backend-service`.
+- Spec gate was rejected once because it still pointed at the stale Phase 0 spec.
+- `.ai/spec.md` was rewritten for Phase 1 backend foundation.
+- `ai-review spec --force` was run, then the user approved with `ai-approve spec --force`.
+- `ai-review plan --force` was run, then the user approved with `ai-approve plan`.
+- Current implementation proceeded after `SPEC_APPROVED` and `PLAN_APPROVED`.
+
+### Dependency Setup
+
+Command run:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py -m pip install -e '.[dev]'
+```
+
+Observed:
+
+- Initial install failed because setuptools auto-discovered multiple top-level folders.
+- Fixed by adding explicit setuptools package discovery for `backend*`.
+- Added `python-multipart` after FastAPI reported it is required for form uploads.
+- Final install passed.
+
+### Build And Automated Tests
+
+Commands run:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py -m compileall backend/app
+& $py -m pytest backend/tests
+```
+
+Observed:
+
+- `compileall backend/app`: passed.
+- `pytest backend/tests`: `37 passed, 1 warning`.
+- Warning: FastAPI/Starlette test client reports `httpx` integration deprecation and suggests `httpx2`; this does not affect Phase 1 correctness.
+
+Required explicit pytest command:
+
+```powershell
+$env:Path='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python;' + $env:Path
+python -m pytest backend/tests
+```
+
+Observed:
+
+- `37 passed, 1 warning`.
+
+### Project Scripts
+
+Command run:
+
+```powershell
+.\scripts\ai_check.ps1
+```
+
+Observed:
+
+- Uses bundled Python when `PYTHON` is not set.
+- Runs `python -m compileall backend/app`.
+- Runs `python -m pytest backend/tests`.
+- Result: passed, `37 passed, 1 warning`.
+
+Command attempted:
+
+```powershell
+$env:PYTHON='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+bash ./scripts/ai_check.sh
+```
+
+Observed:
+
+- Failed because this Windows machine has no usable WSL/Linux distribution for `bash`.
+- This is recorded as not verified. Do not claim bash verification passed.
+- PowerShell script is the primary Windows verification path.
+
+### Manual Smoke
+
+Server command:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
+```
+
+Health smoke:
+
+```powershell
+curl.exe --noproxy "*" http://127.0.0.1:8000/health
+```
+
+Observed:
+
+```json
+{"status":"ok"}
+```
+
+HTTP status: `200`.
+
+Upload smoke:
+
+```powershell
+curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/files/upload" `
+  -F "doc_role=historical_bid" `
+  -F "file=@.\data\samples\phase1-smoke.txt"
+```
+
+Observed:
+
+- HTTP status: `201`.
+- Response fields: `document_id`, `original_filename`, `doc_role`, `parse_status`, `file_size`, `created_at`.
+- `parse_status`: `pending`.
+
+### Reference Repository Checks
+
+Commands run:
+
+```powershell
+git -C F:\BidKonwledge_refs\ragflow rev-parse --short HEAD
+git -C F:\BidKonwledge_refs\haystack-demos rev-parse --short HEAD
+```
+
+Observed:
+
+- RAGFlow: `f90be41`.
+- Haystack demos: `17e6103`.
+- Both remain outside `F:\BidKonwledge`.
+
+### Unverified Or Deferred
+
+- `bash ./scripts/ai_check.sh`: not verified because WSL/bash is unavailable on this Windows machine.
+- Dedicated fault-injection tests now cover file write failure and metadata write failure cleanup.
+
+## Large-Mode Requirement
+
+All future development must run under harness `large` mode and must run the project check scripts before completion.
+
+For this documentation-prep task, verify:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
+.\scripts\ai_check.ps1
+bash ./scripts/ai_check.sh
+```
+
+Observed on 2026-06-27:
+
+- `ai-status`: initialized yes, mode `large`, profile `python-backend-service`, state valid.
+- `ai-doctor`: OK for Git repo, state schema, large-mode files, and task chain; warning only for uncommitted working tree changes.
+- `.\scripts\ai_check.ps1`: passed; script reported Phase 0 has no runnable backend yet and listed future Python checks.
+- `bash ./scripts/ai_check.sh`: not runnable on this machine because no WSL/Linux distribution is installed; PowerShell script is the current Windows check path.
+
+## Reference Repository Checks
+
+Run on 2026-06-27:
+
+```powershell
+git -C F:\BidKonwledge_refs\ragflow rev-parse --short HEAD
+git -C F:\BidKonwledge_refs\haystack-demos rev-parse --short HEAD
+git status --short
+```
+
+Observed:
+
+- RAGFlow reference clone: `f90be41`.
+- Haystack demos reference clone: `17e6103`.
+- Both clones are outside `F:\BidKonwledge`.
+- `git status --short` in the business repository does not include `F:\BidKonwledge_refs`.
+
+## Phase 1 Test-Case Documentation Check
+
+Updated on 2026-06-27:
+
+- `docs/ai/16-phase1-test-cases.md` now defines detailed Phase 1 automated and manual test cases.
+- `docs/ai/16-phase1-test-cases.md` is explicitly an internal backend foundation test spec, not a customer-facing PRD or complete Demo acceptance document.
+- Upload success is now fixed as HTTP `201 Created`.
+- Upload error responses now use the fixed JSON shape `error_code`, `message`, and `details`.
+- SQLite `documents` fields are now fixed in `docs/ai/12-phase1-api-persistence.md`.
+- File safety and atomicity rules now require backend-generated stored filenames and cleanup when validation or persistence fails.
+- Harness commands are documented as delivery command checks, not core business pytest cases.
+- The document is a test-case specification for the next development session, not pytest implementation.
+- Phase 1 pytest files are still expected to be created during backend implementation.
+- `docs/ai/README.md`, `.ai/implementation-plan.md`, and `.ai/handoff.md` now include the detailed test-case document in required Phase 1 context.
+
+Verification commands run after the update:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
+.\scripts\ai_check.ps1
+```
+
+Observed:
+
+- `ai-status`: initialized yes, mode `large`, profile `python-backend-service`, state valid, task chain present.
+- `ai-doctor`: passed required state, mode, profile, large files, and task chain checks; warning only for uncommitted working tree changes.
+- `.\scripts\ai_check.ps1`: exited successfully and reported Phase 0 has no runnable backend yet.
+- `bash ./scripts/ai_check.sh`: not rerun for this documentation-only update; previous blocker remains no WSL/Linux distribution installed.
+
+## Phase 1 Contract-Hardening Check
+
+Updated on 2026-06-27:
+
+- `docs/ai/12-phase1-api-persistence.md` now fixes the Phase 1 upload API contract.
+- `docs/ai/04-api-contract.md` now mirrors the fixed upload success/error response shape.
+- `docs/ai/03-data-model.md` now mirrors the fixed Phase 1 document metadata fields.
+- `docs/ai/16-phase1-test-cases.md` now states that it is an internal backend foundation test spec, not a customer-facing PRD or full Demo acceptance document.
+- `docs/ai/16-phase1-test-cases.md` now separates delivery command checks from business pytest coverage.
+- The current local checkout path remains `F:\BidKonwledge`; `docs/ai/11-local-dev-env.md` records the canonical project name as `BidKnowledge` and warns not to hard-code the absolute path in tests.
+
+Verification commands run after the contract-hardening update:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
+.\scripts\ai_check.ps1
+git diff --check
+```
+
+Observed:
+
+- `ai-status`: initialized yes, mode `large`, profile `python-backend-service`, state valid, task chain present.
+- `ai-doctor`: passed required state, mode, profile, large files, and task chain checks; warning only for uncommitted working tree changes.
+- `.\scripts\ai_check.ps1`: exited successfully and reported Phase 0 has no runnable backend yet.
+- `git diff --check`: passed.
+- `rg` old-contract scan over docs and `.ai`: no matches for the prior loose status-code, old response-field, old DB-field, or pytest/script-mixing wording.
+- Pytest was not run because Phase 1 backend implementation has not started.
+
+## Current Initialization And Documentation Checks
+
+Run on 2026-06-27:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
+git status --short
+Get-ChildItem -Recurse -Force docs\source-materials
+Get-ChildItem -Force docs\ai
+```
+
+Observed:
+
+- `ai-status` now reports initialized large mode with `python-backend-service` profile.
+- `ai-doctor` reports valid state schema and required large files present.
+- `ai-doctor` warns that the working tree has uncommitted changes, which is expected for this newly initialized repository.
+- Source documents copied into `docs/source-materials/originals/`.
+- Large external sample files remain outside Git and are indexed in `docs/source-materials/sample-catalog.md`.
+
+## Phase 0 Checks
+
+Run:
+
+```powershell
+git status --short
+Get-ChildItem -Force
+Get-ChildItem -Force docs/ai
+Get-ChildItem -Force .ai
+```
+
+Expected:
+
+- Git repository exists.
+- Harness files exist.
+- `docs/ai` contains project context files.
+- `.ai` contains current planning files.
+- No business implementation files are present beyond empty scaffold folders and `.gitkeep` files.
+
+## Phase 1 Checks
+
+Future Phase 1 should run:
+
+```powershell
+python -m pytest
+python -m uvicorn app.main:app --reload
+```
+
+The exact Python command may change depending on the selected virtual environment.
+
+Phase 1 acceptance requires:
+
+- `GET /health` returns `{"status":"ok"}`.
+- `POST /api/files/upload` returns HTTP `201 Created` for valid uploads.
+- Upload success response contains `document_id`, `original_filename`, `doc_role`, `parse_status`, `file_size`, and `created_at`.
+- Upload error response contains `error_code`, `message`, and `details`.
+- Upload endpoint saves a file under configured upload root using a backend-generated stored filename.
+- SQLite stores document metadata using the fields in `docs/ai/12-phase1-api-persistence.md`.
+- Invalid uploads do not leave orphan files or metadata rows.
+- Tests cover the P0 cases in `docs/ai/16-phase1-test-cases.md`.
diff --git a/.codex/agents/README.md b/.codex/agents/README.md
new file mode 100644
index 0000000..ceb2e59
--- /dev/null
+++ b/.codex/agents/README.md
@@ -0,0 +1,19 @@
+# Agents
+
+These files are role templates for optional large-mode subagent workflows.
+
+- They are optional enhancement templates.
+- They are not required for small mode.
+- They do not execute anything by themselves.
+- Any real subagent dispatch should copy the role's skill guidance explicitly into the dispatch request.
+- Any real subagent dispatch should be recorded in `.ai/run-trace.md`.
+- If the environment does not support subagents, the main Codex agent should follow the same role contracts sequentially.
+- Human review gates remain authoritative.
+
+Current role templates:
+
+- `planner.md`
+- `explorer.md`
+- `implementer.md`
+- `reviewer.md`
+- `evaluator.md`
diff --git a/.codex/agents/evaluator.md b/.codex/agents/evaluator.md
new file mode 100644
index 0000000..8738812
--- /dev/null
+++ b/.codex/agents/evaluator.md
@@ -0,0 +1,46 @@
+# Evaluator
+
+## Responsibility
+
+- inspect build, test, and check evidence
+- summarize verification, evaluation, context-pack, and handoff material
+- provide evidence for final review
+
+## Inputs
+
+- `scripts/ai_build.sh`
+- `scripts/ai_test.sh`
+- `scripts/ai_check.sh`
+- `.ai/verification.md`
+- `.ai/run-trace.md`
+- `.ai/context-pack.md`
+- `.ai/handoff.md`
+
+## Suggested Outputs
+
+- `.ai/evaluation.md`
+- `.ai/context-pack.md`
+- `.ai/handoff.md`
+- final verification summary
+
+## Skill Guidance
+
+Use when global skills are installed and available:
+
+- `methodology/verification-before-completion`
+- `system/performance-analysis`
+
+Recommended by risk:
+
+- `methodology/systematic-debugging` for failed or flaky checks
+- `methodology/context-engineering` for incomplete evidence
+- `methodology/code-review-and-quality` for final review evidence gaps
+- `system/cpp-linux-system-engineering` for C++ / Linux / backend / system validation
+
+Skills are globally installed advisory guidance. If skills are unavailable, follow this role contract plus `AGENTS.md` and `docs/ai/*` directly.
+
+## Prohibited
+
+- do not claim tests passed without evidence
+- do not delete failing evidence
+- do not skip known issues
diff --git a/.codex/agents/explorer.md b/.codex/agents/explorer.md
new file mode 100644
index 0000000..aa448bb
--- /dev/null
+++ b/.codex/agents/explorer.md
@@ -0,0 +1,45 @@
+# Explorer
+
+## Responsibility
+
+- read project structure, call chain, build/test entrypoints, and risk areas
+- produce evidence that supports later implementation and review
+- record affected files and uncertainty explicitly
+
+## Inputs
+
+- `docs/ai/*`
+- `git status`
+- `git diff`
+- `rg` / `git grep` results
+- build scripts
+- relevant source paths
+
+## Suggested Outputs
+
+- `.ai/affected-files.md`
+- `.ai/context-pack.md`
+- call chain notes
+- risk notes
+
+## Skill Guidance
+
+Use when global skills are installed and available:
+
+- `methodology/context-engineering`
+- `methodology/systematic-debugging`
+
+Recommended by risk:
+
+- `methodology/source-driven-development` for framework, library, or API investigation against official docs
+- `system/cpp-linux-system-engineering` for C++ / Linux / backend / system evidence
+- `system/performance-analysis` for performance-sensitive paths
+- `system/security-review` for trust boundaries, secrets, auth, or destructive operations
+
+Skills are globally installed advisory guidance. If skills are unavailable, follow this role contract plus `AGENTS.md` and `docs/ai/*` directly.
+
+## Prohibited
+
+- do not refactor
+- do not modify source code
+- do not invent call-chain details without evidence
diff --git a/.codex/agents/implementer.md b/.codex/agents/implementer.md
new file mode 100644
index 0000000..78a180b
--- /dev/null
+++ b/.codex/agents/implementer.md
@@ -0,0 +1,47 @@
+# Implementer
+
+## Responsibility
+
+- make small code changes inside the approved spec and implementation plan
+- follow C++ / Linux / backend / system constraints
+- record validation recommendations after the change
+
+## Inputs
+
+- `.ai/spec.md`
+- `.ai/implementation-plan.md`
+- `.ai/affected-files.md`
+- `docs/ai/cpp-system.md`
+- `docs/ai/api-abi.md`
+- `docs/ai/concurrency.md`
+
+## Suggested Outputs
+
+- code diff
+- updated tests
+- `.ai/verification.md`
+
+## Skill Guidance
+
+Use when global skills are installed and available:
+
+- `methodology/karpathy-guidelines`
+- `methodology/verification-before-completion`
+- `system/cpp-linux-system-engineering`
+
+Recommended by risk:
+
+- `methodology/test-driven-development` for behavior-changing code paths or bug fixes
+- `methodology/source-driven-development` for framework or library APIs that must be verified from official docs
+- `methodology/context-engineering` for unfamiliar code paths
+- `system/security-review` for auth, permissions, secrets, IPC, parsing, or network boundaries
+- `system/performance-analysis` for performance-sensitive code
+
+Skills are globally installed advisory guidance. If skills are unavailable, follow this role contract plus `AGENTS.md` and `docs/ai/*` directly.
+
+## Prohibited
+
+- do not cross the approved scope
+- do not do opportunistic refactors
+- do not modify unrelated files
+- do not skip verification guidance
diff --git a/.codex/agents/planner.md b/.codex/agents/planner.md
new file mode 100644
index 0000000..2ee9af3
--- /dev/null
+++ b/.codex/agents/planner.md
@@ -0,0 +1,46 @@
+# Planner
+
+## Responsibility
+
+- turn the user request into spec, scope, and task plan artifacts
+- identify goals, non-goals, risks, and validation approach
+- keep the task within approved scope
+
+## Inputs
+
+- `AGENTS.md`
+- `docs/ai/*`
+- `.ai/spec.md`
+- `.ai/scope.md`
+- `.ai/context-pack.md`
+- `.ai/handoff.md`
+
+## Suggested Outputs
+
+- `.ai/spec.md`
+- `.ai/scope.md`
+- `.ai/implementation-plan.md`
+
+## Skill Guidance
+
+Use when global skills are installed and available:
+
+- `methodology/task-contract-and-leveling`
+- `methodology/karpathy-guidelines`
+- `methodology/context-engineering`
+- `methodology/planning-and-task-breakdown`
+
+Recommended by risk:
+
+- `methodology/source-driven-development` for framework, library, or API-contract work that must follow official docs
+- `system/cpp-linux-system-engineering` for C++ / Linux / backend / system impact
+- `system/performance-analysis` for latency, throughput, or resource claims
+- `system/security-review` for auth, permissions, secrets, IPC, parsing, or network boundaries
+
+Skills are globally installed advisory guidance. If skills are unavailable, follow this role contract plus `AGENTS.md` and `docs/ai/*` directly.
+
+## Prohibited
+
+- do not implement code
+- do not expand scope without justification
+- do not auto-approve any human gate
diff --git a/.codex/agents/reviewer.md b/.codex/agents/reviewer.md
new file mode 100644
index 0000000..dcdbc86
--- /dev/null
+++ b/.codex/agents/reviewer.md
@@ -0,0 +1,44 @@
+# Reviewer
+
+## Responsibility
+
+- review diff, scope, risk, API/ABI impact, concurrency risk, performance risk, and test coverage
+- generate review conclusions and fix guidance
+- focus on correctness and regression risk, not just formatting
+
+## Inputs
+
+- `git diff`
+- `.ai/reviews/*`
+- `.ai/spec.md`
+- `.ai/implementation-plan.md`
+- `docs/ai/*`
+
+## Suggested Outputs
+
+- `.ai/reviews/diff-review.md`
+- risk list
+- fix recommendations
+
+## Skill Guidance
+
+Use when global skills are installed and available:
+
+- `methodology/code-review-and-quality`
+- `methodology/verification-before-completion`
+- `system/cpp-linux-system-engineering`
+
+Recommended by risk:
+
+- `methodology/source-driven-development` for framework/API correctness against official docs
+- `system/security-review` for trust boundaries, secrets, auth, or destructive operations
+- `system/performance-analysis` for performance claims
+- `methodology/systematic-debugging` for bug-fix diffs
+
+Skills are globally installed advisory guidance. If skills are unavailable, follow this role contract plus `AGENTS.md` and `docs/ai/*` directly.
+
+## Prohibited
+
+- do not replace human approval
+- do not auto-advance state
+- do not stop at superficial style review
diff --git a/.github/copilot-instructions.md b/.github/copilot-instructions.md
new file mode 100644
index 0000000..4d1cc73
--- /dev/null
+++ b/.github/copilot-instructions.md
@@ -0,0 +1,15 @@
+# Copilot Instructions
+
+Read `AGENTS.md` before making changes.
+
+Classify each non-trivial task as simple, medium, or complex:
+
+- simple: main agent handles directly with local verification
+- medium: use a short plan and consider scanner or reviewer roles
+- complex: use large-mode `.ai/*` artifacts and review gates
+
+Do not store project facts here.
+Project facts belong in `docs/ai/*`.
+Current task state belongs in `.ai/*`.
+
+If a relevant skill is available, use it as guidance, but do not bypass `AGENTS.md`, review gates, or explicit user constraints.
diff --git a/.gitignore b/.gitignore
new file mode 100644
index 0000000..331a775
--- /dev/null
+++ b/.gitignore
@@ -0,0 +1,27 @@
+# Python
+__pycache__/
+*.py[cod]
+.pytest_cache/
+.ruff_cache/
+.mypy_cache/
+.venv/
+venv/
+*.egg-info/
+
+# Local runtime data
+data/uploads/*
+!data/uploads/.gitkeep
+data/*.db
+*.sqlite
+*.sqlite3
+
+# Environment and secrets
+.env
+.env.*
+!.env.example
+
+# Editor and OS files
+.idea/
+.vscode/
+.DS_Store
+Thumbs.db
diff --git a/AGENTS.md b/AGENTS.md
new file mode 100644
index 0000000..c80d183
--- /dev/null
+++ b/AGENTS.md
@@ -0,0 +1,55 @@
+# AGENTS.md
+
+## Project Type
+
+This repository uses `Auto_AICoding_harness` base workflow.
+
+## Required Reading
+
+Read `docs/ai/README.md` first.
+
+For non-trivial tasks, also read the relevant `docs/ai/*` files for the area you are changing.
+Read `docs/ai/workflow.md` before driving a multi-step or resumed task.
+
+Always read active `.ai/` task files when they exist.
+
+## Workflow
+
+- Project override: after Phase 0, all development work in this repository must run under harness `large` mode.
+- Before starting implementation, run `ai-status` or `ai-doctor` and confirm `.ai/state.json` reports `"mode": "large"`.
+- Every development task must run the project verification scripts before completion. On Windows, run `scripts/ai_check.ps1` first; when shell tooling is available, also run `scripts/ai_check.sh` or document why it was not run.
+- Classify non-trivial tasks as simple, medium, or complex before editing.
+- `small`, `medium`, and `large` share one workflow model with different control strengths.
+- `small` is suitable for direct local work without full planning gates.
+- `medium` is suitable for bounded multi-file work that should keep plan, run trace, and verification artifacts current.
+- `large` is suitable for complex work that needs `spec`, `plan`, `diff`, and `final` gates.
+- If a simple task fails twice or the impact expands, escalate the execution level.
+- Apply `karpathy-guidelines` by default for planning, code changes, reviews, and refactors.
+- In every mode, run a short requirement clarification pass before implementation: restate the target, scope, constraints, and verification plan.
+- Unless the user explicitly says not to ask, do not silently choose between materially different implementations.
+- If ambiguity remains after that clarification pass, ask targeted clarification questions when direction, scope, acceptance criteria, or risk boundaries are ambiguous, but avoid performative questioning that would not change the work.
+
+## Harness Command Protocol
+
+- The agent must not claim a mode or gate change unless the corresponding harness command completed successfully.
+- Use `ai-status` or `ai-doctor` after meaningful workflow transitions when state evidence matters.
+- Read-only commands the agent may run without extra approval: `ai-status`, `ai-state`, `ai-doctor`.
+- Context commands the agent may run: `ai-context-pack`, `ai-handoff`.
+- Workflow commands the agent may run after explaining intent: `ai-review spec|plan|diff|final`.
+- Commands requiring explicit user approval: `ai-upgrade medium|large`, `ai-approve spec|plan|diff|final`, `ai-reject spec|plan|diff|final`.
+- The agent must never approve its own work unless the user explicitly says the review passed and asks for the approval command.
+
+## Knowledge Placement
+
+- `AGENTS.md` is the thin project entrypoint.
+- `docs/ai/*` stores durable project facts.
+- `.ai/*` stores current task runtime, state, plans, verification, reviews, approvals, and handoff artifacts.
+- Skills provide reusable methods when available, but they do not override this file.
+
+## Safety
+
+- do not overwrite existing files unless explicitly allowed
+- do not treat `.ai/` as long-lived architecture knowledge
+- do not bypass review gates or safe-write rules
+- do not refactor unrelated code opportunistically
+- do not describe a workflow transition as complete if `state.json` still says otherwise
diff --git a/CLAUDE.md b/CLAUDE.md
new file mode 100644
index 0000000..25d3741
--- /dev/null
+++ b/CLAUDE.md
@@ -0,0 +1,4 @@
+@AGENTS.md
+
+Claude-compatible shim.
+The repository-level source of truth is `AGENTS.md`.
diff --git a/README.md b/README.md
new file mode 100644
index 0000000..1c3f2bf
--- /dev/null
+++ b/README.md
@@ -0,0 +1,107 @@
+# Bid Knowledge Demo
+
+投标智能知识库能力验证版 Demo。
+
+当前仓库已进入 Phase 1：后端底座。Phase 1 只提供 FastAPI 启动、健康检查、文件上传、本地文件保存和 SQLite 元数据记录，不包含 OCR、RAG、LLM、知识卡片、前端 Demo 或导出能力。
+
+## Harness
+
+本仓库使用 `Auto_AICoding_Harness`，当前为 `large` mode，profile 为 `python-backend-service`。
+
+常用检查命令：
+
+```powershell
+$py = "C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
+& $py "C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status"
+& $py "C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor"
+```
+
+## Local Setup
+
+推荐使用 Codex bundled Python 或本地 Python 3.11+。
+
+```powershell
+$py = "C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
+& $py -m pip install -e ".[dev]"
+```
+
+## Run Backend
+
+```powershell
+$py = "C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
+& $py -m uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
+```
+
+Health check:
+
+```powershell
+curl.exe --noproxy "*" http://127.0.0.1:8000/health
+```
+
+Upload smoke:
+
+```powershell
+Set-Content -Path .\data\samples\phase1-smoke.txt -Value "hello bid knowledge"
+curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/files/upload" `
+  -F "doc_role=historical_bid" `
+  -F "file=@.\data\samples\phase1-smoke.txt"
+```
+
+## Test
+
+```powershell
+$py = "C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
+& $py -m compileall backend/app
+& $py -m pytest backend/tests
+.\scripts\ai_check.ps1
+```
+
+If a shell environment is available:
+
+```powershell
+bash ./scripts/ai_check.sh
+```
+
+On Windows machines without WSL or bash, use `scripts/ai_check.ps1` as the primary project check and record the bash limitation in `.ai/verification.md`.
+
+## Phase 1 API
+
+- `GET /health`
+- `POST /api/files/upload`
+
+Upload request:
+
+- `multipart/form-data`
+- `file`: `.txt`, `.pdf`, `.doc`, or `.docx`
+- `doc_role`: `historical_bid` or `tender`
+
+Successful uploads return HTTP `201 Created` with:
+
+- `document_id`
+- `original_filename`
+- `doc_role`
+- `parse_status`
+- `file_size`
+- `created_at`
+
+Error responses use:
+
+- `error_code`
+- `message`
+- `details`
+
+## Source Documents
+
+- [PRD PDF](docs/source-materials/originals/投标智能知识库能力验证版-PRD-v0.1.pdf)
+- [Deep research report](docs/source-materials/originals/deep-research-report.md)
+- `C:\Users\26561\Desktop\模型训练资料\甲方提供资料`
+
+See [source material index](docs/source-materials/README.md) and [sample catalog](docs/source-materials/sample-catalog.md).
+
+External reference repositories are kept outside Git under `F:\BidKonwledge_refs`; see [reference-repos.md](docs/source-materials/reference-repos.md).
+
+## Boundary
+
+This is not a complete bidding system. Phase 1 is only the backend foundation for later document parsing and knowledge-base capability.
+
+All generated bidding content in future phases must require human review.
diff --git a/backend/__init__.py b/backend/__init__.py
new file mode 100644
index 0000000..76caeb3
--- /dev/null
+++ b/backend/__init__.py
@@ -0,0 +1 @@
+"""Backend package root."""
diff --git a/backend/app/.gitkeep b/backend/app/.gitkeep
new file mode 100644
index 0000000..8b13789
--- /dev/null
+++ b/backend/app/.gitkeep
@@ -0,0 +1 @@
+
diff --git a/backend/app/__init__.py b/backend/app/__init__.py
new file mode 100644
index 0000000..8641a32
--- /dev/null
+++ b/backend/app/__init__.py
@@ -0,0 +1 @@
+"""BidKnowledge Phase 1 backend package."""
diff --git a/backend/app/api/__init__.py b/backend/app/api/__init__.py
new file mode 100644
index 0000000..e68e861
--- /dev/null
+++ b/backend/app/api/__init__.py
@@ -0,0 +1 @@
+"""API routers for Phase 1."""
diff --git a/backend/app/api/files.py b/backend/app/api/files.py
new file mode 100644
index 0000000..6373b88
--- /dev/null
+++ b/backend/app/api/files.py
@@ -0,0 +1,136 @@
+from __future__ import annotations
+
+import logging
+from datetime import UTC, datetime
+from pathlib import Path
+from uuid import uuid4
+
+from fastapi import APIRouter, Depends, File, Form, UploadFile
+from fastapi.responses import JSONResponse
+
+from backend.app.config import Settings, get_settings
+from backend.app.schemas.document import DocumentRecord, DocumentUploadResponse
+from backend.app.storage import database, file_storage
+
+router = APIRouter(prefix="/api/files")
+logger = logging.getLogger(__name__)
+
+ALLOWED_DOC_ROLES = {"historical_bid", "tender"}
+
+
+def error_response(
+    status_code: int,
+    error_code: str,
+    message: str,
+    details: dict[str, object] | None = None,
+) -> JSONResponse:
+    return JSONResponse(
+        status_code=status_code,
+        content={
+            "error_code": error_code,
+            "message": message,
+            "details": details or {},
+        },
+    )
+
+
+@router.post(
+    "/upload",
+    status_code=201,
+    response_model=DocumentUploadResponse,
+    responses={
+        400: {"description": "Upload validation error"},
+        413: {"description": "Upload exceeds configured size limit"},
+        500: {"description": "Upload persistence error"},
+    },
+)
+async def upload_file(
+    file: UploadFile | None = File(default=None),
+    doc_role: str | None = Form(default=None),
+    settings: Settings = Depends(get_settings),
+) -> DocumentUploadResponse | JSONResponse:
+    if file is None:
+        return error_response(400, "MISSING_FILE", "Uploaded file is required")
+    if doc_role is None:
+        return error_response(400, "MISSING_DOC_ROLE", "Document role is required")
+    if doc_role not in ALLOWED_DOC_ROLES:
+        return error_response(
+            400,
+            "INVALID_DOC_ROLE",
+            "Unsupported document role",
+            {"allowed": sorted(ALLOWED_DOC_ROLES)},
+        )
+
+    original_filename = file.filename or ""
+    if file_storage.is_unsafe_filename(original_filename):
+        return error_response(400, "UNSAFE_FILENAME", "Unsafe filename")
+
+    file_ext = file_storage.normalized_extension(original_filename)
+    if file_ext not in settings.allowed_extensions:
+        return error_response(
+            400,
+            "UNSUPPORTED_FILE_TYPE",
+            "Unsupported file extension",
+            {"allowed": list(settings.allowed_extensions)},
+        )
+
+    content = await file.read()
+    if len(content) == 0:
+        return error_response(400, "EMPTY_FILE", "Uploaded file is empty")
+    if len(content) > settings.max_upload_bytes:
+        return error_response(
+            413,
+            "FILE_TOO_LARGE",
+            "Uploaded file exceeds the configured size limit",
+            {"max_upload_bytes": settings.max_upload_bytes},
+        )
+
+    document_id = uuid4().hex
+    generated_filename = file_storage.stored_filename(document_id, file_ext)
+
+    try:
+        stored_path = file_storage.write_uploaded_bytes(
+            settings, generated_filename, content
+        )
+    except OSError:
+        logger.exception("Failed to write uploaded file")
+        return error_response(500, "FILE_WRITE_FAILED", "Failed to store uploaded file")
+
+    created_at = datetime.now(UTC).isoformat().replace("+00:00", "Z")
+    record = DocumentRecord(
+        id=document_id,
+        original_filename=original_filename,
+        stored_filename=generated_filename,
+        stored_path=file_storage.relative_stored_path(settings, stored_path),
+        file_ext=file_ext,
+        content_type=file.content_type,
+        file_size=len(content),
+        doc_role=doc_role,
+        created_at=created_at,
+        updated_at=created_at,
+        parse_status="pending",
+        error_message=None,
+    )
+
+    try:
+        database.insert_document(settings, record)
+    except Exception:
+        try:
+            Path(stored_path).unlink(missing_ok=True)
+        except OSError:
+            logger.exception("Failed to clean up stored file after metadata failure")
+        logger.exception("Failed to insert document metadata")
+        return error_response(
+            500,
+            "METADATA_WRITE_FAILED",
+            "Failed to persist document metadata",
+        )
+
+    return DocumentUploadResponse(
+        document_id=document_id,
+        original_filename=original_filename,
+        doc_role=doc_role,
+        parse_status="pending",
+        file_size=len(content),
+        created_at=created_at,
+    )
diff --git a/backend/app/api/health.py b/backend/app/api/health.py
new file mode 100644
index 0000000..795c588
--- /dev/null
+++ b/backend/app/api/health.py
@@ -0,0 +1,10 @@
+from __future__ import annotations
+
+from fastapi import APIRouter
+
+router = APIRouter()
+
+
+@router.get("/health")
+def health() -> dict[str, str]:
+    return {"status": "ok"}
diff --git a/backend/app/config.py b/backend/app/config.py
new file mode 100644
index 0000000..089ed14
--- /dev/null
+++ b/backend/app/config.py
@@ -0,0 +1,45 @@
+from __future__ import annotations
+
+import os
+from dataclasses import dataclass
+from functools import lru_cache
+from pathlib import Path
+
+
+DEFAULT_MAX_UPLOAD_BYTES = 10 * 1024 * 1024
+DEFAULT_ALLOWED_EXTENSIONS = (".txt", ".pdf", ".doc", ".docx")
+
+
+def _repo_root() -> Path:
+    return Path(__file__).resolve().parents[2]
+
+
+@dataclass(frozen=True)
+class Settings:
+    upload_root: Path
+    database_path: Path
+    max_upload_bytes: int = DEFAULT_MAX_UPLOAD_BYTES
+    allowed_extensions: tuple[str, ...] = DEFAULT_ALLOWED_EXTENSIONS
+
+    @classmethod
+    def from_env(cls) -> "Settings":
+        root = _repo_root()
+        upload_root = Path(
+            os.getenv("BIDKNOWLEDGE_UPLOAD_ROOT", str(root / "data" / "uploads"))
+        )
+        database_path = Path(
+            os.getenv("BIDKNOWLEDGE_DB_PATH", str(root / "data" / "app.sqlite3"))
+        )
+        max_upload_bytes = int(
+            os.getenv("BIDKNOWLEDGE_MAX_UPLOAD_BYTES", str(DEFAULT_MAX_UPLOAD_BYTES))
+        )
+        return cls(
+            upload_root=upload_root,
+            database_path=database_path,
+            max_upload_bytes=max_upload_bytes,
+        )
+
+
+@lru_cache(maxsize=1)
+def get_settings() -> Settings:
+    return Settings.from_env()
diff --git a/backend/app/main.py b/backend/app/main.py
new file mode 100644
index 0000000..9393344
--- /dev/null
+++ b/backend/app/main.py
@@ -0,0 +1,15 @@
+from __future__ import annotations
+
+from fastapi import FastAPI
+
+from backend.app.api import files, health
+
+
+def create_app() -> FastAPI:
+    app = FastAPI(title="BidKnowledge Phase 1 Backend")
+    app.include_router(health.router)
+    app.include_router(files.router)
+    return app
+
+
+app = create_app()
diff --git a/backend/app/schemas/__init__.py b/backend/app/schemas/__init__.py
new file mode 100644
index 0000000..7dc0c8d
--- /dev/null
+++ b/backend/app/schemas/__init__.py
@@ -0,0 +1 @@
+"""Response schemas for Phase 1 APIs."""
diff --git a/backend/app/schemas/document.py b/backend/app/schemas/document.py
new file mode 100644
index 0000000..116ba74
--- /dev/null
+++ b/backend/app/schemas/document.py
@@ -0,0 +1,35 @@
+from __future__ import annotations
+
+from pydantic import BaseModel, ConfigDict
+
+
+class DocumentUploadResponse(BaseModel):
+    document_id: str
+    original_filename: str
+    doc_role: str
+    parse_status: str
+    file_size: int
+    created_at: str
+
+
+class ErrorResponse(BaseModel):
+    error_code: str
+    message: str
+    details: dict[str, object]
+
+
+class DocumentRecord(BaseModel):
+    model_config = ConfigDict(from_attributes=True)
+
+    id: str
+    original_filename: str
+    stored_filename: str
+    stored_path: str
+    file_ext: str
+    content_type: str | None
+    file_size: int
+    doc_role: str
+    created_at: str
+    updated_at: str
+    parse_status: str
+    error_message: str | None = None
diff --git a/backend/app/storage/__init__.py b/backend/app/storage/__init__.py
new file mode 100644
index 0000000..bcb9a13
--- /dev/null
+++ b/backend/app/storage/__init__.py
@@ -0,0 +1 @@
+"""Storage helpers for local files and SQLite metadata."""
diff --git a/backend/app/storage/database.py b/backend/app/storage/database.py
new file mode 100644
index 0000000..58879b8
--- /dev/null
+++ b/backend/app/storage/database.py
@@ -0,0 +1,96 @@
+from __future__ import annotations
+
+import sqlite3
+from pathlib import Path
+from typing import Any
+
+from backend.app.config import Settings
+from backend.app.schemas.document import DocumentRecord
+
+
+CREATE_DOCUMENTS_SQL = """
+CREATE TABLE IF NOT EXISTS documents (
+    id TEXT PRIMARY KEY,
+    original_filename TEXT NOT NULL,
+    stored_filename TEXT NOT NULL,
+    stored_path TEXT NOT NULL,
+    file_ext TEXT NOT NULL,
+    content_type TEXT,
+    file_size INTEGER NOT NULL,
+    doc_role TEXT NOT NULL,
+    created_at TEXT NOT NULL,
+    updated_at TEXT NOT NULL,
+    parse_status TEXT NOT NULL DEFAULT 'pending',
+    error_message TEXT
+)
+"""
+
+
+def connect(database_path: Path) -> sqlite3.Connection:
+    database_path.parent.mkdir(parents=True, exist_ok=True)
+    connection = sqlite3.connect(database_path)
+    connection.row_factory = sqlite3.Row
+    return connection
+
+
+def init_database(settings: Settings) -> None:
+    with connect(settings.database_path) as connection:
+        connection.execute(CREATE_DOCUMENTS_SQL)
+        connection.commit()
+
+
+def insert_document(settings: Settings, record: DocumentRecord) -> None:
+    init_database(settings)
+    values: dict[str, Any] = record.model_dump()
+    with connect(settings.database_path) as connection:
+        connection.execute(
+            """
+            INSERT INTO documents (
+                id,
+                original_filename,
+                stored_filename,
+                stored_path,
+                file_ext,
+                content_type,
+                file_size,
+                doc_role,
+                created_at,
+                updated_at,
+                parse_status,
+                error_message
+            ) VALUES (
+                :id,
+                :original_filename,
+                :stored_filename,
+                :stored_path,
+                :file_ext,
+                :content_type,
+                :file_size,
+                :doc_role,
+                :created_at,
+                :updated_at,
+                :parse_status,
+                :error_message
+            )
+            """,
+            values,
+        )
+        connection.commit()
+
+
+def get_document(settings: Settings, document_id: str) -> DocumentRecord | None:
+    init_database(settings)
+    with connect(settings.database_path) as connection:
+        row = connection.execute(
+            "SELECT * FROM documents WHERE id = ?", (document_id,)
+        ).fetchone()
+    if row is None:
+        return None
+    return DocumentRecord(**dict(row))
+
+
+def count_documents(settings: Settings) -> int:
+    init_database(settings)
+    with connect(settings.database_path) as connection:
+        row = connection.execute("SELECT COUNT(*) AS count FROM documents").fetchone()
+    return int(row["count"])
diff --git a/backend/app/storage/file_storage.py b/backend/app/storage/file_storage.py
new file mode 100644
index 0000000..6e3a968
--- /dev/null
+++ b/backend/app/storage/file_storage.py
@@ -0,0 +1,42 @@
+from __future__ import annotations
+
+from pathlib import Path, PurePosixPath, PureWindowsPath
+
+from backend.app.config import Settings
+
+
+def normalized_extension(filename: str) -> str:
+    return Path(filename).suffix.lower()
+
+
+def is_unsafe_filename(filename: str) -> bool:
+    if not filename or filename in {".", ".."}:
+        return True
+    posix_parts = PurePosixPath(filename).parts
+    windows_parts = PureWindowsPath(filename).parts
+    if len(posix_parts) > 1 or len(windows_parts) > 1:
+        return True
+    return ".." in posix_parts or ".." in windows_parts
+
+
+def stored_filename(document_id: str, file_ext: str) -> str:
+    return f"{document_id}{file_ext}"
+
+
+def resolve_upload_path(settings: Settings, filename: str) -> Path:
+    upload_root = settings.upload_root.resolve()
+    target = (upload_root / filename).resolve()
+    if upload_root != target and upload_root not in target.parents:
+        raise ValueError("stored path escapes upload root")
+    return target
+
+
+def write_uploaded_bytes(settings: Settings, filename: str, content: bytes) -> Path:
+    target = resolve_upload_path(settings, filename)
+    target.parent.mkdir(parents=True, exist_ok=True)
+    target.write_bytes(content)
+    return target
+
+
+def relative_stored_path(settings: Settings, path: Path) -> str:
+    return path.resolve().relative_to(settings.upload_root.resolve()).as_posix()
diff --git a/backend/tests/.gitkeep b/backend/tests/.gitkeep
new file mode 100644
index 0000000..8b13789
--- /dev/null
+++ b/backend/tests/.gitkeep
@@ -0,0 +1 @@
+
diff --git a/backend/tests/conftest.py b/backend/tests/conftest.py
new file mode 100644
index 0000000..e9570eb
--- /dev/null
+++ b/backend/tests/conftest.py
@@ -0,0 +1,52 @@
+from __future__ import annotations
+
+import sqlite3
+from pathlib import Path
+from typing import Iterator
+
+import pytest
+from fastapi.testclient import TestClient
+
+from backend.app.config import Settings, get_settings
+from backend.app.main import app
+
+
+@pytest.fixture
+def test_settings(tmp_path: Path) -> Settings:
+    return Settings(
+        upload_root=tmp_path / "uploads",
+        database_path=tmp_path / "app.sqlite3",
+        max_upload_bytes=1024,
+    )
+
+
+@pytest.fixture
+def client(test_settings: Settings) -> Iterator[TestClient]:
+    app.dependency_overrides[get_settings] = lambda: test_settings
+    with TestClient(app) as test_client:
+        yield test_client
+    app.dependency_overrides.clear()
+
+
+def upload(
+    client: TestClient,
+    filename: str = "sample.txt",
+    content: bytes = b"hello bid knowledge",
+    doc_role: str = "historical_bid",
+):
+    return client.post(
+        "/api/files/upload",
+        data={"doc_role": doc_role},
+        files={"file": (filename, content, "text/plain")},
+    )
+
+
+def document_rows(settings: Settings) -> list[sqlite3.Row]:
+    if not settings.database_path.exists():
+        return []
+    connection = sqlite3.connect(settings.database_path)
+    connection.row_factory = sqlite3.Row
+    try:
+        return list(connection.execute("SELECT * FROM documents ORDER BY created_at"))
+    finally:
+        connection.close()
diff --git a/backend/tests/test_database.py b/backend/tests/test_database.py
new file mode 100644
index 0000000..a190800
--- /dev/null
+++ b/backend/tests/test_database.py
@@ -0,0 +1,91 @@
+from __future__ import annotations
+
+import sqlite3
+
+from backend.tests.conftest import document_rows, upload
+
+
+REQUIRED_COLUMNS = {
+    "id",
+    "original_filename",
+    "stored_filename",
+    "stored_path",
+    "file_ext",
+    "content_type",
+    "file_size",
+    "doc_role",
+    "created_at",
+    "updated_at",
+    "parse_status",
+    "error_message",
+}
+
+
+def test_database_initializes_and_documents_table_exists(client, test_settings):
+    response = upload(client)
+
+    assert response.status_code == 201
+    assert test_settings.database_path.exists()
+    connection = sqlite3.connect(test_settings.database_path)
+    try:
+        rows = connection.execute("PRAGMA table_info(documents)").fetchall()
+    finally:
+        connection.close()
+    assert {row[1] for row in rows} == REQUIRED_COLUMNS
+
+
+def test_valid_upload_inserts_one_metadata_row(client, test_settings):
+    response = upload(client)
+
+    assert response.status_code == 201
+    assert len(document_rows(test_settings)) == 1
+
+
+def test_metadata_row_stores_required_fields(client, test_settings):
+    response = upload(client, filename="sample.txt", content=b"hello")
+
+    assert response.status_code == 201
+    row = document_rows(test_settings)[0]
+    assert set(row.keys()) == REQUIRED_COLUMNS
+    assert row["id"] == response.json()["document_id"]
+    assert row["original_filename"] == "sample.txt"
+    assert row["stored_path"] == row["stored_filename"]
+    assert row["file_ext"] == ".txt"
+    assert row["file_size"] == 5
+    assert row["doc_role"] == "historical_bid"
+    assert row["created_at"]
+    assert row["updated_at"]
+
+
+def test_nullable_metadata_defaults_are_safe(client, test_settings):
+    response = upload(client)
+
+    assert response.status_code == 201
+    row = document_rows(test_settings)[0]
+    assert row["content_type"] == "text/plain"
+    assert row["error_message"] is None
+
+
+def test_parse_status_remains_pending(client, test_settings):
+    response = upload(client)
+
+    assert response.status_code == 201
+    assert document_rows(test_settings)[0]["parse_status"] == "pending"
+
+
+def test_failed_upload_does_not_insert_metadata_row(client, test_settings):
+    response = upload(client, filename="payload.exe")
+
+    assert response.status_code == 400
+    assert document_rows(test_settings) == []
+
+
+def test_multiple_uploads_create_multiple_rows(client, test_settings):
+    first = upload(client, filename="one.txt", content=b"one")
+    second = upload(client, filename="two.txt", content=b"two")
+
+    assert first.status_code == 201
+    assert second.status_code == 201
+    rows = document_rows(test_settings)
+    assert len(rows) == 2
+    assert len({row["id"] for row in rows}) == 2
diff --git a/backend/tests/test_health.py b/backend/tests/test_health.py
new file mode 100644
index 0000000..5dca02e
--- /dev/null
+++ b/backend/tests/test_health.py
@@ -0,0 +1,21 @@
+from __future__ import annotations
+
+
+def test_health_returns_stable_shallow_status(client):
+    response = client.get("/health")
+
+    assert response.status_code == 200
+    assert response.json() == {"status": "ok"}
+
+
+def test_health_does_not_create_database(client, test_settings):
+    response = client.get("/health")
+
+    assert response.status_code == 200
+    assert not test_settings.database_path.exists()
+
+
+def test_health_content_type_is_json(client):
+    response = client.get("/health")
+
+    assert "application/json" in response.headers["content-type"]
diff --git a/backend/tests/test_phase1_boundaries.py b/backend/tests/test_phase1_boundaries.py
new file mode 100644
index 0000000..01f3d79
--- /dev/null
+++ b/backend/tests/test_phase1_boundaries.py
@@ -0,0 +1,34 @@
+from __future__ import annotations
+
+from backend.tests.conftest import document_rows, upload
+
+
+def test_phase1_does_not_require_vector_service(client, monkeypatch):
+    monkeypatch.setenv("QDRANT_URL", "")
+
+    response = upload(client)
+
+    assert response.status_code == 201
+
+
+def test_phase1_does_not_require_llm_credentials(client, monkeypatch):
+    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
+
+    response = upload(client)
+
+    assert response.status_code == 201
+
+
+def test_phase1_upload_does_not_parse_documents(client, test_settings):
+    response = upload(client)
+
+    assert response.status_code == 201
+    row = document_rows(test_settings)[0]
+    assert row["parse_status"] == "pending"
+    assert row["error_message"] is None
+
+
+def test_non_phase1_routes_are_not_exposed_as_complete_features(client):
+    response = client.get("/api/knowledge-cards")
+
+    assert response.status_code == 404
diff --git a/backend/tests/test_storage.py b/backend/tests/test_storage.py
new file mode 100644
index 0000000..53733bb
--- /dev/null
+++ b/backend/tests/test_storage.py
@@ -0,0 +1,93 @@
+from __future__ import annotations
+
+from backend.tests.conftest import document_rows, upload
+
+
+def test_file_write_failure_does_not_insert_metadata(client, test_settings, monkeypatch):
+    def fail_write(*args, **kwargs):
+        raise OSError("forced write failure")
+
+    monkeypatch.setattr(
+        "backend.app.api.files.file_storage.write_uploaded_bytes", fail_write
+    )
+
+    response = upload(client)
+
+    assert response.status_code == 500
+    assert response.json()["error_code"] == "FILE_WRITE_FAILED"
+    assert document_rows(test_settings) == []
+    assert not test_settings.upload_root.exists() or not any(test_settings.upload_root.iterdir())
+
+
+def test_metadata_write_failure_cleans_up_stored_file(client, test_settings, monkeypatch):
+    def fail_insert(*args, **kwargs):
+        raise OSError("forced metadata failure")
+
+    monkeypatch.setattr("backend.app.api.files.database.insert_document", fail_insert)
+
+    response = upload(client)
+
+    assert response.status_code == 500
+    assert response.json()["error_code"] == "METADATA_WRITE_FAILED"
+    assert document_rows(test_settings) == []
+    assert not test_settings.upload_root.exists() or not any(test_settings.upload_root.iterdir())
+
+
+def test_upload_directory_is_created(client, test_settings):
+    assert not test_settings.upload_root.exists()
+
+    response = upload(client)
+
+    assert response.status_code == 201
+    assert test_settings.upload_root.exists()
+
+
+def test_stored_file_bytes_match_upload(client, test_settings):
+    content = b"stored bytes"
+
+    response = upload(client, content=content)
+
+    assert response.status_code == 201
+    files = list(test_settings.upload_root.iterdir())
+    assert len(files) == 1
+    assert files[0].read_bytes() == content
+
+
+def test_stored_file_remains_under_upload_root(client, test_settings):
+    response = upload(client)
+
+    assert response.status_code == 201
+    stored_file = next(test_settings.upload_root.iterdir()).resolve()
+    upload_root = test_settings.upload_root.resolve()
+    assert upload_root == stored_file.parent
+
+
+def test_stored_filename_is_backend_generated(client, test_settings):
+    response = upload(client, filename="raw-name.txt")
+
+    assert response.status_code == 201
+    row = document_rows(test_settings)[0]
+    assert row["stored_filename"] != "raw-name.txt"
+    assert row["stored_filename"].endswith(".txt")
+    assert row["id"] in row["stored_filename"]
+
+
+def test_duplicate_original_filenames_do_not_overwrite(client, test_settings):
+    first = upload(client, filename="same.txt", content=b"first")
+    second = upload(client, filename="same.txt", content=b"second")
+
+    assert first.status_code == 201
+    assert second.status_code == 201
+    rows = document_rows(test_settings)
+    assert len(rows) == 2
+    stored_names = {row["stored_filename"] for row in rows}
+    assert len(stored_names) == 2
+    stored_bytes = sorted(path.read_bytes() for path in test_settings.upload_root.iterdir())
+    assert stored_bytes == [b"first", b"second"]
+
+
+def test_failed_validation_leaves_no_orphan_file(client, test_settings):
+    response = upload(client, filename="payload.exe")
+
+    assert response.status_code == 400
+    assert not test_settings.upload_root.exists() or not any(test_settings.upload_root.iterdir())
diff --git a/backend/tests/test_upload_contract.py b/backend/tests/test_upload_contract.py
new file mode 100644
index 0000000..a165d43
--- /dev/null
+++ b/backend/tests/test_upload_contract.py
@@ -0,0 +1,59 @@
+from __future__ import annotations
+
+from backend.tests.conftest import upload
+
+
+SUCCESS_FIELDS = {
+    "document_id",
+    "original_filename",
+    "doc_role",
+    "parse_status",
+    "file_size",
+    "created_at",
+}
+
+
+def test_upload_accepts_historical_bid(client):
+    response = upload(client, doc_role="historical_bid")
+
+    assert response.status_code == 201
+    body = response.json()
+    assert set(body) == SUCCESS_FIELDS
+    assert body["doc_role"] == "historical_bid"
+    assert body["original_filename"] == "sample.txt"
+
+
+def test_upload_accepts_tender(client):
+    response = upload(client, filename="tender.txt", doc_role="tender")
+
+    assert response.status_code == 201
+    assert response.json()["doc_role"] == "tender"
+
+
+def test_upload_response_has_required_fields(client):
+    response = upload(client)
+
+    assert response.status_code == 201
+    assert set(response.json()) == SUCCESS_FIELDS
+
+
+def test_upload_response_parse_status_is_pending(client):
+    response = upload(client)
+
+    assert response.json()["parse_status"] == "pending"
+
+
+def test_upload_response_does_not_expose_absolute_paths(client, test_settings):
+    response = upload(client)
+
+    body = response.json()
+    serialized_values = " ".join(str(value) for value in body.values())
+    assert str(test_settings.upload_root) not in serialized_values
+    assert ":\\" not in serialized_values
+
+
+def test_upload_preserves_unicode_original_filename(client):
+    response = upload(client, filename="投标 测试 文件.txt")
+
+    assert response.status_code == 201
+    assert response.json()["original_filename"] == "投标 测试 文件.txt"
diff --git a/backend/tests/test_upload_validation.py b/backend/tests/test_upload_validation.py
new file mode 100644
index 0000000..cda19e9
--- /dev/null
+++ b/backend/tests/test_upload_validation.py
@@ -0,0 +1,92 @@
+from __future__ import annotations
+
+from backend.tests.conftest import document_rows, upload
+
+
+def assert_error_shape(response, code: str):
+    body = response.json()
+    assert set(body) == {"error_code", "message", "details"}
+    assert body["error_code"] == code
+    assert isinstance(body["message"], str)
+    assert isinstance(body["details"], dict)
+
+
+def assert_no_persistence(settings):
+    assert not settings.upload_root.exists() or not any(settings.upload_root.iterdir())
+    assert document_rows(settings) == []
+
+
+def test_missing_file_is_rejected(client, test_settings):
+    response = client.post(
+        "/api/files/upload",
+        data={"doc_role": "historical_bid"},
+    )
+
+    assert response.status_code == 400
+    assert_error_shape(response, "MISSING_FILE")
+    assert_no_persistence(test_settings)
+
+
+def test_missing_doc_role_is_rejected(client, test_settings):
+    response = client.post(
+        "/api/files/upload",
+        files={"file": ("sample.txt", b"hello", "text/plain")},
+    )
+
+    assert response.status_code == 400
+    assert_error_shape(response, "MISSING_DOC_ROLE")
+    assert_no_persistence(test_settings)
+
+
+def test_invalid_doc_role_is_rejected(client, test_settings):
+    response = upload(client, doc_role="unknown")
+
+    assert response.status_code == 400
+    assert_error_shape(response, "INVALID_DOC_ROLE")
+    assert_no_persistence(test_settings)
+
+
+def test_empty_file_is_rejected(client, test_settings):
+    response = upload(client, content=b"")
+
+    assert response.status_code == 400
+    assert_error_shape(response, "EMPTY_FILE")
+    assert_no_persistence(test_settings)
+
+
+def test_unsafe_filename_is_rejected(client, test_settings):
+    response = upload(client, filename="../evil.txt")
+
+    assert response.status_code == 400
+    assert_error_shape(response, "UNSAFE_FILENAME")
+    assert_no_persistence(test_settings)
+
+
+def test_windows_unsafe_filename_is_rejected(client, test_settings):
+    response = upload(client, filename="..\\evil.txt")
+
+    assert response.status_code == 400
+    assert_error_shape(response, "UNSAFE_FILENAME")
+    assert_no_persistence(test_settings)
+
+
+def test_unsupported_extension_is_rejected(client, test_settings):
+    response = upload(client, filename="payload.exe")
+
+    assert response.status_code == 400
+    assert_error_shape(response, "UNSUPPORTED_FILE_TYPE")
+    assert_no_persistence(test_settings)
+
+
+def test_oversized_upload_is_rejected(client, test_settings):
+    response = upload(client, content=b"x" * (test_settings.max_upload_bytes + 1))
+
+    assert response.status_code == 413
+    assert_error_shape(response, "FILE_TOO_LARGE")
+    assert_no_persistence(test_settings)
+
+
+def test_uppercase_extension_is_normalized(client):
+    response = upload(client, filename="SAMPLE.TXT")
+
+    assert response.status_code == 201
diff --git a/data/samples/.gitkeep b/data/samples/.gitkeep
new file mode 100644
index 0000000..8b13789
--- /dev/null
+++ b/data/samples/.gitkeep
@@ -0,0 +1 @@
+
diff --git a/data/uploads/.gitkeep b/data/uploads/.gitkeep
new file mode 100644
index 0000000..8b13789
--- /dev/null
+++ b/data/uploads/.gitkeep
@@ -0,0 +1 @@
+
diff --git a/docs/ai/00-project-brief.md b/docs/ai/00-project-brief.md
new file mode 100644
index 0000000..0b000ad
--- /dev/null
+++ b/docs/ai/00-project-brief.md
@@ -0,0 +1,65 @@
+# Project Brief - 投标智能知识库 Demo
+
+## Project One-Liner
+
+This project is a lightweight "投标智能知识库能力验证 Demo" used to validate the core AI knowledge-base chain:
+
+historical bid file ingestion -> document parsing -> section and tag splitting -> tender parsing -> knowledge retrieval -> LLM candidate content generation -> source citation -> risk hints.
+
+## Current Phase
+
+The current phase is 0 阶段初始化.
+
+This phase initializes the repository, records durable AI context, and prepares implementation plans. It does not build business features.
+
+## Demo Goal
+
+The MVP should demonstrate:
+
+1. Upload historical bid files.
+2. Parse doc, docx, and pdf directory text, body text, and tables.
+3. Split content into sections and tagged knowledge cards.
+4. Upload a new tender file.
+5. Extract project requirements, scoring items, and disqualification risks.
+6. Retrieve historical knowledge cards by target tag and query.
+7. Call an external LLM API to generate candidate content.
+8. Return generated content, source citations, risk hints, and human review markers.
+9. Show the result and raw JSON in a minimal demo page.
+
+## Delivery Shape
+
+The validation demo should eventually include:
+
+1. A minimal demo page.
+2. A backend knowledge-base service.
+3. A small sample-file dataset.
+4. Simplified API documentation.
+5. Sample JSON output.
+6. Demo verification notes.
+
+## Technology Direction
+
+Default technical direction:
+
+- Python 3.11+
+- FastAPI
+- Pydantic
+- SQLite for MVP metadata
+- Local file storage for uploaded samples
+- Pluggable document parser
+- Pluggable OCR adapter
+- Pluggable embedding provider
+- Pluggable vector store
+- Pluggable OpenAI-compatible LLM adapter
+- Minimal frontend only for demo display
+
+The research report recommends Haystack + Docling + PaddleOCR + Qdrant as the later practical stack, with RAGFlow as a product reference rather than the initial codebase.
+
+## Priority
+
+First run a vertical slice. Do not chase a complete bidding platform.
+
+Phase 1 should only establish the smallest backend foundation:
+
+upload -> local storage -> document metadata -> SQLite initialization -> health check -> smoke test.
+
diff --git a/docs/ai/01-scope-boundary.md b/docs/ai/01-scope-boundary.md
new file mode 100644
index 0000000..5d9b9f6
--- /dev/null
+++ b/docs/ai/01-scope-boundary.md
@@ -0,0 +1,84 @@
+# Scope Boundary
+
+## In Scope For Capability Demo
+
+The lightweight demo is responsible for:
+
+1. File upload.
+2. Historical bid file parsing.
+3. Tender file parsing.
+4. Section splitting.
+5. Initial tag recognition.
+6. Knowledge card generation.
+7. Vector indexing.
+8. Tag plus semantic retrieval.
+9. Calling an external LLM to generate candidate content.
+10. Returning source citations.
+11. Returning risk hints.
+12. Returning structured JSON.
+13. Providing a minimal demo page.
+
+## Out Of Scope
+
+The current validation demo must not become:
+
+1. A complete bidding system.
+2. A formal frontend system.
+3. A Word or PDF layout/export system.
+4. A cover, table-of-contents, header, footer, logo, or document-formatting engine.
+5. An automatic quotation-file generator.
+6. An automatic qualification-material generator.
+7. A CA signing, bid bond, social security, tax certificate, software copyright, or vendor authorization workflow.
+8. A user login or permission system.
+9. A project management system.
+10. A complete file management system.
+11. A formal human review workflow.
+12. A guarantee that AI output can be used directly for final bidding.
+
+## Phase 0 Scope
+
+Phase 0 only initializes the repository and AI context:
+
+1. Initialize the empty folder as a Git repository.
+2. Copy the Auto_AICoding_Harness baseline workflow files.
+3. Write durable project context under `docs/ai/`.
+4. Generate current task files under `.ai/`.
+
+## Phase 1 Scope
+
+Phase 1 should implement only:
+
+1. FastAPI application startup.
+2. `GET /health`.
+3. `POST /api/files/upload`.
+4. Local file saving to `data/uploads`.
+5. Document metadata schema.
+6. SQLite initialization.
+7. Basic configuration management.
+8. Minimal smoke test.
+9. README local startup commands.
+
+## Phase 1 Non-Goals
+
+Phase 1 must not implement:
+
+1. OCR.
+2. LLM calls.
+3. Embeddings.
+4. Vector store.
+5. Knowledge card generation.
+6. Tender analysis.
+7. Demo page.
+8. User system.
+9. Word/PDF export.
+
+## Safety Rule
+
+All generated content must return:
+
+- `citations`
+- `risks`
+- `need_human_review = true`
+
+Any generated content without a source citation must be marked high risk.
+
diff --git a/docs/ai/02-architecture.md b/docs/ai/02-architecture.md
new file mode 100644
index 0000000..01d6e85
--- /dev/null
+++ b/docs/ai/02-architecture.md
@@ -0,0 +1,62 @@
+# Architecture
+
+## Historical Bid Ingestion Flow
+
+Future historical bid ingestion chain:
+
+1. Upload historical bid file.
+2. `DocumentParser` parses text, titles, pages, and tables.
+3. `SectionSplitter` splits sections by directory, heading, and fallback rules.
+4. `Tagger` assigns initial tags based on titles and deterministic rules.
+5. `KnowledgeCardBuilder` creates knowledge cards.
+6. `EmbeddingService` creates vectors.
+7. `VectorStore` writes vector indexes.
+8. `MetadataStore` writes SQLite metadata.
+
+## Tender Analysis Flow
+
+Future tender analysis chain:
+
+1. Upload tender file.
+2. `DocumentParser` parses text, titles, pages, and tables.
+3. `TenderAnalyzer` extracts project requirements, scoring items, and disqualification risks.
+4. User selects a target tag.
+5. `Retriever` retrieves knowledge cards by tag and query semantics.
+6. `PromptBuilder` combines tender requirements, historical snippets, and output constraints.
+7. `LLMService` generates candidate content.
+8. `RiskChecker` marks low confidence, missing citations, and possible disqualification risks.
+9. API returns generated content, citations, risks, `need_human_review`, and raw JSON.
+
+## Recommended Backend Modules
+
+Future backend module direction:
+
+- `backend/app/main.py`
+- `backend/app/config.py`
+- `backend/app/models/`
+- `backend/app/schemas/`
+- `backend/app/api/`
+- `backend/app/services/document_parser/`
+- `backend/app/services/section_splitter/`
+- `backend/app/services/tagger/`
+- `backend/app/services/knowledge_card/`
+- `backend/app/services/embedding/`
+- `backend/app/services/vector_store/`
+- `backend/app/services/tender_analyzer/`
+- `backend/app/services/retriever/`
+- `backend/app/services/llm/`
+- `backend/app/services/risk_checker/`
+- `backend/app/storage/`
+
+## Adapter Boundary
+
+External or heavy capabilities must sit behind adapters:
+
+- document parsing adapter
+- OCR adapter
+- embedding adapter
+- vector store adapter
+- LLM adapter
+
+This keeps the first demo replaceable and prevents the project from locking into one platform too early.
+
diff --git a/docs/ai/03-data-model.md b/docs/ai/03-data-model.md
new file mode 100644
index 0000000..ba81af7
--- /dev/null
+++ b/docs/ai/03-data-model.md
@@ -0,0 +1,81 @@
+# Data Model
+
+## Document
+
+- `id`: string
+- `original_filename`: string
+- `stored_filename`: string
+- `stored_path`: string
+- `file_ext`: string
+- `content_type`: optional string
+- `file_size`: int
+- `doc_role`: `historical_bid | tender`
+- `created_at`: datetime
+- `updated_at`: datetime
+- `parse_status`: `pending | success | failed`
+- `error_message`: optional string
+
+Phase 1 only creates documents with `parse_status = pending`.
+The original filename is preserved as metadata only; the backend-generated stored filename is the only value used for filesystem persistence.
+
+## Section
+
+- `id`: string
+- `document_id`: string
+- `title`: string
+- `level`: int
+- `order_index`: int
+- `text`: string
+- `page_start`: optional int
+- `page_end`: optional int
+
+## KnowledgeCard
+
+- `id`: string
+- `document_id`: string
+- `section_id`: string
+- `title`: string
+- `tag`: string
+- `content`: string
+- `source_filename`: string
+- `source_section_title`: string
+- `confidence`: float
+- `metadata`: dict
+
+## ScoringItem
+
+- `name`: string
+- `requirement`: string
+- `score`: optional float
+- `source_text`: string
+
+## RiskItem
+
+- `risk_type`: string
+- `description`: string
+- `severity`: `low | medium | high`
+- `source_text`: optional string
+
+## TenderAnalysis
+
+- `document_id`: string
+- `project_requirements`: list[string]
+- `scoring_items`: list[ScoringItem]
+- `disqualification_risks`: list[RiskItem]
+- `raw_text_summary`: string
+
+## Citation
+
+- `source_filename`: string
+- `source_section_title`: string
+- `content_snippet`: string
+- `card_id`: string
+
+## GenerationResult
+
+- `target_tag`: string
+- `generated_content`: string
+- `citations`: list[Citation]
+- `risks`: list[RiskItem]
+- `need_human_review`: bool
+- `raw_prompt`: optional string
diff --git a/docs/ai/04-api-contract.md b/docs/ai/04-api-contract.md
new file mode 100644
index 0000000..55a4cb6
--- /dev/null
+++ b/docs/ai/04-api-contract.md
@@ -0,0 +1,163 @@
+# API Contract
+
+## GET /health
+
+Health check.
+
+Response:
+
+```json
+{
+  "status": "ok"
+}
+```
+
+## POST /api/files/upload
+
+Upload a historical bid file or a tender file.
+
+Parameters:
+
+- `file`: UploadFile
+- `doc_role`: `historical_bid | tender`
+
+Success response:
+
+```json
+{
+  "document_id": "string",
+  "original_filename": "string",
+  "doc_role": "historical_bid",
+  "parse_status": "pending",
+  "file_size": 123,
+  "created_at": "2026-06-27T12:00:00Z"
+}
+```
+
+Success status: `201 Created`
+
+Error response:
+
+```json
+{
+  "error_code": "INVALID_DOC_ROLE",
+  "message": "Unsupported document role",
+  "details": {}
+}
+```
+
+Phase 1 error codes: `MISSING_FILE`, `MISSING_DOC_ROLE`, `INVALID_DOC_ROLE`, `EMPTY_FILE`, `UNSAFE_FILENAME`, `FILE_TOO_LARGE`, `UNSUPPORTED_FILE_TYPE`, `FILE_WRITE_FAILED`, `METADATA_WRITE_FAILED`.
+
+## POST /api/documents/{document_id}/parse
+
+Parse a document.
+
+Response:
+
+```json
+{
+  "document_id": "string",
+  "sections_count": 10,
+  "tables_count": 2,
+  "parse_status": "success"
+}
+```
+
+## POST /api/knowledge/build
+
+Convert historical bid sections into knowledge cards.
+
+Request:
+
+```json
+{
+  "document_id": "string"
+}
+```
+
+Response:
+
+```json
+{
+  "document_id": "string",
+  "cards_count": 20,
+  "tags": ["运维服务实施方案", "突发应急方案和措施"]
+}
+```
+
+## POST /api/tender/analyze
+
+Analyze a new tender document.
+
+Request:
+
+```json
+{
+  "document_id": "string"
+}
+```
+
+Response:
+
+```json
+{
+  "project_requirements": [],
+  "scoring_items": [],
+  "disqualification_risks": []
+}
+```
+
+## POST /api/retrieve
+
+Retrieve knowledge cards.
+
+Request:
+
+```json
+{
+  "query": "生成运维服务实施方案",
+  "tag": "运维服务实施方案",
+  "top_k": 5
+}
+```
+
+Response:
+
+```json
+{
+  "cards": []
+}
+```
+
+## POST /api/generate
+
+Generate candidate content.
+
+Request:
+
+```json
+{
+  "tender_document_id": "string",
+  "target_tag": "运维服务实施方案",
+  "query": "根据招标要求生成运维服务实施方案",
+  "top_k": 5
+}
+```
+
+Response:
+
+```json
+{
+  "target_tag": "运维服务实施方案",
+  "generated_content": "string",
+  "citations": [],
+  "risks": [],
+  "need_human_review": true
+}
+```
+
+## GET /demo
+
+Minimal demo page.
+
+This endpoint is not part of Phase 1.
diff --git a/docs/ai/05-dev-rules.md b/docs/ai/05-dev-rules.md
new file mode 100644
index 0000000..49443d9
--- /dev/null
+++ b/docs/ai/05-dev-rules.md
@@ -0,0 +1,39 @@
+# Codex Development Rules
+
+## General Rules
+
+1. Do not build a complete bidding system.
+2. Do not build user login or a permission system.
+3. Do not build project management.
+4. Do not build final Word/PDF export.
+5. Do not build CA signing or formal bidding workflows.
+6. Keep the MVP backend-first.
+7. Keep the frontend minimal and demo-only.
+8. Every API must return structured JSON.
+9. All generated content must include citations, risks, and `need_human_review`.
+10. All external services must be abstracted behind interfaces.
+
+## Engineering Rules
+
+1. Use Python 3.11+.
+2. Use FastAPI.
+3. Use Pydantic schemas.
+4. Use SQLite for MVP metadata.
+5. Use local storage for uploaded files.
+6. Keep document parsing pluggable.
+7. Keep OCR pluggable.
+8. Keep LLM provider pluggable.
+9. Keep embedding provider pluggable.
+10. Keep vector store pluggable.
+
+## Implementation Rules
+
+1. First build a runnable vertical slice.
+2. Prefer simple deterministic rules before complex LLM logic.
+3. Start with docx and text-based pdf.
+4. Treat scanned pdf as a later OCR enhancement.
+5. If a file cannot be parsed, return `parse_status = failed` and `error_message`.
+6. Do not silently ignore parse errors.
+7. Do not generate content without retrieval context unless explicitly marked high risk.
+8. Never claim generated content is ready for final bidding submission.
+
diff --git a/docs/ai/06-verification.md b/docs/ai/06-verification.md
new file mode 100644
index 0000000..a46036d
--- /dev/null
+++ b/docs/ai/06-verification.md
@@ -0,0 +1,53 @@
+# Verification
+
+## MVP Acceptance Criteria
+
+The MVP must eventually support:
+
+1. Upload 2-3 historical bid files.
+2. Upload 1 tender file.
+3. Parse files into sections.
+4. Build knowledge cards from historical bid files.
+5. Apply initial tags to knowledge cards.
+6. Retrieve knowledge cards by tag and query.
+7. Analyze tender file for project requirements, scoring items, and disqualification risks.
+8. Generate candidate content with an external LLM API.
+9. Return source citations.
+10. Return risk hints.
+11. Mark `need_human_review = true`.
+12. Show results in a simple demo page.
+13. Provide raw JSON response.
+
+## Smoke Test For Future MVP
+
+A minimal successful demo should prove:
+
+1. Historical bid file uploaded successfully.
+2. At least one section is parsed.
+3. At least one knowledge card is created.
+4. A target tag can retrieve relevant cards.
+5. Generate API returns content.
+6. The response includes citations.
+7. The response includes risks.
+8. The response includes `need_human_review = true`.
+
+## Phase 0 Verification
+
+Phase 0 is complete when:
+
+1. The folder is a Git repository.
+2. Harness baseline files exist.
+3. `docs/ai/` contains project brief, scope, architecture, data model, API contract, dev rules, and verification notes.
+4. `.ai/` contains spec, implementation plan, verification, evaluation, and handoff files.
+5. No business code was implemented.
+
+## Phase 1 Verification
+
+Phase 1 should be verified with:
+
+1. Unit or API tests for `GET /health`.
+2. Upload smoke test for `POST /api/files/upload`.
+3. SQLite metadata persistence check.
+4. Local saved-file existence check.
+5. README startup command check.
+
diff --git a/docs/ai/07-source-materials.md b/docs/ai/07-source-materials.md
new file mode 100644
index 0000000..004cee6
--- /dev/null
+++ b/docs/ai/07-source-materials.md
@@ -0,0 +1,38 @@
+# Source Materials
+
+## Project Specification Sources
+
+- PRD: `C:\Users\26561\Desktop\模型训练资料\相关文档\投标智能知识库能力验证版 PRD v0.1.pdf`
+- Research report: `C:\Users\26561\Desktop\模型训练资料\相关文档\deep-research-report.md`
+
+## Sample Material Directory
+
+- `C:\Users\26561\Desktop\模型训练资料\甲方提供资料`
+
+The sample directory contains tender and historical bid materials for later validation. Phase 0 does not copy or process these files.
+
+## Initial Sample Strategy
+
+Later demo validation should use:
+
+1. One new tender file.
+2. Two or three historical bid files.
+3. A few target tags, such as:
+   - 运维服务实施方案
+   - 突发应急方案和措施
+   - 网络和数据安全防护保障措施
+   - 服务质量保障和考核评估方案
+
+## Dependency Direction From Research Report
+
+The research report recommends:
+
+1. RAGFlow as a product reference.
+2. Haystack as the practical Python-oriented backend foundation.
+3. Docling as the primary structured document parser.
+4. PaddleOCR as the later OCR adapter.
+5. Qdrant as the later vector store.
+6. FastAPI as the thin API and demo shell.
+
+These are future implementation directions, not Phase 0 or Phase 1 requirements.
+
diff --git a/docs/ai/08-tech-selection.md b/docs/ai/08-tech-selection.md
new file mode 100644
index 0000000..dfb5a7c
--- /dev/null
+++ b/docs/ai/08-tech-selection.md
@@ -0,0 +1,71 @@
+# Tech Selection
+
+## Source
+
+This file summarizes `docs/source-materials/originals/deep-research-report.md`.
+
+## Main Decision
+
+Use a thin FastAPI service as the project shell.
+
+For later RAG phases, the recommended implementation stack is:
+
+- Haystack for Python-native retrieval/generation pipeline orchestration.
+- Docling as the primary structured document parser.
+- PaddleOCR as the later OCR adapter for scanned PDF and image pages.
+- Qdrant as the later vector store.
+- RAGFlow as the product-reference benchmark, not the codebase to fork.
+
+## Why Not Fork A Full Platform First
+
+Do not start by heavy-forking RAGFlow, Dify, AnythingLLM, or MinerU.
+
+Reasons:
+
+1. The current project is a capability-validation demo, not a general AI platform.
+2. Full platforms bring UI, workflow, team, plugin, and deployment surfaces that are outside the PRD.
+3. Dify and MinerU have custom licenses that need legal review before any deep reuse.
+4. Heavy platform adoption would make two-week demo delivery harder to control.
+
+## Practical Stack By Phase
+
+Phase 1:
+
+- FastAPI
+- Pydantic
+- SQLite
+- local file storage
+- pytest smoke tests
+
+Phase 2:
+
+- Docling adapter for docx and text-based pdf parsing.
+- Unified chunk schema.
+- Deterministic section splitting and tag rules.
+
+Phase 3:
+
+- Qdrant adapter.
+- Haystack retrieval pipeline.
+- Dense retrieval first, hybrid retrieval as an interface-compatible extension.
+
+Phase 4:
+
+- OpenAI-compatible LLM adapter.
+- Prompt builder.
+- Citation-preserving answer formatter.
+- Rule-based risk checker.
+
+Phase 5:
+
+- Minimal FastAPI-hosted demo page.
+- Demo script using 2-3 historical bid files and 1 tender file.
+
+## Dependency Guardrails
+
+1. Prefer MIT or Apache-2.0 dependencies.
+2. Treat Dify and MinerU as reference-only unless license review approves deeper reuse.
+3. Avoid introducing AGPL dependencies into the main path without explicit approval.
+4. Keep external services behind adapters so parser, vector store, embedding, and LLM providers can be replaced.
+5. No generated answer can be returned without citations, risks, and `need_human_review = true`.
+
diff --git a/docs/ai/09-phase-roadmap.md b/docs/ai/09-phase-roadmap.md
new file mode 100644
index 0000000..b17339e
--- /dev/null
+++ b/docs/ai/09-phase-roadmap.md
@@ -0,0 +1,92 @@
+# Phase Roadmap
+
+## Phase 0 - Repository And Context Initialization
+
+Status: complete.
+
+Done:
+
+1. Initialized Git repository.
+2. Applied Auto_AICoding_Harness in medium mode with `python-backend-service` profile.
+3. Created durable project context under `docs/ai/`.
+4. Copied lightweight source documents into `docs/source-materials/originals/`.
+5. Indexed large external sample materials without copying them into Git.
+
+## Phase 1 - Minimal Backend Foundation
+
+Goal: create a runnable backend base without RAG features.
+
+Harness requirement: all Phase 1 development must run in `large` mode and must execute project scripts before completion.
+
+Scope:
+
+1. FastAPI app startup.
+2. `GET /health`.
+3. `POST /api/files/upload`.
+4. Local file saving under `data/uploads`.
+5. Document metadata schema.
+6. SQLite initialization.
+7. Basic configuration management.
+8. Minimal smoke tests.
+9. README startup commands.
+
+Explicitly excluded:
+
+- OCR
+- LLM calls
+- embeddings
+- vector store
+- knowledge cards
+- tender analysis
+- demo page
+- user system
+- Word/PDF export
+
+## Phase 2 - Document Parsing And Chunking
+
+Goal: parse sample docx/text-based pdf files into normalized chunks.
+
+Scope:
+
+1. Docling adapter.
+2. Unified chunk schema.
+3. Section splitting.
+4. Initial deterministic tag rules.
+5. Parse-status and error handling.
+6. Tests with 1-2 small representative files.
+
+## Phase 3 - Retrieval
+
+Goal: retrieve historical chunks by tag and query.
+
+Scope:
+
+1. Qdrant adapter.
+2. Haystack query pipeline wrapper.
+3. Dense retrieval first.
+4. Metadata-preserving result format.
+5. Retrieval tests with fake or small local chunks.
+
+## Phase 4 - Generation, Citations, And Risks
+
+Goal: generate candidate content from retrieval context.
+
+Scope:
+
+1. OpenAI-compatible LLM adapter.
+2. Prompt builder.
+3. Answer formatter.
+4. Citation formatter.
+5. Rule-based risk checker.
+6. `need_human_review = true` always.
+
+## Phase 5 - Demo Page And Script
+
+Goal: present the full capability chain to a stakeholder.
+
+Scope:
+
+1. Minimal upload/query/result page.
+2. Demo script using selected sample files.
+3. Raw JSON display.
+4. Manual verification notes for citations and risk hints.
diff --git a/docs/ai/10-phase1-dev-spec.md b/docs/ai/10-phase1-dev-spec.md
new file mode 100644
index 0000000..f8900c6
--- /dev/null
+++ b/docs/ai/10-phase1-dev-spec.md
@@ -0,0 +1,102 @@
+# Phase 1 Development Spec
+
+## Objective
+
+Build the smallest runnable backend foundation for the 投标智能知识库能力验证版 Demo.
+
+Phase 1 proves that the service can start, accept an uploaded file, save it locally, and persist document metadata. It does not parse document content.
+
+Phase 1 is a backend foundation milestone. It is not the customer-facing Demo and does not prove the knowledge-base capability by itself.
+
+## Required Harness Mode
+
+All Phase 1 development must run under Auto_AICoding_Harness `large` mode.
+
+Before implementation:
+
+1. Run `ai-status` or `ai-doctor`.
+2. Confirm `.ai/state.json` reports `"mode": "large"`.
+3. Keep `.ai/implementation-plan.md`, `.ai/verification.md`, `.ai/evaluation.md`, and `.ai/handoff.md` current.
+
+## In Scope
+
+Implement only:
+
+1. FastAPI application startup.
+2. `GET /health`.
+3. `POST /api/files/upload`.
+4. Local file saving under `data/uploads`.
+5. Document metadata schema.
+6. SQLite initialization.
+7. Basic configuration management.
+8. Minimal smoke tests.
+9. README local startup and test commands.
+
+## Out Of Scope
+
+Do not implement:
+
+1. OCR.
+2. LLM calls.
+3. Embeddings.
+4. Vector store.
+5. Knowledge card generation.
+6. Tender analysis.
+7. Demo page.
+8. User login or permission system.
+9. Word/PDF export.
+10. Production deployment.
+
+## Recommended File Scope
+
+Phase 1 may add or edit:
+
+```text
+backend/
+├── app/
+│   ├── __init__.py
+│   ├── main.py
+│   ├── config.py
+│   ├── api/
+│   │   ├── __init__.py
+│   │   ├── health.py
+│   │   └── files.py
+│   ├── schemas/
+│   │   ├── __init__.py
+│   │   └── document.py
+│   └── storage/
+│       ├── __init__.py
+│       ├── database.py
+│       └── file_storage.py
+├── tests/
+│   ├── test_health.py
+│   └── test_upload.py
+└── pyproject.toml or requirements.txt
+```
+
+Repository-level files that may be updated:
+
+- `README.md`
+- `.gitignore`
+- `scripts/ai_build.sh`
+- `scripts/ai_test.sh`
+- `scripts/ai_check.sh`
+- `scripts/ai_check.ps1`
+- `.ai/verification.md`
+- `.ai/evaluation.md`
+- `.ai/handoff.md`
+
+## Completion Definition
+
+Phase 1 is complete only when:
+
+1. The app can be imported.
+2. `GET /health` returns `{"status": "ok"}`.
+3. `POST /api/files/upload` returns `201 Created` for valid uploads.
+4. Uploading a small file saves it under configured upload root using a backend-generated stored filename.
+5. Uploading a file creates a SQLite metadata row following `docs/ai/12-phase1-api-persistence.md`.
+6. Invalid uploads return the documented structured error JSON.
+7. Invalid uploads do not leave orphan files or metadata rows.
+8. Tests cover the P0 cases in `docs/ai/16-phase1-test-cases.md`.
+9. Project scripts were run and results were recorded.
+10. Deferred RAG/OCR/LLM functionality remains unimplemented.
diff --git a/docs/ai/11-local-dev-env.md b/docs/ai/11-local-dev-env.md
new file mode 100644
index 0000000..af71e13
--- /dev/null
+++ b/docs/ai/11-local-dev-env.md
@@ -0,0 +1,105 @@
+# Local Development Environment
+
+## Target Platform
+
+Primary local development platform:
+
+- Windows
+- PowerShell
+- Python 3.11+
+- FastAPI backend
+- SQLite metadata store
+
+Future deployment may use Docker/Ubuntu, but Phase 1 should first run locally on Windows.
+
+## Python Runtime
+
+Preferred runtime in this Codex desktop environment:
+
+```powershell
+$py = "C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
+```
+
+For normal local development, a project virtual environment is acceptable:
+
+```powershell
+python -m venv .venv
+.\.venv\Scripts\Activate.ps1
+python -m pip install -U pip
+```
+
+Phase 1 should choose one dependency file:
+
+- `pyproject.toml`, preferred if using modern packaging.
+- `requirements.txt`, acceptable for the smallest setup.
+
+Do not introduce both unless there is a specific reason.
+
+## Expected Phase 1 Dependencies
+
+Minimum expected dependencies:
+
+- `fastapi`
+- `uvicorn`
+- `pydantic`
+- `pytest`
+- `httpx` for FastAPI test client support if required by the chosen test style
+
+SQLite should use Python standard library `sqlite3` unless an ORM is deliberately chosen later.
+
+## Local Paths
+
+Canonical project name:
+
+```text
+BidKnowledge
+```
+
+Current local checkout path:
+
+```text
+F:\BidKonwledge
+```
+
+The local folder name currently contains the historical `Konwledge` spelling. Do not hard-code this absolute path in tests; use the current working directory or configurable settings. Rename the local folder only as a separate repository-maintenance task.
+
+Upload directory:
+
+```text
+data/uploads
+```
+
+Recommended SQLite file:
+
+```text
+data/app.sqlite3
+```
+
+These paths must be configurable through a settings module.
+
+## Future Startup Shape
+
+Expected command after Phase 1 implementation:
+
+```powershell
+cd F:\BidKonwledge
+python -m uvicorn backend.app.main:app --reload
+```
+
+The exact command may change if Phase 1 chooses a different Python package layout. README must record the final command.
+
+## Required Scripts
+
+Before claiming development completion, run:
+
+```powershell
+.\scripts\ai_check.ps1
+```
+
+If shell tooling is available, also run:
+
+```powershell
+bash ./scripts/ai_check.sh
+```
+
+If one script cannot run on the current machine, record the reason in `.ai/verification.md`.
diff --git a/docs/ai/12-phase1-api-persistence.md b/docs/ai/12-phase1-api-persistence.md
new file mode 100644
index 0000000..5cb925d
--- /dev/null
+++ b/docs/ai/12-phase1-api-persistence.md
@@ -0,0 +1,150 @@
+# Phase 1 API And Persistence Details
+
+## API Surface
+
+Phase 1 implements only:
+
+1. `GET /health`
+2. `POST /api/files/upload`
+
+All other API contracts in `docs/ai/04-api-contract.md` are future-phase contracts.
+
+## GET /health
+
+Response status: `200 OK`
+
+Response body:
+
+```json
+{
+  "status": "ok"
+}
+```
+
+No database or external dependency check is required in Phase 1.
+
+## POST /api/files/upload
+
+Request:
+
+- `multipart/form-data`
+- `file`: uploaded file
+- `doc_role`: one of `historical_bid`, `tender`
+
+Success response status: `201 Created`
+
+Success response body:
+
+```json
+{
+  "document_id": "string",
+  "original_filename": "string",
+  "doc_role": "historical_bid",
+  "parse_status": "pending",
+  "file_size": 123,
+  "created_at": "2026-06-27T12:00:00Z"
+}
+```
+
+Error response body:
+
+```json
+{
+  "error_code": "INVALID_DOC_ROLE",
+  "message": "Unsupported document role",
+  "details": {}
+}
+```
+
+Required Phase 1 error codes:
+
+| Scenario | HTTP status | `error_code` |
+| --- | --- | --- |
+| Missing file | `400 Bad Request` | `MISSING_FILE` |
+| Missing `doc_role` | `400 Bad Request` | `MISSING_DOC_ROLE` |
+| Invalid `doc_role` | `400 Bad Request` | `INVALID_DOC_ROLE` |
+| Empty file | `400 Bad Request` | `EMPTY_FILE` |
+| Unsafe filename | `400 Bad Request` | `UNSAFE_FILENAME` |
+| File too large | `413 Payload Too Large` | `FILE_TOO_LARGE` |
+| Unsupported file extension | `400 Bad Request` | `UNSUPPORTED_FILE_TYPE` |
+| File write failure | `500 Internal Server Error` | `FILE_WRITE_FAILED` |
+| Metadata write failure | `500 Internal Server Error` | `METADATA_WRITE_FAILED` |
+
+## Upload Rules
+
+Phase 1 should:
+
+1. Save files under `data/uploads`.
+2. Generate a server-side document id.
+3. Generate the stored filename on the backend, for example `<document_id><safe_extension>`.
+4. Preserve the original filename in metadata.
+5. Reject missing file input.
+6. Reject missing or invalid `doc_role`.
+7. Reject empty files.
+8. Reject path traversal filenames.
+9. Reject unsupported extensions: `.exe`, `.bat`, `.cmd`, `.ps1`, and other executable-like uploads.
+10. Return the structured JSON error shape above.
+11. Avoid trusting extension or MIME type as proof of safe content; Phase 1 stores bytes but does not parse them.
+
+Allowed Phase 1 extensions are:
+
+```text
+.txt
+.pdf
+.doc
+.docx
+```
+
+If Phase 1 implements a configurable max upload size, the default should be documented in README and tests should override it with a small test limit.
+
+Do not implement content parsing.
+
+## Atomicity Rules
+
+Upload persistence must avoid inconsistent file/database state:
+
+1. If request validation fails, do not write a file and do not insert metadata.
+2. If file write fails, do not insert metadata.
+3. If database insert fails after file write, delete the stored file before returning the error.
+4. If cleanup after database failure also fails, return `METADATA_WRITE_FAILED` and log the cleanup failure without exposing local absolute paths in the response.
+5. Original filenames are metadata only; never use them as stored filenames.
+
+## Document Metadata
+
+SQLite table: `documents`
+
+Required fields:
+
+| Column | Type | Notes |
+| --- | --- | --- |
+| `id` | text primary key | server-generated id |
+| `original_filename` | text | original filename from upload metadata |
+| `stored_filename` | text | backend-generated filename |
+| `stored_path` | text | relative path under upload root |
+| `file_ext` | text | normalized lower-case extension |
+| `content_type` | text nullable | client-provided MIME type, stored for reference only |
+| `file_size` | integer | uploaded byte length |
+| `doc_role` | text | `historical_bid` or `tender` |
+| `created_at` | text | ISO-8601 timestamp |
+| `updated_at` | text | ISO-8601 timestamp |
+| `parse_status` | text | default `pending` |
+| `error_message` | text nullable | default null |
+
+## Status Rules
+
+Initial upload status:
+
+```text
+parse_status = pending
+```
+
+Phase 1 does not transition documents to `success` or `failed` because parsing is not implemented.
+
+## Security Notes
+
+1. Normalize or replace storage filenames to avoid path traversal.
+2. Store uploads only inside configured upload root.
+3. Do not execute or parse uploaded files in Phase 1.
+4. Do not log file contents.
+5. Do not copy external sample directories into repository history.
+6. Do not return absolute local filesystem paths in public API responses.
diff --git a/docs/ai/13-phase1-verification-checklist.md b/docs/ai/13-phase1-verification-checklist.md
new file mode 100644
index 0000000..0635a98
--- /dev/null
+++ b/docs/ai/13-phase1-verification-checklist.md
@@ -0,0 +1,96 @@
+# Phase 1 Verification Checklist
+
+## Required Command Evidence
+
+Every Phase 1 completion report must include:
+
+1. Harness status command.
+2. Project check script command.
+3. Test command.
+4. Any manual smoke command.
+
+Record results in `.ai/verification.md`.
+
+## Harness Checks
+
+Run:
+
+```powershell
+$py = "C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
+& $py "C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status"
+& $py "C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor"
+```
+
+Expected:
+
+- initialized: yes
+- mode: large
+- state_valid: yes
+- required large files present
+
+## Script Checks
+
+Run:
+
+```powershell
+.\scripts\ai_check.ps1
+```
+
+When available:
+
+```powershell
+bash ./scripts/ai_check.sh
+```
+
+After Phase 1 implementation, these scripts should call the actual build/test commands instead of printing placeholders.
+
+## Automated Tests
+
+Expected test command after implementation:
+
+```powershell
+python -m pytest backend/tests
+```
+
+Minimum test cases:
+
+1. `GET /health` returns `200` and `{"status": "ok"}`.
+2. `POST /api/files/upload` returns `201 Created` for valid `historical_bid` and `tender` uploads.
+3. Upload response contains `document_id`, `original_filename`, `doc_role`, `parse_status`, `file_size`, and `created_at`.
+4. Upload rejects invalid input with the documented error JSON shape: `error_code`, `message`, and `details`.
+5. Upload saves a small file under the configured upload root without using the original filename as the stored filename.
+6. Upload inserts a metadata row into SQLite using the documented `documents` table fields.
+7. Failed validation does not leave orphan files or metadata rows.
+
+Use `docs/ai/16-phase1-test-cases.md` as the detailed acceptance source.
+
+## Manual Smoke Checks
+
+After starting the server, verify:
+
+```powershell
+curl.exe --noproxy "*" http://127.0.0.1:8000/health
+```
+
+Expected response:
+
+```json
+{"status":"ok"}
+```
+
+Use `--noproxy "*"` for localhost checks on this machine because proxy environment variables can distort local requests.
+
+The upload smoke check should expect HTTP `201 Created` and the fixed upload success response documented in `docs/ai/12-phase1-api-persistence.md`.
+
+## Not Required In Phase 1
+
+Do not require these checks before Phase 1 completion:
+
+1. Docling parsing.
+2. OCR parsing.
+3. Qdrant startup.
+4. Haystack retrieval.
+5. LLM generation.
+6. Demo page browser walkthrough.
+
+These belong to later phases.
diff --git a/docs/ai/14-reference-reuse-strategy.md b/docs/ai/14-reference-reuse-strategy.md
new file mode 100644
index 0000000..16fd13c
--- /dev/null
+++ b/docs/ai/14-reference-reuse-strategy.md
@@ -0,0 +1,114 @@
+# Reference Reuse Strategy
+
+## Decision
+
+Do not directly fork a full RAG platform as the main business repository.
+
+Use this repository as the business codebase, and use selected external repositories as reference material outside Git:
+
+```text
+F:\BidKonwledge              # business repository
+F:\BidKonwledge_refs         # external reference repositories, not committed
+├── ragflow
+└── haystack-demos
+```
+
+## Repositories Pulled For Reference
+
+| Repository | Local Path | Commit | Use |
+| --- | --- | --- | --- |
+| `https://github.com/infiniflow/ragflow.git` | `F:\BidKonwledge_refs\ragflow` | `f90be41` | Product reference: document ingestion UX, citation display, RAG workflow shape, deployment complexity. |
+| `https://github.com/deepset-ai/haystack-demos.git` | `F:\BidKonwledge_refs\haystack-demos` | `17e6103` | Engineering reference: Haystack pipeline wrappers, Qdrant indexing/query demo, upload-to-index flow. |
+
+Both were cloned shallowly outside the main repository.
+
+## Can We Directly Build On Someone Else's Project?
+
+Yes, but only under a narrow condition: if the delivery goal changes from "投标智能知识库能力验证 Demo" to "ship or customize an existing RAG platform".
+
+For the current PRD, direct platform forking is not the best default.
+
+## Option Assessment
+
+### Option A - Directly Fork RAGFlow
+
+Pros:
+
+- Already has a full RAG product shape.
+- Has document ingestion, chunking, retrieval, citations, UI, Docker deployment.
+- Apache-2.0 license is acceptable for reference and possible reuse.
+
+Cons:
+
+- Heavy full-stack platform, not a thin FastAPI demo.
+- Uses Flask/Quart backend, React frontend, Docker services, MySQL, Redis, MinIO, and search/vector infrastructure.
+- Requires more environment work before we can show a small custom bidding workflow.
+- Customizing the product down to our narrow PRD may be slower than building the thin vertical slice.
+
+Verdict:
+
+Use as product reference. Do not make it the main repo unless we intentionally pivot to a RAGFlow customization project.
+
+### Option B - Directly Fork Haystack Demos
+
+Pros:
+
+- Small examples of indexing/query pipelines.
+- The `qdrant_indexing` demo directly shows upload -> embed -> write to Qdrant and query -> retrieve from Qdrant.
+- Good fit for later Phase 3 retrieval implementation.
+
+Cons:
+
+- It is a demo collection, not a bidding-product backend.
+- It uses Hayhooks deployment patterns that may be more than we need in Phase 1.
+
+Verdict:
+
+Use as code reference for pipeline shape. Do not make it the main repo.
+
+### Option C - Use Libraries And Build A Thin Business Shell
+
+Pros:
+
+- Not from zero: FastAPI, Haystack, Docling, Qdrant, and PaddleOCR provide most heavy capability.
+- Keeps PRD scope narrow.
+- Lets us implement the exact upload/API/metadata/citation/risk contract we need.
+- Easier for Codex to work in bounded phases.
+
+Cons:
+
+- We must write the glue code ourselves.
+- We need to design our own minimal data model and demo UI.
+
+Verdict:
+
+Recommended path.
+
+## Reuse Rules
+
+1. Do not copy external repository source into `F:\BidKonwledge` unless a later task explicitly approves it.
+2. Prefer dependency usage over source vendoring.
+3. If copying a small snippet becomes necessary, record source file, commit, license, and adaptation notes in the implementing PR/task.
+4. Keep RAGFlow as a product and UX reference.
+5. Keep Haystack demos as an engineering reference.
+6. Treat direct RAGFlow customization as a separate spike, not as the default mainline.
+
+## Not From Zero Means
+
+The project should not hand-roll:
+
+- document parsing engines
+- vector database internals
+- embedding pipelines
+- RAG orchestration primitives
+- OCR engines
+
+The project should own:
+
+- bidding-domain API contract
+- document metadata model
+- tag taxonomy and risk rules
+- source citation response format
+- minimal demo flow
+- integration tests and smoke scripts
+
diff --git a/docs/ai/15-target-architecture.md b/docs/ai/15-target-architecture.md
new file mode 100644
index 0000000..c3ec217
--- /dev/null
+++ b/docs/ai/15-target-architecture.md
@@ -0,0 +1,157 @@
+# Target Architecture
+
+## Architecture Principle
+
+Build a thin bidding-domain service around proven RAG/document components.
+
+The system should not become a generic RAG platform. It should expose the smallest API and demo flow needed to validate the PRD.
+
+## High-Level Shape
+
+```mermaid
+flowchart TD
+    UI["Minimal Demo Page"] --> API["FastAPI Backend"]
+    API --> Upload["Upload Service"]
+    Upload --> LocalFiles["Local File Storage"]
+    Upload --> Metadata["SQLite Metadata Store"]
+
+    API --> Parse["Document Parsing Adapter"]
+    Parse --> Docling["Docling for DOCX / text PDF"]
+    Parse --> OCR["PaddleOCR later for scanned files"]
+
+    Parse --> Chunker["Section Splitter / Chunker"]
+    Chunker --> Tagger["Rule-Based Tagger"]
+    Tagger --> Cards["Knowledge Cards"]
+
+    Cards --> Index["Indexing Adapter"]
+    Index --> Qdrant["Qdrant Vector Store"]
+
+    API --> Retrieve["Retriever"]
+    Retrieve --> Haystack["Haystack Pipeline"]
+    Haystack --> Qdrant
+
+    Retrieve --> Prompt["Prompt Builder"]
+    Prompt --> LLM["OpenAI-Compatible LLM Adapter"]
+    LLM --> Format["Answer Formatter"]
+    Format --> Risk["Risk Checker"]
+    Risk --> API
+```
+
+## Phase 1 Architecture
+
+Phase 1 implements only the foundation:
+
+```mermaid
+flowchart LR
+    Client["API Client / Tests"] --> API["FastAPI"]
+    API --> Health["GET /health"]
+    API --> Upload["POST /api/files/upload"]
+    Upload --> Files["data/uploads"]
+    Upload --> DB["SQLite documents table"]
+```
+
+Phase 1 does not call Docling, PaddleOCR, Haystack, Qdrant, or any LLM.
+
+## Backend Module Plan
+
+```text
+backend/
+├── app/
+│   ├── main.py
+│   ├── config.py
+│   ├── api/
+│   │   ├── health.py
+│   │   └── files.py
+│   ├── schemas/
+│   │   └── document.py
+│   ├── storage/
+│   │   ├── database.py
+│   │   └── file_storage.py
+│   ├── services/
+│   │   ├── document_parser/
+│   │   ├── section_splitter/
+│   │   ├── tagger/
+│   │   ├── knowledge_card/
+│   │   ├── retriever/
+│   │   ├── llm/
+│   │   └── risk_checker/
+│   └── adapters/
+│       ├── docling_parser.py
+│       ├── paddleocr_parser.py
+│       ├── qdrant_store.py
+│       └── llm_gateway.py
+└── tests/
+```
+
+Phase 1 should create only the parts it needs. Empty future service modules should not be added until their phase starts.
+
+## Data Flow By Phase
+
+### Phase 1
+
+1. Upload file.
+2. Save original file under `data/uploads`.
+3. Insert document metadata into SQLite.
+4. Return document id and `parse_status = pending`.
+
+### Phase 2
+
+1. Parse document through Docling adapter.
+2. Produce normalized sections/chunks.
+3. Apply deterministic tags.
+4. Store section/card metadata.
+
+### Phase 3
+
+1. Embed chunks.
+2. Write vectors and payload metadata to Qdrant.
+3. Retrieve by tag and semantic query through Haystack/Qdrant adapter.
+
+### Phase 4
+
+1. Build prompt from tender requirements and retrieved cards.
+2. Generate candidate content through an OpenAI-compatible adapter.
+3. Return generated content with citations, risks, and `need_human_review = true`.
+
+## Key Interfaces
+
+### Document Metadata
+
+See `docs/ai/12-phase1-api-persistence.md`.
+
+### Chunk Payload
+
+Future retrieval payload should include:
+
+- `doc_id`
+- `doc_title`
+- `page_no`
+- `section_path`
+- `chunk_type`
+- `tags`
+- `bbox`
+- `table_html`
+- `ocr_confidence`
+- `source_uri`
+- `ingest_version`
+
+### Generation Result
+
+Every generated response must include:
+
+- `target_tag`
+- `generated_content`
+- `citations`
+- `risks`
+- `need_human_review = true`
+
+## Architecture Decisions
+
+1. Use external platforms as references, not as the mainline codebase.
+2. Keep all heavy capabilities behind adapters.
+3. Keep Phase 1 independent of RAG dependencies.
+4. Prefer local SQLite and local file storage until the demo proves the vertical slice.
+5. Add Qdrant/Haystack only when retrieval work starts.
+6. Add Docling only when parsing work starts.
+7. Add PaddleOCR only when scanned documents become a required validation path.
+
diff --git a/docs/ai/16-phase1-test-cases.md b/docs/ai/16-phase1-test-cases.md
new file mode 100644
index 0000000..09f0a5a
--- /dev/null
+++ b/docs/ai/16-phase1-test-cases.md
@@ -0,0 +1,431 @@
+# Phase 1 Test Spec v0.1
+
+## Purpose
+
+This document is the internal acceptance test specification for the Phase 1 backend foundation.
+
+It is suitable for developers and agents implementing Phase 1 tests. It is not a customer-facing PRD and not a full Demo acceptance document.
+
+Phase 1 verifies only:
+
+1. FastAPI application startup.
+2. `GET /health`.
+3. `POST /api/files/upload`.
+4. Local file persistence.
+5. SQLite metadata persistence.
+6. Configuration isolation.
+7. Windows-local smoke workflow.
+
+Phase 1 is not the customer-facing knowledge-base Demo. Passing Phase 1 does not mean the product can yet demonstrate OCR, document parsing, knowledge cards, retrieval, generation, source tracing, risk prompts, or frontend Demo workflows.
+
+## Scope Boundary
+
+In scope:
+
+1. Backend foundation tests.
+2. Upload API contract tests.
+3. File-storage safety tests.
+4. SQLite metadata tests.
+5. Local script and manual smoke evidence.
+
+Out of scope:
+
+1. OCR.
+2. LLM calls.
+3. Embeddings.
+4. Qdrant or any vector database.
+5. Haystack pipeline execution.
+6. Knowledge-card generation.
+7. Tender-file analysis.
+8. Frontend Demo page.
+9. User accounts.
+10. Word/PDF export.
+11. Customer-facing PRD validation.
+
+## Test Environment Assumptions
+
+1. Run tests from the repository root, not from a hard-coded absolute path.
+2. Primary shell is Windows PowerShell.
+3. Tests should run without WSL.
+4. Python should be 3.11 or newer unless Phase 1 selects a stricter version.
+5. The FastAPI app entrypoint should be importable by tests.
+6. Automated tests must use isolated temporary paths for upload storage and SQLite database files.
+7. Automated tests must not write to real source-material folders.
+8. Automated tests must not require external services or internet access.
+9. Localhost smoke checks should use `curl.exe --noproxy "*"` on this machine.
+
+## Expected Test File Layout
+
+Phase 1 should create a focused automated test suite:
+
+```text
+backend/tests/
+|-- test_health.py
+|-- test_upload_contract.py
+|-- test_upload_validation.py
+|-- test_storage.py
+|-- test_database.py
+`-- test_phase1_boundaries.py
+```
+
+Files may be merged if the implementation is small, but the coverage areas must remain visible.
+
+Harness commands such as `ai-status`, `ai-doctor`, and `scripts/ai_check.ps1` are delivery checks, not core business pytest assertions.
+
+## Required Test Fixtures
+
+Use pytest fixtures for isolation:
+
+| Fixture | Purpose |
+| --- | --- |
+| `tmp_path` | Temporary upload directory and SQLite database path. |
+| `test_settings` | Settings override for upload root, database path, and optional upload limits. |
+| `client` | FastAPI `TestClient` bound to the app with test settings. |
+| `sample_text_file` | Small upload payload such as `hello bid knowledge`. |
+| `empty_file` | Zero-byte file for negative validation. |
+| `unsafe_filename` | Filename such as `../evil.txt` or `..\\evil.txt`. |
+| `unicode_filename` | Filename such as `投标 测试 文件.txt`. |
+| `duplicate_filename_files` | Two files with the same original filename and different byte content. |
+
+The implementation must expose settings in a way tests can override without changing global developer-machine state.
+
+## Test Data Rules
+
+Use synthetic files for automated tests.
+
+Allowed automated fixtures:
+
+1. Small `.txt` files.
+2. Small `.pdf` or `.docx` fixtures only if generated locally and committed intentionally.
+3. In-memory bytes created inside tests.
+
+Do not use:
+
+1. Large customer-provided sample files.
+2. Files from `C:\Users\26561\Desktop\模型训练资料\甲方提供资料`.
+3. Files copied from reference repositories.
+4. Network downloads.
+
+## Phase 1 API Contract
+
+### Upload Endpoint
+
+Endpoint:
+
+```text
+POST /api/files/upload
+```
+
+Content type:
+
+```text
+multipart/form-data
+```
+
+Form fields:
+
+| Field | Required | Allowed value |
+| --- | --- | --- |
+| `file` | yes | uploaded file |
+| `doc_role` | yes | `historical_bid` or `tender` |
+
+Allowed Phase 1 file extensions:
+
+```text
+.txt
+.pdf
+.doc
+.docx
+```
+
+Success status:
+
+```text
+201 Created
+```
+
+Success response:
+
+```json
+{
+  "document_id": "string",
+  "original_filename": "string",
+  "doc_role": "historical_bid",
+  "parse_status": "pending",
+  "file_size": 123,
+  "created_at": "2026-06-27T12:00:00Z"
+}
+```
+
+The success response must not expose absolute local filesystem paths.
+
+Error response:
+
+```json
+{
+  "error_code": "INVALID_DOC_ROLE",
+  "message": "Unsupported document role",
+  "details": {}
+}
+```
+
+Required Phase 1 error codes:
+
+| Scenario | HTTP status | `error_code` |
+| --- | --- | --- |
+| Missing file | `400 Bad Request` | `MISSING_FILE` |
+| Missing `doc_role` | `400 Bad Request` | `MISSING_DOC_ROLE` |
+| Invalid `doc_role` | `400 Bad Request` | `INVALID_DOC_ROLE` |
+| Empty file | `400 Bad Request` | `EMPTY_FILE` |
+| Unsafe filename | `400 Bad Request` | `UNSAFE_FILENAME` |
+| File too large | `413 Payload Too Large` | `FILE_TOO_LARGE` |
+| Unsupported file extension | `400 Bad Request` | `UNSUPPORTED_FILE_TYPE` |
+| File write failure | `500 Internal Server Error` | `FILE_WRITE_FAILED` |
+| Metadata write failure | `500 Internal Server Error` | `METADATA_WRITE_FAILED` |
+
+### Health Endpoint
+
+Endpoint:
+
+```text
+GET /health
+```
+
+Success response:
+
+```json
+{
+  "status": "ok"
+}
+```
+
+`GET /health` is a shallow app-health endpoint in Phase 1. It must not require SQLite, OCR, LLM, Qdrant, Haystack, or internet access.
+
+## SQLite Contract
+
+Table:
+
+```text
+documents
+```
+
+Required fields:
+
+| Column | Type | Required | Notes |
+| --- | --- | --- | --- |
+| `id` | text primary key | yes | server-generated document id |
+| `original_filename` | text | yes | original filename from upload metadata |
+| `stored_filename` | text | yes | backend-generated filename |
+| `stored_path` | text | yes | relative path under upload root |
+| `file_ext` | text | yes | normalized lower-case extension |
+| `content_type` | text nullable | no | client-provided MIME type, reference only |
+| `file_size` | integer | yes | uploaded byte length |
+| `doc_role` | text | yes | `historical_bid` or `tender` |
+| `created_at` | text | yes | ISO-8601 timestamp |
+| `updated_at` | text | yes | ISO-8601 timestamp |
+| `parse_status` | text | yes | default `pending` |
+| `error_message` | text nullable | no | default null |
+
+Phase 1 only creates rows with `parse_status = pending`.
+
+## File Safety Rules
+
+1. Stored filename must be generated by the backend, for example `<document_id><safe_extension>`.
+2. Original filename is preserved only as metadata.
+3. User-provided filenames must never be used as direct storage paths.
+4. Stored files must resolve under the configured upload root.
+5. Path traversal filenames must be rejected or fully neutralized before storage.
+6. Duplicate original filenames must not overwrite stored files.
+7. Extension checks are a basic Phase 1 gate, not proof that content is safe.
+8. Phase 1 stores bytes and metadata only; it does not parse or execute uploaded files.
+9. If validation fails, no file and no metadata row should remain.
+10. If file write fails, no metadata row should be inserted.
+11. If metadata insert fails after file write, the stored file must be cleaned up.
+
+## Priority Levels
+
+| Priority | Meaning |
+| --- | --- |
+| P0 | Must pass before Phase 1 can be called complete. |
+| P1 | Should pass before Phase 1 handoff; required if the related code exists. |
+| P2 | Useful hardening; may be deferred only with an explicit note in `.ai/verification.md`. |
+
+## Automated Test Cases
+
+### Health Endpoint
+
+| ID | Priority | Scenario | Preconditions | Steps | Expected Result |
+| --- | --- | --- | --- | --- | --- |
+| TC-HEALTH-001 | P0 | Health endpoint returns stable shallow status. | App is importable in test mode. | Send `GET /health`. | HTTP 200. Response JSON is exactly `{"status": "ok"}`. |
+| TC-HEALTH-002 | P0 | Health endpoint has no external dependency. | Qdrant, OCR, LLM, internet, and parser tools are unavailable. | Send `GET /health`. | HTTP 200. No attempt to initialize external services. |
+| TC-HEALTH-003 | P1 | Health response content type is JSON. | App is running. | Send `GET /health`. | `content-type` includes `application/json`. |
+
+### Upload Success Contract
+
+| ID | Priority | Scenario | Preconditions | Steps | Expected Result |
+| --- | --- | --- | --- | --- | --- |
+| TC-UPLOAD-001 | P0 | Upload accepts historical bid role. | Test client uses temp upload dir and temp SQLite DB. | POST `/api/files/upload` with `doc_role=historical_bid` and small `.txt` file. | HTTP `201 Created`. Response follows the documented success JSON contract. |
+| TC-UPLOAD-002 | P0 | Upload accepts tender role. | Same as TC-UPLOAD-001. | POST `/api/files/upload` with `doc_role=tender` and small `.txt` file. | HTTP `201 Created`. Response `doc_role` is `tender`. |
+| TC-UPLOAD-003 | P0 | Upload response has required fields. | Valid upload succeeds. | Inspect response JSON. | Fields exist: `document_id`, `original_filename`, `doc_role`, `parse_status`, `file_size`, `created_at`. |
+| TC-UPLOAD-004 | P0 | Upload response uses fixed pending parse status. | Valid upload succeeds. | Inspect response JSON. | `parse_status` is exactly `pending`. |
+| TC-UPLOAD-005 | P0 | Upload response does not expose absolute paths. | Valid upload succeeds. | Inspect response JSON values. | No value contains the local upload root or drive-qualified path. |
+| TC-UPLOAD-006 | P1 | Upload supports Chinese and spaces in original filename. | Unicode filename fixture exists. | POST `投标 测试 文件.txt`. | HTTP `201 Created`. `original_filename` is preserved. Stored filename remains backend-generated. |
+
+### Upload Validation And Errors
+
+| ID | Priority | Scenario | Preconditions | Steps | Expected Result |
+| --- | --- | --- | --- | --- | --- |
+| TC-ERR-001 | P0 | Missing file is rejected. | App is running in test mode. | POST with `doc_role=historical_bid` and no file field. | HTTP 400. Error JSON has `error_code=MISSING_FILE`. No file or metadata row remains. |
+| TC-ERR-002 | P0 | Missing doc role is rejected. | App is running in test mode. | POST with a file and no `doc_role`. | HTTP 400. Error JSON has `error_code=MISSING_DOC_ROLE`. No file or metadata row remains. |
+| TC-ERR-003 | P0 | Invalid doc role is rejected. | App is running in test mode. | POST with `doc_role=unknown` and a small file. | HTTP 400. Error JSON has `error_code=INVALID_DOC_ROLE`. No file or metadata row remains. |
+| TC-ERR-004 | P0 | Empty file is rejected. | Empty file fixture exists. | POST zero-byte file with valid `doc_role`. | HTTP 400. Error JSON has `error_code=EMPTY_FILE`. No file or metadata row remains. |
+| TC-ERR-005 | P0 | Unsafe filename is rejected. | Unsafe filename fixture exists. | POST a file named `../evil.txt` or `..\\evil.txt`. | HTTP 400. Error JSON has `error_code=UNSAFE_FILENAME`, or request succeeds only if storage proves no path escape. Preferred Phase 1 behavior is rejection. |
+| TC-ERR-006 | P0 | Unsupported file extension is rejected. | `.exe` fixture exists. | POST `payload.exe`. | HTTP 400. Error JSON has `error_code=UNSUPPORTED_FILE_TYPE`. No file or metadata row remains. |
+| TC-ERR-007 | P1 | Oversized upload is rejected when max size is configured. | Test settings set small max upload size. | POST file larger than configured max. | HTTP 413. Error JSON has `error_code=FILE_TOO_LARGE`. No file or metadata row remains. |
+| TC-ERR-008 | P1 | Error response shape is stable. | Any invalid request is sent. | Inspect error JSON. | Response contains `error_code`, `message`, and `details`. |
+
+### File Storage
+
+| ID | Priority | Scenario | Preconditions | Steps | Expected Result |
+| --- | --- | --- | --- | --- | --- |
+| TC-STORAGE-001 | P0 | Upload directory is created if missing. | Temp upload root does not exist before upload. | Perform valid upload. | Upload root is created automatically. |
+| TC-STORAGE-002 | P0 | Stored file bytes match uploaded bytes. | Valid upload succeeds. | Read stored file from test upload root. | Stored bytes equal request bytes. |
+| TC-STORAGE-003 | P0 | Stored file remains under configured upload root. | Valid upload succeeds. | Resolve stored path. | Resolved path starts with configured upload root. |
+| TC-STORAGE-004 | P0 | Stored filename is backend-generated. | Valid upload succeeds. | Inspect metadata row. | `stored_filename` is not the raw original filename and includes a generated identifier or equivalent safe name. |
+| TC-STORAGE-005 | P1 | Duplicate original filenames do not overwrite files. | Two files with same original filename exist. | Upload both files. | Both requests succeed. Stored filenames are distinct. Metadata has two rows. Stored bytes for both files are correct. |
+| TC-STORAGE-006 | P1 | Failed validation leaves no orphan file. | Invalid role, empty file, or unsupported extension request is sent. | Inspect upload root after response. | No unexpected file remains. |
+
+### SQLite Persistence
+
+| ID | Priority | Scenario | Preconditions | Steps | Expected Result |
+| --- | --- | --- | --- | --- | --- |
+| TC-DB-001 | P0 | SQLite database initializes. | Temp DB path points to a non-existing file. | Start app or perform first valid upload. | Database file is created. `documents` table exists. |
+| TC-DB-002 | P0 | Valid upload inserts one metadata row. | Temp DB is empty. | Perform valid upload. | Exactly one row is inserted for the uploaded document. |
+| TC-DB-003 | P0 | Metadata row stores required fields. | Valid upload succeeds. | Query metadata row. | Required columns exist and are populated: `id`, `original_filename`, `stored_filename`, `stored_path`, `file_ext`, `file_size`, `doc_role`, `created_at`, `updated_at`, `parse_status`. |
+| TC-DB-004 | P0 | Nullable metadata defaults are safe. | Valid upload succeeds. | Query metadata row. | `content_type` may be null or client value; `error_message` is null. |
+| TC-DB-005 | P0 | Parse status remains pending. | Valid upload succeeds. | Query metadata row. | `parse_status` is exactly `pending`; no parser output is required. |
+| TC-DB-006 | P0 | Failed upload does not insert metadata row. | Temp DB is empty. | Send invalid upload request. | Row count remains zero. |
+| TC-DB-007 | P1 | Multiple uploads create multiple rows. | Temp DB is empty. | Upload two valid files. | Two distinct document ids and two rows exist. |
+
+### Atomicity And Cleanup
+
+| ID | Priority | Scenario | Preconditions | Steps | Expected Result |
+| --- | --- | --- | --- | --- | --- |
+| TC-ATOMIC-001 | P0 | File write failure does not insert metadata. | Storage layer can be forced to fail or upload root is made unwritable in a controlled test. | Perform upload. | Error JSON has `error_code=FILE_WRITE_FAILED`. No metadata row is inserted. |
+| TC-ATOMIC-002 | P1 | Metadata write failure cleans up written file. | Database layer can be forced to fail after file write. | Perform upload. | Error JSON has `error_code=METADATA_WRITE_FAILED`. Stored file is deleted. No metadata row remains. |
+
+If fault injection is too costly for Phase 1, record TC-ATOMIC-001 and TC-ATOMIC-002 as explicit follow-up risks in `.ai/verification.md`; do not silently ignore them.
+
+### Configuration
+
+| ID | Priority | Scenario | Preconditions | Steps | Expected Result |
+| --- | --- | --- | --- | --- | --- |
+| TC-CONFIG-001 | P0 | Upload root is configurable for tests. | Test settings point upload root to `tmp_path`. | Perform valid upload. | File is written under `tmp_path`, not real `data/uploads`. |
+| TC-CONFIG-002 | P0 | Database path is configurable for tests. | Test settings point DB to `tmp_path/test.sqlite3`. | Perform valid upload. | Metadata is written to temp DB, not local dev DB. |
+| TC-CONFIG-003 | P1 | Default local config points under repository data directory. | App runs without test overrides. | Inspect settings. | Upload root and DB path resolve under documented local data paths. |
+| TC-CONFIG-004 | P1 | Missing parent folders are created safely. | Configured upload/DB parent directories do not exist. | Start app or perform upload. | Required folders are created without touching source-material folders. |
+
+### Phase 1 Boundary Tests
+
+| ID | Priority | Scenario | Preconditions | Steps | Expected Result |
+| --- | --- | --- | --- | --- | --- |
+| TC-BOUNDARY-001 | P0 | Phase 1 code does not require vector services. | No Qdrant or vector service is running. | Run Phase 1 automated tests. | Tests pass without vector service. |
+| TC-BOUNDARY-002 | P0 | Phase 1 code does not require LLM credentials. | No LLM API key is configured. | Run Phase 1 automated tests. | Tests pass without LLM credentials. |
+| TC-BOUNDARY-003 | P0 | Phase 1 upload does not parse documents. | Valid upload succeeds. | Inspect response and DB row. | Parse status is pending; no OCR, LLM, parser, or embedding output is expected. |
+| TC-BOUNDARY-004 | P1 | Deferred endpoints are not exposed as complete features. | App is running. | Probe non-Phase-1 routes only if router list exposes them. | Any non-Phase-1 route is absent, clearly stubbed, or returns not implemented; it must not pretend to be complete. |
+
+## Delivery Command Checks
+
+These checks are required for Phase 1 completion evidence, but they should not be mixed into core business pytest files.
+
+| ID | Priority | Scenario | Command | Expected Result |
+| --- | --- | --- | --- | --- |
+| DC-001 | P0 | Harness status confirms large mode. | `ai-status` | Output reports initialized project and `mode: large`. |
+| DC-002 | P0 | Harness doctor validates workflow state. | `ai-doctor` | State schema and large-mode files pass. Uncommitted working tree warning is acceptable during active work. |
+| DC-003 | P0 | Windows project check script runs. | `.\scripts\ai_check.ps1` | Script exits 0 and runs real Phase 1 checks after implementation. |
+| DC-004 | P1 | Bash project check is recorded when unavailable. | `bash ./scripts/ai_check.sh` | If unavailable, record blocker in `.ai/verification.md`; do not claim it passed. |
+
+## Manual Smoke Cases
+
+Manual smoke is required after the server can run locally.
+
+### MS-001 Health Smoke
+
+Command:
+
+```powershell
+curl.exe --noproxy "*" http://127.0.0.1:8000/health
+```
+
+Expected:
+
+```json
+{"status":"ok"}
+```
+
+### MS-002 Upload Smoke
+
+Create a temporary file:
+
+```powershell
+Set-Content -Path .\data\samples\phase1-smoke.txt -Value "hello bid knowledge"
+```
+
+Upload it:
+
+```powershell
+curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/files/upload" `
+  -F "doc_role=historical_bid" `
+  -F "file=@.\data\samples\phase1-smoke.txt"
+```
+
+Expected:
+
+1. HTTP `201 Created`.
+2. Response follows the upload success JSON contract.
+3. A stored file appears under configured upload root.
+4. SQLite contains one metadata row.
+5. Stored file bytes match the source file.
+
+## Phase 1 Definition Of Done
+
+Phase 1 is complete only when:
+
+1. FastAPI app starts locally on Windows.
+2. `GET /health` returns stable JSON response.
+3. `POST /api/files/upload` accepts `historical_bid` and `tender`.
+4. Uploaded file bytes are persisted under configured upload root.
+5. Metadata is persisted into configured SQLite database.
+6. Invalid requests do not leave orphan files or metadata rows.
+7. Upload response follows the documented JSON contract.
+8. Error responses follow the documented JSON contract.
+9. SQLite `documents` table follows the documented field contract.
+10. Phase 1 does not initialize OCR, LLM, vector database, parser, embedding, or frontend Demo logic.
+11. All P0 automated tests pass.
+12. Any deferred P1/P2 item is recorded in `.ai/verification.md`.
+13. `ai-status`, `ai-doctor`, and `.\scripts\ai_check.ps1` evidence is recorded.
+14. Manual health and upload smoke evidence is recorded, unless server startup is explicitly blocked.
+
+Phase 1 is only the backend foundation for later document parsing and knowledge-base capability. It is not the customer-facing Demo.
+
+## Suggested Pytest Mapping
+
+| Test file | Case IDs |
+| --- | --- |
+| `backend/tests/test_health.py` | TC-HEALTH-001 to TC-HEALTH-003 |
+| `backend/tests/test_upload_contract.py` | TC-UPLOAD-001 to TC-UPLOAD-006 |
+| `backend/tests/test_upload_validation.py` | TC-ERR-001 to TC-ERR-008 |
+| `backend/tests/test_storage.py` | TC-STORAGE-001 to TC-STORAGE-006 |
+| `backend/tests/test_database.py` | TC-DB-001 to TC-DB-007 |
+| `backend/tests/test_phase1_boundaries.py` | TC-BOUNDARY-001 to TC-BOUNDARY-004 |
+
+Delivery command checks should be recorded in `.ai/verification.md` or CI logs, not treated as upload/business pytest cases.
+
+## Common Failure Diagnosis
+
+1. If localhost calls fail, check proxy variables first and use `curl.exe --noproxy "*"`.
+2. If cleanup fails on Windows, make sure SQLite connections are closed before deleting temp directories.
+3. If tests write to real `data/uploads`, the settings override is broken.
+4. If tests require customer sample files, replace them with synthetic fixtures.
+5. If tests require external services, the implementation crossed the Phase 1 boundary.
+6. If response fields drift from this document, fix the implementation or update the API contract intentionally before changing tests.
diff --git a/docs/ai/README.md b/docs/ai/README.md
new file mode 100644
index 0000000..9dce83e
--- /dev/null
+++ b/docs/ai/README.md
@@ -0,0 +1,42 @@
+# docs/ai
+
+This directory stores durable AI context for the 投标智能知识库能力验证版 Demo.
+
+Read these files before implementation work:
+
+1. `00-project-brief.md` - product goal and current phase.
+2. `01-scope-boundary.md` - in-scope, out-of-scope, and Phase 1 limits.
+3. `02-architecture.md` - future backend module and adapter boundaries.
+4. `03-data-model.md` - domain entities and JSON result shapes.
+5. `04-api-contract.md` - expected API surface across phases.
+6. `05-dev-rules.md` - project-specific engineering rules.
+7. `06-verification.md` - MVP and phase verification criteria.
+8. `07-source-materials.md` - external source material paths.
+9. `08-tech-selection.md` - selected stack and rejected alternatives.
+10. `09-phase-roadmap.md` - staged delivery plan.
+11. `10-phase1-dev-spec.md` - exact Phase 1 implementation boundary.
+12. `11-local-dev-env.md` - local runtime, paths, and script expectations.
+13. `12-phase1-api-persistence.md` - upload API and SQLite details.
+14. `13-phase1-verification-checklist.md` - required checks before completion.
+15. `14-reference-reuse-strategy.md` - direct二开 decision and reference-repo rules.
+16. `15-target-architecture.md` - target architecture and phase data flow.
+17. `16-phase1-test-cases.md` - detailed Phase 1 test-case specification.
+
+Python backend profile files from Auto_AICoding_Harness are also present:
+
+- `python.md`
+- `frameworks.md`
+- `dependency.md`
+- `security.md`
+- `testing.md`
+- `typing.md`
+- `data.md`
+- `async.md`
+- `packaging.md`
+- `observability.md`
+- `performance.md`
+- `verification-matrix.md`
+
+Source documents and sample-material indexes live under `docs/source-materials/`.
+
+Task runtime state belongs in `.ai/`, not in this directory.
diff --git a/docs/ai/async.md b/docs/ai/async.md
new file mode 100644
index 0000000..f85600c
--- /dev/null
+++ b/docs/ai/async.md
@@ -0,0 +1,18 @@
+# Python Async And Concurrency Guidance
+
+## Concurrency Risk
+
+- Treat asyncio, threading, multiprocessing, Celery, RQ, Dramatiq, and scheduler changes as concurrency risk.
+- Keep sync and async boundaries explicit.
+- Avoid blocking calls inside event-loop code unless they are isolated with a documented executor strategy.
+
+## Async Code Notes
+
+- Preserve timeout, cancellation, retry, and exception propagation semantics.
+- Be explicit about context propagation for tracing, request state, auth, and logging.
+- Avoid unbounded task creation, queues, retries, or worker concurrency without backpressure notes.
+
+## Verification
+
+- Prefer deterministic tests for timeout, cancellation, and failure paths.
+- For worker changes, document queue, retry, dead-letter, and idempotency behavior.
diff --git a/docs/ai/check-rules/drafts/init-large-spec.md b/docs/ai/check-rules/drafts/init-large-spec.md
new file mode 100644
index 0000000..aefd56a
--- /dev/null
+++ b/docs/ai/check-rules/drafts/init-large-spec.md
@@ -0,0 +1,19 @@
+# Check Rule Draft
+
+## Status
+
+DRAFT_NOT_ENFORCED
+
+## Activation Policy
+
+This draft must not be added to `docs/ai/check-rules/index.md` automatically. It requires explicit human approval before becoming an enforced rule.
+
+## Trigger
+
+- task_id: init-large
+- gate: spec
+- created_at: 2026-06-28T00:50:22+08:00
+
+## Candidate Rule
+
+Before rerunning `spec` review, confirm the rejected issue is fixed and documented in `.ai/verification.md`.
diff --git a/docs/ai/check-rules/index.md b/docs/ai/check-rules/index.md
new file mode 100644
index 0000000..b621350
--- /dev/null
+++ b/docs/ai/check-rules/index.md
@@ -0,0 +1,5 @@
+# Check Rules
+
+This directory may contain human-approved check rules and generated drafts.
+
+Generated drafts under `drafts/` are not enforced automatically. Move or reference a draft here only after explicit human approval.
diff --git a/docs/ai/data.md b/docs/ai/data.md
new file mode 100644
index 0000000..32342d3
--- /dev/null
+++ b/docs/ai/data.md
@@ -0,0 +1,18 @@
+# Python Data And Persistence Guidance
+
+## Persistence Risk
+
+- Treat SQLAlchemy, Django ORM, Alembic, Django migrations, raw SQL, and data model changes as data compatibility risk.
+- Review transaction boundaries, session scope, lazy loading, cascade behavior, and retry semantics.
+- Avoid silent migration or query behavior changes without rollback notes.
+
+## Model And Serialization Changes
+
+- Treat Pydantic, dataclass, attrs, TypedDict, marshmallow, protobuf, and ORM model changes as contract changes.
+- Check N+1 query risk, pagination behavior, and filtering defaults.
+- State migration order and compatibility when schema changes affect deployed services.
+
+## Verification
+
+- Prefer repository/service tests that cover success, validation failure, missing data, and rollback paths.
+- Record database engine and migration command assumptions when relevant.
diff --git a/docs/ai/dependency.md b/docs/ai/dependency.md
new file mode 100644
index 0000000..d65e9b5
--- /dev/null
+++ b/docs/ai/dependency.md
@@ -0,0 +1,18 @@
+# Python Dependency Guidance
+
+## Dependency Risk
+
+- Treat dependency changes as security, lockfile, packaging, and deployment risk.
+- Keep direct dependencies explicit and avoid unnecessary broad upgrades.
+- Check whether dependency versions are constrained by deployment images, serverless runtimes, or platform policy.
+
+## Serialization And Frameworks
+
+- Treat changes to JSON schemas, Pydantic models, dataclasses, marshmallow schemas, protobufs, or ORM models as contract changes.
+- Treat FastAPI, Django, Flask, Celery, SQLAlchemy, or similar configuration changes as runtime behavior changes.
+- Document migration impact for settings, environment variables, middleware, and background workers.
+
+## Verification
+
+- Run dependency-aware tests or import smoke tests after dependency changes.
+- Record exact commands and skipped checks in `.ai/verification.md` for medium or large work.
diff --git a/docs/ai/frameworks.md b/docs/ai/frameworks.md
new file mode 100644
index 0000000..47cfdfe
--- /dev/null
+++ b/docs/ai/frameworks.md
@@ -0,0 +1,18 @@
+# Python Framework Guidance
+
+## Framework Discovery
+
+- Identify whether the project uses FastAPI, Django, Flask, Starlette, Celery, or another framework before applying conventions.
+- Prefer existing routing, dependency injection, settings, middleware, and test-client patterns.
+- Treat decorator, middleware, settings, and lifecycle-hook changes as runtime behavior changes.
+
+## API Framework Notes
+
+- For FastAPI or Starlette, review dependency injection, request models, response models, background tasks, and async boundaries.
+- For Django, review settings, middleware, apps, migrations, ORM behavior, and management commands.
+- For Flask, review app factory, blueprints, context usage, and extension initialization.
+
+## Verification
+
+- Use framework test clients or integration tests for routing, middleware, authentication, and error handling changes.
+- Record any external service assumptions in `.ai/verification.md` for medium or large work.
diff --git a/docs/ai/migrations/index.md b/docs/ai/migrations/index.md
new file mode 100644
index 0000000..14002a4
--- /dev/null
+++ b/docs/ai/migrations/index.md
@@ -0,0 +1,4 @@
+# Migrations
+
+Migration declarations are optional hardening metadata for existing template updates.
+They must not change public directory semantics, introduce `.harness/`, or rename `small / medium / large`.
diff --git a/docs/ai/observability.md b/docs/ai/observability.md
new file mode 100644
index 0000000..d64cb8a
--- /dev/null
+++ b/docs/ai/observability.md
@@ -0,0 +1,18 @@
+# Python Observability Guidance
+
+## Logging
+
+- Keep logs actionable and avoid leaking secrets, tokens, passwords, or PII.
+- Preserve existing structured logging conventions.
+- Include useful request, job, or correlation identifiers when already supported by the project.
+
+## Metrics And Tracing
+
+- For latency-sensitive paths, consider whether metrics or tracing need updates.
+- For background workers, document retry, dead-letter, and failure visibility expectations.
+- Follow existing OpenTelemetry, Prometheus, StatsD, or framework-specific conventions when present.
+
+## Runtime Operations
+
+- Note deployment impact for worker concurrency, process model, queue consumers, or async event loops.
+- Treat timeout, retry, and connection-pool changes as operational risk.
diff --git a/docs/ai/packaging.md b/docs/ai/packaging.md
new file mode 100644
index 0000000..00d5298
--- /dev/null
+++ b/docs/ai/packaging.md
@@ -0,0 +1,18 @@
+# Python Packaging Guidance
+
+## Environment Discovery
+
+- Inspect `pyproject.toml`, `requirements*.txt`, `setup.cfg`, `setup.py`, `tox.ini`, `noxfile.py`, or project docs before running commands.
+- Prefer existing project tooling such as `uv`, `poetry`, `hatch`, `pip-tools`, `tox`, or `nox` when already configured.
+- Do not add a package manager or formatter only because it is familiar.
+
+## Dependency Risk
+
+- Treat dependency changes as security, lockfile, and deployment compatibility risk.
+- Keep runtime, development, test, and optional dependencies distinct.
+- When lockfiles exist, update them consistently with the project convention.
+
+## Verification
+
+- Record the exact environment and command used when running tests or checks.
+- Prefer virtual environments such as `venv` or the project-defined tool environment.
diff --git a/docs/ai/performance.md b/docs/ai/performance.md
new file mode 100644
index 0000000..5f879d7
--- /dev/null
+++ b/docs/ai/performance.md
@@ -0,0 +1,18 @@
+# Python Performance Guidance
+
+## Performance Risk
+
+- Treat hot-path allocation, serialization, ORM access, network calls, import-time work, and cache changes as performance-sensitive.
+- Check startup time, memory growth, event-loop blocking, and connection-pool behavior when relevant.
+- Avoid broad caching changes without invalidation and memory-growth notes.
+
+## Runtime Considerations
+
+- Note GIL, multiprocessing, thread pool, and async event-loop implications when concurrency changes.
+- For batch or streaming work, check backpressure, chunking, and pagination behavior.
+- Keep profiling assumptions separate from correctness changes unless the target project owns them.
+
+## Verification
+
+- Prefer existing benchmarks or project-defined performance smoke tests.
+- If no benchmark exists, record manual risk assessment and the reason a benchmark was not run.
diff --git a/docs/ai/python.md b/docs/ai/python.md
new file mode 100644
index 0000000..dccae47
--- /dev/null
+++ b/docs/ai/python.md
@@ -0,0 +1,21 @@
+# Python Backend Guidance
+
+## Review Focus
+
+- Keep public API and wire-format changes explicit.
+- Treat dependency, packaging, import-path, and configuration changes as compatibility risks.
+- Prefer small, testable functions around IO, serialization, and business rules.
+- Preserve existing framework conventions instead of introducing new ones without a clear reason.
+
+## Runtime Notes
+
+- State the expected Python version before using new language or typing features.
+- Keep sync, async, thread, and process boundaries explicit.
+- Avoid hidden global state in request handlers, workers, and tests.
+- Document migration impact for module moves, settings changes, and package metadata changes.
+
+## Agent Checklist
+
+- Inspect `pyproject.toml`, `requirements*.txt`, `setup.cfg`, `tox.ini`, or project docs before choosing commands.
+- Prefer project-defined scripts or task runners when present.
+- Record build, test, lint, and type-check commands in `.ai/verification.md` for medium or large work.
diff --git a/docs/ai/security.md b/docs/ai/security.md
new file mode 100644
index 0000000..f1f519f
--- /dev/null
+++ b/docs/ai/security.md
@@ -0,0 +1,18 @@
+# Python Security Guidance
+
+## Review Focus
+
+- Treat authentication, authorization, session, token, CORS, CSRF, and input-validation changes as high risk.
+- Check deserialization, path traversal, SSRF, SQL injection, command injection, pickle usage, and template injection surfaces.
+- Do not log secrets, bearer tokens, cookies, passwords, or sensitive request bodies.
+
+## Dependency And Framework Security
+
+- Review dependency updates for CVEs and transitive impact where project tooling supports it.
+- For FastAPI, Django, Flask, or Starlette security changes, verify both allowed and denied paths.
+- Keep security defaults explicit; avoid relying on incidental framework behavior.
+
+## Verification
+
+- Add negative authorization tests for protected endpoints.
+- Record skipped security tests and the reason in `.ai/verification.md` for medium or large work.
diff --git a/docs/ai/tasks/README.md b/docs/ai/tasks/README.md
new file mode 100644
index 0000000..10af412
--- /dev/null
+++ b/docs/ai/tasks/README.md
@@ -0,0 +1,14 @@
+# Task Evidence Chain
+
+Each subdirectory under `docs/ai/tasks/` represents one large-mode task keyed by `.ai/state.json::task_id`.
+
+Expected files:
+
+- `00-prd.md`
+- `01-spec.md`
+- `02-tech-design.md`
+- `03-implementation-plan.md`
+- `04-diff-review.md`
+- `05-verification.md`
+- `06-risk-and-rollback.md`
+- `07-handoff.md`
diff --git a/docs/ai/tasks/init-large/00-prd.md b/docs/ai/tasks/init-large/00-prd.md
new file mode 100644
index 0000000..e1de3b9
--- /dev/null
+++ b/docs/ai/tasks/init-large/00-prd.md
@@ -0,0 +1,22 @@
+# Epic - Large-Mode Phase 1 Preparation
+
+## Objective
+
+Make this repository ready for Phase 1 development under Auto_AICoding_Harness `large` mode.
+
+## Outcome
+
+Before any business code is written, the repository must contain:
+
+1. Large-mode harness state.
+2. Project-level rule that future development must use large mode.
+3. Phase 1 development spec.
+4. Local development environment guide.
+5. Phase 1 API and persistence details.
+6. Phase 1 verification checklist.
+7. Updated `.ai` task artifacts and handoff.
+
+## Non-Goal
+
+This task does not implement FastAPI, upload handling, SQLite code, parsing, retrieval, LLM calls, or UI.
+
diff --git a/docs/ai/tasks/init-large/01-spec.md b/docs/ai/tasks/init-large/01-spec.md
new file mode 100644
index 0000000..b8d6bcc
--- /dev/null
+++ b/docs/ai/tasks/init-large/01-spec.md
@@ -0,0 +1,156 @@
+# Spec - Phase 1 Backend Foundation
+
+## Objective
+
+Implement the smallest runnable FastAPI backend foundation for the 投标智能知识库能力验证版 Demo.
+
+Phase 1 proves that the service can start, accept an uploaded file, save it under a configurable local upload root, and persist document metadata in SQLite.
+
+Phase 1 is a backend foundation milestone. It is not the customer-facing Demo acceptance milestone.
+
+## Required Execution Mode
+
+This task must run under Auto_AICoding_Harness `large` mode with the `python-backend-service` profile.
+
+Before implementation:
+
+1. Run `ai-status` or `ai-doctor`.
+2. Confirm `.ai/state.json` reports `"mode": "large"`.
+3. Use large-mode gates according to `AGENTS.md`.
+4. Use subagent orchestration because the user explicitly requested it.
+
+## In Scope
+
+Implement only:
+
+1. FastAPI application startup.
+2. `GET /health`.
+3. `POST /api/files/upload`.
+4. Upload success response with HTTP `201 Created`.
+5. Upload success fields:
+   - `document_id`
+   - `original_filename`
+   - `doc_role`
+   - `parse_status`
+   - `file_size`
+   - `created_at`
+6. Structured error response fields:
+   - `error_code`
+   - `message`
+   - `details`
+7. Configurable upload root.
+8. Backend-generated stored filenames that do not use raw user filenames.
+9. SQLite `documents` table matching `docs/ai/12-phase1-api-persistence.md`.
+10. Pytest coverage for all P0 cases in `docs/ai/16-phase1-test-cases.md`.
+11. README local startup and test commands.
+12. Updated `.ai/verification.md`, `.ai/evaluation.md`, and `.ai/handoff.md`.
+
+## Out Of Scope
+
+Do not implement:
+
+1. OCR.
+2. LLM calls.
+3. Embeddings.
+4. Vector store or Qdrant.
+5. Haystack pipeline execution.
+6. Knowledge card generation.
+7. Tender file analysis.
+8. Frontend Demo.
+9. User system.
+10. Word or PDF export.
+11. Production deployment.
+
+## Expected File Scope
+
+Allowed implementation scope:
+
+```text
+backend/
+├── app/
+│   ├── __init__.py
+│   ├── main.py
+│   ├── config.py
+│   ├── api/
+│   │   ├── __init__.py
+│   │   ├── health.py
+│   │   └── files.py
+│   ├── schemas/
+│   │   ├── __init__.py
+│   │   └── document.py
+│   └── storage/
+│       ├── __init__.py
+│       ├── database.py
+│       └── file_storage.py
+└── tests/
+    ├── test_health.py
+    ├── test_upload_contract.py
+    ├── test_upload_validation.py
+    ├── test_storage.py
+    ├── test_database.py
+    └── test_phase1_boundaries.py
+```
+
+Repository-level files may be updated only as needed:
+
+- `README.md`
+- `.gitignore`
+- one dependency file, preferably `pyproject.toml`
+- `scripts/ai_check.ps1`
+- `scripts/ai_check.sh`
+- `.ai/implementation-plan.md`
+- `.ai/affected-files.md`
+- `.ai/run-trace.md`
+- `.ai/verification.md`
+- `.ai/evaluation.md`
+- `.ai/handoff.md`
+
+## Reference Repository Rule
+
+Reference repositories must remain outside this repository under:
+
+```text
+F:\BidKonwledge_refs
+```
+
+Use RAGFlow only for product/document ingestion/citation reference and Haystack demos only for later pipeline-shape reference. Do not vendor either repository into `F:\BidKonwledge`.
+
+## Acceptance Criteria
+
+Phase 1 is accepted when:
+
+1. The FastAPI app is importable.
+2. `GET /health` returns HTTP 200 and exactly `{"status": "ok"}`.
+3. `POST /api/files/upload` accepts valid `historical_bid` and `tender` uploads.
+4. Valid upload returns HTTP `201 Created`.
+5. Success responses contain only the documented Phase 1 fields and do not expose absolute local paths.
+6. Invalid upload requests return the documented structured error shape and error codes.
+7. Uploaded bytes are stored under the configured upload root.
+8. Stored filenames are generated by the backend and are distinct from raw original filenames.
+9. SQLite creates and uses a `documents` table with the required Phase 1 fields.
+10. Validation failures do not leave orphan files or metadata rows.
+11. P0 pytest coverage from `docs/ai/16-phase1-test-cases.md` passes.
+12. `scripts/ai_check.ps1` runs real Phase 1 checks.
+13. `scripts/ai_check.sh` is run when available, or the WSL/bash blocker is recorded.
+14. Local uvicorn and `curl.exe --noproxy "*"` smoke checks are run if the app starts locally.
+15. `.ai/verification.md`, `.ai/evaluation.md`, and `.ai/handoff.md` record the actual command evidence and residual risks.
+
+## Required Verification Commands
+
+Run before completion:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
+.\scripts\ai_check.ps1
+python -m pytest backend/tests
+```
+
+When shell tooling is available:
+
+```powershell
+bash ./scripts/ai_check.sh
+```
+
+If WSL/bash is unavailable, record the reason in `.ai/verification.md` and do not claim the bash script passed.
diff --git a/docs/ai/tasks/init-large/02-tech-design.md b/docs/ai/tasks/init-large/02-tech-design.md
new file mode 100644
index 0000000..02cf8c6
--- /dev/null
+++ b/docs/ai/tasks/init-large/02-tech-design.md
@@ -0,0 +1,34 @@
+# Tech Design
+
+## Current Task Design
+
+This task is documentation and workflow configuration only.
+
+The design is to keep the repository as a generated target project for Auto_AICoding_Harness:
+
+- `docs/ai/` stores durable product and engineering context.
+- `.ai/` stores current large-mode task runtime artifacts.
+- `docs/source-materials/` stores source document copies and sample indexes.
+- `backend/` and `frontend/` remain placeholders until Phase 1 implementation begins.
+
+## Phase 1 Design Boundary
+
+Phase 1 will later implement:
+
+- FastAPI app startup.
+- `GET /health`.
+- `POST /api/files/upload`.
+- local file storage.
+- SQLite document metadata.
+- smoke tests.
+
+Phase 1 will not implement parsing, retrieval, generation, OCR, vector storage, or UI.
+
+## Interface Decisions For Future Implementation
+
+1. Upload status starts as `parse_status = pending`.
+2. SQLite table `documents` stores metadata only.
+3. Uploaded files are saved under configurable `data/uploads`.
+4. User-provided filenames are preserved as metadata but must not be trusted as storage paths.
+5. Tests and scripts must be run before completion.
+
diff --git a/docs/ai/tasks/init-large/03-implementation-plan.md b/docs/ai/tasks/init-large/03-implementation-plan.md
new file mode 100644
index 0000000..77bed23
--- /dev/null
+++ b/docs/ai/tasks/init-large/03-implementation-plan.md
@@ -0,0 +1,173 @@
+# Implementation Plan - Phase 1 Backend Foundation
+
+## Execution Classification
+
+- Harness mode: `large`
+- Task level: Level 3 / complex
+- Reason: this task introduces the backend app entrypoint, upload API contract, local file persistence, SQLite metadata persistence, project scripts, and P0 automated tests for a complete backend workflow.
+- Rollback: normal Git revert before commit; no migrations beyond local SQLite initialization.
+
+## Target Outcome
+
+Implement the Phase 1 backend foundation only:
+
+1. FastAPI app startup.
+2. `GET /health`.
+3. `POST /api/files/upload`.
+4. HTTP `201 Created` upload success contract.
+5. Structured upload error contract.
+6. Configurable local upload root and SQLite database path.
+7. Backend-generated stored filenames.
+8. `documents` SQLite table matching `docs/ai/12-phase1-api-persistence.md`.
+9. P0 pytest coverage from `docs/ai/16-phase1-test-cases.md`.
+10. README and `.ai` evidence updates.
+
+## Non-Goals
+
+Do not implement OCR, LLM calls, embedding, Qdrant/vector store, Haystack pipeline execution, knowledge cards, tender analysis, frontend Demo, user system, or Word/PDF export.
+
+## Expected File Scope
+
+Implementation files:
+
+```text
+backend/app/__init__.py
+backend/app/main.py
+backend/app/config.py
+backend/app/api/__init__.py
+backend/app/api/health.py
+backend/app/api/files.py
+backend/app/schemas/__init__.py
+backend/app/schemas/document.py
+backend/app/storage/__init__.py
+backend/app/storage/database.py
+backend/app/storage/file_storage.py
+```
+
+Test files:
+
+```text
+backend/tests/conftest.py
+backend/tests/test_health.py
+backend/tests/test_upload_contract.py
+backend/tests/test_upload_validation.py
+backend/tests/test_storage.py
+backend/tests/test_database.py
+backend/tests/test_phase1_boundaries.py
+```
+
+Project files:
+
+```text
+pyproject.toml
+README.md
+scripts/ai_check.ps1
+scripts/ai_check.sh
+.ai/affected-files.md
+.ai/run-trace.md
+.ai/verification.md
+.ai/evaluation.md
+.ai/handoff.md
+```
+
+## Subagent Plan
+
+Use subagents for read-only and review work only. Main agent owns all writes to avoid conflicting edits.
+
+1. Explorer Hooke: read-only API/persistence/test-contract scan.
+2. Explorer Meitner: read-only script/README/verification-artifact scan.
+3. After implementation, use reviewer/evaluator subagent only if useful for final contract review.
+
+## Implementation Stages
+
+### Stage 1 - Package And App Skeleton
+
+1. Add a single dependency file, `pyproject.toml`, with FastAPI, Uvicorn, Pydantic, pytest, and HTTPX.
+2. Add FastAPI app factory/import entrypoint in `backend/app/main.py`.
+3. Add `GET /health` router.
+
+Verification:
+
+```powershell
+python -m compileall backend/app
+python -m pytest backend/tests/test_health.py
+```
+
+### Stage 2 - Configuration, SQLite, And File Storage
+
+1. Add settings object with configurable upload root, database path, allowed extensions, and max upload size.
+2. Add SQLite initialization and `documents` insert/query helpers.
+3. Add file-storage helper that generates stored filenames using backend document ids and writes only under upload root.
+
+Verification:
+
+```powershell
+python -m pytest backend/tests/test_storage.py backend/tests/test_database.py
+```
+
+### Stage 3 - Upload API And Error Contract
+
+1. Add `POST /api/files/upload`.
+2. Validate missing file, missing/invalid doc role, empty file, unsafe filename, unsupported extension, and file-too-large.
+3. Save file before metadata insert.
+4. Clean up stored file if metadata insert fails.
+5. Return only documented success fields.
+6. Return fixed error fields: `error_code`, `message`, `details`.
+
+Verification:
+
+```powershell
+python -m pytest backend/tests/test_upload_contract.py backend/tests/test_upload_validation.py
+```
+
+### Stage 4 - Boundary Tests And Scripts
+
+1. Add tests proving Phase 1 does not require OCR, LLM credentials, vector service, or parser output.
+2. Replace PowerShell project check placeholder with real compile and pytest commands.
+3. Replace bash project check placeholder with the same real check sequence for shell environments.
+
+Verification:
+
+```powershell
+.\scripts\ai_check.ps1
+python -m pytest backend/tests
+```
+
+Run `bash ./scripts/ai_check.sh` when available. If WSL/bash is unavailable on this Windows machine, record the blocker in `.ai/verification.md`.
+
+### Stage 5 - README, Evidence, And Smoke
+
+1. Update README with large-mode status, dependency install, local startup, pytest, and curl commands.
+2. Start uvicorn locally if dependencies are available.
+3. Run `curl.exe --noproxy "*"` health and upload smoke checks.
+4. Update `.ai/verification.md`, `.ai/evaluation.md`, and `.ai/handoff.md` with real command evidence.
+
+Verification:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
+.\scripts\ai_check.ps1
+python -m pytest backend/tests
+curl.exe --noproxy "*" http://127.0.0.1:8000/health
+```
+
+## Mid-Task Review Checkpoint
+
+After Stage 3, perform a self-review:
+
+1. Status versus this plan.
+2. Scope changes since start.
+3. Newly discovered risks.
+4. Decision: keep plan, revise plan, or escalate.
+
+## Escalation Triggers
+
+Escalate or pause if:
+
+1. The upload contract conflicts with docs.
+2. Dependencies cannot be installed or imported.
+3. Tests require external services.
+4. File/database atomicity cannot be verified locally.
+5. Harness gate state blocks implementation.
diff --git a/docs/ai/tasks/init-large/04-diff-review.md b/docs/ai/tasks/init-large/04-diff-review.md
new file mode 100644
index 0000000..6e3f11b
--- /dev/null
+++ b/docs/ai/tasks/init-large/04-diff-review.md
@@ -0,0 +1,3 @@
+# Diff Review
+
+Diff review has not been generated yet.
diff --git a/docs/ai/tasks/init-large/05-verification.md b/docs/ai/tasks/init-large/05-verification.md
new file mode 100644
index 0000000..df3c267
--- /dev/null
+++ b/docs/ai/tasks/init-large/05-verification.md
@@ -0,0 +1,162 @@
+# Verification
+
+## Large-Mode Requirement
+
+All future development must run under harness `large` mode and must run the project check scripts before completion.
+
+For this documentation-prep task, verify:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
+.\scripts\ai_check.ps1
+bash ./scripts/ai_check.sh
+```
+
+Observed on 2026-06-27:
+
+- `ai-status`: initialized yes, mode `large`, profile `python-backend-service`, state valid.
+- `ai-doctor`: OK for Git repo, state schema, large-mode files, and task chain; warning only for uncommitted working tree changes.
+- `.\scripts\ai_check.ps1`: passed; script reported Phase 0 has no runnable backend yet and listed future Python checks.
+- `bash ./scripts/ai_check.sh`: not runnable on this machine because no WSL/Linux distribution is installed; PowerShell script is the current Windows check path.
+
+## Reference Repository Checks
+
+Run on 2026-06-27:
+
+```powershell
+git -C F:\BidKonwledge_refs\ragflow rev-parse --short HEAD
+git -C F:\BidKonwledge_refs\haystack-demos rev-parse --short HEAD
+git status --short
+```
+
+Observed:
+
+- RAGFlow reference clone: `f90be41`.
+- Haystack demos reference clone: `17e6103`.
+- Both clones are outside `F:\BidKonwledge`.
+- `git status --short` in the business repository does not include `F:\BidKonwledge_refs`.
+
+## Phase 1 Test-Case Documentation Check
+
+Updated on 2026-06-27:
+
+- `docs/ai/16-phase1-test-cases.md` now defines detailed Phase 1 automated and manual test cases.
+- `docs/ai/16-phase1-test-cases.md` is explicitly an internal backend foundation test spec, not a customer-facing PRD or complete Demo acceptance document.
+- Upload success is now fixed as HTTP `201 Created`.
+- Upload error responses now use the fixed JSON shape `error_code`, `message`, and `details`.
+- SQLite `documents` fields are now fixed in `docs/ai/12-phase1-api-persistence.md`.
+- File safety and atomicity rules now require backend-generated stored filenames and cleanup when validation or persistence fails.
+- Harness commands are documented as delivery command checks, not core business pytest cases.
+- The document is a test-case specification for the next development session, not pytest implementation.
+- Phase 1 pytest files are still expected to be created during backend implementation.
+- `docs/ai/README.md`, `.ai/implementation-plan.md`, and `.ai/handoff.md` now include the detailed test-case document in required Phase 1 context.
+
+Verification commands run after the update:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
+.\scripts\ai_check.ps1
+```
+
+Observed:
+
+- `ai-status`: initialized yes, mode `large`, profile `python-backend-service`, state valid, task chain present.
+- `ai-doctor`: passed required state, mode, profile, large files, and task chain checks; warning only for uncommitted working tree changes.
+- `.\scripts\ai_check.ps1`: exited successfully and reported Phase 0 has no runnable backend yet.
+- `bash ./scripts/ai_check.sh`: not rerun for this documentation-only update; previous blocker remains no WSL/Linux distribution installed.
+
+## Phase 1 Contract-Hardening Check
+
+Updated on 2026-06-27:
+
+- `docs/ai/12-phase1-api-persistence.md` now fixes the Phase 1 upload API contract.
+- `docs/ai/04-api-contract.md` now mirrors the fixed upload success/error response shape.
+- `docs/ai/03-data-model.md` now mirrors the fixed Phase 1 document metadata fields.
+- `docs/ai/16-phase1-test-cases.md` now states that it is an internal backend foundation test spec, not a customer-facing PRD or full Demo acceptance document.
+- `docs/ai/16-phase1-test-cases.md` now separates delivery command checks from business pytest coverage.
+- The current local checkout path remains `F:\BidKonwledge`; `docs/ai/11-local-dev-env.md` records the canonical project name as `BidKnowledge` and warns not to hard-code the absolute path in tests.
+
+Verification commands run after the contract-hardening update:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
+.\scripts\ai_check.ps1
+git diff --check
+```
+
+Observed:
+
+- `ai-status`: initialized yes, mode `large`, profile `python-backend-service`, state valid, task chain present.
+- `ai-doctor`: passed required state, mode, profile, large files, and task chain checks; warning only for uncommitted working tree changes.
+- `.\scripts\ai_check.ps1`: exited successfully and reported Phase 0 has no runnable backend yet.
+- `git diff --check`: passed.
+- `rg` old-contract scan over docs and `.ai`: no matches for the prior loose status-code, old response-field, old DB-field, or pytest/script-mixing wording.
+- Pytest was not run because Phase 1 backend implementation has not started.
+
+## Current Initialization And Documentation Checks
+
+Run on 2026-06-27:
+
+```powershell
+$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
+& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
+git status --short
+Get-ChildItem -Recurse -Force docs\source-materials
+Get-ChildItem -Force docs\ai
+```
+
+Observed:
+
+- `ai-status` now reports initialized large mode with `python-backend-service` profile.
+- `ai-doctor` reports valid state schema and required large files present.
+- `ai-doctor` warns that the working tree has uncommitted changes, which is expected for this newly initialized repository.
+- Source documents copied into `docs/source-materials/originals/`.
+- Large external sample files remain outside Git and are indexed in `docs/source-materials/sample-catalog.md`.
+
+## Phase 0 Checks
+
+Run:
+
+```powershell
+git status --short
+Get-ChildItem -Force
+Get-ChildItem -Force docs/ai
+Get-ChildItem -Force .ai
+```
+
+Expected:
+
+- Git repository exists.
+- Harness files exist.
+- `docs/ai` contains project context files.
+- `.ai` contains current planning files.
+- No business implementation files are present beyond empty scaffold folders and `.gitkeep` files.
+
+## Phase 1 Checks
+
+Future Phase 1 should run:
+
+```powershell
+python -m pytest
+python -m uvicorn app.main:app --reload
+```
+
+The exact Python command may change depending on the selected virtual environment.
+
+Phase 1 acceptance requires:
+
+- `GET /health` returns `{"status":"ok"}`.
+- `POST /api/files/upload` returns HTTP `201 Created` for valid uploads.
+- Upload success response contains `document_id`, `original_filename`, `doc_role`, `parse_status`, `file_size`, and `created_at`.
+- Upload error response contains `error_code`, `message`, and `details`.
+- Upload endpoint saves a file under configured upload root using a backend-generated stored filename.
+- SQLite stores document metadata using the fields in `docs/ai/12-phase1-api-persistence.md`.
+- Invalid uploads do not leave orphan files or metadata rows.
+- Tests cover the P0 cases in `docs/ai/16-phase1-test-cases.md`.
diff --git a/docs/ai/tasks/init-large/06-risk-and-rollback.md b/docs/ai/tasks/init-large/06-risk-and-rollback.md
new file mode 100644
index 0000000..285fd3a
--- /dev/null
+++ b/docs/ai/tasks/init-large/06-risk-and-rollback.md
@@ -0,0 +1,22 @@
+# Risk And Rollback
+
+## Risks
+
+1. Harness profile drift: `ai-upgrade large` defaults to `cpp-linux-backend-system` unless `--profile python-backend-service` is provided.
+2. Scope drift: Phase 1 could accidentally start parsing/RAG work too early.
+3. Large sample files could accidentally enter Git history.
+4. Placeholder scripts could be mistaken for real build/test coverage after Phase 1 implementation.
+
+## Mitigations
+
+1. `.ai/state.json` is set to `mode = large` and `profile = python-backend-service`.
+2. `AGENTS.md`, `README.md`, and Phase 1 docs explicitly require large mode and script execution.
+3. `docs/source-materials/sample-catalog.md` indexes large files without copying them.
+4. `docs/ai/13-phase1-verification-checklist.md` requires real script/test evidence before Phase 1 completion.
+
+## Rollback
+
+This task is documentation-only. Rollback is a normal Git revert before commit.
+
+If harness-generated large-mode files are not wanted, remove the files listed in `.ai/affected-files.md` and restore `.ai/state.json` from `.ai/backups/20260627-214154/.ai/state.json`.
+
diff --git a/docs/ai/tasks/init-large/07-handoff.md b/docs/ai/tasks/init-large/07-handoff.md
new file mode 100644
index 0000000..733fbb2
--- /dev/null
+++ b/docs/ai/tasks/init-large/07-handoff.md
@@ -0,0 +1,96 @@
+# Handoff
+
+## Current State
+
+The repository has been initialized for the 投标智能知识库能力验证版 Demo.
+
+Auto_AICoding_Harness has been upgraded to `large` mode with the `python-backend-service` profile.
+
+Future development in this repository must use large mode and must run the project scripts before completion.
+
+Latest verification:
+
+- `ai-status` and `ai-doctor` pass for large mode.
+- `scripts/ai_check.ps1` runs successfully.
+- `bash ./scripts/ai_check.sh` was attempted but cannot run because WSL is not installed.
+
+## Important Context
+
+Read these first:
+
+1. `docs/ai/00-project-brief.md`
+2. `docs/ai/01-scope-boundary.md`
+3. `docs/ai/05-dev-rules.md`
+4. `docs/ai/08-tech-selection.md`
+5. `docs/ai/09-phase-roadmap.md`
+6. `docs/source-materials/README.md`
+7. `docs/source-materials/sample-catalog.md`
+8. `.ai/spec.md`
+9. `.ai/implementation-plan.md`
+10. `docs/ai/10-phase1-dev-spec.md`
+11. `docs/ai/11-local-dev-env.md`
+12. `docs/ai/12-phase1-api-persistence.md`
+13. `docs/ai/13-phase1-verification-checklist.md`
+14. `docs/ai/14-reference-reuse-strategy.md`
+15. `docs/ai/15-target-architecture.md`
+16. `docs/ai/16-phase1-test-cases.md`
+
+## Next Recommended Prompt
+
+```md
+当前仓库已经完成 0 阶段初始化，并已升级到 Auto_AICoding_Harness large mode。请先运行 ai-status / ai-doctor，确认 .ai/state.json 中 mode=large 且 profile=python-backend-service。
+
+请先阅读：
+- AGENTS.md
+- docs/ai/10-phase1-dev-spec.md
+- docs/ai/11-local-dev-env.md
+- docs/ai/12-phase1-api-persistence.md
+- docs/ai/13-phase1-verification-checklist.md
+- docs/ai/16-phase1-test-cases.md
+- .ai/implementation-plan.md
+- .ai/verification.md
+
+现在开始执行 Phase 1。
+
+只实现以下内容：
+
+1. FastAPI app 启动；
+2. GET /health；
+3. POST /api/files/upload，成功响应固定为 HTTP 201；
+4. 结构化错误响应，字段为 error_code / message / details；
+5. 本地文件保存到配置化 upload root，真实存储名由后端生成；
+6. Document metadata schema，字段按 docs/ai/12-phase1-api-persistence.md；
+7. SQLite 初始化；
+8. 基础配置管理；
+9. docs/ai/16-phase1-test-cases.md 中的 P0 pytest 覆盖；
+10. 最小 smoke test；
+11. README 中补充本地启动命令。
+
+不要实现 OCR、LLM、embedding、vector store、知识卡片生成、招标文件分析、Demo 页面、用户系统、Word/PDF 导出。
+
+注意：Phase 1 只是后端底座，不是甲方 Demo 验收。
+
+实现完成后更新 .ai/evaluation.md 和 .ai/handoff.md，并列出新增文件、修改文件、运行命令、测试命令、验证结果、下一步建议。
+
+必须运行项目脚本，并把结果写入 .ai/verification.md。
+```
+
+## Source Materials
+
+Project materials are under:
+
+`C:\Users\26561\Desktop\模型训练资料`
+
+Copied lightweight source documents:
+
+- `docs/source-materials/originals/投标智能知识库能力验证版-PRD-v0.1.pdf`
+- `docs/source-materials/originals/deep-research-report.md`
+
+Large sample files were not copied into Git. Use `docs/source-materials/sample-catalog.md` to select validation files.
+
+Reference repositories:
+
+- `F:\BidKonwledge_refs\ragflow`
+- `F:\BidKonwledge_refs\haystack-demos`
+
+These are reference-only clones and should not be committed into the business repo.
diff --git a/docs/ai/testing.md b/docs/ai/testing.md
new file mode 100644
index 0000000..1899bca
--- /dev/null
+++ b/docs/ai/testing.md
@@ -0,0 +1,19 @@
+# Python Testing Guidance
+
+## Test Strategy
+
+- Prefer focused `pytest` tests near the changed behavior before broad suite runs.
+- Distinguish unit, integration, contract, and external-service tests in verification notes.
+- Keep fixtures deterministic and avoid relying on undeclared local services.
+
+## Common Commands
+
+- `pytest`
+- `python -m pytest`
+- project-defined wrappers such as `tox`, `nox`, `uv run pytest`, or `poetry run pytest`
+
+## Review Checks
+
+- Cover success, error, and boundary cases for API or serialization changes.
+- For async code, cover cancellation, timeout, and event-loop behavior where practical.
+- For database or migration changes, cover rollback or compatibility paths when feasible.
diff --git a/docs/ai/typing.md b/docs/ai/typing.md
new file mode 100644
index 0000000..0e5f3ce
--- /dev/null
+++ b/docs/ai/typing.md
@@ -0,0 +1,18 @@
+# Python Typing Guidance
+
+## Static Analysis
+
+- Respect the project's existing type-checking tool: `mypy`, `pyright`, `basedpyright`, or none.
+- Do not introduce strictness changes as part of an unrelated task.
+- Keep public function and data-model annotations accurate when changing interfaces.
+
+## Runtime Boundaries
+
+- Validate untrusted input at API, CLI, queue, or file boundaries.
+- Treat dataclass, Pydantic, attrs, TypedDict, and protocol changes as contract changes.
+- Avoid using `Any` to silence real interface uncertainty without documenting why.
+
+## Verification
+
+- Run the project-defined type-check command when type-facing code changes.
+- Record skipped type checks and the reason in `.ai/verification.md` for medium or large work.
diff --git a/docs/ai/verification-matrix.md b/docs/ai/verification-matrix.md
new file mode 100644
index 0000000..1baa742
--- /dev/null
+++ b/docs/ai/verification-matrix.md
@@ -0,0 +1,16 @@
+# Python Verification Matrix
+
+| Risk Trigger | Suggested Verification |
+| --- | --- |
+| `public_api_change` | Focused API tests plus compatibility notes. |
+| `dependency_change` | Project-defined dependency install/check and focused tests. |
+| `serialization_change` | Fixture round-trip or contract tests. |
+| `database_migration_change` | Migration upgrade/downgrade or compatibility tests when available. |
+| `async_concurrency_change` | Async timeout, cancellation, and concurrency behavior tests. |
+| `packaging_change` | Build/import smoke test and project-defined packaging checks. |
+
+## Notes
+
+- Prefer `pytest` or project-defined wrappers already present in the target repository.
+- Run type checking when interface or typing changes are part of the task.
+- Record actual commands and results in `.ai/verification.md` for medium and large work.
diff --git a/docs/ai/workflow.md b/docs/ai/workflow.md
new file mode 100644
index 0000000..3985eee
--- /dev/null
+++ b/docs/ai/workflow.md
@@ -0,0 +1,57 @@
+# Workflow
+
+This document captures the durable AI collaboration workflow for the target project.
+It complements `AGENTS.md` and the runtime files under `.ai/`.
+
+## Mode Selection
+
+- Use the lightest execution level that still controls risk.
+- Stay in `small` for local, easy-to-verify work with low rollback cost.
+- Upgrade to `medium` when the task becomes bounded multi-file work and should keep `.ai/implementation-plan.md`, `.ai/run-trace.md`, and `.ai/verification.md` current.
+- Upgrade to `large` when the task needs explicit `spec`, `plan`, `diff`, and `final` gates.
+- Escalate when touched scope expands, rollback gets harder, or verification depth increases.
+- A mode change is only real after `ai-upgrade medium|large` succeeds and `.ai/state.json` reflects it.
+
+## Command Protocol
+
+- `ai-status`, `ai-state`, and `ai-doctor` are safe read-only commands.
+- `ai-review spec|plan|diff|final` creates review artifacts and advances the state into the matching waiting gate.
+- `ai-approve` and `ai-reject` require explicit human authorization and must match the current waiting gate.
+- `ai-doctor` is the health check for state, generated files, and obvious mode mismatches.
+- If a command was not executed successfully, do not describe its state transition as complete.
+
+## Runtime Files
+
+- `.ai/state.json`: authoritative workflow mode, status, current gate, and approved gates.
+- `.ai/spec.md`: task goal, non-goals, allowed scope, and validation target.
+- `.ai/tech-design.md`: technical design, data flow, and interface boundaries for large-mode work.
+- `.ai/implementation-plan.md`: concrete execution steps and verification points.
+- `.ai/affected-files.md`: expected edit surface before implementation drifts.
+- `.ai/run-trace.md`: notable execution evidence and checkpoints during the task.
+- `.ai/verification.md`: what was run, what passed, and what remains unverified.
+- `.ai/risk-and-rollback.md`: residual risk, rollback path, and required follow-up.
+- `.ai/evaluation.md`: final acceptance summary and residual risk.
+- `.ai/context-pack.md`: compact resumable state for the next clean session.
+- `.ai/handoff.md`: explicit transfer artifact when stopping or switching sessions.
+- `docs/ai/tasks/<task-id>/`: durable large-mode evidence chain for PRD, spec, design, plan, review, verification, risk, and handoff.
+
+## Verification Discipline
+
+- Record real commands and outcomes in `.ai/verification.md`.
+- Keep `.ai/evaluation.md` for the final acceptance conclusion, not raw command logs.
+- Do not claim build, test, benchmark, or review coverage unless the evidence exists.
+- If something was not run, write why it was skipped and what follow-up is required.
+
+## Long-Running Work
+
+- When the task becomes multi-step, keep `.ai/implementation-plan.md`, `.ai/run-trace.md`, and `.ai/verification.md` current.
+- When a real subagent is dispatched, record the role, scope, required skills, optional skills, objective, and result location in `.ai/run-trace.md`.
+- Use `.ai/context-pack.md` before ending a session that may resume soon.
+- Use `.ai/handoff.md` when another agent or a later clean-context session needs to continue.
+- If context is getting noisy or the scope is drifting, stop expanding the task and write down the next safe step.
+
+## Durable Versus Runtime Knowledge
+
+- Put project facts that outlive the task in `docs/ai/`.
+- Put task-specific plans, evidence, and approvals in `.ai/`.
+- Do not turn `.ai/` into long-lived architecture documentation.
diff --git a/docs/source-materials/README.md b/docs/source-materials/README.md
new file mode 100644
index 0000000..912769e
--- /dev/null
+++ b/docs/source-materials/README.md
@@ -0,0 +1,35 @@
+# Source Materials
+
+This folder organizes the project input documents.
+
+## Original Documents Copied Into This Repository
+
+- `originals/投标智能知识库能力验证版-PRD-v0.1.pdf`
+- `originals/deep-research-report.md`
+
+These files are small enough to keep with the project context.
+
+## External Sample Materials Not Copied Into Git
+
+The full sample set remains at:
+
+`C:\Users\26561\Desktop\模型训练资料\甲方提供资料`
+
+Large bid documents, archives, and image batches are intentionally not copied into the repository.
+
+Use `sample-catalog.md` to choose files for validation.
+
+## External Reference Repositories
+
+Reference repositories are cloned outside this repo under:
+
+`F:\BidKonwledge_refs`
+
+See `reference-repos.md`.
+
+## Reading Order
+
+1. PRD PDF for product boundary.
+2. `deep-research-report.md` for technology selection.
+3. `sample-catalog.md` for later validation data.
+4. `docs/ai/` for normalized project context.
diff --git a/docs/source-materials/originals/deep-research-report.md b/docs/source-materials/originals/deep-research-report.md
new file mode 100644
index 0000000..66eb453
--- /dev/null
+++ b/docs/source-materials/originals/deep-research-report.md
@@ -0,0 +1,312 @@
+# 投标智能知识库 Demo GitHub 对标与二开方案
+
+## 执行摘要
+
+这次选型要分成两个问题来回答：**谁最像你们要给甲方看的成品**，以及**谁最适合按你们的默认值在两周内 fork 并二开**。结合你给定的约束——Python + FastAPI、极简前端、允许外部模型/API、OCR 优先本地开源、第一阶段只处理 2–3 份样例、优先 MIT/Apache、Docker/Ubuntu 本地开发——结论是：**RAGFlow 最像“投标智能知识库 Demo”的成品对标样板；Haystack 最适合作为真正落地的主项目底座**。RAGFlow 的强项是“深文档理解 + 引用追溯 + 现成 RAG 工作流”，但官方要求的本地资源更高，默认栈也更重；Haystack 则是 Python 原生、检索/编排模块化、Qdrant/多家模型提供方集成成熟，更适合用 FastAPI 包一层极简 API 和页面快速交付。citeturn13search2turn13search12turn19search2turn6view0turn20search3turn20search4
+
+如果把“对标”和“实做”拆开，最稳妥的执行方案是：**主底座选 Haystack，文档解析选 Docling，OCR 选 PaddleOCR，向量检索选 Qdrant，前端不直接套完整平台，而是在 FastAPI 里做很薄的一层上传/检索/生成页面**。这组组合的优点是许可证干净、组件边界清晰、Codex 容易读源码和改补丁、未来也能逐步替换成更强的解析器或更大的模型而不推翻整体。Docling 官方已经给出与 Haystack 和 Qdrant 的联动示例；Qdrant 本地可直接用 Docker 启动；PaddleOCR 则已经把 PDF/图片转结构化 JSON/Markdown、坐标信息和多语言 OCR 做成成熟能力。citeturn15search5turn15search1turn14view0turn6view5
+
+不建议第一阶段直接重度 fork Dify 或 MinerU。Dify 虽然功能很全，且支持知识库检索、引用与外部知识 API，但它采用 **Dify Open Source License**，是基于 Apache 2.0 的自定义许可证；MinerU 也刚从 AGPLv3 迁到 **MinerU Open Source License**，同样是基于 Apache 2.0 的自定义许可证。对“可商用演示 + 后续可继续本地二开”的项目来说，这两类自定义许可证都应进入法务复核清单，而不是默认当作“纯 Apache 项目”直接开抄。citeturn1view0turn17search1turn17search2turn6view7turn4search0
+
+本报告的核心建议可以压缩成一句话：**功能对标看 RAGFlow，工程落地 fork Haystack，组件补齐用 Docling + PaddleOCR + Qdrant，FastAPI 自己包一层极简演示壳。** 这样既能在演示上贴近“上传历史文件 → 解析/切分 → 入库标签化 → RAG 检索 → LLM 生成 → 来源追溯 → 风险提示”的链路，也能把两周内真正要写的代码控制在一个小而清晰的边界里。citeturn13search2turn20search2turn15search2turn6view5turn14view0
+
+## 需求上下文与边界
+
+从交付形态看，这不是“做一个通用 AI 平台”，而是做一个**投标智能知识库 Demo**：把少量历史投标文件导入，尽可能保留章节、表格、页码、表头、附件等文档结构；对新的招标文件或提问做检索增强生成；回答必须能回到来源片段；并对明显的风险项给出提示。按你给定的默认值，第一阶段只需要 2–3 份样例，目标是把主链路跑通，而不是做大规模批量治理、企业级权限管理或完整标书自动生成。这个边界决定了我们要优先选择**组件化、可裁剪、可快速出 Demo 的 repo**，而不是“带完整后台、工作流画布、团队协作、插件市场”的大而全平台。citeturn13search2turn17search3turn17search9
+
+明确不做项也很重要。第一阶段不建议把范围扩到：完整投标编制系统、多租户权限体系、工作流编排台、复杂审批流、全文精细字段抽取训练、模型微调平台、全量样本治理、复杂报表统计。这些能力 Dify、RAGFlow、AnythingLLM 等平台中有不少已经做成了完整产品形态，但它们恰恰会把你们拖进“抄平台”而不是“做交付链路”的陷阱。Dify 的文档明确支持知识检索节点、知识库 API 和外部知识服务接入；RAGFlow 的文档则直接把自己定位为带 Agent 能力的 RAG 引擎；AnythingLLM 也提供完整 Docker 化应用与文档聊天界面。对你们现在的阶段，这些都是“可参考的能力清单”，不是“第一阶段必须照抄的系统边界”。citeturn17search2turn17search3turn17search4turn13search2turn19search7
+
+建议把 Demo 核心链路固定成下面这个最短闭环，并且围绕这个闭环做一切代码取舍：
+
+```mermaid
+flowchart LR
+    A[上传历史文件] --> B[文档解析]
+    B --> C[章节切分与表格抽取]
+    C --> D[标签化入库]
+    D --> E[Qdrant 检索]
+    E --> F[LLM 生成候选响应]
+    F --> G[来源追溯]
+    G --> H[风险提示]
+    H --> I[极简展示页]
+```
+
+这条链路在开源项目中的映射是很清晰的：Docling / PaddleOCR / MinerU / Unstructured 负责“解析”；Qdrant 负责“存”；Haystack / RAGFlow / Dify 负责“检索与生成编排”；FastAPI 负责“对外 API 和页面”；引用追溯则来自解析阶段保留下来的页码、章节路径、坐标和源文档元数据。官方资料也都在强调这些点：Docling突出统一文档表示和高级 PDF 理解；PaddleOCR突出结构化 JSON/Markdown 与坐标信息；Qdrant 支持本地向量检索；Haystack 支持检索、生成、路由、追踪和多模型接入。citeturn15search10turn15search2turn6view5turn14view0turn6view0
+
+## GitHub 对标项目池与评分
+
+下表中的 stars / forks / 最近更新日期，均取自 **2026-06-27** 访问到的 GitHub 仓库页面或官方文档中的 latest release / visible update 信息。分数是**按你们的默认值**打的主观工程分：更看重 Python/FastAPI 适配、二开速度、许可证清晰度，以及两周内出 Demo 的可控性，而不是单纯看功能堆叠。citeturn2view0turn2view3turn2view5turn1view2turn12view0turn12view1turn7view0turn7view1turn7view3turn8view0turn10view0turn7view6
+
+| 类别 | 项目 | 功能简介 | 主要语言 | 许可证 | 部署复杂度 | 来源追溯 | 易二开 | 适合本地 Codex | 最近更新日期 | stars / forks | 业务匹配 | 二开速度 | 文档解析 | RAG 引用 | 许可证风险 | 总体推荐分 |
+|---|---|---|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
+| RAG 平台 | RAGFlow citeturn1view1turn13search2turn13search12turn16view1turn19search2 | 深文档理解、RAG、Agent、引用追溯一体化，最像“成品 Demo” | Go / Python / TypeScript | Apache-2.0 | 高 | 是 | 中 | 中 | 2026-06-17 | 83.7k / 9.7k | 5 | 2 | 5 | 5 | 5 | 4.2 |
+| RAG 平台 | Dify citeturn1view0turn17search1turn17search2turn17search3turn16view0turn19search1turn19search4 | 工作流、知识库、外部知识 API、引用与归因支持完整 | TypeScript / Python | Dify Open Source License | 中高 | 是 | 中 | 中 | 2026-06-25 | 147k / 23.1k | 4 | 2 | 3 | 4 | 2 | 3.4 |
+| RAG 编排 | Haystack citeturn6view0turn12view0turn12view2turn20search2turn20search3turn20search4turn20search5 | Python 原生检索/生成/路由框架，适合定制 FastAPI 服务 | Python | Apache-2.0 | 低中 | 部分 | 是 | 是 | 2026-06-18 | 25.7k / 2.9k | 4 | 5 | 3 | 3 | 5 | 4.4 |
+| RAG 平台 | AnythingLLM citeturn1view3turn2view5turn2view6turn2view7turn13search19turn19search7turn16view2 | 文档聊天、Workspace、/proof 引用查看、本地优先 | JavaScript | MIT | 中 | 是 | 中 | 低 | 2026-06-25 | 62.2k / 6.8k | 3 | 2 | 2 | 4 | 5 | 3.2 |
+| 中文 RAG | Langchain-Chatchat citeturn1view2turn18search0turn18search9turn18search3 | 中文本地知识库问答、FastAPI + Streamlit、File RAG | Python | Apache-2.0 | 中 | 部分 | 中高 | 中高 | 2024-07-12 | 38.2k / 6.2k | 4 | 4 | 2 | 3 | 5 | 3.9 |
+| 后端模板 | full-stack-fastapi-template citeturn6view3turn7view7turn12view1 | 现代 FastAPI + React + Docker 模板，适合参考工程组织方式 | Python / TypeScript | MIT | 中 | 否 | 是 | 是 | 2026-01-23 | 43.9k / 8.7k | 2 | 4 | 1 | 1 | 5 | 3.1 |
+
+平台层的结论很明确：**如果只问“GitHub 上谁最像你们要展示的业务成品”，答案是 RAGFlow；如果问“谁最适合按默认值二开成自己的 Demo backend”，答案是 Haystack。** RAGFlow 官方明确把“深文档理解 + 引用支撑的问答”作为核心卖点，甚至在后续版本中直接提到会调用 MinerU 和 Docling 这类解析模型；但它的本地前提也更高，官方 quickstart 给出的建议是 x86 CPU 至少 4 核、16GB 内存、50GB 磁盘。相比之下，Haystack 更像一套可控的零件库，官方强调它是 Python 的生产级 LLM 应用编排框架，支持本地和云端多种模型、明确的检索/路由/生成组件，以及通过 HTTP 暴露 pipeline 的方式。citeturn13search2turn13search21turn19search2turn6view0turn20search2turn20search12
+
+Dify 的参考价值不在“直接 fork”，而在“功能对照表”和“外部知识 API 思路”。官方文档写得很清楚：知识检索节点可以搜索知识库并把结果作为上下文喂给下游 LLM；在应用层面可以开启 Citation and Attribution；还可以通过 External Knowledge API 直接接入你们自己的检索服务，只让 Dify 充当 UI 和工作流外壳。也就是说，如果第二阶段甲方突然想要一个低代码可视化工作流台，Dify 是强备选；但第一阶段如果你们只需要极简前端，它会引入比收益更高的平台复杂度和许可证审查成本。citeturn17search1turn17search2turn17search3turn17search4
+
+组件层则更适合做“拼装式选择”。下面这张表是更贴近你们 Demo 主链路的零件池。citeturn15search10turn6view5turn6view7turn8view0turn10view0turn7view6
+
+| 类别 | 项目 | 功能简介 | 主要语言 | 许可证 | 部署复杂度 | 追溯支撑 | 易二开 | 适合本地 Codex | 最近更新日期 | stars / forks | 业务匹配 | 二开速度 | 文档解析 | RAG 引用支撑 | 许可证风险 | 总体推荐分 |
+|---|---|---|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
+| 文档解析 | Docling citeturn6view4turn3search20turn15search1turn15search2turn15search5turn15search10 | 多格式转统一文档对象，保留阅读顺序、表格结构、元数据 | Python | MIT | 低中 | 是 | 是 | 是 | 2026-06-26 | 62k / 4.4k | 5 | 5 | 5 | 4 | 5 | 4.8 |
+| OCR / 视觉理解 | PaddleOCR citeturn6view5turn7view1turn3search6turn14view4 | 图片/PDF 转 JSON/Markdown，支持坐标、表格、100+ 语言 | Python | Apache-2.0 | 中 | 是 | 是 | 是 | 2026-06-11 | 84k / 10.9k | 5 | 4 | 5 | 4 | 5 | 4.7 |
+| 文档解析 | MinerU citeturn6view7turn7view3turn14view5turn4search0 | 复杂 PDF / Office 文档转 LLM-ready Markdown/JSON，支持扫描、跨页表格 | Python | MinerU Open Source License | 中高 | 是 | 中 | 中 | 2026-06-18 | 70.5k / 5.9k | 5 | 3 | 5 | 4 | 2 | 3.9 |
+| 文档预处理 | Unstructured citeturn6view6turn8view0 | 通用文档预处理/ETL，支持多类文件和容器化运行 | Python | Apache-2.0 | 中 | 部分 | 是 | 是 | 2026-06-11 | 15k / 1.3k | 3 | 4 | 4 | 2 | 5 | 3.8 |
+| 表格解析 | Camelot citeturn10view0 | PDF 表格抽取，核心安装轻，支持 OCR/ML 可选扩展 | Python | MIT | 低 | 部分 | 是 | 是 | 2026-06-04 | 3.8k / 540 | 3 | 4 | 3 | 2 | 5 | 3.6 |
+| 向量库 | Qdrant citeturn6view2turn7view6turn14view0turn20search3turn20search5 | 本地 Docker 可起，支持 dense / sparse / hybrid 检索 | Rust / Python | Apache-2.0 | 低 | 是 | 是 | 是 | 2026-06-04 | 32.7k / 2.4k | 5 | 5 | 1 | 4 | 5 | 4.6 |
+
+Docling 之所以最适合做主解析器，不是因为它“名气最大”，而是因为它正好卡在你们的工程甜点位：**Python 优先、统一文档表示、保留结构、对 RAG 友好、官方直接给出 Haystack 与 Qdrant 的示例**。相比之下，MinerU 对复杂 PDF 的上限更高，但第一阶段会被它更重的部署方案和自定义许可证拖慢；Unstructured 则更偏通用 ETL 组件，且官方文档明确列出了 poppler、tesseract、libreoffice 等额外系统依赖，这对两周 Demo 并不划算。citeturn15search1turn15search2turn15search5turn14view5turn8view0
+
+还有两个值得放进备忘录但不建议放进第一阶段主路径的项目。**MarkItDown** 是微软的轻量转换工具，支持 PDF、Word、Excel、PowerPoint、图片 OCR 等多种输入，MIT 许可证，星标极高，适合做“Office 转 Markdown”的补充工具；但官方 README 同时明确提醒，它以当前进程权限执行 I/O，请在不可信输入场景里收紧调用范围，因此更适合作为工具函数，而不是你们的主解析引擎。**pdfplumber** 则非常适合做低层调试和规则兜底，因为它能拿到字符、线段、矩形等细粒度对象并可视化，但它官方也明确写了：不提供 OCR，对 OCR 后文档的表格提取支持也不强；因此它更适合作为“手术刀”，不是主战车。citeturn10view3turn11view0turn10view1turn11view1
+
+## 推荐底座与组合架构
+
+**推荐主项目底座：Haystack。**
+**推荐补充组件：Docling + PaddleOCR + Qdrant。**
+**推荐前端策略：FastAPI 内嵌极简页面，不直接套平台前端。** citeturn6view0turn15search5turn15search1turn14view0turn6view5
+
+这样选的原因很直接。Haystack 的长处不在“自带一个很炫的 UI”，而在于它把检索、嵌入、路由、生成、文档存储和模型接入都做成了很适合代码二开的 Python 组件；官方文档里同时给出了 QdrantDocumentStore、QdrantEmbeddingRetriever、QdrantHybridRetriever，多家云端/本地模型接入，以及通过 HTTP 提供 pipeline 的方式。换句话说，它非常适合被 FastAPI 包成你们自己的 API，而不是反过来让前端和平台牵着业务走。citeturn20search2turn20search3turn20search5turn20search10turn20search12
+
+Docling 作为主解析器，是因为它能把 PDF、DOCX、PPTX、XLSX、HTML、图片等多种格式转成统一的 `DoclingDocument`，并且官方反复强调它支持高级 PDF 理解、页面布局、阅读顺序、表格结构以及与 Qdrant / Haystack 的集成示例。这意味着你们不需要在第一阶段自己发明“章节切分”和“来源追溯”的基础表示，只要把 Docling 文档对象切成更适合检索的 chunk，并把页码、章节路径、bbox、原文件名塞进 payload 就行。citeturn15search2turn15search10turn15search1turn15search5
+
+PaddleOCR 作为 OCR 补充组件，负责吃掉第一阶段最容易翻车的那类样本：**扫描版 PDF、盖章页、图片型附件、复杂表格页**。它现在强调的是“把 PDF/图片直接转成 LLM-ready 的 JSON/Markdown”，并且能返回更细粒度坐标信息；这些信息非常适合拿来做“来源追溯”和“风险提示”中的可视化高亮。更重要的是，它已经被 Dify 和 RAGFlow 等顶层开源项目采用，这从侧面说明它在 LLM 场景里的工程适配性已经很成熟。citeturn6view5turn7view1
+
+Qdrant 作为向量库，是因为它同时满足了三件事：**本地 Docker 起得快、Haystack 官方支持、而且能做 dense / sparse / hybrid 检索**。官方 README 直接给出了 `docker run -p 6333:6333 qdrant/qdrant` 的本地启动方式；Haystack 官方则给出了 Qdrant document store 和 hybrid retriever 的文档；Docling 甚至也有“用 Qdrant 做检索”的官方例子。因此它是典型的“现在先用、以后不用推翻”的底层选择。citeturn14view0turn20search3turn20search5turn15search1
+
+推荐架构如下：
+
+```mermaid
+flowchart TD
+    U[历史投标文件 / 新招标文件] --> A[FastAPI 上传接口]
+    A --> B{文件判型}
+    B -->|DOCX / 可搜索 PDF| C[Docling 解析]
+    B -->|扫描 PDF / 图片页| D[PaddleOCR 解析]
+    C --> E[统一 Chunk 生成器]
+    D --> E
+    E --> F[标签化与元数据补齐]
+    F --> G[Qdrant 索引]
+    Q[用户问题 / 招标要求] --> H[Haystack Query Pipeline]
+    G --> H
+    H --> I[Hybrid Retrieval + Rerank]
+    I --> J[LLM 生成]
+    J --> K[来源追溯格式化]
+    J --> L[风险规则检查]
+    K --> M[极简 Web 页面 / API 返回]
+    L --> M
+```
+
+这里最关键的不是“用了多少开源项目”，而是**数据流要稳定**。推荐把每个 chunk 的 payload 固定为：`doc_id`、`doc_title`、`page_no`、`section_path`、`chunk_type`、`tags`、`bbox`、`table_html`、`ocr_confidence`、`source_uri`、`ingest_version`。这样一来，检索返回的不是“只有文本”的向量结果，而是“带页码、章节和坐标的证据对象”，后面的来源追溯和高亮才能自然成立。这个思路也是 RAGFlow、Dify 等平台为什么都强调知识检索结果、chunk API、citation / attribution 的原因。citeturn13search2turn17search1turn17search4turn17search6
+
+## 二开实施方案与两周开发计划
+
+**直接复用的模块** 建议包括：Haystack 的 indexing/query pipeline、Qdrant document store 与 retriever、Docling 的 `DocumentConverter`、PaddleOCR 的文档解析与结构化输出能力。**需要改造的模块** 主要包括：文件类型判型、统一 chunk schema、投标业务标签体系、回答格式器、来源追溯格式器、风险规则引擎。**建议舍弃的模块** 包括：Dify / RAGFlow 的工作流画布、团队协作、插件市场、多租户权限、复杂渠道接入；full-stack-fastapi-template 的完整 React 管理后台；AnythingLLM 的 Workspace / Agent UI；以及一切与第一阶段闭环无关的运维附加件。这样做的目的，是把“读源码 → 抄能力 → 改成投标业务字段”控制在最小改动面上。citeturn6view0turn15search2turn6view5turn12view1
+
+建议的新仓库目录长这样：
+
+```text
+bid-kb-demo/
+├── app/
+│   ├── api/
+│   │   ├── upload.py
+│   │   ├── ingest.py
+│   │   ├── query.py
+│   │   └── health.py
+│   ├── core/
+│   │   ├── settings.py
+│   │   ├── logging.py
+│   │   └── schemas.py
+│   ├── adapters/
+│   │   ├── docling_parser.py
+│   │   ├── paddleocr_parser.py
+│   │   ├── qdrant_store.py
+│   │   └── llm_gateway.py
+│   ├── services/
+│   │   ├── file_router.py
+│   │   ├── chunker.py
+│   │   ├── tagger.py
+│   │   ├── retrieve.py
+│   │   ├── answer_formatter.py
+│   │   └── risk_checker.py
+│   ├── web/
+│   │   ├── templates/
+│   │   └── static/
+│   └── main.py
+├── tests/
+├── docker/
+├── scripts/
+└── data/
+```
+
+这个目录的好处是**调用链非常清楚**：上传接口只管存文件并发起 ingest；`file_router.py` 负责根据 MIME、可搜索文本检测、页图像比例等规则决定走 Docling 还是 PaddleOCR；`chunker.py` 负责把统一文档对象切段并补 metadata；`retrieve.py` 负责走 Haystack + Qdrant；`answer_formatter.py` 负责把文档证据渲染成“来源文档 / 页码 / 章节 / 片段”；`risk_checker.py` 则把 OCR 置信度、检索得分阈值、招标强制要求命中情况合并成风险提示。citeturn15search2turn6view5turn20search3turn20search5
+
+**向量库与 Embedding 方案** 建议从一开始就分成本地优先和云端降级两档。
+本地优先：Qdrant + 本地 embedding 模型，例如 BAAI 的 `bge-m3`。BGE-M3 官方模型卡明确强调多语言、多粒度和多功能，且支持 dense 与 sparse / hybrid 思路；这与 Qdrant 的 hybrid retrieval 路线天然贴合。云端降级：如果本地 embedding 吞吐不够，就直接走 provider-hosted embeddings API；Haystack 官方文档写明它支持大量云端和本地模型提供方，因此在封装 `llm_gateway.py` 时应统一成 OpenAI-compatible / provider-agnostic 接口，不把上层业务绑死到某一家。citeturn22search0turn22search11turn20search5turn20search12
+
+**外部模型调用策略** 建议做成三层：
+第一层，主生成模型走云端 API，以保证 Demo 稳定和响应速度；Haystack 官方支持 provider-hosted APIs 与本地选项并存。
+第二层，保留本地生成接口占位，例如 Ollama / vLLM / 兼容 OpenAI SDK 的本地服务，用于断网或降成本演示。
+第三层，在 query pipeline 里加入“无检索直答禁用”策略，也就是对投标问答默认必须带检索结果入模，除非显式走闲聊模式。这样能最大限度降低“模型凭常识瞎编”的风险。citeturn20search4turn20search12turn1view2
+
+**许可证合规注意点** 要单独强调。Haystack、Qdrant、PaddleOCR、Unstructured 都是 Apache-2.0；Docling、Camelot、AnythingLLM、full-stack-fastapi-template 都是 MIT；这些是优先可用池。Dify 和 MinerU 则都不是纯 Apache，而是加了额外条件的自定义许可证，应当进入法务复核。另一个容易踩坑的点是文档处理链上的“隐性 AGPL 依赖”：pdfplumber 的比较章节明确把 PyMuPDF 标成 AGPL，因此如果你们未来做 PDF 兜底工具，不要因为示例代码方便就把 AGPL组件无审查地带进主路径。citeturn6view0turn7view6turn7view1turn8view0turn6view4turn10view0turn1view3turn7view7turn1view0turn6view7turn10view1
+
+下面是更贴近落地的两周计划。
+
+| 天 | 任务 | 产出 | 验收标准 |
+|---|---|---|---|
+| Day 1 | 初始化仓库；接入 FastAPI、Haystack、Qdrant；定义 chunk schema | 可启动服务、Qdrant 连通、数据模型固定 | `GET /health` 正常；能写入/查询空 collection |
+| Day 2 | 接入 Docling，把 DOCX / 可搜索 PDF 转统一文档对象 | `docling_parser.py` | 两份样例能输出正文、页码、章节层级 |
+| Day 3 | 接入 PaddleOCR，用于扫描 PDF / 图片页 | `paddleocr_parser.py` | 扫描 PDF 可返回文本块和坐标 |
+| Day 4 | 实现 file router 与 chunker | `file_router.py`、`chunker.py` | 同一批样例能根据类型走不同解析路径并生成统一 chunk |
+| Day 5 | 建立 Qdrant 索引与基础检索 | `qdrant_store.py`、`retrieve.py` | 给定 query 能返回 top-k chunk 和 metadata |
+| Day 6 | 接入生成模型网关；把检索结果喂给 LLM | `llm_gateway.py` | 能输出带来源片段的候选答案 |
+| Day 7 | 做来源追溯格式器 | `answer_formatter.py` | 每个答案至少返回文档名、页码、章节、片段 |
+| Day 8 | 做风险规则引擎 | `risk_checker.py` | 低 OCR 置信度、低检索分、高风险关键词能触发提示 |
+| Day 9 | 做极简前端页面 | 上传 / 查询 / 结果页 | 可在浏览器完成上传、提问、查看来源 |
+| Day 10 | 补测试、修稳定性、准备演示脚本 | Demo 版本 | 三个样例完整跑通，部署脚本一键启动 |
+
+样例测试用例至少要覆盖三种格式：
+
+| 样例 | 格式 | 设计重点 | 预期结果 |
+|---|---|---|---|
+| 样例 A | DOCX | 有规范标题层级、表格、附件说明 | 章节切分正确，表格转为可检索文本/HTML |
+| 样例 B | 可搜索 PDF | 有目录、页眉页脚、跨页表格 | 能保留页码和章节路径，页眉页脚不过度污染 chunk |
+| 样例 C | 扫描 PDF | 有盖章、图片页、低清晰文字 | OCR 可出文本，低置信度页能给出风险提示 |
+
+这三类覆盖面已经足够把“解析链”“检索链”和“风险链”打透。若你们第一阶段只做 2–3 份样例，宁可把这三份做得结构复杂一些，也不要找过分干净的 Word 文档让 Demo 失真。Docling、PaddleOCR、MinerU 等项目都在强调对表格、布局、扫描页、跨页内容的处理差异，这恰恰是投标类文档的主要难点。citeturn15search10turn6view5turn14view5
+
+## Codex 路线、多 Agent 审核与附录
+
+本地 Codex 的正确用法不是“让它生成一个完整产品”，而是让它**按仓库边界读源码、按模块输出补丁、每一步都带测试**。建议顺序是：先让 Codex 阅读 Haystack 官方示例和 Qdrant 集成方式，再阅读 Docling 的 `DocumentConverter`、Qdrant 检索示例和 Haystack RAG 示例，最后阅读 PaddleOCR 的文档解析输出格式。Docling 官方已经明确给出 Qdrant 和 Haystack 集成例子；Haystack 官方也明确给出了 Qdrant document store / retriever 和本地/云端模型接入文档。这意味着 Codex 的输入上下文应该先围绕“最短调用链”，而不是先把整个仓库都塞进去。citeturn15search1turn15search5turn20search3turn20search5turn20search12
+
+建议给 Codex 的 prompt 模板做成固定化、模块化：
+
+```text
+你要修改的仓库是 bid-kb-demo。
+只阅读并修改以下文件：
+- app/adapters/docling_parser.py
+- app/services/chunker.py
+目标：
+1. 接收本地 docx/pdf 文件路径；
+2. 使用 Docling 转成统一文档对象；
+3. 产出 List[Chunk]，每个 chunk 必须包含：
+   doc_id, page_no, section_path, text, bbox, chunk_type, source_uri
+约束：
+- 不改动 API 层；
+- 产生完整 Python 代码；
+- 为新增逻辑补 pytest；
+- 如果某字段拿不到，显式返回 None，不要伪造。
+```
+
+```text
+你要为 app/adapters/paddleocr_parser.py 生成补丁。
+目标：
+1. 输入扫描 PDF 或图片；
+2. 使用 PaddleOCR 文档解析能力；
+3. 输出统一 Chunk；
+4. 返回 OCR confidence；
+5. 如果 OCR confidence 低于阈值，写入 risk_flags。
+约束：
+- 不改 chunk schema；
+- 不新增数据库依赖；
+- 给出最小可运行版本；
+- 补一份假数据单测。
+```
+
+```text
+你要为 app/services/retrieve.py 和 app/adapters/qdrant_store.py 生成补丁。
+目标：
+1. 建立 Qdrant collection；
+2. 支持写入 chunk payload；
+3. 实现 top-k 检索；
+4. 支持 hybrid retrieval 的接口占位。
+约束：
+- 先实现 dense 检索；
+- payload 必须原样返回 doc_id/page_no/section_path/source_uri；
+- 所有异常统一抛 RepositoryError。
+```
+
+```text
+你要为 app/services/answer_formatter.py 生成补丁。
+目标：
+1. 把检索结果格式化成给 LLM 的 context；
+2. 在 API 返回中附带 sources 数组；
+3. 每条 source 必须包含 title, page_no, section_path, snippet。
+约束：
+- 不要拼接 HTML；
+- 保持 JSON 可序列化；
+- 加 3 个测试：无结果、单结果、多结果。
+```
+
+```text
+你要为 app/services/risk_checker.py 生成补丁。
+目标：
+1. 根据 OCR 置信度、检索分数、关键词规则产出 risk_flags；
+2. 关键词至少包含：必须、不得、废标、资格、交付周期、加盖公章。
+约束：
+- 规则写到可配置常量；
+- 先做纯规则版，不要接 LLM；
+- 补单测。
+```
+
+```text
+你要为 app/web/ 生成最小前端。
+页面只需要：
+- 上传文件
+- 查看入库状态
+- 输入问题
+- 展示答案、来源、风险提示
+约束：
+- 不引入重型前端框架；
+- 使用 FastAPI 模板或最小静态资源；
+- 样式保持极简。
+```
+
+人工审核点一定要放在三个位置：**解析结果抽样、来源追溯正确性、许可证与依赖树**。解析结果抽样要看 chunk 是否把页眉页脚当正文、表格是否断裂、扫描页是否错行；来源追溯要随机抽 10 条答案证据，人工回看原文页码；许可证要把 `pip freeze`、`poetry.lock` 或 `uv.lock` 跑一遍，确认没有把 AGPL 或自定义许可证组件偷偷带进主路径。尤其是 Dify 和 MinerU 的许可证，以及 PDF 工具链中对 AGPL 组件的潜在引入，都应该由人工二次审查。citeturn1view0turn6view7turn10view1
+
+多 Agent 审核机制建议至少设三个角色，并要求它们输出**独立锐评**，最后再汇总冲突点：
+
+| 子 Agent 角色 | 核心职责 | 检查清单 | 验收标准 |
+|---|---|---|---|
+| 功能评估 Agent | 看链路是否跑通、是否像 Demo | 上传→解析→入库→检索→生成→追溯→风险 是否闭环；三类样例是否全过 | 至少 3 份样例全流程通过；来源字段不为空 |
+| 代码安全 / 许可证 Agent | 看依赖风险、接口风险、许可证风险 | 依赖树、上传接口、文件路径处理、临时文件清理、自定义许可证审查 | 无高危路径穿越/任意文件读写风险；许可证清单可出文档 |
+| 部署 / 运维 Agent | 看 Docker、资源占用、可重启性 | `docker compose up` 是否一键可起；Qdrant 持久化；模型/权重缓存；日志 | Ubuntu/Docker 环境下文档可复现；冷启动时间可接受 |
+
+三份**独立锐评**建议这样写。
+功能评估 Agent 的锐评：**如果直接用 RAGFlow，视觉和演示完成度最高，但两周内做“减法”比做“加法”更难；Haystack 需要自己补 UI 和业务胶水，但每一步都可控。** 这个结论来自 RAGFlow 的成品能力定位与 Haystack 的模块化定位差异。citeturn13search2turn6view0
+
+代码安全 / 许可证 Agent 的锐评：**第一阶段最大的非技术风险不是 OCR，而是许可证和依赖污染。** Dify 与 MinerU 都是带附加条件的自定义许可证；MarkItDown 也特别提醒了 I/O 权限边界；pdfplumber 文档则直接把 PyMuPDF 标成 AGPL。只要你们把主路径收敛在 Haystack + Docling + PaddleOCR + Qdrant，这个风险面会显著下降。citeturn1view0turn6view7turn10view3turn10view1
+
+部署 / 运维 Agent 的锐评：**不要在第一阶段同时扛“重平台 + 重解析器 + 重前端”。** RAGFlow 官方 quickstart 对本地资源要求明显高于 Dify；Qdrant 则可以一条 Docker 命令启动；Docling 和 PaddleOCR 都能以库或服务形态接入。因此，最稳的做法是先把应用层做薄，把复杂度留在可替换的 adapter 上。citeturn19search2turn19search4turn14view0turn15search0
+
+最终冲突点也很清楚：**功能评估更偏向 RAGFlow，安全与部署评估更偏向 Haystack。** 解决办法不是二选一，而是**把 RAGFlow 当产品对标样板，把 Haystack 当实际代码底座**。这样既能对外回答“我们参考了业界最成熟的开源 RAG 产品长什么样”，也能对内保证“我们的代码仓库仍然是轻量、可控、可审计的”。citeturn13search2turn6view0
+
+最后给出附加清单，方便开发团队直接开工。
+
+**建议测试数据集**：
+内部主数据建议用你们自己脱敏后的标书 / 招标文件样例；公开回归集建议补三类：DocLayNet（大规模文档布局，包含 tender 等多种领域）、OmniDocBench（多样文档解析评测基准）、FUNSD（表单与键值关系识别）。DocLayNet 官方说明包含 80,863 页并覆盖多种文档来源；OmniDocBench 强调 9 类真实世界文档和多层级评测；FUNSD 则是 199 份噪声扫描表单。它们不等于投标业务数据，但很适合做解析器回归测试。citeturn21search0turn21search20turn21search3turn21search7turn21search13
+
+**建议演示脚本**：
+第一步，上传三份历史文件并展示“解析完成、章节数、表格数、页数、标签”；第二步，输入一个新招标需求问题，例如“请给出类似项目实施方案与交付周期说明”；第三步，展示检索到的历史片段、页码、章节；第四步，展示模型生成的候选响应；第五步，点击来源回看原文页码；第六步，展示风险提示，例如“扫描页 OCR 置信度较低”“未命中资格条件证据”“交付周期要求未直接命中历史案例”。这个脚本能完整覆盖甲方最关心的“可复用、可追踪、可人工复核”。citeturn13search2turn17search1turn6view5turn15search2
+
+**本地环境准备清单**：
+Ubuntu + Docker Compose；Qdrant 容器；Python 3.11 应用容器；Docling 运行环境或可选的 `docling-serve` 服务；PaddleOCR 模型与权重缓存；本地 embedding 模型如 `BAAI/bge-m3`；至少一个云端生成模型 API Key；以及上传样例目录。Qdrant 官方给了本地 Docker 启动方式；Docling 官方提供了 API 服务仓库；BGE-M3 官方模型卡说明了其多语言与 hybrid 检索特性。citeturn14view0turn15search0turn22search0turn22search11
+
+可以直接 pin 的基础版本建议如下：
+
+| 组件 | 建议版本 / 形态 | 说明 |
+|---|---|---|
+| Ubuntu | 22.04 或等效 Docker 基础镜像 | 与多数 Python / OCR 依赖兼容 |
+| Python | 3.11 | 兼顾生态兼容性与稳定性 |
+| Qdrant | `qdrant/qdrant`，建议 pin 到 1.18.x | 本地快速启动，后续可平滑升级 citeturn7view6turn14view0 |
+| Haystack | 2.30.x 左右 | 当前活跃且 Qdrant 集成成熟 citeturn12view0turn20search3 |
+| Docling | 1.x 主线或文档对应版本 | 支持多格式解析与统一表示 citeturn6view4turn15search2 |
+| PaddleOCR | 3.7.x 左右 | 当前官方已支持结构化文档解析输出 citeturn7view1turn6view5 |
+| Embedding | `BAAI/bge-m3` | 适合中英混合与 hybrid 检索思路 citeturn22search0turn22search11 |
+| 生成模型 | 任一 Haystack 支持的 provider-hosted API | 先保稳定，再决定是否本地化 citeturn20search4turn20search12 |
+
+**最终建议**：研发上按 **Haystack + Docling + PaddleOCR + Qdrant + FastAPI 薄壳** 开工；产品和汇报上以 **RAGFlow** 作为功能对标样板；法务和安全上明确把 **Dify / MinerU** 列入“只参考、不直接重度 fork”的清单。这样最符合你们当前的时间预算、默认技术栈和可交付目标。citeturn13search2turn6view0turn15search2turn6view5turn14view0turn1view0turn6view7
\ No newline at end of file
diff --git "a/docs/source-materials/originals/\346\212\225\346\240\207\346\231\272\350\203\275\347\237\245\350\257\206\345\272\223\350\203\275\345\212\233\351\252\214\350\257\201\347\211\210-PRD-v0.1.pdf" "b/docs/source-materials/originals/\346\212\225\346\240\207\346\231\272\350\203\275\347\237\245\350\257\206\345\272\223\350\203\275\345\212\233\351\252\214\350\257\201\347\211\210-PRD-v0.1.pdf"
new file mode 100644
index 0000000..660cc7f
--- /dev/null
+++ "b/docs/source-materials/originals/\346\212\225\346\240\207\346\231\272\350\203\275\347\237\245\350\257\206\345\272\223\350\203\275\345\212\233\351\252\214\350\257\201\347\211\210-PRD-v0.1.pdf"
@@ -0,0 +1,174 @@
+投标智能知识库能力验证版 PRD v0.1
+
+1. 文档定位
+
+本文档用于说明轻量验证版 Demo 的建设范围、交付内容和验证方式。
+本阶段目标不是交付完整投标系统，而是验证“历史投标文件知识库构建、招标文件解析、内容检索、候选内
+容生成、来源追溯和风险提示”这条核心链路是否可行。
+
+本 PRD 仅用于确认能力方向和验证范围，不作为完整版系统验收文件。
+
+2. 项目目标
+
+建设一个轻量 Demo，用于演示以下能力：
+
+      1. 导入历史投标文件；
+      2. 解析文件目录、正文和表格；
+      3. 按章节和标签拆分为知识卡片；
+      4. 导入新招标文件；
+      5. 识别项目要求、评分项、废标风险；
+      6. 按目标标签检索历史知识卡片；
+      7. 调用外部模型 API 生成候选内容；
+      8. 返回生成内容、来源引用、风险提示和人工复核标记；
+      9. 通过 Demo 页面展示上述结果。
+
+3. 交付形式
+
+本阶段交付形式为：
+
+      1. 一个简易 Demo 页面；
+      2. 一个后端知识库能力服务；
+      3. 一组样例文件演示数据；
+      4. 简版接口说明；
+      5. 样例 JSON 输出；
+      6. Demo 验证说明。
+
+Demo 页面仅用于能力展示，不作为正式前端系统交付。核心处理能力在后端服务中完成。
+
+4. 明确交付范围
+
+本阶段负责交付：
+
+模块    说明
+
+文件导入  支持导入样例招标文件和历史投标文件
+
+文档解析  解析 doc、docx、pdf 中的目录、正文、表格
+
+知识卡片生成 按目录、章节、标签拆分历史文件内容
+
+          1
+    模块       说明
+
+    招标文件解析 提取项目要求、评分项、废标风险
+
+    内容检索     根据目标标签检索相关历史知识卡片
+
+    内容生成     调用外部模型 API 生成候选内容
+
+    来源追溯     返回来源文件、章节、片段
+
+    风险提示     返回废标风险、低置信度、人工复核提示
+
+    Demo 展示  展示解析结果、检索结果、生成结果和 JSON
+
+5. 明确不负责范围
+
+本阶段不负责以下内容：
+
+      1. 不负责完整标书生成；
+      2. 不负责正式前端系统；
+      3. 不负责 Word / PDF 排版导出；
+      4. 不负责封面、目录、页眉页脚、Logo 等文档排版；
+      5. 不负责报价文件自动生成；
+      6. 不负责资格证明材料自动生成；
+      7. 不负责 CA 签章、投标保证金、社保、完税、软著、厂家授权等真实材料处理；
+      8. 不负责用户登录、权限系统、项目管理、文件管理等完整业务系统功能；
+      9. 不负责正式人工审核页面；
+     10. 不承诺 AI 输出可直接用于最终投标，所有生成结果均需人工复核。
+
+6. 轻量版标签范围
+
+本阶段标签先根据当前样例文件目录确定，不额外设计复杂标签体系。
+
+初始标签包括：
+
+标签  标签示例
+类型
+    投标函、开标一览表、投标分项报价表、单位负责人授权书、投标单位情况一览表、商务条款偏
+投标  离表、技术规格响应表
+正文
+类   业绩情况、团队人员、运维服务实施方案、服务重点难点分析、项目现状及需求理解、重大信息
+    安全事故保障、突发应急方案和措施、培训方案、网络和数据安全防护保障措施、服务质量保障
+评分  和考核评估方案
+响应
+类   资格条件自查表、营业执照、资格承诺函、中小企业声明函、残疾人福利性单位声明函、监狱企
+    业声明函、信用查询截图
+资格
+材料
+类
+
+完整版阶段可根据甲方后续文件继续扩展标签体系。
+
+                         2
+7. Demo 验证方式
+
+7.1 验证数据
+
+本阶段建议使用：
+
+      1. 1 份新招标文件；
+      2. 2～3 份历史投标文件；
+      3. 若干目标标签，例如：运维服务实施方案、突发应急方案和措施、网络和数据安全防护保障措施、服务
+
+          质量保障和考核评估方案。
+
+7.2 验证流程
+
+      1. 在 Demo 页面导入历史投标文件；
+      2. 后端解析目录、正文和表格；
+      3. 系统按章节和标签生成知识卡片；
+      4. 在 Demo 页面导入新招标文件；
+      5. 后端提取项目要求、评分项和废标风险；
+      6. 用户选择目标标签；
+      7. 系统检索相关历史知识卡片；
+      8. 系统调用外部模型 API 生成候选内容；
+      9. Demo 页面展示生成内容、来源引用、风险提示和 JSON 返回结果。
+
+7.3 验证结果
+
+轻量版 Demo 通过以下结果验证能力：
+
+验证项      通过标准
+
+历史文件入库 能看到历史文件拆分出的知识卡片
+
+招标文件解析 能看到项目要求、评分项、废标风险
+
+内容检索     能返回与目标标签相关的历史内容
+
+内容生成     能生成可人工修改的候选内容
+
+来源追溯     能看到内容来源文件和章节
+
+风险提示     能标记需要人工复核的风险点
+
+JSON 输出  能查看后端结构化返回结果
+
+8. 交付周期
+
+轻量验证版计划在 2 周以内完成。
+
+9. 与完整系统的关系
+
+甲方现有完整系统或其他外包团队负责正式业务系统建设。
+本阶段仅做 AI 知识库核心能力验证，不替代完整系统开发。
+
+         3
+完整系统中的用户权限、项目管理、文件管理、正式前端页面、人工审核流程、最终标书生成、文档导出等功
+能，不属于本阶段交付范围。
+
+10. 后续扩展方向
+
+若甲方认可轻量版效果，可进入完整版建设阶段，扩展方向包括：
+      1. 批量导入更多历史投标文件；
+      2. 扩展标签体系；
+      3. 扩展更多文件格式；
+      4. 增强评分项、废标项、风险项识别；
+      5. 对接甲方正式业务系统；
+      6. 增加更完整的日志、审计、权限和部署能力；
+      7. 增强模型调用稳定性和多模型适配能力。
+      8. 其他方向
+
+                                                                         4
+
diff --git a/docs/source-materials/reference-repos.md b/docs/source-materials/reference-repos.md
new file mode 100644
index 0000000..532e247
--- /dev/null
+++ b/docs/source-materials/reference-repos.md
@@ -0,0 +1,22 @@
+# Reference Repositories
+
+Reference repositories are stored outside the business repo:
+
+```text
+F:\BidKonwledge_refs
+```
+
+## Current Clones
+
+| Repo | Local Path | Commit | Notes |
+| --- | --- | --- | --- |
+| `https://github.com/infiniflow/ragflow.git` | `F:\BidKonwledge_refs\ragflow` | `f90be41` | Full RAG product reference. Use for product behavior, citations, document ingestion UX, and deployment tradeoffs. |
+| `https://github.com/deepset-ai/haystack-demos.git` | `F:\BidKonwledge_refs\haystack-demos` | `17e6103` | Engineering reference. Use `qdrant_indexing` for later indexing/query pipeline shape. |
+
+## Rules
+
+1. Do not commit these repositories into `F:\BidKonwledge`.
+2. Do not copy source files without recording origin, commit, and license.
+3. Prefer dependency usage and small adapted patterns over vendoring.
+4. Re-run `git -C <path> rev-parse --short HEAD` before relying on a reference commit in a future task.
+
diff --git a/docs/source-materials/sample-catalog.md b/docs/source-materials/sample-catalog.md
new file mode 100644
index 0000000..2da1664
--- /dev/null
+++ b/docs/source-materials/sample-catalog.md
@@ -0,0 +1,53 @@
+# Sample Catalog
+
+Source directory:
+
+`C:\Users\26561\Desktop\模型训练资料\甲方提供资料`
+
+The files below are indexed for future validation. They are not copied into Git because several are large binary documents or generated image batches.
+
+## Candidate Tender Files
+
+| File | Size | Suggested Use |
+| --- | ---: | --- |
+| `202507251108191419招标文件.doc` | 491 KB | Legacy Word tender sample; useful for later doc conversion compatibility. |
+| `KSDQZFCG（GK）2026-64喀什大学重大设备更新（5.4人工智能数据抓取及衍生智能服务创新平台-多场景应用系统-人力资源管理平台(一期））项目（二次）.docx` | 606 KB | Modern docx tender sample; good candidate for Phase 2 parsing. |
+
+## Candidate Historical Bid Files
+
+| File | Size | Suggested Use |
+| --- | ---: | --- |
+| `宁波运维项目\牧鸿\省人事工资管理服务系统宁波人社运维投标文件-投标书.docx` | 1.1 MB | Small historical bid docx; preferred early parsing sample. |
+| `宁波运维项目\牧鸿\省人事工资管理服务系统宁波人社运维投标文件-投标书.pdf` | 2.3 MB | Matching PDF; useful for pdf parsing comparison. |
+| `宁波运维项目\牧鸿\省人事工资管理服务系统-宁波人社运维-资格证明文件.docx` | 163 KB | Small qualification-material sample; useful for out-of-scope boundary checks. |
+| `宁波运维项目\九州拓新\九州拓新-资格文件.docx` | 3.0 MB | Qualification material; use only after bid-text parsing works. |
+| `宁波运维项目\九州拓新\九州拓新-投标书.docx` | 37 MB | Large historical bid file; defer until parser memory behavior is known. |
+| `宁波运维项目\浙江速微科技有限公司\浙江速微科技有限公司-投标书.docx` | 18 MB | Large historical bid file; defer until parser memory behavior is known. |
+| `5.25-带报价-喀什文件-九州拓新(1).docx` | 194 MB | Very large sample; do not use in early smoke tests. |
+
+## Image And Scanned Material
+
+| Path | Suggested Use |
+| --- | --- |
+| `宁波运维项目\九州拓新\批量输出为图片\...` | Future OCR and scanned-page validation. |
+| `宁波运维项目\浙江速微科技有限公司\批量输出为图片\...` | Future OCR and scanned-page validation. |
+| `宁波运维项目\浙江速微科技有限公司\社保证明8.11(1)\...` | Qualification evidence; useful for out-of-scope and risk handling tests. |
+
+## Other Material
+
+| File | Size | Suggested Use |
+| --- | ---: | --- |
+| `2026年-投标智能-开发计划-技术补充版.xlsx` | 38 KB | Later planning/reference material; inspect before turning into requirements. |
+| `detailQA.docx` | 14 KB | Later Q&A/reference material; inspect before using as acceptance criteria. |
+| `宁波运维项目.rar` | 229 MB | Archive copy; do not ingest directly while source folder exists. |
+
+## Recommended First Validation Set
+
+Use this set after Phase 1 is complete and Phase 2 begins:
+
+1. Tender: `KSDQZFCG（GK）2026-64...docx`
+2. Historical bid: `宁波运维项目\牧鸿\省人事工资管理服务系统宁波人社运维投标文件-投标书.docx`
+3. Historical bid PDF comparison: `宁波运维项目\牧鸿\省人事工资管理服务系统宁波人社运维投标文件-投标书.pdf`
+
+Avoid the 18 MB, 37 MB, 194 MB, and 229 MB files until parser behavior and timeout limits are known.
+
diff --git a/frontend/.gitkeep b/frontend/.gitkeep
new file mode 100644
index 0000000..8b13789
--- /dev/null
+++ b/frontend/.gitkeep
@@ -0,0 +1 @@
+
diff --git a/pyproject.toml b/pyproject.toml
new file mode 100644
index 0000000..cc63a4e
--- /dev/null
+++ b/pyproject.toml
@@ -0,0 +1,28 @@
+[project]
+name = "bidknowledge"
+version = "0.1.0"
+description = "Phase 1 backend foundation for Bid Knowledge Demo"
+requires-python = ">=3.11"
+dependencies = [
+    "fastapi>=0.115,<1.0",
+    "python-multipart>=0.0.20,<1.0",
+    "uvicorn[standard]>=0.30,<1.0",
+]
+
+[project.optional-dependencies]
+dev = [
+    "httpx>=0.27,<1.0",
+    "pytest>=8.0,<9.0",
+]
+
+[build-system]
+requires = ["setuptools>=68"]
+build-backend = "setuptools.build_meta"
+
+[tool.setuptools.packages.find]
+include = ["backend*"]
+exclude = ["data*", "frontend*", "docs*", "scripts*"]
+
+[tool.pytest.ini_options]
+testpaths = ["backend/tests"]
+pythonpath = ["."]
diff --git a/scripts/ai_build.sh b/scripts/ai_build.sh
new file mode 100644
index 0000000..98a9711
--- /dev/null
+++ b/scripts/ai_build.sh
@@ -0,0 +1,18 @@
+#!/usr/bin/env sh
+set -eu
+
+cat <<'EOF'
+Placeholder: replace scripts/ai_build.sh with this project's real build commands.
+
+Guidance:
+- This is a Python/FastAPI backend project.
+- Keep dependency installation outside this script.
+- Once Phase 1 creates packaging files, this script should run import/build checks only.
+- Keep debug and release paths distinct.
+- Do not install dependencies here.
+- Do not modify business source code here.
+
+Example shape only, not a default:
+  python -m compileall backend/app
+  python -m pip check
+EOF
diff --git a/scripts/ai_check.ps1 b/scripts/ai_check.ps1
new file mode 100644
index 0000000..aaf3d1b
--- /dev/null
+++ b/scripts/ai_check.ps1
@@ -0,0 +1,24 @@
+$ErrorActionPreference = "Stop"
+
+$repoRoot = Split-Path -Parent $PSScriptRoot
+Set-Location $repoRoot
+
+$bundledPython = "C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
+
+if ($env:PYTHON) {
+    $python = $env:PYTHON
+} elseif (Test-Path $bundledPython) {
+    $python = $bundledPython
+} else {
+    $python = "python"
+}
+
+Write-Host "Using Python: $python"
+
+Write-Host "Running compile check..."
+& $python -m compileall backend/app
+
+Write-Host "Running backend tests..."
+& $python -m pytest backend/tests
+
+Write-Host "Phase 1 project checks passed."
diff --git a/scripts/ai_check.sh b/scripts/ai_check.sh
new file mode 100644
index 0000000..12ca9ae
--- /dev/null
+++ b/scripts/ai_check.sh
@@ -0,0 +1,18 @@
+#!/usr/bin/env sh
+set -eu
+
+SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
+REPO_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
+cd "$REPO_ROOT"
+
+PYTHON_BIN=${PYTHON:-python}
+
+echo "Using Python: $PYTHON_BIN"
+
+echo "Running compile check..."
+"$PYTHON_BIN" -m compileall backend/app
+
+echo "Running backend tests..."
+"$PYTHON_BIN" -m pytest backend/tests
+
+echo "Phase 1 project checks passed."
diff --git a/scripts/ai_test.sh b/scripts/ai_test.sh
new file mode 100644
index 0000000..463da2a
--- /dev/null
+++ b/scripts/ai_test.sh
@@ -0,0 +1,17 @@
+#!/usr/bin/env sh
+set -eu
+
+cat <<'EOF'
+Placeholder: replace scripts/ai_test.sh with this project's real test commands.
+
+Guidance:
+- Run unit tests first, then integration or system tests as appropriate.
+- Keep failure output visible.
+- Do not delete failing tests to make the run pass.
+- If tests cannot run, document the reason in the task artifacts.
+- Do not install dependencies here.
+- Do not modify business source code here.
+
+Example shape only, not a default:
+  python -m pytest backend/tests
+EOF
```

## Scope Check

* [ ] Only expected files changed
* [ ] No unrelated formatting
* [ ] No generated/runtime files accidentally committed
* [ ] No public API change unless approved
* [ ] No large hidden refactor

## C++ / System Risk Check

* [ ] Ownership/lifetime safe
* [ ] Error handling complete
* [ ] No data race introduced
* [ ] API/ABI compatibility checked
* [ ] Timeout/retry semantics unchanged or explained
* [ ] Tests updated or not required with reason

## Human Decision

* [ ] Approved
* [ ] Needs fix
* [ ] Needs replan
* [ ] Rejected

## Human Notes
