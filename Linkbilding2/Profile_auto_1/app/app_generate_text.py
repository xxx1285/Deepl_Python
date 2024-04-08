import os
import random
import re

# Базовый путь к каталогу с файлами
base_path = "Linkbilding2/Profile_auto_1/profile_gener_text"

url_dict = {
    'en': ['/en/', 'variants'],
    'es': ['/es/'],
    'de': ['/de/'],
    'fr': ['/fr/'],
    'pt': ['/pt/'],
    'ru': ['/ru/'],
    'tr': ['/tr/']
}

def generate_random_sentence(string, url):
    # Функция для замены блока в фигурных скобках на случайное значение из этого блока
    def replace_block(match):
        options = match.group(1).split('|')
        return random.choice(options)

    # Паттерн для поиска блоков в фигурных скобках
    pattern = re.compile(r'\{(.*?)\}')

    # Замена блоков на случайные значения
    result = pattern.sub(replace_block, string) + f" {url}"

    return result

def generate_text_about_us(url):
    for lang, paths in url_dict.items():
        for path in paths:
            if path in url:
                # Полный путь к файлу .txt для выбранного языка
                file_path = os.path.join(base_path, f"{lang}.txt")
                # Открываем файл .txt
                with open(file_path, 'r', encoding='utf-8') as file:
                    random_line = random.choice(file.readlines())
                    # Обрабатываем случайную строку функцией generate_random_sentence
                    result = generate_random_sentence(random_line.strip(), url)
                    return result
    # Если совпадение не найдено, используем "en"
    file_path = os.path.join(base_path, "en.txt")
    with open(file_path, 'r', encoding='utf-8') as file:
        random_line = random.choice(file.readlines())
        result = generate_random_sentence(random_line.strip(), url)
        return result
