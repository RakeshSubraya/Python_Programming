from bpe_from_scratch.corpus import Corpus

def main():
    print("Loading and summarizing the corpus...")
    corpus = Corpus("data/sample_corpus.txt")
    corpus.load_corpus()
    corpus.print_summary()

    print("\nRaw Text:")
    print(corpus.get_raw_text())
    print("-" * 60)

if __name__ == "__main__":
        main()
