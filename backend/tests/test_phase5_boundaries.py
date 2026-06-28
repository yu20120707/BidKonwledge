from __future__ import annotations

from pathlib import Path


def test_phase5_demo_route_does_not_require_external_service_env(client, monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("QDRANT_URL", raising=False)
    monkeypatch.delenv("HAYSTACK_API_KEY", raising=False)
    monkeypatch.delenv("PADDLEOCR_HOME", raising=False)

    response = client.get("/demo")

    assert response.status_code == 200
    assert "need_human_review" in response.text


def test_phase5_demo_files_do_not_introduce_forbidden_scope():
    repo_root = Path(__file__).resolve().parents[2]
    demo_files = [
        repo_root / "backend" / "app" / "api" / "demo.py",
        repo_root / "backend" / "app" / "static" / "demo.html",
    ]
    content = "\n".join(path.read_text(encoding="utf-8").lower() for path in demo_files)

    forbidden_terms = [
        "paddleocr",
        "qdrant",
        "haystack",
        "embedding",
        "dense retrieval",
        "export",
        "login",
        "authentication",
    ]
    for term in forbidden_terms:
        assert term not in content
