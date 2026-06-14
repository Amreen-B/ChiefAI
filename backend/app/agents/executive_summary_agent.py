from app.services.llm_service import LLMService
from app.services.json_parser import JsonParser


class ExecutiveSummaryAgent:

    def run(self, startup_text):

        prompt = f"""
        You are an experienced startup advisor.

        Analyze the startup below.

        Return ONLY valid JSON.

        Generate ALL fields.

        If information is missing,
        infer a realistic answer.

        Never return null.

        {{
            "executive_summary":"",
            "ai_insight":"",
            "business_model":"",
            "target_customer":""
        }}

        Rules:

        executive_summary:
        - 40-50 words
        - Mention startup, problem, solution, market and funding.

        ai_insight:
        - One actionable recommendation.
        - Maximum 20 words.

        business_model:
        - One sentence.

        target_customer:
        - One sentence.

        Startup Description:

        {startup_text}
        """
        response = LLMService.ask(prompt)
        response = JsonParser.parse(response)

        print("\n========== EXECUTIVE SUMMARY AGENT ==========")
        print(response)
        print("=============================================\n")

        return response