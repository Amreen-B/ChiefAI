from app.services.llm_service import LLMService


class ExecutionAgent:

    def run(self, startup_text):

        prompt = f"""
        Create execution roadmap.

        Startup:

        {startup_text}

        Return:

        - First 30 days
        - First 60 days
        - First 90 days
        - MVP plan
        """

        return LLMService.ask(prompt)