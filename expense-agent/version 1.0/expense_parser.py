from ollama import chat

prompt = """
Extract expense details from the text.

Return ONLY valid JSON.

Text:
Spent 250 on lunch

Example Output:
{
  "amount": 250,
  "category": "Food",
  "description": "Lunch"
}
"""

response = chat(
    model='gemma3:4b',
    messages=[
        {
            'role': 'user',
            'content': prompt
        }
    ]
)

print(response['message']['content'])