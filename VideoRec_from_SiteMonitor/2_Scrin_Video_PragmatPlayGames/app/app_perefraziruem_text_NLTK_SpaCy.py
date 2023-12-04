import spacy
import nltk
from nltk.corpus import wordnet
# Инициализация NLTK и spaCy
nltk.download('wordnet')
# Загрузка модели spaCy
nlp = spacy.load("en_core_web_sm")


# Функция для поиска синонимов
def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonym = lemma.name().replace('_', ' ')
            synonyms.add(synonym)
    return list(synonyms)

# Функция для удаления лишних пробелов перед пунктуацией
def remove_unwanted_spaces(text):
    unwanted_space_patterns = [' ,', ' .', ' !', ' :', ' ;', ' ?', " ’"]
    for pattern in unwanted_space_patterns:
        if pattern[0] != " ":
            text = text.replace(' ' + pattern, pattern)
        else:
            text = text.replace(pattern, pattern.strip())
    return text

# Функция для перефразирования текста с использованием spaCy и NLTK
def paraphrase_with_spacy(text):
    doc = nlp(text)
    new_words = []

    for token in doc:
        # Использование частеречной разметки для определения существительных
        if token.pos_ in ['NOUN'] and not token.is_punct:
            synonyms = get_synonyms(token.text)
            if synonyms:
                new_word = synonyms[0]  # Выбор первого синонима
                new_words.append(new_word)
            else:
                new_words.append(token.text)
        else:
            new_words.append(token.text)
    
    paraphrased_text = ' '.join(new_words)
    return remove_unwanted_spaces(paraphrased_text)