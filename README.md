# Bid Knowledge Demo

投标智能知识库能力验证版 Demo。

当前仓库已进入 Phase 1：后端底座。Phase 1 只提供 FastAPI 启动、健康检查、文件上传、本地文件保存和 SQLite 元数据记录，不包含 OCR、RAG、LLM、知识卡片、前端 Demo 或导出能力。

## Harness

本仓库使用 `Auto_AICoding_Harness`，当前为 `large` mode，profile 为 `python-backend-service`。

常用检查命令：

```powershell
$py = "C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
& $py "C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-status"
& $py "C:\Users\26561\Documents\Auto_AICoding_Harness\bin\ai-doctor"
```

## Local Setup

推荐使用 Codex bundled Python 或本地 Python 3.11+。

```powershell
$py = "C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
& $py -m pip install -e ".[dev]"
```

## Run Backend

```powershell
$py = "C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
& $py -m uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
```

Health check:

```powershell
curl.exe --noproxy "*" http://127.0.0.1:8000/health
```

Upload smoke:

```powershell
Set-Content -Path .\data\samples\phase1-smoke.txt -Value "hello bid knowledge"
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/files/upload" `
  -F "doc_role=historical_bid" `
  -F "file=@.\data\samples\phase1-smoke.txt"
```

## Test

```powershell
$py = "C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
& $py -m compileall backend/app
& $py -m pytest backend/tests
.\scripts\ai_check.ps1
```

If a shell environment is available:

```powershell
bash ./scripts/ai_check.sh
```

On Windows machines without WSL or bash, use `scripts/ai_check.ps1` as the primary project check and record the bash limitation in `.ai/verification.md`.

## Phase 1 API

- `GET /health`
- `POST /api/files/upload`

Upload request:

- `multipart/form-data`
- `file`: `.txt`, `.pdf`, `.doc`, or `.docx`
- `doc_role`: `historical_bid` or `tender`

Successful uploads return HTTP `201 Created` with:

- `document_id`
- `original_filename`
- `doc_role`
- `parse_status`
- `file_size`
- `created_at`

Error responses use:

- `error_code`
- `message`
- `details`

## Source Documents

- [PRD PDF](docs/source-materials/originals/投标智能知识库能力验证版-PRD-v0.1.pdf)
- [Deep research report](docs/source-materials/originals/deep-research-report.md)
- `C:\Users\26561\Desktop\模型训练资料\甲方提供资料`

See [source material index](docs/source-materials/README.md) and [sample catalog](docs/source-materials/sample-catalog.md).

External reference repositories are kept outside Git under `F:\BidKonwledge_refs`; see [reference-repos.md](docs/source-materials/reference-repos.md).

## Boundary

This is not a complete bidding system. Phase 1 is only the backend foundation for later document parsing and knowledge-base capability.

All generated bidding content in future phases must require human review.
