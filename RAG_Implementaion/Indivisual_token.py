import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4.1")

text = "Write an email for apologizing to Sarah"

tokens = encoding.encode(text)

print(f"{'Token ID':<10}{'Decoded Piece'}")
print("-" * 30)

for token in tokens:
    piece = encoding.decode([token])
    print(f"{token:<10}{repr(piece)}")