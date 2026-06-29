# Verification

## Phase 10 PRD-shaped Demo Page Flow Verification

Updated on 2026-06-29.

Updated files:

- `backend/app/static/demo.html`
- `backend/tests/test_demo_page.py`
- `backend/tests/test_phase5_boundaries.py`
- `backend/tests/test_phase5_demo_workflow.py`
- `docs/ai/09-phase-roadmap.md`
- `docs/ai/README.md`
- `docs/ai/33-phase10-prd-demo-flow-dev-spec.md`
- `docs/ai/34-phase10-test-cases.md`
- `docs/ai/35-phase10-demo-runbook.md`
- `.ai/spec.md`
- `.ai/implementation-plan.md`
- `.ai/affected-files.md`
- `.ai/run-trace.md`
- `.ai/verification.md`
- `.ai/evaluation.md`
- `.ai/handoff.md`

Commands run:

```powershell
git status --short --branch
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
& $py -m pytest backend/tests/test_demo_page.py backend/tests/test_phase5_demo_workflow.py
.\scripts\ai_check.ps1
git diff --check
bash ./scripts/ai_check.sh
@'
from fastapi.testclient import TestClient
from backend.app.main import app
with TestClient(app) as client:
    response = client.get('/demo')
    print(response.status_code)
'@ | & $py -
```

Observed:

- `git status --short --branch`: clean baseline before Phase 10 edits.
- `ai-status`: passed, `mode: large`, status `DONE`, `current_gate: none`.
- `ai-doctor`: passed, working tree clean before edits.
- targeted pytest:
  - first run: `5 passed, 1 failed, 1 warning`
  - failure cause: fake parser dependency override returned a new parser
    instance per request, so the tender parse did not use the intended tender
    fixture text
  - fix: share one fake parser instance in the workflow test
  - rerun: `6 passed, 1 warning`
- targeted regression after boundary-test update:
  - `backend/tests/test_phase5_boundaries.py`
  - `backend/tests/test_demo_page.py`
  - `backend/tests/test_phase5_demo_workflow.py`
  - result: `8 passed, 1 warning`
- `.\scripts\ai_check.ps1`: passed
  - compile check passed
  - backend pytest passed: `111 passed, 1 warning`
- `git diff --check`: passed with line-ending normalization warnings only
- `bash ./scripts/ai_check.sh`: failed because no usable WSL/Linux distro is
  available on this Windows machine
- `/demo` HTTP smoke through FastAPI TestClient: HTTP `200`; response contained
  the Phase 10 title and OCR production-readiness boundary copy

Unverified:

1. Bash verification remains unavailable because WSL/Linux distro is not
   installed.
