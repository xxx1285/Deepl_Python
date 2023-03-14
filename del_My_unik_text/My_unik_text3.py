import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup

# Відкриваємо HTML файл
with open(r"C:\Gembling\Deepl_Python\Deepl_Python\My_unik_text\txt\no_unik_html.txt", 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Отримуємо всі тексти з HTML тегів
texts = soup.findAll(text=True)

# Об'єднуємо тексти в один рядок
all_text = "".join(texts)

# Створюємо клас Tokenizer для перетворення тексту на людиноподібну мову
class Tokenizer:
    @staticmethod
    def humanize_text(text):
        # Розбиваємо текст на речення
        sentences = sent_tokenize(text)

        # Ініціалізуємо лематизатор
        lemmatizer = WordNetLemmatizer()

        # Проходимося по кожному реченню
        for i in range(len(sentences)):
            # Розбиваємо речення на слова
            words = word_tokenize(sentences[i])

            # Проходимося по кожному слову
            for j in range(len(words)):
                # Знаходимо базову форму слова за допомогою лематизатора
                base_word = lemmatizer.lemmatize(words[j], wordnet.VERB)

                # Замінюємо слово на базову форму
                words[j] = base_word

            # З'єднуємо слова назад у речення
            sentences[i] = " ".join(words)

        # З'єднуємо речення назад у текст
        humanized_text = " ".join(sentences)

        return humanized_text

# Використовуємо Tokenizer для перетворення тексту на людиноподібну мову
tokenizer = Tokenizer()
humanized_text = tokenizer.humanize_text(all_text)

# Виводимо результат
print(humanized_text)
