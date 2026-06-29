# Implementation Plan - Phase 11 Sample Outputs

## Execution Classification

- Harness mode: `large`
- Task level: Level 2 / medium
- Reason: bounded docs/sample-output/test work across multiple files
- Escalation trigger: backend API/schema/dependency changes become necessary

## Target Outcome

Another engineer can replay the demo with fixed samples and compare observed
API shape against committed representative JSON outputs.

## Plan

1. Confirm clean repo and large-mode harness state.
2. Read Phase 11 roadmap, Phase 10 runbook, source sample catalog, and current
   `.ai` handoff.
3. Add fixed sample manifest and representative JSON files.
4. Add Phase 11 dev spec, test cases, and repeatable runbook.
5. Add pytest validation for sample JSON and boundary rules.
6. Update roadmap, docs index, and `.ai` runtime artifacts.
7. Run targeted tests, project check, diff hygiene, and bash script attempt.

## Mid-Task Review

Status versus original plan:

- The task stayed inside docs/sample-output/test scope.
- No backend API, schema, dependency, or demo-page changes were required.
- The first targeted JSON test failed because `expected-failures.json` included
  a concrete secret environment-variable name. The sample was changed to use a
  generic server LLM environment phrase.

Decision: keep the Level 2 plan. No escalation is needed.

## Verification Plan

Required:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_phase11_sample_outputs.py
.\scripts\ai_check.ps1
git diff --check
```

Also attempt:

```powershell
bash ./scripts/ai_check.sh
```

If WSL/Linux distro is unavailable, record the blocker and do not claim bash
verification passed.
