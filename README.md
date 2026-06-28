# Bid Knowledge Demo

投标智能知识库能力验证版 Demo。

当前仓库已完成 Phase 8A：Legacy / Mislabeled Word Conversion Adapter。

Phase 3 提供后端最小检索能力：基于 Phase 2 已入库 chunks，支持 tag 过滤、简单 query 关键词匹配、确定性排序和 metadata-preserving 检索结果。

Phase 3 本身不包含 OCR、embedding、vector store、Haystack/Qdrant runtime、LLM generation、Prompt builder、知识卡片完整生成、用户系统或 Word/PDF 导出。

Phase 4 提供后端最小生成能力：基于 Phase 3 retrieval context 生成候选内容，保留 citations，输出 rule-based risks，并始终返回 `need_human_review = true`。

Phase 5 提供最小 FastAPI-hosted demo page，串联 upload、parse、retrieve、generate，并展示 raw JSON、citations、risks 和 human-review 状态。

Phase 6 提供历史标书知识卡片能力：从已解析 chunks 构建可追溯 knowledge cards，写入 SQLite，并输出 PRD 对齐标签。

Phase 7 提供招标文件分析能力：从已解析 tender chunks 提取项目需求、评分项、废标/否决风险，并保留证据来源和 human review 状态。

Phase 8A 提供 legacy Word / mislabeled `.docx` 转换适配：parse 前检测真实文件头，识别 true `.docx` ZIP 内容和 legacy OLE `.doc` 内容；legacy `.doc` 或 OLE 内容的 mislabeled `.docx` 会在内部派生路径转换为 true `.docx` 后进入现有 Docling parse。原始上传文件不被修改，转换元数据记录在 parse metadata 中。

Phase 8B 提供最小 OCR adapter：`POST /api/documents/{document_id}/parse` 支持 `parse_mode=auto|text|ocr`。默认 `auto` 保持 Docling 文本解析优先；PDF 文本解析失败或无 chunks 时回退 OCR。自动化测试使用 fake OCR，不依赖 PaddleOCR。

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
  "top_k": 5,
  "llm_config": {
    "api_key": "user-provided-key",
    "base_url": "https://api.openai.com/v1",
    "model": "gpt-4o-mini"
  }
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

`llm_config` is optional. If it is omitted, the backend uses `OPENAI_API_KEY`,
`OPENAI_BASE_URL`, and `OPENAI_MODEL` from the server environment. If it is
provided, the API key is used only for that request and is not returned in the
response. Request-scoped `base_url` must be HTTPS.

Phase 4 must be testable with an injected fake LLM and must not require real LLM credentials in automated tests.

## Phase 5 Demo

- `GET /demo`

Start backend:

```powershell
$py = "C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
& $py -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
```

Open:

```powershell
curl.exe --noproxy "*" http://127.0.0.1:8000/demo
```

Demo flow:

1. Upload a small `.docx` or text-based `.pdf`.
2. Parse the uploaded document.
3. Retrieve relevant chunks by tag/query.
4. Generate candidate content from retrieval context.
5. Display raw JSON, citations, risks, and `need_human_review`.
6. Optionally enter a user-owned OpenAI-compatible API key, HTTPS base URL, and model for the generate step.

Phase 5 remains a local capability demo. It must not introduce OCR, Qdrant, Haystack, production authentication, Word/PDF export, or final approved bidding output.

If no real LLM key is configured, the generate step returns the existing structured `LLM_NOT_CONFIGURED` response. The demo page keeps the human-review state visible and displays this as a risk item. Automated tests do not require a real LLM key.

## Phase 6 Knowledge Cards

- `POST /api/knowledge/build`
- `GET /api/documents/{document_id}/knowledge-cards`

Build cards for a parsed historical bid document:

```powershell
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/knowledge/build" `
  -H "Content-Type: application/json" `
  -d "{\"document_id\":\"<document_id>\"}"
```

List cards:

