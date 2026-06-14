from app.services.llm_service import LLMService
from app.services.json_parser import JsonParser

class BusinessAgent:

    def run(self, startup_text):

        prompt = f"""
        You are an expert startup strategy consultant.

        Analyze the startup and infer missing information when necessary.

        Return ONLY a valid JSON object.

        Do not include explanations.

        Do not include markdown.

        Do not wrap the JSON inside ```json.

        Every key below MUST be present.

        Never return null.

        Never omit a field.

        Use empty strings "" or [] only if absolutely impossible to infer.

        Return exactly this schema:

        {{
        "business_model": "",
        "startup_vision": "",
        "mission_statement": "",
        "value_proposition": "",
        "usp": "",

        "target_customer": "",
        "customer_segments": [],
        "customer_pain_points": [],

        "pricing_strategy": "",
        "revenue_model": "",
        "revenue_streams": [],
        "monetization_strategy": "",
        "expected_revenue_growth": "",

        "go_to_market": "",
        "sales_strategy": "",
        "marketing_channels": [],
        "distribution_channels": [],
        "acquisition_channels": [],

        "partnership_strategy": "",

        "growth_strategy": "",
        "expansion_strategy": "",
        "scaling_plan": "",
        "market_expansion": "",
        "growth_roadmap": [],
        "growth_strategy?: [],

        "innovation_strategy": "",
        "technology_advantage": "",
        "ai_advantage": "",

        "key_advantages": [],
        "competitive_differentiators": []
        }}

        Startup:
        {startup_text}
        """

        response = LLMService.ask(prompt)

        print("\n========== BUSINESS RAW ==========\n")
        print(response)

        business = JsonParser.parse(response)

        print("\n========== BUSINESS PARSED ==========\n")
        print(business)

        return business
