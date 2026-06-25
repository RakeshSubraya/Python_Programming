import argparse
import sys

import tiktoken


DEFAULT_MODEL = "gpt-4.1"
DEFAULT_TEXT = "Write an email apologizing to Sarah."


def get_encoding(model):
    return tiktoken.encoding_for_model(model)


def show_python_environment():
    print("Python Executable:")
    print(sys.executable)

    print("\nPython version:")
    print(sys.version)


def show_encoded_tokens(text, model):
    encoding = get_encoding(model)
    tokens = encoding.encode(text)

    print("Original Text:")
    print(text)

    print("\nToken IDs:")
    print(tokens)

    print(f"\nNumber of tokens: {len(tokens)}")


def show_decoded_text(text, model):
    encoding = get_encoding(model)
    tokens = encoding.encode(text)
    decoded = encoding.decode(tokens)

    print("Encoded:")
    print(tokens)

    print("\nDecoded:")
    print(decoded)


def show_individual_tokens(text, model):
    encoding = get_encoding(model)
    tokens = encoding.encode(text)

    print(f"{'Token ID':<10}{'Decoded Piece'}")
    print("-" * 30)

    for token in tokens:
        piece = encoding.decode([token])
        print(f"{token:<10}{repr(piece)}")


def show_raw_token_bytes(text, model):
    encoding = get_encoding(model)
    tokens = encoding.encode(text)

    for token in tokens:
        print(
            f"ID: {token:<8}"
            f"Bytes: {encoding.decode_single_token_bytes(token)}"
        )


def compare_models(text):
    models = [
        "gpt-4.1",
        "gpt-4o",
        "gpt-4",
        "gpt-3.5-turbo",
    ]

    for model in models:
        encoding = get_encoding(model)
        tokens = encoding.encode(text)

        print("=" * 50)
        print(f"Model: {model}")
        print(f"Token count: {len(tokens)}")
        print(tokens)


def echo_arguments(values):
    print(values)


def run_all_examples(text, model, echo_values):
    sections = [
        ("Python Environment", lambda: show_python_environment()),
        ("Encode Text", lambda: show_encoded_tokens(text, model)),
        ("Decode Tokens", lambda: show_decoded_text(text, model)),
        ("Individual Tokens", lambda: show_individual_tokens(text, model)),
        ("Raw Token Bytes", lambda: show_raw_token_bytes(text, model)),
        ("Model Comparison", lambda: compare_models(text)),
    ]

    if echo_values:
        sections.append(("Echo Arguments", lambda: echo_arguments(echo_values)))

    for title, action in sections:
        print("\n" + "=" * 60)
        print(title)
        print("=" * 60)
        action()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run OpenAI tokenizer examples with tiktoken."
    )
    parser.add_argument(
        "--text",
        default=DEFAULT_TEXT,
        help="Text to tokenize.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="Model name used to select the tokenizer.",
    )
    parser.add_argument(
        "--demo",
        choices=[
            "all",
            "env",
            "encode",
            "decode",
            "pieces",
            "bytes",
            "compare",
            "echo",
        ],
        default="all",
        help="Tokenizer demo to run.",
    )
    parser.add_argument(
        "echo_values",
        nargs="*",
        help="Values to echo when using --demo echo.",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    actions = {
        "env": lambda: show_python_environment(),
        "encode": lambda: show_encoded_tokens(args.text, args.model),
        "decode": lambda: show_decoded_text(args.text, args.model),
        "pieces": lambda: show_individual_tokens(args.text, args.model),
        "bytes": lambda: show_raw_token_bytes(args.text, args.model),
        "compare": lambda: compare_models(args.text),
        "echo": lambda: echo_arguments(args.echo_values),
        "all": lambda: run_all_examples(args.text, args.model, args.echo_values),
    }

    actions[args.demo]()


if __name__ == "__main__":
    main()
