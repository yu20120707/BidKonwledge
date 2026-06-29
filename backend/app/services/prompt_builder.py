from __future__ import annotations

from backend.app.schemas.document import RetrievalResult


def build_generation_prompt(
    target_tag: str,
    query: str,
    retrieval_results: list[RetrievalResult],
) -> str:
    context_blocks = []
    for index, result in enumerate(retrieval_results, start=1):
        context_blocks.append(
            "\n".join(
                [
                    f"[{index}] chunk_id={result.chunk_id}",
                    f"document_id={result.document_id}",
                    f"source_filename={result.source.original_filename}",
                    f"section_title={result.section_title}",
                    f"section_path={result.section_path}",
                    f"tags={', '.join(result.tags)}",
                    *_knowledge_card_context(result),
                    f"text={result.text}",
                ]
            )
        )
    context = "\n\n".join(context_blocks) if context_blocks else "No retrieval context."
    return "\n".join(
        [
            "你是投标文档候选内容生成助手。",
            "只基于给定检索上下文生成候选内容，不要编造来源。",
            "输出内容必须适合人工审核，不得声称已最终定稿。",
            f"目标标签: {target_tag}",
            f"用户需求: {query}",
            "检索上下文:",
            context,
        ]
    )


def _knowledge_card_context(result: RetrievalResult) -> list[str]:
    knowledge_card = result.source.chunk_metadata.get("knowledge_card")
    if not isinstance(knowledge_card, dict):
        return []
    lines = []
    tag = knowledge_card.get("tag")
    title = knowledge_card.get("title")
    confidence = knowledge_card.get("confidence")
    if tag:
        lines.append(f"knowledge_card_tag={tag}")
    if title:
        lines.append(f"knowledge_card_title={title}")
    if confidence is not None:
        lines.append(f"knowledge_card_confidence={confidence}")
    return lines
