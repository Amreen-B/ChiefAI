from app.services.llm_service import LLMService


class ExecutiveSummaryAgent:

    def run(self, startup_text):

        prompt = f"""
        Create an executive summary.

        Startup:

        {startup_text}

        Return:

        - Startup Overview
        - Problem
        - Solution
        - Market
        - Business Model
        - Growth Potential
        - Investment Readiness

        Keep it concise and professional.
        """

        return LLMService.ask(prompt)