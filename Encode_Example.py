import tiktoken

# Choose the tokenizer for your model
encoding = tiktoken.encoding_for_model("gpt-4.1")

text = "Write an email apologizing to Sarah for the tragic garden"

tokens = encoding.encode(text)

print("Original Text:")
print(text)

print("\n Token ID:")
print(tokens)

print(f"\nNumber of tokens: {len(tokens)}")
