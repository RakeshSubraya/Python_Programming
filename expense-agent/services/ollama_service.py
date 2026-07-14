import json
import re
from datetime import date, timedelta

try:
    from ollama import chat
    _OLLAMA_AVAILABLE = True
except ImportError:
    chat = None
    _OLLAMA_AVAILABLE = False


class OllamaService:

    def __init__(self, model_name="gemma3:4b"):
        self.model_name = model_name
        if not _OLLAMA_AVAILABLE:
            print("Warning: ollama package is not installed. Using local extraction fallback.")

    def extract_expense(self, user_text: str) -> dict:
        if _OLLAMA_AVAILABLE:
            return self._extract_with_ollama(user_text)

        return self._extract_locally(user_text)

    def _extract_with_ollama(self, user_text: str) -> dict:
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

    def _extract_locally(self, user_text: str) -> dict:
        cleaned_text = user_text.strip()
        if not cleaned_text:
            raise ValueError("Expense text cannot be empty.")

        amount = self._parse_amount(cleaned_text)
        category = self._parse_category(cleaned_text)
        expense_date = self._parse_date(cleaned_text)
        description = self._parse_description(cleaned_text)

        return {
            "amount": amount,
            "category": category,
            "description": description,
            "expense_date": expense_date
        }

    def _parse_amount(self, text: str):
        match = re.search(r"(\d+[\.,]?\d*)", text)
        if not match:
            raise ValueError("Could not find an amount in the text.")

        amount_text = match.group(1).replace(",", "")
        try:
            return float(amount_text)
        except ValueError as exc:
            raise ValueError("Invalid amount format.") from exc

    def _parse_category(self, text: str):
        categories = {
            "Food": ["food", "lunch", "dinner", "breakfast", "restaurant", "cafe", "coffee", "tea", "bread", "grocery", "snack"],
            "Travel": ["taxi", "uber", "bus", "train", "flight", "petrol", "fuel", "travel", "taxi", "trip", "parking"],
            "Shopping": ["shopping", "mall", "store", "clothes", "shoes", "gift", "purchase", "amazon", "online"],
            "Bills": ["rent", "electricity", "water", "internet", "bill", "phone", "utilities", "subscription"],
            "Medical": ["doctor", "hospital", "medicine", "pharmacy", "medical", "clinic"],
            "Entertainment": ["movie", "cinema", "concert", "game", "netflix", "party", "entertainment"],
            "Education": ["course", "tuition", "books", "class", "training", "education"]
        }

        lower = text.lower()
        for category, keywords in categories.items():
            if any(keyword in lower for keyword in keywords):
                return category

        return "Other"

    def _parse_date(self, text: str):
        lower = text.lower()
        today = date.today()

        if "today" in lower:
            return today.isoformat()
        if "yesterday" in lower:
            return (today - timedelta(days=1)).isoformat()
        if "last month" in lower:
            first_of_month = today.replace(day=1)
            previous_month = first_of_month - timedelta(days=1)
            return previous_month.replace(day=1).isoformat()
        if "last week" in lower:
            return (today - timedelta(days=7)).isoformat()

        date_match = re.search(r"(\d{4}-\d{2}-\d{2})", text)
        if date_match:
            return date_match.group(1)

        return today.isoformat()

    def _parse_description(self, text: str):
        stripped = text.strip()
        return re.sub(r"\s+", " ", stripped)
