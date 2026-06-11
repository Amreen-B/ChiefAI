from app.services.llm_service import LLMService
from app.services.json_parser import JsonParser


class MarketAgent:

    def run(self, startup_text):

        prompt = f"""
       You are a startup market analyst.

        Return ONLY valid JSON.

        Do not add explanations.
        Do not add markdown.
        Do not add ```json.

        Return exactly:

        {{
        "market_size": "",
        "growth_rate": "",
        "tam": "",
        "tam_explanation": "",
        "sam": "",
        "sam_explanation": "",
        "som": "",
        "som_explanation": "",
        "competitors": [],
        "market_trends": [],
        "opportunities": [],
        "risks": []
        }}

        Market Trends should contain 3-5 short bullet point trends relevant to the startup's industry.

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