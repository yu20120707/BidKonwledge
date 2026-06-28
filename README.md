# Bid Knowledge Demo

投标智能知识库能力验证版 Demo。

当前仓库已进入 Phase 2：Document Parsing And Chunking。Phase 2 提供后端最小解析能力：文件上传、Docling 解析适配、section/chunk 入库、确定性标签、解析状态流转和最小查询 API。

Phase 2 仍不包含 OCR、embedding、vector store、Haystack retrieval、LLM generation、知识卡片完整生成、前端 Demo、用户系统或 Word/PDF 导出。

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

基础后端和测试依赖：

```powershell
$py = "C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
& $py -m pip install -e ".[dev]"
```

真实 Docling 解析依赖：

```powershell
$py = "C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
& $py -m pip install -e ".[parsing]"
```

If Docling installation is unavailable or too slow on the current machine, the app still imports and tests can validate the API/state/persistence flow with an injected parser. Real `.docx`/text PDF parsing requires the `parsing` extra.

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
Set-Content -Path .\data\samples\phase2-smoke.docx -Value "synthetic docx placeholder"
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/files/upload" `
  -F "doc_role=historical_bid" `
  -F "file=@.\data\samples\phase2-smoke.docx"
```

Parse an uploaded document:

```powershell
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/documents/<document_id>/parse"
curl.exe --noproxy "*" "http://127.0.0.1:8000/api/documents/<document_id>"
curl.exe --noproxy "*" "http://127.0.0.1:8000/api/documents/<document_id>/chunks"
```

Use a real small `.docx` or text-based `.pdf` when Docling is installed. The synthetic placeholder command only demonstrates the upload path.

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

## Phase 2 API

- `POST /api/documents/{document_id}/parse`
- `GET /api/documents/{document_id}`
- `GET /api/documents/{document_id}/chunks`

Parse statuses:

- `pending`
- `parsing`
- `parsed`
- `failed`

Chunks are persisted in SQLite with normalized text payloads, section metadata, page placeholders, deterministic tags, and metadata identifying `deterministic_v1` tagging.

## Source Documents

- [PRD PDF](docs/source-materials/originals/投标智能知识库能力验证版-PRD-v0.1.pdf)
- [Deep research report](docs/source-materials/originals/deep-research-report.md)
- `C:\Users\26561\Desktop\模型训练资料\甲方提供资料`

See [source material index](docs/source-materials/README.md) and [sample catalog](docs/source-materials/sample-catalog.md).

External reference repositories are kept outside Git under `F:\BidKonwledge_refs`; see [reference-repos.md](docs/source-materials/reference-repos.md).

## Boundary

This is not a complete bidding system. Phase 2 is only the backend parsing/chunking foundation for later retrieval and generation.

All generated bidding content in future phases must require human review.
