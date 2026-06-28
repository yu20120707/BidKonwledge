# Handoff

## Current State - Phase 2 Document Parsing And Chunking

Phase 2 backend parsing/chunking has been implemented locally.

Current harness state:

- mode: `large`
- profile: `python-backend-service`
- state status: `DONE`
- current gate: none

Implemented backend capabilities:

1. Lazy Docling adapter at `backend/app/adapters/docling_parser.py`.
2. `POST /api/documents/{document_id}/parse`.
3. `GET /api/documents/{document_id}`.
4. `GET /api/documents/{document_id}/chunks`.
5. Additive SQLite tables for parsed sections and chunks.
6. Parse status flow: `pending -> parsing -> parsed` on injected-parser success, and `pending -> parsing -> failed` on parser or unsupported-input failure.
7. Deterministic keyword tag rules.
8. Reparse replacement of old sections/chunks.
9. Pytest coverage for success, failure, status flow, chunk persistence, boundary checks, and no RAG/LLM/vector dependency.
10. README and docs updated for Phase 2 commands and API/data-model semantics.
11. Text-based PDF parsing uses Docling with OCR explicitly disabled.
12. Parser failure messages redact local paths.
13. Parse outputs and final parse status writes use atomic SQLite helpers.

Important files changed or added:

- `pyproject.toml`
- `backend/app/main.py`
- `backend/app/api/documents.py`
- `backend/app/adapters/docling_parser.py`
- `backend/app/services/document_parsing.py`
- `backend/app/services/section_chunker.py`
- `backend/app/services/tagger.py`
- `backend/app/schemas/document.py`
- `backend/app/storage/database.py`
- `backend/tests/test_document_parse_api.py`
- `backend/tests/test_document_chunks.py`
- `backend/tests/test_phase2_boundaries.py`
- `README.md`
- `docs/ai/03-data-model.md`
- `docs/ai/04-api-contract.md`
- `.ai/spec.md`
- `.ai/implementation-plan.md`
- `.ai/affected-files.md`
- `.ai/run-trace.md`
- `.ai/verification.md`
- `.ai/evaluation.md`
- `.ai/handoff.md`

