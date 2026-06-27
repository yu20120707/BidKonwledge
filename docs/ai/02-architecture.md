# Architecture

## Historical Bid Ingestion Flow

Future historical bid ingestion chain:

1. Upload historical bid file.
2. `DocumentParser` parses text, titles, pages, and tables.
3. `SectionSplitter` splits sections by directory, heading, and fallback rules.
4. `Tagger` assigns initial tags based on titles and deterministic rules.
5. `KnowledgeCardBuilder` creates knowledge cards.
6. `EmbeddingService` creates vectors.
7. `VectorStore` writes vector indexes.
8. `MetadataStore` writes SQLite metadata.

## Tender Analysis Flow

Future tender analysis chain:

1. Upload tender file.
2. `DocumentParser` parses text, titles, pages, and tables.
3. `TenderAnalyzer` extracts project requirements, scoring items, and disqualification risks.
4. User selects a target tag.
5. `Retriever` retrieves knowledge cards by tag and query semantics.
6. `PromptBuilder` combines tender requirements, historical snippets, and output constraints.
7. `LLMService` generates candidate content.
8. `RiskChecker` marks low confidence, missing citations, and possible disqualification risks.
9. API returns generated content, citations, risks, `need_human_review`, and raw JSON.

## Recommended Backend Modules

Future backend module direction:

- `backend/app/main.py`
- `backend/app/config.py`
- `backend/app/models/`
- `backend/app/schemas/`
- `backend/app/api/`
- `backend/app/services/document_parser/`
- `backend/app/services/section_splitter/`
- `backend/app/services/tagger/`
- `backend/app/services/knowledge_card/`
- `backend/app/services/embedding/`
- `backend/app/services/vector_store/`
- `backend/app/services/tender_analyzer/`
- `backend/app/services/retriever/`
- `backend/app/services/llm/`
- `backend/app/services/risk_checker/`
- `backend/app/storage/`

## Adapter Boundary

External or heavy capabilities must sit behind adapters:

- document parsing adapter
- OCR adapter
- embedding adapter
- vector store adapter
- LLM adapter

This keeps the first demo replaceable and prevents the project from locking into one platform too early.
