import sentencepiece as spm

MODEL_FILE = "tokenizer.model"

DEFAULT_TEXT = "Write a email apologizing to Sarah."

def load_tokenizer():
    print("Loading SentencePiece tokenizer...")

    processor = spm.SentencePieceProcessor()
    processor.load(MODEL_FILE)

    print(f"Tokenizer loaded from {MODEL_FILE}")

    return processor

def encode_text(text, processor):
    return processor.encode(text, out_type=int)

def encode_text_to_token(text, processor):
    return processor.encode(text, out_type=str)

def decode_tokens(tokens, processor):
    return processor.decode(tokens)

def print_token_info(tokens, processor):

    print("\nToken Information")
    print("-" * 60)

    print(f"{'Index':<8}{'ID':<10}{'Piece'}")

    print("-" * 60)

    for index, token_id in enumerate(tokens):
        piece = processor.id_to_piece(token_id)
        print(f"{index:<8}{token_id:<10}{piece}")


def main():
    processor = load_tokenizer()

    encoded_tokens = encode_text(DEFAULT_TEXT, processor)
    print("\nEncoded Tokens:")
    print(encoded_tokens)

    token_string = encode_text_to_token(DEFAULT_TEXT, processor)
    print("\nEncoded Tokens as Strings:")
    print(token_string) 

    print_token_info(encoded_tokens, processor)

    decoded_text = decode_tokens(encoded_tokens, processor)
    print("\nDecoded Text:")
    print(decoded_text) 



if __name__ == "__main__":
    main()