```powershell
curl.exe --noproxy "*" "http://127.0.0.1:8000/api/documents/<document_id>/knowledge-cards"
```

Knowledge cards preserve source chunk id, source filename, section title/path, page fields, confidence, and deterministic tagger metadata. Phase 6 tags are keyword-based PRD labels such as `运维服务实施方案`, `突发应急方案和措施`, `网络和数据安全防护保障措施`, and `服务质量保障和考核评估方案`.

Phase 6 does not implement OCR, tender analysis, Qdrant, Haystack, embeddings, production user accounts, export, or final approved bidding output.

## Phase 7 Tender Analysis

APIs:

- `POST /api/tender/analyze`
- `GET /api/documents/{document_id}/tender-analysis`

Analyze a parsed tender document:

```powershell
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/tender/analyze" `
  -H "Content-Type: application/json" `
  -d "{\"document_id\":\"<document_id>\"}"
```

Get the latest analysis:

```powershell
curl.exe --noproxy "*" "http://127.0.0.1:8000/api/documents/<document_id>/tender-analysis"
```

Response shape:

```json
{
  "document_id": "string",
  "project_requirements": [],
  "scoring_items": [],
  "disqualification_risks": [],
  "raw_text_summary": "string",
  "analysis_method": "deterministic_tender_v1",
  "need_human_review": true,
  "metadata": {}
}
```

Phase 7 is deterministic and evidence-based. It does not claim legal or
compliance completeness, and it does not require OCR, Qdrant, Haystack,
embeddings, or LLM credentials.

Sample note: the recommended `KSDQZFCG...项目（二次）.docx` tender sample has a
`.docx` extension but legacy OLE `.doc` content. Direct Docling parsing rejects
it. Manual smoke passed after converting a temporary copy to true `.docx` with
Word. Phase 8A now provides the automatic local conversion adapter for this
case when Microsoft Word COM is available on Windows.

## Phase 8A Legacy Word Conversion

Phase 8A adds parse-time format detection and optional Word conversion.

Detected formats:

- true `.docx`: ZIP header `PK`
- legacy Word `.doc`: OLE header `D0 CF 11 E0`
- PDF: `%PDF`

Behavior:

1. True `.docx` and text-based `.pdf` continue through the existing Docling
   parser path.
2. Legacy `.doc` and mislabeled `.docx` with OLE content are converted to an
   internal derived `.docx` path before parsing.
3. The original uploaded file remains unchanged.
4. `parse_metadata` records original extension, detected format, conversion
   method, and converted relative path.
5. Automated tests use fake converters and do not require Microsoft Word.

This phase does not implement OCR, PaddleOCR, Qdrant, Haystack, embeddings,
LLM-based parsing, user systems, export, or final bidding output.

Real Windows conversion requires Microsoft Word and pywin32. On this local
machine, `pywin32 312` is installed in the bundled Python runtime and
`win32com.client` imports successfully.

## Phase 8B OCR Adapter

Install optional OCR dependencies only when running real OCR smoke:

```powershell
$py = "C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
& $py -m pip install -e ".[ocr]"
```

Parse modes:

```powershell
curl.exe --noproxy "*" -X POST "http://127.0.0.1:8000/api/documents/<document_id>/parse" `
  -H "Content-Type: application/json" `
  -d "{\"parse_mode\":\"auto\"}"
```

- `auto`: existing parser first; PDF can fallback to OCR.
- `text`: existing parser only; OCR disabled.
- `ocr`: OCR only for PDF in Phase 8B.

OCR output is persisted through the normal sections/chunks tables. Chunk
metadata includes OCR evidence such as engine, page count, and confidence.
Phase 8B does not implement table reconstruction, certificate validation,
Qdrant/Haystack, embeddings, LLM parsing, or final document output.

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

This is not a complete bidding system. Phase 5 is only a local demo layer over the existing backend chain. Phase 6 adds a deterministic historical knowledge-card layer, not final document generation. Phase 4/5 generated content must remain candidate content only.

All generated bidding content in future phases must require human review.
