from __future__ import annotations

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from backend.app.adapters.llm_gateway import (
    LLMClient,
    LLMConfigurationError,
    LLMRequestConfigurationError,
    OpenAICompatibleLLMClient,
)
from backend.app.api.files import error_response
from backend.app.config import Settings, get_settings
from backend.app.schemas.document import GenerationRequest, GenerationResponse
from backend.app.services import generation

router = APIRouter(prefix="/api")


def get_llm_client() -> LLMClient | None:
    return None


def _active_llm_client(
    request: GenerationRequest,
    injected_llm_client: LLMClient | None,
) -> LLMClient:
    if injected_llm_client is not None:
        return injected_llm_client
    if request.llm_config is not None:
        return OpenAICompatibleLLMClient.from_request(
            api_key=request.llm_config.api_key,
            base_url=request.llm_config.base_url,
            model=request.llm_config.model,
        )
    return OpenAICompatibleLLMClient.from_env()


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
        active_llm_client = _active_llm_client(request, llm_client)
        return generation.generate_content(
            settings=settings,
            target_tag=request.target_tag,
            query=request.query,
            top_k=request.top_k,
            llm_client=active_llm_client,
        )
    except generation.InvalidGenerationRequestError as exc:
        return error_response(400, "INVALID_GENERATION_REQUEST", str(exc))
    except LLMRequestConfigurationError as exc:
        return error_response(400, "INVALID_LLM_CONFIG", str(exc))
    except LLMConfigurationError as exc:
        return error_response(503, "LLM_NOT_CONFIGURED", str(exc))
