from pydantic import BaseModel


class StrategyReport(BaseModel):
    business_model: str
    pricing_strategy: str
    go_to_market: str
    ninety_day_plan: list[str]