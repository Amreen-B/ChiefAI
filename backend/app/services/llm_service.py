import os

from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_AI_KEY"),
    azure_endpoint=os.getenv("AZURE_AI_ENDPOINT"),
    api_version="2024-10-21"
)


class LLMService:

    @staticmethod
    def ask(prompt: str):

        response = client.chat.completions.create(
            model=os.getenv("AZURE_DEPLOYMENT_NAME"),
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=300
        )

        return response.choices[0].message.content