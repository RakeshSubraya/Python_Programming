import json
import re

from ollama import chat
from datetime import date


class OllamaService:

    def __init__(self, model_name="gemma3:4b"):
        self.model_name = model_name

    def extract_expense(self, user_text: str) -> dict:

        today = date.today().isoformat()

        prompt = f"""
        Today's date is {today}.

        Extract expense information.

        Return ONLY valid JSON.

        Rules:
        - amount must be a number
        - category should be one of:
          Food, Travel, Shopping, Bills, Medical,
          Entertainment, Education, Other
        - description should contain the purchased item/service
        - Convert any date expression to YYYY-MM-DD format
        - If no date is mentioned, use today's date

        Fields:
        - amount
        - category
        - description
        - expense_date

        Examples:

        Input:
        Spent 49 rupees on bread last month

        Output:
        {{
            "amount": 49,
            "category": "Food",
            "description": "bread",
            "expense_date": "2026-05-01"
        }}

        Input:
        Spent 100 on petrol yesterday

        Output:
        {{
            "amount": 100,
            "category": "Travel",
            "description": "petrol",
            "expense_date": "2026-06-02"
        }}

        Text:
        {user_text}
        """

        response = chat(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = response.get("message", {}).get("content", "")
        if not content:
            raise Exception("Empty response from Ollama")

        match = re.search(r'\{.*\}', content, re.DOTALL)
        if not match:
            raise Exception(f"JSON not found in model response: {content}")

        try:
            return json.loads(match.group())
        except json.JSONDecodeError as exc:
            raise Exception(f"Failed to parse JSON from response: {exc}\n{content}") from exc
