# Verification

## Phase 8B OCR Adapter Verification

Updated on 2026-06-28.

This section records Phase 8B implementation verification.

Implemented files:

- `backend/app/adapters/ocr_adapter.py`
- `backend/tests/test_ocr_adapter_parse.py`
- `backend/tests/test_phase8b_boundaries.py`
- `docs/ai/27-phase8b-ocr-adapter-dev-spec.md`
- `docs/ai/28-phase8b-test-cases.md`
- `docs/ai/29-phase8b-demo-runbook.md`

Updated files:

- `backend/app/api/documents.py`
- `backend/app/services/document_parsing.py`
- `backend/app/services/section_chunker.py`
- `backend/app/schemas/document.py`
- `pyproject.toml`
- `README.md`
- `docs/ai/03-data-model.md`
- `docs/ai/04-api-contract.md`
- `docs/ai/09-phase-roadmap.md`
- `docs/ai/17-lightweight-prd-completion-plan.md`
- `docs/ai/README.md`
- `.ai/*` evidence files

Commands run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
& $py -m pytest backend/tests/test_ocr_adapter_parse.py backend/tests/test_phase8b_boundaries.py backend/tests/test_document_parse_api.py backend/tests/test_word_conversion_parse.py
& $py -m pytest backend/tests
& $py -m pip check
& $py -c "import importlib.util; print(importlib.util.find_spec('paddleocr') is not None)"
.\scripts\ai_check.ps1
git diff --check
$env:PYTHON='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
bash ./scripts/ai_check.sh
```

Observed:

- `ai-status`: passed, `mode: large`, status `DONE`, `current_gate: none`.
- `ai-doctor`: passed with expected uncommitted-change warning.
- Targeted Phase 8B and parse regression pytest: `20 passed, 1 warning`.
- Explicit `python -m pytest backend/tests`: `109 passed, 1 warning`.
- `.\scripts\ai_check.ps1`: passed. It ran `compileall backend/app` and backend
  pytest: `109 passed, 1 warning`.
- `python -m pip check`: passed with no broken requirements.
- `paddleocr_available=False`; real PaddleOCR smoke was not run.
- `git diff --check`: passed with line-ending normalization warnings only.
- `bash ./scripts/ai_check.sh`: failed because no usable WSL/Linux distribution
  is available on this Windows machine.

Coverage:

- No-body parse defaults to `auto`.
- Text PDF success path does not call OCR.
- `parse_mode=text` never calls OCR.
- `parse_mode=ocr` converts fake OCR page text into sections/chunks.
- `parse_mode=auto` falls back to OCR when PDF text parse fails.
- `parse_mode=auto` falls back to OCR when text parse produces no chunks.
- OCR failures are sanitized.
- Automated OCR tests do not require PaddleOCR, Qdrant, Haystack, embeddings,
  LLM credentials, or real external services.

Unverified:

- Real PaddleOCR model/runtime smoke is not verified because PaddleOCR is not
  installed in the current bundled Python runtime.
- Bash verification remains unavailable because WSL/bash is not installed.

## Phase 8A Development Prep Verification

Updated on 2026-06-28.

This section records the documentation-prep baseline before starting Phase 8A
implementation. Phase 8A business code has not been implemented yet.

Files updated:

- `.ai/spec.md`
- `.ai/implementation-plan.md`
- `.ai/affected-files.md`
- `.ai/run-trace.md`
- `.ai/verification.md`
- `.ai/evaluation.md`
- `.ai/handoff.md`

Scope confirmed:

- Phase 8A is legacy Word / mislabeled `.docx` conversion only.
- OCR/PaddleOCR remains out of scope for this phase.
- Converted customer sample files must not be committed.
- Automated tests must not require real Word COM.

Commands run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
git diff --check
.\scripts\ai_check.ps1
```

Observed:

- `ai-status`: passed, `mode: large`, status `DONE`, `current_gate: none`.
- `ai-doctor`: passed with expected uncommitted-change warning.
- `git diff --check`: passed with line-ending normalization warnings only.
- `.\scripts\ai_check.ps1`: passed. It ran `compileall backend/app` and backend
  pytest: `91 passed, 1 warning`.

Unverified:

- Phase 8A implementation has not started yet.
- Direct KSDQZFCG upload -> parse -> tender analyze without manual conversion
  remains unverified until the adapter is implemented.
- `bash ./scripts/ai_check.sh` was not rerun in this prep update; the known
  blocker remains no usable WSL/Linux distribution on this Windows machine.

