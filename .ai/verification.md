# Verification

## Ran

- command: .\scripts\ai_check.ps1
- result: passed
- notes: Ran compileall and backend pytest; 37 passed, 1 warning.

- command: python -m pytest backend/tests
- result: passed
- notes: Ran with bundled Python on PATH; 37 passed, 1 warning.

- command: curl.exe --noproxy "*" http://127.0.0.1:8000/health
- result: passed
- notes: Local uvicorn smoke returned HTTP 200 and {"status":"ok"}.

## Not Run

- item: bash ./scripts/ai_check.sh
- reason: WSL/bash is unavailable on this Windows machine.
- required follow-up: Run in a shell/WSL environment before claiming bash verification.

## Phase 1 Backend Foundation Verification

Updated on 2026-06-28.

### Harness Gate And Status

Commands run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
```

Observed:

- `ai-status`: initialized yes, mode `large`, profile `python-backend-service`.
- Spec gate was rejected once because it still pointed at the stale Phase 0 spec.
- `.ai/spec.md` was rewritten for Phase 1 backend foundation.
- `ai-review spec --force` was run, then the user approved with `ai-approve spec --force`.
- `ai-review plan --force` was run, then the user approved with `ai-approve plan`.
- Current implementation proceeded after `SPEC_APPROVED` and `PLAN_APPROVED`.

### Dependency Setup

Command run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pip install -e '.[dev]'
```

Observed:

- Initial install failed because setuptools auto-discovered multiple top-level folders.
- Fixed by adding explicit setuptools package discovery for `backend*`.
- Added `python-multipart` after FastAPI reported it is required for form uploads.
- Final install passed.

### Build And Automated Tests

Commands run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m compileall backend/app
& $py -m pytest backend/tests
```

Observed:

- `compileall backend/app`: passed.
- `pytest backend/tests`: `37 passed, 1 warning`.
- Warning: FastAPI/Starlette test client reports `httpx` integration deprecation and suggests `httpx2`; this does not affect Phase 1 correctness.

Required explicit pytest command:

```powershell
$env:Path='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python;' + $env:Path
python -m pytest backend/tests
```

Observed:

- `37 passed, 1 warning`.

### Project Scripts

Command run:

```powershell
.\scripts\ai_check.ps1
```

Observed:

- Uses bundled Python when `PYTHON` is not set.
- Runs `python -m compileall backend/app`.
- Runs `python -m pytest backend/tests`.
- Result: passed, `37 passed, 1 warning`.

Command attempted:

```powershell
$env:PYTHON='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
bash ./scripts/ai_check.sh
```

Observed:

- Failed because this Windows machine has no usable WSL/Linux distribution for `bash`.
- This is recorded as not verified. Do not claim bash verification passed.
- PowerShell script is the primary Windows verification path.

### Manual Smoke

Server command:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
```

Health smoke:

```powershell
curl.exe --noproxy "*" http://127.0.0.1:8000/health
```

Observed:

```json
{"status":"ok"}
```

HTTP status: `200`.

Upload smoke:

```powershell
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/files/upload" `
  -F "doc_role=historical_bid" `
  -F "file=@.\data\samples\phase1-smoke.txt"
```

Observed:

- HTTP status: `201`.
- Response fields: `document_id`, `original_filename`, `doc_role`, `parse_status`, `file_size`, `created_at`.
- `parse_status`: `pending`.

### Reference Repository Checks

Commands run:

```powershell
git -C F:\BidKonwledge_refs\ragflow rev-parse --short HEAD
git -C F:\BidKonwledge_refs\haystack-demos rev-parse --short HEAD
```

Observed:

- RAGFlow: `f90be41`.
- Haystack demos: `17e6103`.
- Both remain outside `F:\BidKonwledge`.

### Unverified Or Deferred

- `bash ./scripts/ai_check.sh`: not verified because WSL/bash is unavailable on this Windows machine.
- Dedicated fault-injection tests now cover file write failure and metadata write failure cleanup.

## Large-Mode Requirement

All future development must run under harness `large` mode and must run the project check scripts before completion.

