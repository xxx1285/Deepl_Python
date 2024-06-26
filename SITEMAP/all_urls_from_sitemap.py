import requests
import xml.etree.ElementTree as ET
import json
import datetime
import urllib.parse


# SITEMAP_URL = "https://the-dog-house.org/my-sitemap.xml"
# SITEMAP_URL = "https://aviator--game.com/my-sitemap.xml"
SITEMAP_URL = "https://onlyfans-models.com/sitemap1.xml"
# if you like add this == https://www.youtube.com/redirect?q=https://site.com/vavada-gates-of-olympus/
NACHALO_URL = 'https://www.youtube.com/redirect?q='
# NACHALO_URL = 'https://medium.com/r?url='

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

# Получение текущей даты в формате 'гггг-мм-дд'
current_date = datetime.datetime.now().strftime('%Y-%m-%d')


def fetch_sitemap_urls():
    headers = {
        "User-Agent": user_agent
    }
    response = requests.get(SITEMAP_URL, headers=headers)
    sitemap = ET.fromstring(response.content)

    # Извлекаем все URL из sitemap.xml
    urls = [elem.text for elem in sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]

    # Всі URLs  з карти сайтів
    with open(r'SITEMAP\output\sitemap_url_onlyfans-models-sitemap1-' + current_date + '.txt', 'w') as file_urls:
        for url in urls:
            # url = urllib.parse.quote(url, safe='')  # Якщо потрыбно Виведе: http%3A%2F%2Fdance-c.ru - для medium.com 
            # file_urls.write(NACHALO_URL + url + '\n')
            file_urls.write(url + '\n')

    return urls

def main():
    urls = fetch_sitemap_urls()


if __name__ == "__main__":
    main()