## Phase 8A Legacy Word Conversion Verification

Updated on 2026-06-28.

This section records Phase 8A implementation verification.

Implemented files:

- `backend/app/services/document_format.py`
- `backend/app/adapters/word_converter.py`
- `backend/tests/test_document_format.py`
- `backend/tests/test_word_conversion_parse.py`
- `backend/tests/test_phase8a_boundaries.py`

Updated files:

- `backend/app/api/documents.py`
- `backend/app/services/document_parsing.py`
- `backend/app/storage/database.py`
- `backend/app/schemas/document.py`
- `backend/tests/conftest.py`
- `backend/tests/test_database.py`
- `README.md`
- `docs/ai/03-data-model.md`
- `docs/ai/04-api-contract.md`
- `docs/ai/09-phase-roadmap.md`
- `docs/ai/17-lightweight-prd-completion-plan.md`
- `docs/ai/23-phase7-demo-runbook.md`
- `docs/ai/24-phase8a-word-conversion-dev-spec.md`
- `docs/ai/25-phase8a-test-cases.md`
- `docs/ai/26-phase8a-demo-runbook.md`
- `.ai/*` evidence files

Commands run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
& $py -m pytest backend/tests/test_document_format.py backend/tests/test_word_conversion_parse.py backend/tests/test_phase8a_boundaries.py
& $py -m pytest backend/tests
.\scripts\ai_check.ps1
git diff --check
$env:PYTHON='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
bash ./scripts/ai_check.sh
```

Observed:

- `ai-status`: passed, `mode: large`, status `DONE`, `current_gate: none`.
- `ai-doctor`: passed with expected uncommitted-change warning.
- Targeted Phase 8A pytest: `11 passed, 1 warning`.
- Explicit `python -m pytest backend/tests`: `102 passed, 1 warning`.
- `.\scripts\ai_check.ps1`: passed. It ran `compileall backend/app` and backend
  pytest: `102 passed, 1 warning`.
- `git diff --check`: passed with line-ending normalization warnings only.
- `bash ./scripts/ai_check.sh`: failed because no usable WSL/Linux distribution
  is available on this Windows machine.

Real sample smoke:

- Sample:
  `C:\Users\26561\Desktop\模型训练资料\甲方提供资料\KSDQZFCG（GK）2026-64喀什大学重大设备更新（5.4人工智能数据抓取及衍生智能服务创新平台-多场景应用系统-人力资源管理平台(一期））项目（二次）.docx`
- The original sample was uploaded as `doc_role=tender`; no manual
  pre-conversion was performed.
- Parse metadata:
  - `original_extension = .docx`
  - `detected_format = legacy_ole_word`
  - `is_mislabeled = true`
  - `requires_conversion = true`
  - `conversion_required = true`
  - `conversion_method = word_com`
  - `converted_path = _derived/<document_id>.converted.docx`
- Parse result:
  - `parse_status = parsed`
  - `sections_count = 10`
  - `chunks_count = 142`
- Tender analysis result:
  - `project_requirements = 26`
  - `scoring_items = 34`
  - `disqualification_risks = 52`
  - `need_human_review = true`

Notes:

- An initial smoke attempt also completed the business chain but exited non-zero
  because Windows held a temporary SQLite file during temp-directory cleanup.
  The smoke was rerun with tolerant cleanup and exited successfully.
- Local dependency confirmation:
  - `python -m pip show pywin32`: installed, version `312`
  - `python -c "import win32com.client"`: passed
  - `pyproject.toml` now declares `pywin32>=306; platform_system == 'Windows'`
    in the `parsing` optional dependency group.

Unverified:

- Bash verification remains unavailable because WSL/bash is not installed.
- Real Word COM conversion is verified on this machine, but other Windows
  environments still need Microsoft Word and pywin32 installed for manual smoke.

## Phase 7 Tender Analysis Verification

Updated on 2026-06-28.

This section records Phase 7 implementation verification.

Implemented files:

- `backend/app/api/tender.py`
- `backend/app/services/tender_analysis.py`
- `backend/tests/test_tender_analysis_api.py`
- `backend/tests/test_phase7_boundaries.py`

Updated files:

- `backend/app/main.py`
- `backend/app/schemas/document.py`
- `backend/app/storage/database.py`
- `README.md`
- `docs/ai/03-data-model.md`
- `docs/ai/04-api-contract.md`
- `docs/ai/09-phase-roadmap.md`
- `docs/ai/17-lightweight-prd-completion-plan.md`
- `docs/ai/21-phase7-tender-analysis-dev-spec.md`
- `docs/ai/22-phase7-test-cases.md`
- `docs/ai/23-phase7-demo-runbook.md`
- `.ai/*` evidence files

Commands run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
& $py -m pytest backend/tests/test_tender_analysis_api.py backend/tests/test_phase7_boundaries.py
.\scripts\ai_check.ps1
python -m pytest backend/tests
git diff --check
$env:PYTHON='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
bash ./scripts/ai_check.sh
```

Observed:

- `ai-status`: passed, `mode: large`, status `DONE`, `current_gate: none`.
- `ai-doctor`: passed with expected uncommitted-change warning.
- Targeted Phase 7 pytest: `10 passed, 1 warning`.
- `.\scripts\ai_check.ps1`: passed. It ran `compileall backend/app` and backend
  pytest: `91 passed, 1 warning`.
- Explicit `python -m pytest backend/tests`: `91 passed, 1 warning`.
- `git diff --check`: passed with line-ending normalization warnings only.
- `bash ./scripts/ai_check.sh`: failed because no usable WSL/Linux distribution
  is available on this Windows machine.

Live smoke:

- A Python smoke script seeded a temporary SQLite database with a parsed tender
  document and one chunk.
- Started uvicorn on `127.0.0.1:8786`.
- `curl.exe --noproxy "*"` `POST /api/tender/analyze` returned one project
  requirement, one scoring item with score `20.0`, and one high-severity
  disqualification risk.
- `curl.exe --noproxy "*"` `GET /api/documents/{document_id}/tender-analysis`
  returned the same persisted analysis.

Real sample smoke:

- Sample:
  `C:\Users\26561\Desktop\模型训练资料\甲方提供资料\KSDQZFCG（GK）2026-64喀什大学重大设备更新（5.4人工智能数据抓取及衍生智能服务创新平台-多场景应用系统-人力资源管理平台(一期））项目（二次）.docx`
- Direct upload/parse failed because the file extension is `.docx` but the file
  header is legacy OLE `D0 CF 11 E0`; Docling reports format `None` and skips it
  as not allowed for DOCX.
- A temporary copy renamed to `.doc` was converted to real `.docx` with Word COM.
- The converted `.docx` completed live HTTP smoke:
  - upload as `doc_role=tender`: passed
  - parse: `parse_status=parsed`, `sections_count=10`, `chunks_count=142`
  - analyze: `project_requirements=26`, `scoring_items=34`,
    `disqualification_risks=52`
  - get analysis: returned the same persisted analysis
  - `need_human_review=true`, `analysis_method=deterministic_tender_v1`

Unverified:

- Automatic legacy `.doc` or mislabeled `.docx` conversion is not implemented.
- Direct parsing of the original mislabeled `.docx` remains unsupported.
- Bash verification remains unavailable on this Windows machine unless WSL is
  installed.

## Phase 5 Demo Page And Script Verification

Updated on 2026-06-28.

### Harness And Context

Commands run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
```

Observed:

- `ai-status`: passed, initialized yes, `mode: large`, profile
  `python-backend-service`, status `DONE`, `current_gate: none`.
- `ai-doctor`: passed required checks; warning only that the working tree has
  uncommitted Phase 5 changes.
- No Phase 5 harness gate transition is claimed.

### Targeted Automated Tests

Command run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_demo_page.py backend/tests/test_phase5_boundaries.py
```

Observed:

- Passed: `4 passed, 1 warning`.
- Covered `GET /demo`, expected upload/parse/retrieve/generate hooks, raw JSON,
  citations, risks, `need_human_review`, and boundary checks that Phase 5 does
  not require external service environment variables or forbidden demo-scope
  dependencies.

### Full Backend Tests

Commands run:

```powershell
.\scripts\ai_check.ps1
$env:Path='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python;' + $env:Path
python -m pytest backend/tests
```

Observed:

- `.\scripts\ai_check.ps1`: passed. It ran `compileall backend/app` and backend
  pytest.
- Explicit `python -m pytest backend/tests`: passed, `68 passed, 1 warning`.
- Warning: existing FastAPI/Starlette test client `httpx` deprecation warning.

### Manual Smoke

Smoke command:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
# Python script starts uvicorn, then calls:
curl.exe --noproxy "*" -i "http://127.0.0.1:8770/demo"
```

Observed:

- First smoke attempt hit a Windows subprocess text-decoding error while
  reading Chinese HTML output.
- Rerun in byte mode passed.
- `GET /demo`: HTTP `200 OK`, `content-type: text/html; charset=utf-8`, and the
  response contained `BidKnowledge Demo`.

### Project Scripts And Diff Hygiene

Command attempted:

```powershell
$env:PYTHON='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
bash ./scripts/ai_check.sh
```

Observed:

- Failed because this Windows machine has no usable WSL/Linux distribution for
  `bash`.
- This is recorded as not verified. Do not claim bash verification passed.

Command run:

```powershell
git diff --check
```

Observed:

- Passed.
- Git reported line-ending normalization warnings only.

### Unverified Or Deferred

- `bash ./scripts/ai_check.sh`: not verified because WSL/bash is unavailable.
- Real external LLM provider integration is not verified. The demo page can call
  the existing generate endpoint, but automated tests do not require a real LLM
  key by design.
- OCR, Qdrant, Haystack, embeddings, production user system, and Word/PDF
  export are intentionally not part of Phase 5.

## Phase 5 Multi-Subagent Hardening Review Verification

Updated on 2026-06-28.

### Subagent Evidence

Subagents dispatched:

- Bohr: code/security review with `code-review-and-quality` and
  `security-review`.
- Aristotle: workflow/test review with `verification-before-completion` and
  `systematic-debugging`.
- Bernoulli: harness/doc review with `task-router` and
  `verification-before-completion`.

Durable review artifact:

- `.ai/reviews/phase5-demo-hardening-review.md`

Observed:

- Bohr: no blocking findings; one P2 UI robustness finding for no-LLM generate
  path.
- Aristotle: recommended persisting fake end-to-end API chain test.
- Bernoulli: required durable review artifact and `.ai` evidence updates.

### Checks Run Before Fixes

Commands run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_demo_page.py backend/tests/test_phase5_boundaries.py

$env:Path='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python;' + $env:Path
python -m pytest backend/tests

.\scripts\ai_check.ps1
```

Observed:

- Targeted Phase 5 tests: `4 passed, 1 warning`.
- Full backend pytest: `68 passed, 1 warning`.
- `.\scripts\ai_check.ps1`: passed.
- Live uvicorn + `curl.exe --noproxy "*"` `GET /demo` smoke: HTTP 200 and
  expected demo hooks.

### Fix Verification

Command run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_demo_page.py backend/tests/test_phase5_boundaries.py backend/tests/test_phase5_demo_workflow.py backend/tests/test_generation_api.py
```

Observed:

- First run failed in the new workflow test because a long Chinese sentence
  query did not match Phase 3 lexical retrieval and produced
  `MISSING_CITATIONS`.
- The test was corrected to query `应急`, matching the current deterministic
  retrieval contract.
- Rerun passed: `11 passed, 1 warning`.

### Unverified Or Deferred

- Browser JavaScript execution is still not verified with Playwright or a real
  browser; current coverage uses static hook assertions plus live HTTP smoke.
- Real external LLM provider integration is not verified.
- `bash ./scripts/ai_check.sh` remains not verified because WSL/bash is
  unavailable.

### Final Hardening Verification

Commands run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
& $py -m pytest backend/tests/test_demo_page.py backend/tests/test_phase5_boundaries.py backend/tests/test_phase5_demo_workflow.py backend/tests/test_generation_api.py
.\scripts\ai_check.ps1
$env:Path='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python;' + $env:Path
python -m pytest backend/tests
# Python script starts uvicorn, then calls:
curl.exe --noproxy "*" -i "http://127.0.0.1:8772/demo"
$env:PYTHON='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
bash ./scripts/ai_check.sh
git diff --check
```

Observed:

- `ai-status`: passed, `mode: large`, status `DONE`, `current_gate: none`.
- `ai-doctor`: passed with expected uncommitted-change warning.
- Targeted hardening pytest: `11 passed, 1 warning`.
- `.\scripts\ai_check.ps1`: passed; compileall plus backend pytest with
  `70 passed, 1 warning`.
- Explicit `python -m pytest backend/tests`: `70 passed, 1 warning`.
- Live `GET /demo` smoke: HTTP 200 and response contained
  `renderGenerationError` and `LLM_NOT_CONFIGURED`.
- `bash ./scripts/ai_check.sh`: failed because WSL/Linux distribution is
  unavailable; not verified.
- `git diff --check`: passed with line-ending normalization warnings only.

## Phase 5 User-Scoped External LLM API Config Verification

Updated on 2026-06-28.

### Targeted Tests

Command run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_generation_api.py backend/tests/test_demo_page.py backend/tests/test_phase5_demo_workflow.py
```

Observed:

- Passed: `12 passed, 1 warning`.
- Covered request-scoped `llm_config`, API key not appearing in responses,
  rejection of non-HTTPS request-scoped base URL, existing no-key environment
  fallback behavior, and demo page controls for user-provided LLM config.

### Unverified Or Deferred

- A real external LLM provider call with a real user key was not run.
- Request-scoped base URLs are intentionally limited to HTTPS. Local HTTP
  OpenAI-compatible services are not enabled through the page in this version.

### Final Verification

Commands run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_generation_api.py backend/tests/test_demo_page.py backend/tests/test_phase5_demo_workflow.py
.\scripts\ai_check.ps1
$env:Path='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python;' + $env:Path
python -m pytest backend/tests
# Python script starts uvicorn, then calls:
curl.exe --noproxy "*" -i "http://127.0.0.1:8773/demo"
$env:PYTHON='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
bash ./scripts/ai_check.sh
git diff --check
```

Observed:

- Targeted tests: `12 passed, 1 warning`.
- `.\scripts\ai_check.ps1`: passed with backend pytest `73 passed, 1 warning`.
- Explicit `python -m pytest backend/tests`: `73 passed, 1 warning`.
- Live `/demo` smoke: HTTP 200 and response contained `llm-api-key`,
  `llm-base-url`, `llm-model`, `currentLlmConfig`, and
  `requestBody.llm_config`.
- `bash ./scripts/ai_check.sh`: failed because WSL/Linux distribution is
  unavailable; not verified.
- `git diff --check`: passed with line-ending normalization warnings only.

## Lightweight PRD Completion Plan With OCR Verification

Updated on 2026-06-28.

Commands run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
git diff --check
.\scripts\ai_check.ps1
```

Observed:

- `ai-status`: passed, `mode: large`, status `DONE`, `current_gate: none`.
- `ai-doctor`: passed with expected uncommitted-change warning.
- `git diff --check`: passed with line-ending normalization warnings only.
- `.\scripts\ai_check.ps1`: passed with backend pytest `73 passed, 1 warning`.

Documentation result:

- Added `docs/ai/17-lightweight-prd-completion-plan.md`.
- Updated `docs/ai/README.md`.
- Updated `docs/ai/09-phase-roadmap.md`.

Unverified:

- No OCR implementation or real PaddleOCR smoke was run. This task only added
  the supplemental plan.

## Phase 6 Knowledge Cards And PRD Tags Verification

Updated on 2026-06-28.

This section records Phase 6 implementation verification.

Implemented files:

- `backend/app/api/knowledge.py`
- `backend/app/services/knowledge_cards.py`
- `backend/tests/test_knowledge_cards_api.py`
- `backend/tests/test_phase6_boundaries.py`

Updated files:

- `backend/app/main.py`
- `backend/app/schemas/document.py`
- `backend/app/services/tagger.py`
- `backend/app/storage/database.py`
- `README.md`
- `docs/ai/03-data-model.md`
- `docs/ai/04-api-contract.md`
- `docs/ai/09-phase-roadmap.md`
- `docs/ai/18-phase6-knowledge-cards-dev-spec.md`
- `docs/ai/19-phase6-test-cases.md`
- `docs/ai/20-phase6-demo-runbook.md`
- `.ai/*` evidence files

Commands run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
& $py -m pytest backend/tests/test_knowledge_cards_api.py backend/tests/test_phase6_boundaries.py
.\scripts\ai_check.ps1
$env:Path='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python;' + $env:Path
python -m pytest backend/tests
git diff --check
$env:PYTHON='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
bash ./scripts/ai_check.sh
```

Observed:

- `ai-status`: passed, `mode: large`, status `DONE`, `current_gate: none`.
- `ai-doctor`: passed with expected uncommitted-change warning.
- Targeted Phase 6 pytest: `8 passed, 1 warning`.
- `.\scripts\ai_check.ps1`: passed. It ran `compileall backend/app` and backend
  pytest: `81 passed, 1 warning`.
- Explicit `python -m pytest backend/tests`: `81 passed, 1 warning`.
- `git diff --check`: passed with line-ending normalization warnings only.
- `bash ./scripts/ai_check.sh`: failed because no usable WSL/Linux distribution
  is available on this Windows machine.

Live smoke:

- A Python smoke script seeded a temporary SQLite database with a parsed
  historical bid document and one chunk.
- Started uvicorn on `127.0.0.1:8785`.
- `curl.exe --noproxy "*"` `POST /api/knowledge/build` returned one card tagged
  `突发应急方案和措施`.
- `curl.exe --noproxy "*"` `GET /api/documents/{document_id}/knowledge-cards`
  returned the source chunk id and source filename.

Unverified:

- Real customer sample `.docx` knowledge-card smoke was not run in this step;
  automated and live smoke coverage used injected parser output / seeded parsed
  chunks to keep Phase 6 independent of Docling runtime.
- `bash ./scripts/ai_check.sh` remains not verified because WSL/bash is
  unavailable.

## Phase 5 Development Prep Verification

Updated on 2026-06-28.

This section records the documentation-prep baseline before starting Phase 5
implementation. Phase 5 code has not been implemented yet.

### Context And Scope

Files updated:

- `.ai/spec.md`
- `.ai/implementation-plan.md`
- `.ai/affected-files.md`
- `.ai/run-trace.md`
- `.ai/verification.md`
- `.ai/evaluation.md`
- `.ai/handoff.md`
- `README.md`

Observed:

- Phase 5 scope is limited to a minimal FastAPI-hosted demo page and demo
  script/runbook.
- OCR, Qdrant, Haystack, embeddings, production authentication, user
  management, Word/PDF export, and final approved bidding output remain out of
  scope.
- No Phase 5 business code was implemented in this prep step.

### Verification To Run For This Prep Step

Run:

```powershell
git diff --check
```

Expected:

- Passes with no whitespace errors. Line-ending normalization warnings are
  acceptable on this Windows checkout.

## Phase 4 Generation, Citations, And Risks Verification

Updated on 2026-06-28.

### Harness And Context

Commands run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
```

Observed:

- `ai-status`: passed, initialized yes, `mode: large`, profile
  `python-backend-service`, status `DONE`, `current_gate: none`.
- `ai-doctor`: passed required checks; warning only that the working tree has
  uncommitted Phase 3/4 changes.
- No Phase 4 harness gate transition is claimed.

### Targeted Automated Tests

Command run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_generation_api.py backend/tests/test_phase4_boundaries.py
```

Observed:

- Passed: `6 passed, 1 warning`.
- Covered successful generation with fake LLM, prompt source preservation,
  citations, risk flags for empty generation and missing citations, invalid
  request validation, structured not-configured LLM response, and no external
  LLM/vector/Haystack/Qdrant dependency in tests.

### Full Backend Tests

Commands run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests
.\scripts\ai_check.ps1
$env:Path='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python;' + $env:Path
python -m pytest backend/tests
```

Observed:

- Full backend pytest: passed, `64 passed, 1 warning`.
- `.\scripts\ai_check.ps1`: passed. It ran `compileall backend/app` and backend
  pytest.
- Explicit `python -m pytest backend/tests`: passed, `64 passed, 1 warning`.
- Warning: existing FastAPI/Starlette test client `httpx` deprecation warning.

### Manual Smoke

Smoke command:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
# Python script starts uvicorn, then calls:
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8766/api/generate"
```

Observed:

- `GET /health`: passed before the generation call.
- `POST /api/generate`: returned HTTP `503` with structured
  `error_code=LLM_NOT_CONFIGURED` when `OPENAI_API_KEY` was unset.
- This verifies the live route and structured no-LLM-config behavior without
  making any external LLM call.

### Project Scripts And Diff Hygiene

Command attempted:

```powershell
$env:PYTHON='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
bash ./scripts/ai_check.sh
```

Observed:

- Failed because this Windows machine has no usable WSL/Linux distribution for
  `bash`.
- This is recorded as not verified. Do not claim bash verification passed.

Command run:

```powershell
git diff --check
```

Observed:

- Passed.
- Git reported line-ending normalization warnings only.

### Unverified Or Deferred

- Live external LLM provider integration is not verified. Automated coverage
  uses a fake LLM by design.
- `bash ./scripts/ai_check.sh`: not verified because WSL/bash is unavailable.
- OCR, Qdrant ingestion, Haystack runtime, embeddings, frontend, user system,
  and export are intentionally not part of Phase 4.

## Phase 3 Retrieval Verification

Updated on 2026-06-28.

### Harness And Context

Commands run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
```

Observed:

- `ai-status`: passed, initialized yes, `mode: large`, profile
  `python-backend-service`, status `DONE`, `current_gate: none`.
- `ai-doctor`: passed required checks; warning only that the working tree has
  uncommitted Phase 3 changes.
- Harness state remains the previous completed task state. No Phase 3 gate
  transition is claimed.

### Automated Tests

Targeted Phase 3 command run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests/test_retrieval_api.py backend/tests/test_phase3_boundaries.py
```

Observed:

- Passed: `7 passed, 1 warning`.
- Covered tag-only retrieval, query-only retrieval, tag + query retrieval,
  no-match behavior, deterministic ordering and score, invalid empty request,
  and no LLM/vector-service dependency.

Full backend command run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pytest backend/tests
```

Observed:

- Passed: `58 passed, 1 warning`.
- Warning: existing FastAPI/Starlette test client `httpx` deprecation warning.

Required explicit pytest command:

```powershell
$env:Path='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python;' + $env:Path
python -m pytest backend/tests
```

Observed:

- Passed: `58 passed, 1 warning`.

### Project Scripts

Command run:

```powershell
.\scripts\ai_check.ps1
```

Observed:

- Runs `compileall backend/app`.
- Runs `pytest backend/tests`.
- Result: passed, `58 passed, 1 warning`.

Command attempted:

```powershell
$env:PYTHON='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
bash ./scripts/ai_check.sh
```

Observed:

- Failed because this Windows machine has no usable WSL/Linux distribution for
  `bash`.
- This is recorded as not verified. Do not claim bash verification passed.

### Manual Smoke

Smoke command:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
# Python script starts uvicorn against a temporary SQLite DB, then calls:
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8765/api/retrieve"
```

Observed:

- Temporary SQLite DB was pre-seeded with one parsed chunk.
- `GET /health`: passed before the retrieval call.
- `POST /api/retrieve`: passed with tag `运维服务`, query `应急`, and returned
  the expected `smoke-chunk`.
- A first smoke attempt passed the business assertion but exited non-zero during
  temporary SQLite cleanup because Windows held a file lock. The smoke was rerun
  with tolerant temporary cleanup and exited successfully.

### Diff Hygiene

Command run:

```powershell
git diff --check
```

Observed:

- Passed.
- Git reported line-ending normalization warnings only.

### Unverified Or Deferred

- `bash ./scripts/ai_check.sh`: not verified because WSL/bash is unavailable.
- Qdrant, Haystack, embeddings, LLM generation, prompt builder, OCR, frontend,
  user system, and export are intentionally not part of Phase 3 minimal local
  retrieval.

## Phase 2 Document Parsing And Chunking Verification

Updated on 2026-06-28.

### Harness And Context

Commands run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
```

Observed:

- `ai-status`: passed, initialized yes, `mode: large`, profile `python-backend-service`, status `DONE`.
- `ai-doctor`: passed required checks; warning only that the working tree has uncommitted Phase 2 changes.

### Docling Dependency Probe

Commands run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -c "import importlib.util; print(importlib.util.find_spec('docling') is not None)"
& $py -m pip index versions docling
& $py -m pip install 'docling>=2.107,<3.0'
```

Observed:

- `docling` was not installed in bundled Python.
- `pip index versions docling` found latest `2.107.0`.
- `pip install 'docling>=2.107,<3.0'` timed out after about 304 seconds.
- A residual pip Python process was confirmed by command line and stopped.
- The timeout was an interrupted heavy dependency install, not a permanent
  incompatibility. A later `pip --dry-run` showed only four packages remained.
- Retrying `pip install 'docling>=2.107,<3.0'` completed successfully and
  installed `docling-2.107.0`, `docling-slim-2.107.0`,
  `docling-ibm-models-3.13.3`, and `docling-parse-7.0.0`.

Result:

- Real Docling `.docx` parsing is verified on this machine with a synthetic
  fixture.
- Real Docling text-based `.pdf` parsing is verified on this machine with a
  generated text-layer PDF fixture.
- The code keeps Docling behind a lazy adapter and exposes it as optional `parsing` extra.
- Tests verify API, status, persistence, chunking, and tagging through an injected parser without RAG/LLM/vector dependencies.

Validation commands run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -c "import docling; from docling.document_converter import DocumentConverter; print('docling_import_ok')"
& $py -m pip check
```

Observed:

- Docling import passed.
- `pip check`: no broken requirements.
- Direct `DoclingParserAdapter` parse of a small generated `.docx`: one section parsed.
- Initial direct `DoclingParserAdapter` parse of a generated text PDF failed
  because Docling defaulted to OCR and RapidOCR failed with `Unsupported
  configuration: torch.PP-OCRv6.det.small`.
- The adapter was updated to set `PdfPipelineOptions(do_ocr=False)` for `.pdf`.
- Direct `DoclingParserAdapter` parse of the generated text PDF then passed:
  `pdfplumber` confirmed a text layer, and Docling returned one section.

### Build And Automated Tests

Commands run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pip install -e '.[dev]'
& $py -m compileall backend/app
& $py -m pytest backend/tests/test_document_parse_api.py backend/tests/test_document_chunks.py backend/tests/test_phase2_boundaries.py
& $py -m pytest backend/tests
```

Observed:

- `pip install -e '.[dev]'`: passed after adding the optional `parsing` extra.
- `compileall backend/app`: passed.
- Targeted Phase 2 tests: `13 passed, 1 warning`.
- Full backend tests: `50 passed, 1 warning`.
- Warning: FastAPI/Starlette test client reports `httpx` integration deprecation and suggests `httpx2`; no functional failure observed.
- After final self-review and CR fixes, targeted parser/chunk/database tests
  passed: `19 passed, 1 warning`.
- After final CR fixes, full backend tests passed: `51 passed, 1 warning`.

Required explicit pytest command:

```powershell
$env:Path='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python;' + $env:Path
python -m pytest backend/tests
```

Observed:

- Initially `50 passed, 1 warning`.
- After final CR fixes: `51 passed, 1 warning`.

### Final Code Review Fixes

Self-review and CR subagent review found and fixed:

- Parser failure messages could expose local absolute paths. The parsing service
  now redacts backslash Windows paths, forward-slash Windows paths, `file:///`
  URIs, configured upload roots, and configured DB parent paths.
- Parse output replacement and final `parsed` / `failed` status writes were split
  across transactions. The storage layer now has atomic
  `complete_document_parse_success` and `complete_document_parse_failure`
  helpers for the main parse success/failure paths.

Final CR subagent result:

- No blocking findings.
- No remaining findings from the prior CR.

### Project Scripts

Command run:

```powershell
.\scripts\ai_check.ps1
```

Observed:

- Runs `compileall backend/app`.
- Runs `pytest backend/tests`.
- Result: passed, `50 passed, 1 warning`.

Command attempted:

```powershell
$env:PYTHON='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
bash ./scripts/ai_check.sh
```

Observed:

- Failed because this Windows machine has no usable WSL/Linux distribution for `bash`.
- This is recorded as not verified. Do not claim bash verification passed.

### Manual Smoke

PowerShell `Start-Process` and `Start-Job` uvicorn background startup attempts failed with Windows `Access is denied`.

Fallback smoke used a Python process to start uvicorn in a thread, then called `curl.exe --noproxy "*"` against the live local server with temporary upload root and SQLite DB.

Observed before Docling retry:

- `GET /health`: passed, `{"status":"ok"}`.
- `POST /api/files/upload`: passed.
- `POST /api/documents/{document_id}/parse`: returned expected `failed` status because Docling was not installed.

Observed after Docling retry:

- `GET /health`: passed.
- `POST /api/files/upload`: passed with `parse_status=pending`.
- `POST /api/documents/{document_id}/parse`: passed with `parse_status=parsed`, `sections_count=1`, `chunks_count=1`.
- `GET /api/documents/{document_id}`: returned persisted `parsed` status.
- `GET /api/documents/{document_id}/chunks`: returned one chunk with deterministic tags `运维服务`, `应急响应`, and `项目管理`.
- Temporary upload root and SQLite DB were removed after smoke.

Observed after text-based PDF smoke:

- Generated a small synthetic text-layer PDF using `reportlab`.
- Verified the PDF text layer with `pdfplumber`.
- Direct adapter parse passed after disabling PDF OCR.
- Live API `POST /api/documents/{document_id}/parse` returned `parse_status=parsed`, `sections_count=1`, and `chunks_count=1`.
- `GET /api/documents/{document_id}/chunks` returned one chunk containing the PDF text and deterministic tags `运维服务`, `应急响应`, and `项目管理`.
- Temporary upload root, SQLite DB, and generated PDF were removed after smoke.

### Diff Hygiene

Command run:

```powershell
git diff --check
```

Observed:

- Passed.
- Git reported line-ending normalization warnings only.

### Unverified Or Deferred

- `bash ./scripts/ai_check.sh`: not verified because WSL/bash is unavailable.

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
