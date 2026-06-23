import tiktoken

text = "Write an email apologizing to Sarah."

models=[
	"gpt-4.1",
	"gpt-4o",
	"gpt-4",
	"gpt-3.5-turbo",
]

for model in models:
    enc = tiktoken.encoding_for_model(model)
    tokens = enc.encode(text)
    
    print("="*50)
    print(f"Model: {model}")
    print(f"Token: {len(tokens)}")
    print(tokens)