from app.services.llm_service import LLMService
from app.services.json_parser import JsonParser


class InvestorAgent:

    def run(self, startup_text):

        prompt = f"""
        Analyze this startup from an investor perspective.

        Return ONLY valid JSON.

        {{
            "readiness_score": 0,
            "funding_stage": "",
            "recommended_raise": "",
            "strengths": [],
            "risks": []
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