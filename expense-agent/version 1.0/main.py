import json
import re
import sqlite3
from ollama import chat

# Get user input
user_input = input("Enter expense: ")

# Prompt for Gemma
prompt = f"""
You are an expense extraction engine.

Extract the expense details from the text below.

Return ONLY valid JSON.
Do not use markdown.
Do not use ```json.
Do not provide explanations.

Expected format:

{{
    "amount": 250,
    "category": "Food",
    "description": "Lunch"
}}

Text:
{user_input}
"""

# Call Ollama
response = chat(
    model="gemma3:4b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

response_text = response["message"]["content"]

print("\nGemma Response:")
print(response_text)

# Extract JSON safely
match = re.search(r'\{.*\}', response_text, re.DOTALL)

if not match:
    print("\nError: No JSON found in model response")
    exit(1)

try:
    expense = json.loads(match.group())
except json.JSONDecodeError as e:
    print(f"\nError parsing JSON: {e}")
    exit(1)

# Connect to database
conn = sqlite3.connect("expense.db")
cursor = conn.cursor()

# Save expense
cursor.execute("""
INSERT INTO expenses
(expense_date, amount, category, description)
VALUES
(date('now'), ?, ?, ?)
""",
(
    expense["amount"],
    expense["category"],
    expense["description"]
))

conn.commit()
conn.close()

print("\nExpense saved successfully!")
print(f"Amount      : ₹{expense['amount']}")
print(f"Category    : {expense['category']}")
print(f"Description : {expense['description']}")