from app.services.llm_service import LLMService


class FundingAgent:

    def run(self, startup_text):

        prompt = f"""
        Analyze funding opportunities.

        Startup:

        {startup_text}

        Recommend:

        - Bootstrapping
        - Angel funding
        - Seed funding
        - Accelerators
        - Grants

        Give reasoning.
        """

        return LLMService.ask(prompt)