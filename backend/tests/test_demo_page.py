from __future__ import annotations


def test_demo_route_available(client):
    response = client.get("/demo")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "BidKnowledge Demo" in response.text


def test_demo_page_includes_expected_api_hooks_and_sections(client):
    response = client.get("/demo")

    assert response.status_code == 200
    html = response.text
    assert 'id="upload-section"' in html
    assert 'id="parse-section"' in html
    assert 'id="retrieve-section"' in html
    assert 'id="generate-section"' in html
    assert 'id="raw-json-section"' in html
    assert 'id="citations-section"' in html
    assert 'id="risks-section"' in html
    assert 'id="need-human-review"' in html
    assert 'fetch("/api/files/upload"' in html
    assert "fetch(`/api/documents/${documentId}/parse`" in html
    assert 'fetch("/api/retrieve"' in html
    assert 'fetch("/api/generate"' in html
    assert "JSON.stringify(payload, null, 2)" in html


def test_demo_page_handles_no_llm_generate_error_in_review_panel(client):
    response = client.get("/demo")

    assert response.status_code == 200
    html = response.text
    assert "renderGenerationError" in html
    assert "LLM_NOT_CONFIGURED" in html
    assert 'reviewStatus.textContent = "need_human_review: true"' in html
    assert "risksList.replaceChildren(item)" in html


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
