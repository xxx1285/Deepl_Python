import requests
import xml.etree.ElementTree as ET
import json
import datetime


SITEMAP_URL = "https://gatesofolympus.club/my-sitemap.xml"
# SITEMAP_URL = "https://gatesofolympus.club/my-sitemap.xml"
SITEMAP_URL_AMP = "https://gatesofolympus.club/xml-amp-sitemap.xml"

api_endpoint = "https://acceleratedmobilepageurl.googleapis.com/v1/ampUrls:batchGet"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

# Получение текущей даты в формате 'гггг-мм-дд'
current_date = datetime.datetime.now().strftime('%Y-%m-%d')

# GOOGLE_DEVELOPER_KEY
with open(r'SETTINGS\Google_Developer_API_key_for_AMP\GOOGLE_API_DEVELOPER_KEY.json', 'r') as file:
    key_api = json.load(file)
API_GOOGLE_DEVELOPER_KEY = key_api["google_api_developer_key"]


def fetch_sitemap_urls():
    headers = {
        "User-Agent": user_agent
    }
    response = requests.get(SITEMAP_URL, headers=headers)
    sitemap = ET.fromstring(response.content)

    # Извлекаем все URL из sitemap.xml
    urls = [elem.text for elem in sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]

    # Всі URLs  з карти сайтів
    with open(r'AMP\1-Sbor_s_Sitemap_all_AMP\output\sitemap_url_' + current_date + '.txt', 'w') as file_urls:
        for url in urls:
            file_urls.write(url + '\n')

    return urls


def fetch_sitemap_amp_urls():
    headers = {
        "User-Agent": user_agent
    }
    response = requests.get(SITEMAP_URL_AMP, headers=headers)
    sitemap = ET.fromstring(response.content)

    # Извлекаем все URL из sitemap.xml
    urls_amp = [elem.text for elem in sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]

    # Переводим и сохраняем AMP в Google формат
    transformed_urls_amp = []
    for url in urls_amp:
        # Убедитесь, что URL начинается с "https://", иначе операция замены может привести к ошибке.
        if url.startswith("https://"):
            # Удаляем 'https://' из URL
            stripped_url = url[8:]
            # Добавляем новый префикс и суффикс
            new_url = f"https://gatesofolympus-club.cdn.ampproject.org/c/s/{stripped_url}"
            # Добавляем трансформированный URL в список
            transformed_urls_amp.append(new_url)

    # Всі URLs AMP з карти AMP
    with open(r'AMP\1-Sbor_s_Sitemap_all_AMP\output\sitemap_url_amp__' + current_date + '.txt', 'w') as file_urls:
        for url in urls_amp:
            file_urls.write(url + '\n')
    # Всі URLs AMP з карти AMP в Google форматі
    with open(r'AMP\1-Sbor_s_Sitemap_all_AMP\output\sitemap_url_ampproject__' + current_date + '.txt', 'w') as file_ampproject:
        for url in transformed_urls_amp:
            file_ampproject.write(url + '\n')


def fetch_amp_urls(urls):
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_GOOGLE_DEVELOPER_KEY
    }
    data = {
        "urls": urls
    }

    response = requests.post(api_endpoint, headers=headers, json=data)

    return response.json()

def main():
    urls = fetch_sitemap_urls()
    test_all_amp_and_googleAMP = fetch_sitemap_amp_urls()

    # Разбиваем список URL на группы по 50, так как API принимает максимум 50 URL за раз
    chunks = [urls[i:i + 50] for i in range(0, len(urls), 50)]

    all_results = []

    for chunk in chunks:
        result = fetch_amp_urls(chunk)
        all_results.append(result)

    with open(r'AMP\1-Sbor_s_Sitemap_all_AMP\output\AMP_map__' + current_date + '.json', 'w') as file:
        json.dump(all_results, file, indent=4)

if __name__ == "__main__":
    main()
