"""
corpus.py
This module contains the Corpus class, which is responsible for loading and storing the training corpus.

This class DOES NOT tokenize any text.
It simply reads the corpus from the disk.

"""

from pathlib import Path
from common.logger import logger

class Corpus:
    def __init__(self, file_path:str):
        self.file_path = Path(file_path)
        self.raw_text = ""

    def load_corpus(self):
        """
        Reads the corpus from the disk.
        """
        if not self.file_path.exists():
            raise FileNotFoundError(f"Corpus file not found: {self.file_path}")
        
        logger.info(f"Loading corpus from {self.file_path}...")

        with self.file_path.open("r", encoding="utf-8") as file:
            self.raw_text = file.read()

    def get_raw_text(self)-> str:
        """
        Returns the complete corpus text 
        """
        return self.raw_text
    def print_summary(self)-> None:
        """
        Prints a summary of the corpus.
        """
        print("=" * 60)
        print(f"Corpus Summary")
        print(f"file    :{self.file_path}")
        print(f"Characters: {len(self.raw_text)}")
        print(f"lines     : {len(self.raw_text.splitlines())}")