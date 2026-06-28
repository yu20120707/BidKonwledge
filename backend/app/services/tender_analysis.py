from __future__ import annotations

import re
from datetime import UTC, datetime
from hashlib import sha256

from backend.app.config import Settings
from backend.app.schemas.document import (
    DocumentChunkRecord,
    TenderAnalysisRecord,
    TenderAnalysisResponse,
    TenderEvidenceItem,
)
from backend.app.storage import database


ANALYSIS_METHOD = "deterministic_tender_v1"
REQUIREMENT_KEYWORDS = ("需求", "服务内容", "项目内容", "建设内容", "运维", "实施")
SCORING_KEYWORDS = ("评分", "分值", "得分", "评审", "评分标准", "技术分", "商务分")
RISK_KEYWORDS = ("废标", "无效投标", "否决", "不接受", "不符合", "资格审查", "必须", "不得")
HIGH_RISK_KEYWORDS = ("废标", "无效投标", "否决")
SCORE_PATTERN = re.compile(r"(\d+(?:\.\d+)?)\s*分")


class DocumentNotFoundError(Exception):
    pass


class DocumentNotParsedError(Exception):
    pass


class UnsupportedDocumentRoleError(Exception):
    pass


class TenderAnalysisNotFoundError(Exception):
    pass


def analyze_tender(settings: Settings, document_id: str) -> TenderAnalysisResponse:
    document = database.get_document(settings, document_id)
    if document is None:
        raise DocumentNotFoundError
    if document.parse_status != "parsed":
        raise DocumentNotParsedError
    if document.doc_role != "tender":
        raise UnsupportedDocumentRoleError

    chunks = database.list_document_chunks(settings, document_id)
    created_at = _utc_now()
    analysis = TenderAnalysisRecord(
        id=_analysis_id(document_id),
        document_id=document_id,
        project_requirements=_extract_items(
            document.original_filename,
            chunks,
            item_type="requirement",
            title="项目需求",
            keywords=REQUIREMENT_KEYWORDS,
        ),
        scoring_items=_extract_items(
            document.original_filename,
            chunks,
            item_type="scoring_item",
            title="评分项",
            keywords=SCORING_KEYWORDS,
        ),
        disqualification_risks=_extract_items(
            document.original_filename,
            chunks,
            item_type="disqualification_risk",
            title="废标/否决风险",
            keywords=RISK_KEYWORDS,
        ),
        raw_text_summary=_raw_text_summary(chunks),
        analysis_method=ANALYSIS_METHOD,
        need_human_review=True,
        metadata={
            "source_chunks_count": len(chunks),
            "rule_sets": {
                "project_requirements": list(REQUIREMENT_KEYWORDS),
                "scoring_items": list(SCORING_KEYWORDS),
                "disqualification_risks": list(RISK_KEYWORDS),
            },
            "no_match": not any(
                _matched_keywords(chunk.text, REQUIREMENT_KEYWORDS + SCORING_KEYWORDS + RISK_KEYWORDS)
                for chunk in chunks
            ),
        },
        created_at=created_at,
    )
    database.replace_document_tender_analysis(settings, analysis)
    return _to_response(analysis)


def get_tender_analysis(settings: Settings, document_id: str) -> TenderAnalysisResponse:
    if database.get_document(settings, document_id) is None:
        raise DocumentNotFoundError
    analysis = database.get_document_tender_analysis(settings, document_id)
    if analysis is None:
        raise TenderAnalysisNotFoundError
    return _to_response(analysis)


def _extract_items(
    source_filename: str,
    chunks: list[DocumentChunkRecord],
    item_type: str,
    title: str,
    keywords: tuple[str, ...],
) -> list[TenderEvidenceItem]:
    items: list[TenderEvidenceItem] = []
    for chunk in chunks:
        haystack = f"{chunk.section_title}\n{chunk.text}"
        matched = _matched_keywords(haystack, keywords)
        if not matched:
            continue
        score = _score_from_text(haystack) if item_type == "scoring_item" else None
        severity = _risk_severity(matched) if item_type == "disqualification_risk" else None
        items.append(
            TenderEvidenceItem(
                item_id=_item_id(chunk.document_id, chunk.id, item_type, matched),
                item_type=item_type,
                title=title,
                description=chunk.text,
                source_filename=source_filename,
                source_chunk_id=chunk.id,
                source_section_title=chunk.section_title,
                source_section_path=chunk.section_path,
                page_start=chunk.page_start,
                page_end=chunk.page_end,
                matched_keywords=matched,
                severity=severity,
                score=score,
            )
        )
    return items


def _matched_keywords(text: str, keywords: tuple[str, ...]) -> list[str]:
    normalized = text.lower()
    return [keyword for keyword in keywords if keyword.lower() in normalized]


def _score_from_text(text: str) -> float | None:
    match = SCORE_PATTERN.search(text)
    if match is None:
        return None
    return float(match.group(1))


def _risk_severity(matched_keywords: list[str]) -> str:
    if any(keyword in HIGH_RISK_KEYWORDS for keyword in matched_keywords):
        return "high"
    return "medium"


def _raw_text_summary(chunks: list[DocumentChunkRecord], max_chars: int = 300) -> str:
    text = "\n".join(chunk.text.strip() for chunk in chunks if chunk.text.strip())
    return text[:max_chars]


def _analysis_id(document_id: str) -> str:
    digest = sha256(f"{document_id}:tender-analysis".encode("utf-8")).hexdigest()
    return f"ta_{digest[:24]}"


def _item_id(
    document_id: str, chunk_id: str, item_type: str, matched_keywords: list[str]
) -> str:
    seed = f"{document_id}:{chunk_id}:{item_type}:{','.join(matched_keywords)}"
    digest = sha256(seed.encode("utf-8")).hexdigest()
    return f"tai_{digest[:24]}"


def _to_response(analysis: TenderAnalysisRecord) -> TenderAnalysisResponse:
    return TenderAnalysisResponse(
        document_id=analysis.document_id,
        project_requirements=analysis.project_requirements,
        scoring_items=analysis.scoring_items,
        disqualification_risks=analysis.disqualification_risks,
        raw_text_summary=analysis.raw_text_summary,
        analysis_method=analysis.analysis_method,
        need_human_review=analysis.need_human_review,
        metadata=analysis.metadata,
    )


def _utc_now() -> str:
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")
