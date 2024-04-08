import aiohttp
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

SAVE_ALL_URLS = r'Parsing\Search_All_UrlsSite\output\allurls.txt'

START_URL = "https://casino-vulkan24.top/"
LIMIT_URLS = 20
DOMAIN = re.search('(?<=://)([^/]+)', START_URL).group(1)

STOP_URLS = ["email", "cdn-cgi", "privileges"]

visited_urls = set()
semaphore = asyncio.Semaphore(5)  # Ограничение на 5 одновременных запросов
headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15Z (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1 (Applebot/0.1)"}

async def fetch_html(session, url):
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            return await response.text()
        else:
            print(f"Failed to fetch HTML from {url}: Status code {response.status}")
            return None

async def get_links_from_page(session, url):
    try:
        async with semaphore:  # Захватываем семафор
            html = await fetch_html(session, url)
        soup = BeautifulSoup(html, 'lxml')
        links = [link['href'] for link in soup.find_all('a', href=True)]
        # Удаление хвостов, начинающихся с "#", и добавление START_URL, если не осталось ссылок
        links = [re.sub(r'#.*$', '', link) for link in links]
        # Удаление пустых строк и удаление согласно списка
        links = [link for link in links if link and not any(keyword in link for keyword in STOP_URLS)]

        ########################################################################
        # Фильтрация ссылок: оставляем только ссылки первого уровня вложенности
        filtered_links = []
        for link in links:
            parsed_link = urlparse(link)
            if link.startswith('/'):  # Если ссылка относительная (начинается с '/')
                if parsed_link.path.count('/') <= 1:  # Если количество слешей не превышает одного
                    filtered_links.append(link)
                elif parsed_link.path.count('/') == 2 and parsed_link.path.endswith('/'):  # Если есть два слеша и последний символ - слеш
                    filtered_links.append(link)
            elif link.startswith('http'):  # Если ссылка абсолютная (начинается с 'http' или 'https')
                if parsed_link.netloc == DOMAIN:  # Убеждаемся, что домен соответствует целевому домену
                    if parsed_link.path.count('/') <= 1:  # Если количество слешей не превышает одного
                        filtered_links.append(link)
                    elif parsed_link.path.count('/') == 2 and parsed_link.path.endswith('/'):  # Если есть два слеша и последний символ - слеш
                        filtered_links.append(link)
        ########################################################################
        ########################################################################

        filtered_links.insert(0, START_URL)  # Добавление START_URL в начало списка
        return [urljoin(url, link) for link in filtered_links]

    except Exception as e:
        print(f"Error fetching links from {url}: {e}")
        return []

async def get_page_title(html):
    # Получаем Тайтл страницы
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find('title')
    if title and title.text.strip():  # Если найден и не пустой
        return title.text.strip()
    else:
        h1 = soup.find('h1')
        if h1 and h1.text.strip():  # Если найден и не пустой
            return h1.text.strip()
        else:
            return ''
        

async def crawl_site(start_url):
    global visited_urls
    queue = set([start_url])  # Используем множество для хранения очереди
    visited_urls = set()
    links_visited = 0

    async with aiohttp.ClientSession() as session:
        while queue and links_visited < LIMIT_URLS:
            url = queue.pop()  # Получаем URL из очереди
            if url not in visited_urls:
                print(f"Crawling: {url}")
                visited_urls.add(url)  # Добавляем URL в посещенные
                links = await get_links_from_page(session, url)
                for link in links:
                    if urlparse(link).netloc == DOMAIN:
                        if link not in visited_urls and link not in queue:
                            queue.add(link)  # Добавляем в очередь, если еще не был посещен и не в очереди
                with open(SAVE_ALL_URLS, 'a') as f:
                    f.write(f"{url}\n")  # Записываем посещенный URL в файл

async def main():
    await crawl_site(START_URL)

if __name__ == "__main__":
    asyncio.run(main())
