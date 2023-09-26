"""
Скрипт для пошуку унікальних URL у текстовому файлі, вилучення доменного імені з протоколом, 
та категоризації URL на основі визначених ключових слів. Результати записуються у CSV-файл.
"""

import re
import csv


def sanitize_url(url):
    """
    Функція для видалення одинарних та подвійних кавичок з URL і додавання "/" в кінці, якщо необхідно.
    """
    sanitized_url = url.replace("'", "").replace('"', '')
    if '://' in sanitized_url and sanitized_url.count('/') == 2:
        sanitized_url += '/'
    return sanitized_url


def categorize_url(url):
    """
    Функція для категоризації URL на основі заданих ключових слів.
    - Якщо URL містить слова, які вказують на профіль користувача, повертає "profile".
    - Якщо URL вказує на статтю або пост, повертає "article".
    - Інакше повертає порожній рядок.
    """
    profile_keywords = ["user", "profile", "author", "member", "redact"]
    article_keywords = ["post", "article", "story"]
    comment_keywords = ["comment"]

    url_lower = url.lower()
    if any(keyword in url_lower for keyword in profile_keywords):
        return "profile"
    elif any(keyword in url_lower for keyword in article_keywords):
        return "article"
    elif any(keyword in url_lower for keyword in comment_keywords):
        return "comment"
    return ""

def extract_domain_and_url(match):
    """
    Витягує доменне ім'я із протоколом та повний URL з регулярного виразу.
    """
    protocol = match.group(1)
    domain = match.group(2)
    domain_with_protocol = protocol + domain
    full_url = match.group(0)
    full_url = full_url.replace('"', '')
    domain_with_protocol = sanitize_url(domain_with_protocol)
    return domain_with_protocol, full_url

def extract_unique_urls(text, excluded_words):
    """
    Проходить текст, знаходить усі URL, витягує доменне ім'я з протоколом, 
    та видаляє URL, які містять слова із excluded_words. Повертає унікальний список доменних імен та повних URL.
    """
    url_pattern = re.compile(r'(https?://)([^/]+)[^\s]*')
    # url_pattern = re.compile(r'https?://[^/\s]+(?:/[^\s]*)?')

    matches = url_pattern.finditer(text)
    
    unique_pairs = {}
    for match in matches:
        domain, url = extract_domain_and_url(match)
        if "," in url:  # Перевірка на наявність коми у URL
            continue
        if domain and domain not in excluded_words and domain not in unique_pairs:
            unique_pairs[domain] = url

    return [(domain, url, categorize_url(url)) for domain, url in unique_pairs.items()]

def save_to_csv(pairs, filename):
    """
    Зберігає пари доменного імені, URL та його категорії у CSV-файл.
    """
    with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Domain", "URL", "Category"])
        for domain, url, category in pairs:
            writer.writerow([domain, url, category])

def read_from_txt(filename):
    """
    Читає текст із заданого текстового файлу.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

if __name__ == "__main__":
    input_filename = r'Linkbilding\Find_URl_in_Text_Chistim\docs\text.txt'
    output_filename = r'Linkbilding\Find_URl_in_Text_Chistim\docs\extracted_urls4.csv'

    excluded_words = ["google"]

    text = read_from_txt(input_filename)
    domain_url_pairs = extract_unique_urls(text, excluded_words)
    save_to_csv(domain_url_pairs, output_filename)
