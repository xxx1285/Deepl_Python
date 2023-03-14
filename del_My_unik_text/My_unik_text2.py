from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# Відкриваємо HTML файл
with open(r"C:\Gembling\Deepl_Python\Deepl_Python\My_unik_text\txt\no_unik_html.txt", 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Отримуємо весь текст з HTML файлу
text = soup.get_text()

# Отримуємо всі тексти з HTML тегів
texts = soup.findAll(text=True)

# Функція для перетворення слів на людиноподібну мову
def humanize_text(text):
    # Розбиваємо текст на речення
    sentences = sent_tokenize(text)
    # Ініціалізуємо лематизатор слів
    lemmatizer = WordNetLemmatizer()

    # Проходимось по кожному реченню і перетворюємо слова на людиноподібну мову
    for i in range(len(sentences)):
        words = word_tokenize(sentences[i])
        for j in range(len(words)):
            # Отримуємо синоніми для слова
            synonyms = wordnet.synsets(words[j])
            # Якщо є синоніми, то замінюємо слово на перший синонім, інакше залишаємо слово
            if synonyms:
                words[j] = synonyms[0].lemmas()[0].name().replace('_', ' ')
            else:
                words[j] = lemmatizer.lemmatize(words[j])
        # Збираємо речення знову
        sentences[i] = ' '.join(words)

    # Збираємо текст знову
    text = ' '.join(sentences)
    return text

# Відправляємо текст на обробку в окремий файл
with open('dop.py', 'w', encoding='utf-8') as f:
    f.write(humanize_text(text))
