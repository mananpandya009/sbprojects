"""Word Finder: finds random words from a dictionary."""
from random import choice, randint


class WordFinder:

    def __init__(self, path):
        self.file_path = path
        file_data = open(self.file_path)
        self.text_list = self.parse_file(file_data)
        print(f"We parsed {len(self.text_list)} words!!")

    def parse_file(self, file_data):
        return file_data.readlines()

    def random(self):
        word = choice(self.text_list)
        return word


wf = WordFinder("/Users/panmanan/Downloads/python-oo-practice/words.txt")

print(wf.random())
