from app.services.llm_service import LLMService


class CompetitorAgent:

    def run(self, startup_text):

        prompt = f"""
        Analyze this startup idea.

        Startup:
        {startup_text}

        Return:

        1. Top competitors
        2. Their strengths
        3. Their weaknesses
        4. Market gaps
        """

        return LLMService.ask(prompt)