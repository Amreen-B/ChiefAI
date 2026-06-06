from app.services.llm_service import LLMService
from app.services.json_parser import JsonParser


class MarketAgent:

    def run(self, startup_text):

        prompt = f"""
        Analyze this startup.

        Return ONLY valid JSON.

        {{
            "market_size": "",
            "growth_rate": "",
            "tam": "",
            "sam": "",
            "som": "",
            "competitors": [],
            "market_trends": []
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