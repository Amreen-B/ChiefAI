from app.services.llm_service import LLMService
from app.services.json_parser import JsonParser


class SWOTAgent:

    def run(self, startup_text):

        prompt = f"""
        Return ONLY JSON.
        Always infer threats.

        Never leave threats empty.


        {{
            "strengths": [],
            "weaknesses": [],
            "opportunities": [],
            "threats": []
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