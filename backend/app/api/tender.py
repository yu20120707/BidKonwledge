from __future__ import annotations

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from backend.app.api.files import error_response
from backend.app.config import Settings, get_settings
from backend.app.schemas.document import TenderAnalysisResponse, TenderAnalyzeRequest
from backend.app.services import tender_analysis

router = APIRouter(prefix="/api")


@router.post(
    "/tender/analyze",
    response_model=TenderAnalysisResponse,
    responses={
        404: {"description": "Document not found"},
        409: {"description": "Document is not ready for tender analysis"},
    },
)
def analyze_tender(
    request: TenderAnalyzeRequest,
    settings: Settings = Depends(get_settings),
) -> TenderAnalysisResponse | JSONResponse:
    try:
        return tender_analysis.analyze_tender(settings, request.document_id)
    except tender_analysis.DocumentNotFoundError:
        return error_response(404, "DOCUMENT_NOT_FOUND", "Document not found")
    except tender_analysis.DocumentNotParsedError:
        return error_response(409, "DOCUMENT_NOT_PARSED", "Document is not parsed")
    except tender_analysis.UnsupportedDocumentRoleError:
        return error_response(
            409,
            "UNSUPPORTED_DOCUMENT_ROLE",
            "Tender analysis is only supported for tender documents",
        )


@router.get(
    "/documents/{document_id}/tender-analysis",
    response_model=TenderAnalysisResponse,
    responses={
        404: {"description": "Document or tender analysis not found"},
    },
)
def get_tender_analysis(
    document_id: str,
    settings: Settings = Depends(get_settings),
) -> TenderAnalysisResponse | JSONResponse:
    try:
        return tender_analysis.get_tender_analysis(settings, document_id)
    except tender_analysis.DocumentNotFoundError:
        return error_response(404, "DOCUMENT_NOT_FOUND", "Document not found")
    except tender_analysis.TenderAnalysisNotFoundError:
        return error_response(
            404,
            "TENDER_ANALYSIS_NOT_FOUND",
            "Tender analysis not found",
        )
