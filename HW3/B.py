import os.path
import nltk


class FileReader:
    def __init__(self, path):
        self.path = path
        if not os.path.isfile(self.path):
            self.exist = False
        else:
            self.exist = True
        self.line_count = 0
        self.word_count = 0

    def read(self):
        if not self.exist:
            return ''
        with open(self.path, "r") as file:
            return file.read()

    def write(self, text):
        if not self.exist:
            return
        with open(self.path, "a") as file:
            file.write(text)

    def __str__(self):
        return os.path.abspath(self.path)

    def __add__(self, other):
        if self.exist and other.exist:
            new_path = f"add_{os.path.basename(self.path)}_{os.path.basename(other.path)}"
            with open(new_path, "w") as new:
                new.write(self.read() + other.read())
            return FileReader(new_path)
        else:
            raise Exception("Trying adding not existing files!")

    def count(self):
        if self.word_count == 0:
            self.word_count = len(nltk.word_tokenize(self.read()))
        if self.line_count == 0:
            self.line_count = len(self.read().split('\n'))
        return self.line_count, self.word_count
