# Bid Knowledge Demo

投标智能知识库能力验证版 Demo。

当前仓库已完成 Phase 4：Generation, Citations, And Risks。

Phase 3 提供后端最小检索能力：基于 Phase 2 已入库 chunks，支持 tag 过滤、简单 query 关键词匹配、确定性排序和 metadata-preserving 检索结果。

Phase 3 仍不包含 OCR、embedding、vector store、Haystack/Qdrant runtime、LLM generation、Prompt builder、知识卡片完整生成、前端 Demo、用户系统或 Word/PDF 导出。

Phase 4 提供后端最小生成能力：基于 Phase 3 retrieval context 生成候选内容，保留 citations，输出 rule-based risks，并始终返回 `need_human_review = true`。

Phase 5 尚未实现。Phase 5 的开发前目标是：提供最小 FastAPI-hosted demo page 和 demo script，串联 upload、parse、retrieve、generate，并展示 raw JSON、citations、risks 和 human-review 状态。

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

Retrieve persisted chunks:

```powershell
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/retrieve" `
  -H "Content-Type: application/json" `
  -d "{\"tag\":\"运维服务\",\"query\":\"应急\",\"top_k\":5}"
```

Retrieval is deterministic and local in Phase 3. It reads parsed chunks from SQLite and does not call Qdrant, Haystack, embeddings, or LLM services.

## Phase 4 API

- `POST /api/generate`

Request:

```json
{
  "target_tag": "运维服务",
  "query": "根据招标要求生成运维服务应急方案",
  "top_k": 5
}
```

Response:

```json
{
  "target_tag": "运维服务",
  "generated_content": "string",
  "citations": [],
  "risks": [],
  "need_human_review": true
}
```

Phase 4 must be testable with an injected fake LLM and must not require real LLM credentials in automated tests.

## Phase 5 Planned Demo

- `GET /demo`

Planned demo flow:

1. Upload a small `.docx` or text-based `.pdf`.
2. Parse the uploaded document.
3. Retrieve relevant chunks by tag/query.
4. Generate candidate content from retrieval context.
5. Display raw JSON, citations, risks, and `need_human_review`.

Phase 5 remains a local capability demo. It must not introduce OCR, Qdrant, Haystack, production authentication, Word/PDF export, or final approved bidding output.

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

## Phase 3 API

- `POST /api/retrieve`

Retrieval request:

```json
{
  "query": "应急",
  "tag": "运维服务",
  "top_k": 5
}
```

`query` or `tag` is required. Results are chunk-based and preserve source metadata:

```json
{
  "query": "应急",
  "tag": "运维服务",
  "results": [
    {
      "chunk_id": "string",
      "document_id": "string",
      "section_id": "string",
      "section_title": "运维服务应急",
      "section_path": "运维服务应急",
      "text": "string",
      "tags": ["运维服务", "应急响应"],
      "score": 2.0,
      "source": {
        "original_filename": "retrieval.docx",
        "doc_role": "historical_bid",
        "file_ext": ".docx",
        "page_start": null,
        "page_end": null,
        "chunk_metadata": {
          "tagger": "deterministic_v1"
        }
      }
    }
  ]
}
```

## Source Documents

- [PRD PDF](docs/source-materials/originals/投标智能知识库能力验证版-PRD-v0.1.pdf)
- [Deep research report](docs/source-materials/originals/deep-research-report.md)
- `C:\Users\26561\Desktop\模型训练资料\甲方提供资料`

See [source material index](docs/source-materials/README.md) and [sample catalog](docs/source-materials/sample-catalog.md).

External reference repositories are kept outside Git under `F:\BidKonwledge_refs`; see [reference-repos.md](docs/source-materials/reference-repos.md).

## Boundary

This is not a complete bidding system. Phase 3 is only the backend parsing/chunking plus local retrieval foundation. Phase 4 generated content must remain candidate content only.

All generated bidding content in future phases must require human review.
