import json

from app.services.llm_service import LLMService


class ScoringService:

    @staticmethod
    def generate_scores(startup_text: str):

        prompt = f"""
        Analyze this startup.

        Startup:

        {startup_text}

        Return ONLY valid JSON.

        Example:

        {{
            "opportunity_score": 8.5,
            "risk_score": 4.2,
            "market_score": 9.0,
            "execution_score": 7.8,
            "investor_readiness": 80
        }}
        """

        response = LLMService.ask(prompt)

        try:

            scores = json.loads(response)

            scores["overall_score"] = round(
                (
                    scores["opportunity_score"]
                    + scores["market_score"]
                    + scores["execution_score"]
                    + (10 - scores["risk_score"])
                ) / 4,
                1
            )

            return scores

        except Exception:

            return {
                "opportunity_score": 0,
                "risk_score": 0,
                "market_score": 0,
                "execution_score": 0,
                "investor_readiness": 0,
                "overall_score": 0
            }