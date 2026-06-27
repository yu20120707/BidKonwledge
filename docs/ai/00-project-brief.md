# Project Brief - 投标智能知识库 Demo

## Project One-Liner

This project is a lightweight "投标智能知识库能力验证 Demo" used to validate the core AI knowledge-base chain:

historical bid file ingestion -> document parsing -> section and tag splitting -> tender parsing -> knowledge retrieval -> LLM candidate content generation -> source citation -> risk hints.

## Current Phase

The current phase is 0 阶段初始化.

This phase initializes the repository, records durable AI context, and prepares implementation plans. It does not build business features.

## Demo Goal

The MVP should demonstrate:

1. Upload historical bid files.
2. Parse doc, docx, and pdf directory text, body text, and tables.
3. Split content into sections and tagged knowledge cards.
4. Upload a new tender file.
5. Extract project requirements, scoring items, and disqualification risks.
6. Retrieve historical knowledge cards by target tag and query.
7. Call an external LLM API to generate candidate content.
8. Return generated content, source citations, risk hints, and human review markers.
9. Show the result and raw JSON in a minimal demo page.

## Delivery Shape

The validation demo should eventually include:

1. A minimal demo page.
2. A backend knowledge-base service.
3. A small sample-file dataset.
4. Simplified API documentation.
5. Sample JSON output.
6. Demo verification notes.

## Technology Direction

Default technical direction:

- Python 3.11+
- FastAPI
- Pydantic
- SQLite for MVP metadata
- Local file storage for uploaded samples
- Pluggable document parser
- Pluggable OCR adapter
- Pluggable embedding provider
- Pluggable vector store
- Pluggable OpenAI-compatible LLM adapter
- Minimal frontend only for demo display

The research report recommends Haystack + Docling + PaddleOCR + Qdrant as the later practical stack, with RAGFlow as a product reference rather than the initial codebase.

## Priority

First run a vertical slice. Do not chase a complete bidding platform.

Phase 1 should only establish the smallest backend foundation:

upload -> local storage -> document metadata -> SQLite initialization -> health check -> smoke test.
