import sentencepiece as spm

MODEL_PREFIX = "tokenizer"

VOCAB_SIZE = 59

INPUT_FILE = "tokenizer_corpus.txt"

def train_tokenizer():
    print("Training SentencePiece tokenizer...")

    spm.SentencePieceTrainer.train(
        input=INPUT_FILE,
        model_prefix=MODEL_PREFIX,
        vocab_size=VOCAB_SIZE,
        model_type="Unigram"
    )

    print(f"Tokenizer trained and saved as {MODEL_PREFIX}.model and {MODEL_PREFIX}.vocab")

def main():
    train_tokenizer()

if __name__ == "__main__":
    main()