import json
import re


class JsonParser:

    @staticmethod
    def parse(response):

        try:
            return json.loads(response)

        except Exception:

            try:

                cleaned = response.strip()

                cleaned = cleaned.replace(
                    "```json",
                    ""
                )

                cleaned = cleaned.replace(
                    "```",
                    ""
                )

                match = re.search(
                    r"\{.*\}",
                    cleaned,
                    re.DOTALL
                )

                if match:

                    return json.loads(
                        match.group()
                    )

            except Exception as e:

                print(
                    "JSON Parse Error:",
                    e
                )

            return {}