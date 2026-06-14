import json
import re


class JsonParser:
    @staticmethod
    def parse(response):

        if not response:
            return {}

        try:
            return json.loads(response)

        except Exception:
            pass

        cleaned = response.strip()

        cleaned = cleaned.replace("```json", "")
        cleaned = cleaned.replace("```", "")
        cleaned = cleaned.replace("\u201c", "\"")
        cleaned = cleaned.replace("\u201d", "\"")
        cleaned = cleaned.replace("\u2018", "'")
        cleaned = cleaned.replace("\u2019", "'")

        match = re.search(r"\{[\s\S]*\}", cleaned)

        if not match:
            print("JSON Parse Error: No JSON object found.")
            return {}

        json_text = match.group()

        try:
            return json.loads(json_text)

        except Exception as e:
            print("JSON Parse Error:")
            print(e)
            print("\nRaw JSON:\n")
            print(json_text)

            print("\n========== JSON ERROR ==========")
            print(response)
            print("================================")
            return {}