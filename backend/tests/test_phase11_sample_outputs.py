from __future__ import annotations

import json
from pathlib import Path


PHASE11_OUTPUT_DIR = (
    Path(__file__).resolve().parents[2] / "docs" / "ai" / "sample-outputs" / "phase11"
)


def _sample_json_files() -> list[Path]:
    return sorted(PHASE11_OUTPUT_DIR.glob("*.json"))


def test_phase11_sample_outputs_are_valid_json():
    files = _sample_json_files()

    assert files
    for path in files:
        payload = json.loads(path.read_text(encoding="utf-8"))
        assert payload["sample_kind"]
        assert any(key in payload for key in ("stage", "phase", "title"))


def test_phase11_manifest_references_existing_outputs():
    manifest_path = PHASE11_OUTPUT_DIR / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    for filename in manifest["sample_outputs"]:
        assert (PHASE11_OUTPUT_DIR / filename).is_file()

    roles = [sample["doc_role"] for sample in manifest["fixed_sample_files"]]
    assert roles.count("historical_bid") >= 2
    assert roles.count("tender") == 1
    assert any(sample["sample_id"] == "ocr_smoke_image" for sample in manifest["fixed_sample_files"])

    selected_tags = manifest["selected_tags"]
    assert {tag["prd_label"] for tag in selected_tags} >= {
        "运维服务实施方案",
        "突发应急方案和措施",
        "网络和数据安全防护保障措施",
    }
    assert all(tag["retrieval_tag"] for tag in selected_tags)


def test_phase11_sample_outputs_do_not_commit_secrets_or_runtime_paths():
    combined = "\n".join(path.read_text(encoding="utf-8").lower() for path in _sample_json_files())

    forbidden_fragments = [
        '"api_key"',
        "bearer ",
        "openai_api_key",
        "c:\\users\\",
        "%temp%",
    ]
    for fragment in forbidden_fragments:
        assert fragment not in combined

    assert "not_project_dependency" in combined
    assert "local_smoke_only" in combined
    assert "not production-ready" in combined
    assert "large_files_deferred" in combined
