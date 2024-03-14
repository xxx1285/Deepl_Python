"""
Шукаємо в тексті лінки, чистимо та зберігаємо
"""

import re

def trim_url(url):
        if ")" in url:
            url = url.split(")")[0]
        if '"' in url:
            url = url.split('"')[0]
        return url

# якщо в url всьго 2 сим '/', додати в кінці '/
def ensure_trailing_slash(url):
    if url.count('/') == 2:
        url += '/'
    return url


def extract_urls(text, excluded_words):
    # Регулярний вираз для знаходження url-адрес
    url_pattern = re.compile(r'http[^\s]+')

    # Знаходимо всі url-адреси у тексті
    urls = url_pattern.findall(text)

    # Видаляємо url, які містять слова
    urls = [url for url in urls if not any(word in url for word in excluded_words)]

    # Пост-обробка: видалення символів після закриваючої дужки, якщо вона є в кінці URL
    # urls = [url.split(")")[0] if ")" in url else url for url in urls]
    # urls = [url.split(")")[0].split('"')[0] for url in urls]

    urls = [trim_url(url) for url in urls]

    # Додавання завершувального символу '/' до URL, якщо в ньому тільки 2 символи '/'
    urls = [ensure_trailing_slash(url) for url in urls]

    # Видалення URL, які мають менше 10 символів
    urls = [url for url in urls if len(url) >= 10]


    return urls

def save_to_txt(urls, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for url in urls:
            file.write(url + '\n')

def read_from_txt(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

if __name__ == "__main__":
    input_filename = r'Linkbilding\1_Telegram_link_chistim\input\text_and_telegramText.txt'
    output_filename = r'Linkbilding\1_Telegram_link_chistim\output\soroka.txt'

    excluded_words = ["google", "t.me", "joxi.ru", "youtube", "telegra.ph", "motozilla.com.ua", "bit.ly", "serpstat.com", \
                      "mebel.com.ua", "interfax.com", "similarweb.com", "ahrefs.com", "wikipedia.org", "yandex", "wordpress.org", \
                        "moz.com", "screamingfrog", "semrush", "youtu.be", "sitemaps.org", "rush-analytics", "key-collector", \
                        "gtmetrix.com", "copyscape.com", "keyword.io", "serprobot.com", "atlassian.com", "keyword", "seo", \
                        "collaborator.pro", ".png", ".js", "jpg", ".webp", "vc.ru", "prnt"]
    # excluded_words = ["g543344e"]

    text = read_from_txt(input_filename)

    urls = extract_urls(text, excluded_words)
    save_to_txt(urls, output_filename)
