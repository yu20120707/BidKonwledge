from __future__ import annotations

from backend.app.schemas.document import Citation, RiskItem


def check_generation_risks(
    generated_content: str,
    citations: list[Citation],
) -> list[RiskItem]:
    risks: list[RiskItem] = []
    if not generated_content.strip():
        risks.append(
            RiskItem(
                risk_type="EMPTY_GENERATION",
                description="Generated content is empty.",
                severity="high",
            )
        )
    if not citations:
        risks.append(
            RiskItem(
                risk_type="MISSING_CITATIONS",
                description="No retrieval citations are available for this output.",
                severity="high",
            )
        )
    return risks
