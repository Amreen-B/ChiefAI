from app.services.llm_service import LLMService


class PitchDeckAgent:

    def run(self, startup_text):

        prompt = f"""
        Create an investor pitch deck.

        Startup:

        {startup_text}

        Generate:

        Slide 1 - Startup Overview
        Slide 2 - Problem
        Slide 3 - Solution
        Slide 4 - Market
        Slide 5 - Business Model
        Slide 6 - Competition
        Slide 7 - Go-To-Market
        Slide 8 - Financials
        Slide 9 - Funding Ask
        Slide 10 - Vision

        Return slide-wise content.
        """

        return LLMService.ask(prompt)