import nltk
import random


class NLTKTextConverter:
    def __init__(self):
        self.text = ""
        self.tokenized_text = []
        self.tagged_text = []
        self.pos_counts = {}
        self.pos_to_word = {}
        self.word_to_pos = {}

    def load_text(self, filename):
        # Завантажуємо текстовий файл
        with open(filename, "r", encoding="utf-8") as file:
            self.text = file.read()

    def tokenize_text(self):
        # Розбиваємо текст на токени
        self.tokenized_text = nltk.word_tokenize(self.text)

    def tag_text(self):
        # Виконуємо POS-тегування тексту
        self.tagged_text = nltk.pos_tag(self.tokenized_text)

    def count_pos(self):
        # Рахуємо кількість слів з кожною частином мови (POS)
        for word, pos in self.tagged_text:
            if pos not in self.pos_counts:
                self.pos_counts[pos] = 1
            else:
                self.pos_counts[pos] += 1

    def map_words_to_pos(self):
        # Створюємо словники, що містять відображення між словами та їх частинами мови
        for word, pos in self.tagged_text:
            if pos not in self.pos_to_word:
                self.pos_to_word[pos] = [word]
            else:
                self.pos_to_word[pos].append(word)
            self.word_to_pos[word] = pos

    def convert_text(self):
        # Перетворюємо текст на людиноподібну мову, замінюючи слова на інші, що мають ту саму POS-ознаку
        converted_text = []
        for word, pos in self.tagged_text:
            if pos in self.pos_to_word:
                options = self.pos_to_word[pos]
                if len(options) > 1:
                    options.remove(word)
                    converted_text.append(random.choice(options))
                else:
                    converted_text.append(word)
            else:
                converted_text.append(word)
        return " ".join(converted_text)
