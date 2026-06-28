from __future__ import annotations

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from backend.app.adapters.llm_gateway import (
    LLMClient,
    LLMConfigurationError,
    OpenAICompatibleLLMClient,
)
from backend.app.api.files import error_response
from backend.app.config import Settings, get_settings
from backend.app.schemas.document import GenerationRequest, GenerationResponse
from backend.app.services import generation

router = APIRouter(prefix="/api")


def get_llm_client() -> LLMClient | None:
    return None


@router.post(
    "/generate",
    response_model=GenerationResponse,
    responses={
        400: {"description": "Invalid generation request"},
        503: {"description": "LLM is not configured"},
    },
)
def generate(
    request: GenerationRequest,
    settings: Settings = Depends(get_settings),
    llm_client: LLMClient | None = Depends(get_llm_client),
) -> GenerationResponse | JSONResponse:
    try:
        active_llm_client = llm_client or OpenAICompatibleLLMClient.from_env()
        return generation.generate_content(
            settings=settings,
            target_tag=request.target_tag,
            query=request.query,
            top_k=request.top_k,
            llm_client=active_llm_client,
        )
    except generation.InvalidGenerationRequestError as exc:
        return error_response(400, "INVALID_GENERATION_REQUEST", str(exc))
    except LLMConfigurationError as exc:
        return error_response(503, "LLM_NOT_CONFIGURED", str(exc))
