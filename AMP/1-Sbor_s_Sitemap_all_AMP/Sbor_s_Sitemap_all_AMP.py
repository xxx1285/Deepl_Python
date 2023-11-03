import requests
import xml.etree.ElementTree as ET
import json

API_ENDPOINT = "https://acceleratedmobilepageurl.googleapis.com/v1/ampUrls:batchGet"
SITEMAP_URL = "https://gatesofolympus.club/my-sitemap.xml"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

# GOOGLE_DEVELOPER_KEY
with open(r'SETTINGS\Google_Developer_API_key_for_AMP\GOOGLE_API_DEVELOPER_KEY.json', 'r') as file:
    key_api = json.load(file)
API_GOOGLE_DEVELOPER_KEY = key_api["google_api_developer_key"]


def fetch_sitemap_urls():
    headers = {
        "User-Agent": USER_AGENT
    }
    response = requests.get(SITEMAP_URL, headers=headers)
    sitemap = ET.fromstring(response.content)

    # Извлекаем все URL из sitemap.xml
    urls = [elem.text for elem in sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]

    return urls

def fetch_amp_urls(urls):
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_GOOGLE_DEVELOPER_KEY
    }
    data = {
        "urls": urls
    }
    
    response = requests.post(API_ENDPOINT, headers=headers, json=data)
    
    return response.json()

def main():
    urls = fetch_sitemap_urls()
    
    # Разбиваем список URL на группы по 50, так как API принимает максимум 50 URL за раз
    chunks = [urls[i:i + 50] for i in range(0, len(urls), 50)]
    
    all_results = []
    
    for chunk in chunks:
        result = fetch_amp_urls(chunk)
        all_results.append(result)
    
    with open(r'AMP\1-Sbor_s_Sitemap_all_AMP\output\amp_mapping3.json', 'w') as file:
        json.dump(all_results, file, indent=4)

if __name__ == "__main__":
    main()
