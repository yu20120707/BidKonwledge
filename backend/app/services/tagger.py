from __future__ import annotations


TAG_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("运维服务", ("运维", "维护", "服务")),
    ("应急响应", ("应急", "突发", "响应")),
    ("安全保障", ("安全", "保密", "数据安全")),
    ("人员资质", ("人员", "团队", "资质", "证书")),
    ("项目管理", ("项目管理", "进度", "质量", "实施")),
    ("商务报价", ("报价", "价格", "费用")),
)


def deterministic_tags(text: str) -> list[str]:
    normalized = text.lower()
    tags = [
        tag
        for tag, keywords in TAG_RULES
        if any(keyword.lower() in normalized for keyword in keywords)
    ]
    return tags or ["未分类"]
