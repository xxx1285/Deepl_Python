"""
    Отримуємо самий частотний вираз біграмми ta триграмми тайтла та тексту  
"""


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from collections import Counter


def most_frequent_phrase_in_body(title_text, body_text):

    # Список стоп-слов
    stop_words = set(stopwords.words('english'))
    # Добавляем символы "|" и "/" в список стоп-слов
    stop_words.update(["|", "-"])

    # Разбиваем title на токены
    title_tokens = [word for word in word_tokenize(title_text.lower()) if word.isalnum() and word not in stop_words]

    # Генерируем биграммы и триграммы для title
    bigrams_title = list(ngrams(title_tokens, 2))
    trigrams_title = list(ngrams(title_tokens, 3))

    # Подсчитываем частоту каждой фразы в тексте body
    body_text_lower = body_text.lower()
    trigram_counts = Counter(ngram for ngram in trigrams_title if ' '.join(ngram) in body_text_lower)
    bigram_counts = Counter(ngram for ngram in bigrams_title if ' '.join(ngram) in body_text_lower)

    # Проверяем, есть ли элементы в trigram_counts
    if trigram_counts:
        # Возвращаем самую часто встречающуюся триграмму
        most_common_ngram, count = trigram_counts.most_common(1)[0]
        return ' '.join(most_common_ngram)
    elif bigram_counts:
        # Возвращаем самую часто встречающуюся биграмму
        most_common_ngram, count = bigram_counts.most_common(1)[0]
        return ' '.join(most_common_ngram)
    else:
        return "Best atricles"