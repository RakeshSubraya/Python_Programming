import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4.1")

text = "Write an email apologizing to Sarah."

tokens = encoding.encode(text)

decoded = encoding.decode(tokens)

print("Encoded: ")
print(tokens)

print("\nDecoded: ")
print(decoded)

