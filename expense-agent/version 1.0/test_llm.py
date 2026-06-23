# test_llm.py

from ollama import chat

response = chat(
    model='gemma3:4b',
    messages=[
        {
            'role': 'user',
            'content': 'Say Hello'
        }
    ]
)

print(response['message']['content'])