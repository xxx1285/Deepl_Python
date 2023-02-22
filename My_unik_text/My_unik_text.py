import os
import re
import requests
import json
from my_class_nltk import NLTKTextConverter
from bs4 import BeautifulSoup


def clean_text(text):
    # функція для видалення символів з тексту
    remove_chars = ['&nbsp;', '&', '\'', '"', "'"]
    for char in remove_chars:
        text = text.replace(char, '')
    return text


def translate_text(text):
    # переклад тексту через API Deepl
    url = 'https://api-free.deepl.com/v2/translate'
    params = {
        'auth_key': 'your_auth_key',
        'text': text,
        'target_lang': 'UK'
    }
    response = requests.post(url, data=params)
    json_data = response.json()
    translated_text = json_data['translations'][0]['text']
    return translated_text


# SQL Зчитуємо параметри з конфігураційного файлу
with open(r'\configs\config_sql.json') as f:
    config = json.load(f)

# Створюємо об'єкт класу NLTKTextConverter
converter = NLTKTextConverter()

# Відкриваємо файл з HTML-кодом
with open(r'txt\no_unik_html.txt', 'r', encoding='utf-8') as f:
    html = f.read()

# Розбираємо HTML за допомогою BeautifulSoup
soup = BeautifulSoup(html, "html.parser")



# Знаходимо всі тексти в HTML
texts = soup.find_all(text=True)
text = soup.find("p").get_text()
# Видаляємо символи з тексту
for char in chars_to_remove:
    texts = re.sub(re.escape(char), "", texts)

for text in texts:
    # Якщо тексти не є частиною структури тегів, пропускаємо їх
    if text.parent.name in ["style", "script", "head", "title", "meta"]:
        continue

    # Розбиваємо текст на токени
    unique_text = converter.tokenize_text(text)

    # Виконуємо POS-тегування тексту
    unique_text = converter.tag_text(unique_text)

    # Рахуємо кількість слів з кожною частином мови (POS)
    unique_text = converter.count_pos(unique_text)

    # Створюємо словники, що містять відображення між словами та їх частинами мови
    unique_text = converter.map_words_to_pos(unique_text)

    # Перетворюємо текст на людиноподібну мову
    converted_text = converter.convert_text(unique_text)

    # Замінюємо оригінальний текст на унікальний
    text.replace_with(unique_text)

# Зберігаємо змінений HTML у файлі
with open(r"txt\unik_html.txt", "w") as f:
    f.write(str(soup))
