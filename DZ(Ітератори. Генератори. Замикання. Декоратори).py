class WordL:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        current_word = self.words[self.index]
        self.index += 1
        return current_word, len(current_word)

user_input = input("Введіть слова (через пробіл, без коми): ")
words_list = user_input.split()
iterator = WordL(words_list)

for word, length in iterator:
    print(f"{word}: {length}")