from app.services.llm_service import LLMService
from app.services.json_parser import JsonParser


class RiskAgent:

    def run(self, startup_text):

        prompt = f"""

        You are an startup experienced consultant.

        Return ONLY valid JSON.

        Generate ALL fields.

        If information is missing,
        infer a realistic answer.

        Never return null.

        Always identify at least 5 realistic risks.

        If the startup looks strong,
        infer realistic business risks.
        Also give overall risk score out of 10.

        Analyze risks for:

        - Market risk
        - Product risk
        - Financial risk
        - Competition risk

        Return:
        {{
            "major_risks":[]
        }}

        Startup:{startup_text}
        """
    
        response = LLMService.ask(prompt)
        response = JsonParser.parse(response)

        print("\n========== Risk AGENT ==========")
        print(response)
        print("=============================================\n")

        return response