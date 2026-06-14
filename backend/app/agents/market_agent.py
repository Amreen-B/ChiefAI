from app.services.llm_service import LLMService
from app.services.json_parser import JsonParser


class MarketAgent:

    def run(self, startup_text):

        prompt = f"""

        You are a professional Market Intelligence AI Agent.

        Your ONLY task is to perform market analysis.

        Return ONLY valid JSON.

        Do not explain.
        Do not write markdown.
        Do not write ```json.

        Return EXACTLY this schema:

        {{
        "market_size": "",
        "growth_rate": "",
        "tam": "",
        "tam_explanation": "",
        "sam": "",
        "sam_explanation": "",
        "som": "",
        "som_explanation": "",
        "competitors": [
            {{
                "name": "",
                "strength": ""
            }}
        ],
        "market_trends": [],
        "opportunities": [],
        "risks": []
        }}

        Rules:

        - market_size must include estimated market value.
        - growth_rate must include CAGR.
        - TAM, SAM and SOM should contain realistic estimates.
        - competitors should contain 4-6 major competitors.
        - market_trends should contain 5 trends.
        - opportunities should contain 5 opportunities.
        - risks should contain 5 risks.

        Startup Idea:

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