For this documentation-prep task, verify:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
.\scripts\ai_check.ps1
bash ./scripts/ai_check.sh
```

Observed on 2026-06-27:

- `ai-status`: initialized yes, mode `large`, profile `python-backend-service`, state valid.
- `ai-doctor`: OK for Git repo, state schema, large-mode files, and task chain; warning only for uncommitted working tree changes.
- `.\scripts\ai_check.ps1`: passed; script reported Phase 0 has no runnable backend yet and listed future Python checks.
- `bash ./scripts/ai_check.sh`: not runnable on this machine because no WSL/Linux distribution is installed; PowerShell script is the current Windows check path.

## Reference Repository Checks

Run on 2026-06-27:

```powershell
git -C F:\BidKonwledge_refs\ragflow rev-parse --short HEAD
git -C F:\BidKonwledge_refs\haystack-demos rev-parse --short HEAD
git status --short
```

Observed:

- RAGFlow reference clone: `f90be41`.
- Haystack demos reference clone: `17e6103`.
- Both clones are outside `F:\BidKonwledge`.
- `git status --short` in the business repository does not include `F:\BidKonwledge_refs`.

## Phase 1 Test-Case Documentation Check

Updated on 2026-06-27:

- `docs/ai/16-phase1-test-cases.md` now defines detailed Phase 1 automated and manual test cases.
- `docs/ai/16-phase1-test-cases.md` is explicitly an internal backend foundation test spec, not a customer-facing PRD or complete Demo acceptance document.
- Upload success is now fixed as HTTP `201 Created`.
- Upload error responses now use the fixed JSON shape `error_code`, `message`, and `details`.
- SQLite `documents` fields are now fixed in `docs/ai/12-phase1-api-persistence.md`.
- File safety and atomicity rules now require backend-generated stored filenames and cleanup when validation or persistence fails.
- Harness commands are documented as delivery command checks, not core business pytest cases.
- The document is a test-case specification for the next development session, not pytest implementation.
- Phase 1 pytest files are still expected to be created during backend implementation.
- `docs/ai/README.md`, `.ai/implementation-plan.md`, and `.ai/handoff.md` now include the detailed test-case document in required Phase 1 context.

Verification commands run after the update:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
.\scripts\ai_check.ps1
```

Observed:

- `ai-status`: initialized yes, mode `large`, profile `python-backend-service`, state valid, task chain present.
- `ai-doctor`: passed required state, mode, profile, large files, and task chain checks; warning only for uncommitted working tree changes.
- `.\scripts\ai_check.ps1`: exited successfully and reported Phase 0 has no runnable backend yet.
- `bash ./scripts/ai_check.sh`: not rerun for this documentation-only update; previous blocker remains no WSL/Linux distribution installed.

## Phase 1 Contract-Hardening Check

Updated on 2026-06-27:

- `docs/ai/12-phase1-api-persistence.md` now fixes the Phase 1 upload API contract.
- `docs/ai/04-api-contract.md` now mirrors the fixed upload success/error response shape.
- `docs/ai/03-data-model.md` now mirrors the fixed Phase 1 document metadata fields.
- `docs/ai/16-phase1-test-cases.md` now states that it is an internal backend foundation test spec, not a customer-facing PRD or full Demo acceptance document.
- `docs/ai/16-phase1-test-cases.md` now separates delivery command checks from business pytest coverage.
- The current local checkout path remains `F:\BidKonwledge`; `docs/ai/11-local-dev-env.md` records the canonical project name as `BidKnowledge` and warns not to hard-code the absolute path in tests.

Verification commands run after the contract-hardening update:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
.\scripts\ai_check.ps1
git diff --check
```

Observed:

- `ai-status`: initialized yes, mode `large`, profile `python-backend-service`, state valid, task chain present.
- `ai-doctor`: passed required state, mode, profile, large files, and task chain checks; warning only for uncommitted working tree changes.
- `.\scripts\ai_check.ps1`: exited successfully and reported Phase 0 has no runnable backend yet.
- `git diff --check`: passed.
- `rg` old-contract scan over docs and `.ai`: no matches for the prior loose status-code, old response-field, old DB-field, or pytest/script-mixing wording.
- Pytest was not run because Phase 1 backend implementation has not started.

## Current Initialization And Documentation Checks

Run on 2026-06-27:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
git status --short
Get-ChildItem -Recurse -Force docs\source-materials
Get-ChildItem -Force docs\ai
```

Observed:

- `ai-status` now reports initialized large mode with `python-backend-service` profile.
- `ai-doctor` reports valid state schema and required large files present.
- `ai-doctor` warns that the working tree has uncommitted changes, which is expected for this newly initialized repository.
- Source documents copied into `docs/source-materials/originals/`.
- Large external sample files remain outside Git and are indexed in `docs/source-materials/sample-catalog.md`.

## Phase 0 Checks

Run:

```powershell
git status --short
Get-ChildItem -Force
Get-ChildItem -Force docs/ai
Get-ChildItem -Force .ai
```

Expected:

- Git repository exists.
- Harness files exist.
- `docs/ai` contains project context files.
- `.ai` contains current planning files.
- No business implementation files are present beyond empty scaffold folders and `.gitkeep` files.

## Phase 1 Checks

Future Phase 1 should run:

```powershell
python -m pytest
python -m uvicorn app.main:app --reload
```

The exact Python command may change depending on the selected virtual environment.

Phase 1 acceptance requires:

- `GET /health` returns `{"status":"ok"}`.
- `POST /api/files/upload` returns HTTP `201 Created` for valid uploads.
- Upload success response contains `document_id`, `original_filename`, `doc_role`, `parse_status`, `file_size`, and `created_at`.
- Upload error response contains `error_code`, `message`, and `details`.
- Upload endpoint saves a file under configured upload root using a backend-generated stored filename.
- SQLite stores document metadata using the fields in `docs/ai/12-phase1-api-persistence.md`.
- Invalid uploads do not leave orphan files or metadata rows.
- Tests cover the P0 cases in `docs/ai/16-phase1-test-cases.md`.
