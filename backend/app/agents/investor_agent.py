from app.services.llm_service import LLMService
from app.services.json_parser import JsonParser


class InvestorAgent:

    def run(self, startup_text):

        prompt = f"""
        You are a venture capital analyst.

        Return ONLY valid JSON.

        {{
        "readiness_score": 0,
        "funding_stage": "",
        "recommended_raise": "",
        "strengths": [],
        "weaknesses": [],
        "risks": [],
        "investment_risk": "",
        "recommendations": []
        }}


        Startup:
        {startup_text}
        """

        response = LLMService.ask(prompt)

        print("\n===== MARKET RESPONSE =====")
        print(response)
        print("==========================\n")

        parsed = JsonParser.parse(response)

        print("\n===== MARKET PARSED =====")
        print(parsed)
        print("========================\n")

        return parsed