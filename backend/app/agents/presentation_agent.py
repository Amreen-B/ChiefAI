from app.services.llm_service import LLMService
from app.services.json_parser import JsonParser


class PresentationAgent:

    def run(self, startup_text):

        prompt = f"""
        Create startup pitch content.

        Return ONLY valid JSON.

        {{
            "elevator_pitch": "",
            "problem": "",
            "solution": "",
            "traction": "",
            "ask": ""
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