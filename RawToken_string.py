import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4.1")

text = "Write an email to apologizing to Sarah"

tokens = encoding.encode(text)

for token in tokens:
    print(
        f"ID: {token:<8}"
        f"Bytes: {encoding.decode_single_token_bytes(token)}"
    )