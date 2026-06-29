from __future__ import annotations


def test_demo_route_available(client):
    response = client.get("/demo")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "BidKnowledge Demo" in response.text
    assert "BidKnowledge PRD-shaped Demo" in response.text


def test_demo_page_includes_phase10_prd_flow_sections_and_api_hooks(client):
    response = client.get("/demo")

    assert response.status_code == 200
    html = response.text
    assert 'id="historical-section"' in html
    assert 'id="historical-evidence-pool-list"' in html
    assert 'id="knowledge-section"' in html
    assert 'id="tender-section"' in html
    assert 'id="tag-selection-section"' in html
    assert 'id="retrieval-evidence-section"' in html
    assert 'id="candidate-section"' in html
    assert 'id="review-section"' in html
    assert 'id="ocr-status-section"' in html
    assert 'fetch("/api/files/upload"' in html
    assert "fetch(`/api/documents/${documentId}/parse`" in html
    assert 'fetch("/api/knowledge/build"' in html
    assert 'fetch(`/api/documents/${state.historicalDocumentId}/knowledge-cards`)' in html
    assert 'fetch("/api/tender/analyze"' in html
    assert 'fetch("/api/retrieve"' in html
    assert 'fetch("/api/generate"' in html
    assert "JSON.stringify(payload, null, 2)" in html


def test_demo_page_shows_prd_tag_mapping_and_ocr_smoke_boundaries(client):
    response = client.get("/demo")

    assert response.status_code == 200
    html = response.text
    assert "PRD_TAG_OPTIONS" in html
    assert "运维服务实施方案" in html
    assert "突发应急方案和措施" in html
    assert "fallbackTag: \"运维服务\"" in html
    assert "fetchRetrievalForTag(option.label, query)" in html
    assert "fetchRetrievalForTag(option.fallbackTag, query)" in html
    assert "state.retrievalEffectiveTag = effectiveTag" in html
    assert "used_fallback: usedFallback" in html
    assert "target_tag: effectiveTag" in html
    assert "selectedTenderRequirement" in html
    assert "generationQueryWithTenderContext" in html
    assert "tender_requirement_used: tenderRequirement" in html
    assert "generation_query: generationQuery" in html
    assert "historicalEvidencePool" in html
    assert "upsertHistoricalEvidencePool" in html
    assert "renderHistoricalEvidencePool" in html
    assert "历史证据池" in html
    assert "fallback_chunk_tag: option.fallbackTag" in html
    assert "setButtonReadiness(\"generate-button\", state.retrievalResults.length > 0)" in html
    assert "setButtonReadiness(\"knowledge-refresh-button\", state.historicalParse?.parse_status === \"parsed\")" in html
    assert "runButtonAction(\"generate-button\", \"Generating...\", generateCandidate)" in html
    assert "outline: 3px solid rgba(23, 107, 90, 0.28)" in html
    assert "prefers-reduced-motion: reduce" in html
    assert "rel=\"icon\"" in html
    assert "historical-sample-guide" in html
    assert "tender-sample-guide" in html
    assert "Smoke Evidence Only" in html
    assert "paddleocr 2.10.0 / paddlepaddle 2.6.2" in html
    assert "1 section / 1 chunk" in html
    assert "PyMuPDF was used only as a local smoke dependency" in html
    assert "does not claim OCR is production-ready" in html


def test_demo_page_handles_no_llm_generate_error_in_review_panel(client):
    response = client.get("/demo")

    assert response.status_code == 200
    html = response.text
    assert "renderGenerationError" in html
    assert "LLM_NOT_CONFIGURED" in html
    assert 'reviewStatus.textContent = "need_human_review: true"' in html
    assert 'generatedContent.textContent = "未配置外部 LLM，当前没有候选内容。"' in html
    assert 'makeListItem("high · LLM_NOT_CONFIGURED"' in html


def test_demo_page_includes_user_scoped_llm_config_controls(client):
    response = client.get("/demo")

    assert response.status_code == 200
    html = response.text
    assert 'id="llm-api-key"' in html
    assert 'type="password"' in html
    assert 'id="llm-base-url"' in html
    assert 'id="llm-model"' in html
    assert "currentLlmConfig" in html
    assert "requestBody.llm_config = llmConfig" in html
