from app.services.llm_service import LLMService


class RiskAgent:

    def run(self, startup_text):

        prompt = f"""
        Analyze risks for:

        {startup_text}

        Return:

        - Market risk
        - Product risk
        - Financial risk
        - Competition risk

        Also give overall risk score out of 10.
        """

        return LLMService.ask(prompt)