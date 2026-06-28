from __future__ import annotations


TAG_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("运维服务", ("运维", "维护", "服务")),
    ("应急响应", ("应急", "突发", "响应")),
    ("安全保障", ("安全", "保密", "数据安全")),
    ("人员资质", ("人员", "团队", "资质", "证书")),
    ("项目管理", ("项目管理", "进度", "质量", "实施")),
    ("商务报价", ("报价", "价格", "费用")),
)

PRD_TAG_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("突发应急方案和措施", ("应急", "突发", "响应", "故障")),
    ("网络和数据安全防护保障措施", ("网络安全", "数据安全", "安全", "防护", "保密")),
    ("服务质量保障和考核评估方案", ("质量", "考核", "评估", "sla", "保障")),
    ("团队人员", ("团队", "人员", "项目经理", "工程师")),
    ("业绩情况", ("业绩", "案例", "合同", "客户")),
    ("资格材料", ("营业执照", "资格", "承诺函", "中小企业")),
    ("商务报价", ("报价", "价格", "费用")),
    ("运维服务实施方案", ("运维", "维护", "服务", "实施")),
)


def deterministic_tags(text: str) -> list[str]:
    normalized = text.lower()
    tags = [
        tag
        for tag, keywords in TAG_RULES
        if any(keyword.lower() in normalized for keyword in keywords)
    ]
    return tags or ["未分类"]


def prd_knowledge_tag(text: str) -> tuple[str, list[str]]:
    normalized = text.lower()
    for tag, keywords in PRD_TAG_RULES:
        matched = [keyword for keyword in keywords if keyword.lower() in normalized]
        if matched:
            return tag, matched
    return "未分类", []
