import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

text = "The new Aviator game has won the minds of many people with its unconventional approach among the classic casino slot games."

# Розбиваємо текст на окремі слова (токени)
tokens = word_tokenize(text)

# Ініціалізуємо лематизатор
lemmatizer = WordNetLemmatizer()

# Функція, яка шукає синоніми для слова
def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return synonyms

# Перебираємо кожне слово в тексті та замінюємо його на синонім,
# якщо слово не є Aviator або game
for i in range(len(tokens)):
    word = tokens[i]
    if word not in ['Aviator', 'game']:
        synonyms = get_synonyms(word)
        if synonyms:
            synonyms = [s for s in synonyms if s != word]
            if synonyms:
                new_word = lemmatizer.lemmatize(synonyms[0], pos='a')
                tokens[i] = new_word

# Формуємо новий текст зі зміненими словами
new_text = " ".join(tokens)

print(new_text)
