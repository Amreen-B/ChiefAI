from app.services.llm_service import LLMService
from app.services.json_parser import JsonParser

class BusinessAgent:

    def run(self, startup_text):

        prompt = f"""
        You are a startup strategy consultant.

        Return ONLY valid JSON.

        {{
        "business_model": "",
        "target_customer": "",
        "go_to_market": "",
        "revenue_streams": [],
        "key_advantages": [],
        "customer_segments": [],
        "acquisition_channels": [],
        "pricing_strategy": "",
        "partnership_strategy": "",
        "growth_strategy": ""
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