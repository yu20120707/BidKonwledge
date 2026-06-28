from __future__ import annotations

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from backend.app.api.files import error_response
from backend.app.config import Settings, get_settings
from backend.app.schemas.document import RetrievalRequest, RetrievalResponse
from backend.app.services import retrieval

router = APIRouter(prefix="/api")


@router.post(
    "/retrieve",
    response_model=RetrievalResponse,
    responses={400: {"description": "Invalid retrieval request"}},
)
def retrieve(
    request: RetrievalRequest,
    settings: Settings = Depends(get_settings),
) -> RetrievalResponse | JSONResponse:
    try:
        return retrieval.retrieve_chunks(
            settings=settings,
            query=request.query,
            tag=request.tag,
            top_k=request.top_k,
        )
    except retrieval.InvalidRetrievalRequestError as exc:
        return error_response(400, "INVALID_RETRIEVAL_REQUEST", str(exc))
