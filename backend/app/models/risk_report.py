from pydantic import BaseModel


class RiskReport(BaseModel):

    market_risk: str

    competition_risk: str

    execution_risk: str

    risk_score: int

    mitigation_plan: list[str]