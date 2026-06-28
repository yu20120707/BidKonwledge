from __future__ import annotations

from backend.app.adapters.llm_gateway import LLMClient
from backend.app.config import Settings
from backend.app.schemas.document import GenerationResponse
from backend.app.services import answer_formatter, prompt_builder, retrieval, risk_checker


class InvalidGenerationRequestError(ValueError):
    pass


def generate_content(
    settings: Settings,
    target_tag: str,
    query: str,
    top_k: int,
    llm_client: LLMClient,
) -> GenerationResponse:
    normalized_target_tag = target_tag.strip()
    normalized_query = query.strip()
    if not normalized_target_tag:
        raise InvalidGenerationRequestError("target_tag is required")
    if not normalized_query:
        raise InvalidGenerationRequestError("query is required")
    if top_k < 1:
        raise InvalidGenerationRequestError("top_k must be greater than zero")

    retrieval_response = retrieval.retrieve_chunks(
        settings=settings,
        query=normalized_query,
        tag=normalized_target_tag,
        top_k=top_k,
    )
    prompt = prompt_builder.build_generation_prompt(
        target_tag=normalized_target_tag,
        query=normalized_query,
        retrieval_results=retrieval_response.results,
    )
    generated_content = answer_formatter.normalize_generated_content(
        llm_client.generate(prompt)
    )
    citations = answer_formatter.build_citations(retrieval_response.results)
    risks = risk_checker.check_generation_risks(generated_content, citations)
    return GenerationResponse(
        target_tag=normalized_target_tag,
        generated_content=generated_content,
        citations=citations,
        risks=risks,
        need_human_review=True,
    )