Verification run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status'
& $py 'C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor'
& $py -m pip install -e '.[dev]'
& $py -m compileall backend/app
& $py -m pytest backend/tests
.\scripts\ai_check.ps1
$env:Path='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python;' + $env:Path
python -m pytest backend/tests
bash ./scripts/ai_check.sh
```

Results:

- `ai-status`: passed, large mode confirmed.
- `ai-doctor`: passed with active-worktree warning only.
- `pip install -e '.[dev]'`: passed.
- `compileall backend/app`: passed.
- `pytest backend/tests`: initially `50 passed, 1 warning`; after final CR fixes `51 passed, 1 warning`.
- `.\scripts\ai_check.ps1`: passed.
- Explicit `python -m pytest backend/tests`: `50 passed, 1 warning`.
- `bash ./scripts/ai_check.sh`: attempted and failed because WSL/bash is unavailable.
- uvicorn + `curl.exe --noproxy "*"` smoke: health, upload, parse, document, and chunks passed with a synthetic `.docx`; parse returned `parsed`, one section, one chunk, and deterministic tags.
- uvicorn + `curl.exe --noproxy "*"` smoke: health, upload, parse, document, and chunks passed with a generated text-layer `.pdf`; parse returned `parsed`, one section, one chunk, and deterministic tags.
- CR subagent final review: no blocking findings and no remaining findings.

Docling note:

- Bundled Python initially did not have `docling`.
- `pip index versions docling` found latest `2.107.0`.
- The first `pip install 'docling>=2.107,<3.0'` timed out after about 304 seconds after installing most large dependencies.
- A second `pip install 'docling>=2.107,<3.0'` completed successfully.
- Real Docling `.docx` parse success is verified with a small generated fixture.
- Initial text-based `.pdf` parse failed because Docling defaulted to OCR and RapidOCR rejected `torch.PP-OCRv6.det.small`.
- The adapter now sets `PdfPipelineOptions(do_ocr=False)` for `.pdf`, and text-based PDF smoke passes.

Next recommended action:

```md
Use the current Phase 2 parser for small `.docx` and text-based `.pdf` only. Keep scanned PDFs/OCR as a later explicit phase.
```

## Current State - Phase 1 Backend Foundation

Phase 1 backend foundation has been implemented locally.

Current harness state before final gate review:

- mode: `large`
- profile: `python-backend-service`
- spec gate: approved by user
- plan gate: approved by user
- next harness action after implementation: `ai-review diff`

Implemented backend capabilities:

1. FastAPI app startup through `backend.app.main:app`.
2. `GET /health`.
3. `POST /api/files/upload`.
4. Configurable local upload root.
5. Backend-generated stored filename.
6. SQLite `documents` metadata persistence.
7. Fixed upload success and error response contracts.
8. P0 pytest coverage for Phase 1 backend foundation.

Important files changed or added:

- `pyproject.toml`
- `backend/__init__.py`
- `backend/app/__init__.py`
- `backend/app/main.py`
- `backend/app/config.py`
- `backend/app/api/health.py`
- `backend/app/api/files.py`
- `backend/app/schemas/document.py`
- `backend/app/storage/database.py`
- `backend/app/storage/file_storage.py`
- `backend/tests/conftest.py`
- `backend/tests/test_health.py`
- `backend/tests/test_upload_contract.py`
- `backend/tests/test_upload_validation.py`
- `backend/tests/test_storage.py`
- `backend/tests/test_database.py`
- `backend/tests/test_phase1_boundaries.py`
- `scripts/ai_check.ps1`
- `scripts/ai_check.sh`
- `README.md`
- `.ai/spec.md`
- `.ai/implementation-plan.md`
- `.ai/affected-files.md`
- `.ai/run-trace.md`
- `.ai/verification.md`
- `.ai/evaluation.md`
- `.ai/handoff.md`

Verification run:

```powershell
$py='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m pip install -e '.[dev]'
& $py -m compileall backend/app
& $py -m pytest backend/tests
.\scripts\ai_check.ps1
$env:Path='C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python;' + $env:Path
python -m pytest backend/tests
curl.exe --noproxy "*" http://127.0.0.1:8000/health
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/files/upload" -F "doc_role=historical_bid" -F "file=@.\data\samples\phase1-smoke.txt"
```

Results:

- `compileall backend/app`: passed.
- `pytest backend/tests`: `37 passed, 1 warning`.
- `.\scripts\ai_check.ps1`: passed.
- `python -m pytest backend/tests`: passed with bundled Python placed on PATH.
- Health smoke: HTTP 200, `{"status":"ok"}`.
- Upload smoke: HTTP 201, fixed Phase 1 success fields.
- `bash ./scripts/ai_check.sh`: attempted and failed because WSL/bash is unavailable; do not claim passed.

Subagents used:

1. Hooke: read-only API/persistence/test-contract scan.
2. Meitner: read-only scripts/README/verification scan.
3. Bohr: read-only implementation review after coding.

Residual risks:

- Dedicated forced file-write and metadata-write failure tests are now covered.
- FastAPI/Starlette test client emits a deprecation warning related to `httpx`; tests still pass.
- Phase 1 remains backend foundation only; it is not OCR/RAG/LLM/frontend demo completion.

Next recommended action:

```md
Review the Phase 1 diff. If acceptable, approve the diff gate so the agent can run final gate review and close the Phase 1 backend foundation task.
```

## Current State

The repository has been initialized for the 投标智能知识库能力验证版 Demo.

Auto_AICoding_Harness has been upgraded to `large` mode with the `python-backend-service` profile.

Future development in this repository must use large mode and must run the project scripts before completion.

Latest verification:

- `ai-status` and `ai-doctor` pass for large mode.
- `scripts/ai_check.ps1` runs successfully.
- `bash ./scripts/ai_check.sh` was attempted but cannot run because WSL is not installed.

## Important Context

Read these first:

1. `docs/ai/00-project-brief.md`
2. `docs/ai/01-scope-boundary.md`
3. `docs/ai/05-dev-rules.md`
4. `docs/ai/08-tech-selection.md`
5. `docs/ai/09-phase-roadmap.md`
6. `docs/source-materials/README.md`
7. `docs/source-materials/sample-catalog.md`
8. `.ai/spec.md`
9. `.ai/implementation-plan.md`
10. `docs/ai/10-phase1-dev-spec.md`
11. `docs/ai/11-local-dev-env.md`
12. `docs/ai/12-phase1-api-persistence.md`
13. `docs/ai/13-phase1-verification-checklist.md`
14. `docs/ai/14-reference-reuse-strategy.md`
15. `docs/ai/15-target-architecture.md`
16. `docs/ai/16-phase1-test-cases.md`

## Next Recommended Prompt

```md
当前仓库已经完成 0 阶段初始化，并已升级到 Auto_AICoding_Harness large mode。请先运行 ai-status / ai-doctor，确认 .ai/state.json 中 mode=large 且 profile=python-backend-service。

请先阅读：
- AGENTS.md
- docs/ai/10-phase1-dev-spec.md
- docs/ai/11-local-dev-env.md
- docs/ai/12-phase1-api-persistence.md
- docs/ai/13-phase1-verification-checklist.md
- docs/ai/16-phase1-test-cases.md
- .ai/implementation-plan.md
- .ai/verification.md

现在开始执行 Phase 1。

只实现以下内容：

1. FastAPI app 启动；
2. GET /health；
3. POST /api/files/upload，成功响应固定为 HTTP 201；
4. 结构化错误响应，字段为 error_code / message / details；
5. 本地文件保存到配置化 upload root，真实存储名由后端生成；
6. Document metadata schema，字段按 docs/ai/12-phase1-api-persistence.md；
7. SQLite 初始化；
8. 基础配置管理；
9. docs/ai/16-phase1-test-cases.md 中的 P0 pytest 覆盖；
10. 最小 smoke test；
11. README 中补充本地启动命令。

不要实现 OCR、LLM、embedding、vector store、知识卡片生成、招标文件分析、Demo 页面、用户系统、Word/PDF 导出。

注意：Phase 1 只是后端底座，不是甲方 Demo 验收。

实现完成后更新 .ai/evaluation.md 和 .ai/handoff.md，并列出新增文件、修改文件、运行命令、测试命令、验证结果、下一步建议。

必须运行项目脚本，并把结果写入 .ai/verification.md。
```

## Source Materials

Project materials are under:

`C:\Users\26561\Desktop\模型训练资料`

Copied lightweight source documents:

- `docs/source-materials/originals/投标智能知识库能力验证版-PRD-v0.1.pdf`
- `docs/source-materials/originals/deep-research-report.md`

Large sample files were not copied into Git. Use `docs/source-materials/sample-catalog.md` to select validation files.

Reference repositories:

- `F:\BidKonwledge_refs\ragflow`
- `F:\BidKonwledge_refs\haystack-demos`

These are reference-only clones and should not be committed into the business repo.
