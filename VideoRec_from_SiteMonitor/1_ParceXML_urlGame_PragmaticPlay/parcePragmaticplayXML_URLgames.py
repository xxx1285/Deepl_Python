import requests
import os
from bs4 import BeautifulSoup

def find_a_href_by_key_sitemap_index(url, key_in_href):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    found_urls = []
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'xml')
        filtered_urls = [loc.text for loc  in soup.find_all('loc') if key_in_href in loc.text]
        found_urls.extend(filtered_urls)
    return found_urls


def find_a_href_by_key__all_games(sitemap_games_urls, key_in_href):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    found_urls = []
    for url in sitemap_games_urls:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'xml')
            filtered_urls = [loc.text for loc  in soup.find_all('loc') if key_in_href in loc.text]
            found_urls.extend(filtered_urls)
    return found_urls


def main():
    sitemap_url = "https://www.pragmaticplay.com/sitemap_index.xml"
    sitemaps_games_urls = find_a_href_by_key_sitemap_index(sitemap_url, "/games")
    all_games_urls = find_a_href_by_key__all_games(sitemaps_games_urls, "/en/")

    output_dir = r'VideoRec_from_SiteMonitor\1_ParceXML_urlGame_PragmaticPlay\output'
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, 'output-urls-games-02-12-2023.txt')
    with open(output_file, 'w') as file:
        for url in all_games_urls:
            file.write(url + '\n')

if __name__ == "__main__":
    main()
