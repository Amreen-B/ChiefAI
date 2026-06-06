from app.services.llm_service import LLMService


class ResearchAgent:

    def run(self, startup_text):

        prompt = f"""
        You are a startup research analyst.

        Analyze this startup idea.

        Startup Idea:
        {startup_text}

        Return:

        1. Problem
        2. Market Size
        3. Competitors
        4. Industry Trends
        5. Opportunity Score (1-10)
        """

        return LLMService.ask(prompt)