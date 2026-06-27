# Source Materials

## Project Specification Sources

- PRD: `C:\Users\26561\Desktop\模型训练资料\相关文档\投标智能知识库能力验证版 PRD v0.1.pdf`
- Research report: `C:\Users\26561\Desktop\模型训练资料\相关文档\deep-research-report.md`

## Sample Material Directory

- `C:\Users\26561\Desktop\模型训练资料\甲方提供资料`

The sample directory contains tender and historical bid materials for later validation. Phase 0 does not copy or process these files.

## Initial Sample Strategy

Later demo validation should use:

1. One new tender file.
2. Two or three historical bid files.
3. A few target tags, such as:
   - 运维服务实施方案
   - 突发应急方案和措施
   - 网络和数据安全防护保障措施
   - 服务质量保障和考核评估方案

## Dependency Direction From Research Report

The research report recommends:

1. RAGFlow as a product reference.
2. Haystack as the practical Python-oriented backend foundation.
3. Docling as the primary structured document parser.
4. PaddleOCR as the later OCR adapter.
5. Qdrant as the later vector store.
6. FastAPI as the thin API and demo shell.

These are future implementation directions, not Phase 0 or Phase 1 requirements.
