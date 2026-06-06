from app.services.llm_service import LLMService


class StrategyAgent:

    def run(self, startup_text):

        prompt = f"""
        You are a startup strategist.

        Startup:

        {startup_text}

        Return:

        - Business model
        - Pricing strategy
        - Go-to-market plan
        - Growth strategy
        """

        return LLMService.ask(prompt)