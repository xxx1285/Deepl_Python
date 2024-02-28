import os
import re
import json
import scrapy
from scrapy.crawler import CrawlerProcess
from urllib.parse import urlparse
from twisted.internet.error import TimeoutError, TCPTimedOutError
import asyncio
import aiofiles
from concurrent.futures import ThreadPoolExecutor


class WikipediaUrlSpider(scrapy.Spider):
    name = 'wikipedia_urls'
    allowed_urls = ['wikipedia.org']
    # start_urls = ['https://uk.wikipedia.org/wiki/%D0%9D%D0%BE%D0%B2%D0%B8%D0%BD%D0%B8']
    # start_urls = ['https://ru.wikipedia.org/wiki/%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8']
    # start_urls = ['https://en.wikipedia.org/wiki/Plane']
    # start_urls = ['https://en.wikipedia.org/wiki/Big_Brother_Africa']

    # start_urls = ['https://en.wikipedia.org/wiki/Backstage_(South_African_TV_series)']
    # медведчук
    # start_urls = ['https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B4%D0%B2%D0%B5%D0%B4%D1%87%D1%83%D0%BA,_%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87']
    # Africa
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:News_sources/Africa']
    custom_settings = {
        'DOWNLOAD_DELAY': 1,  # Затримка між запитами
        'CONCURRENT_REQUESTS_PER_URL': 25,  # Кількість одночасних запитів на один домен
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'HTTPCACHE_ENABLED': True,
        'COOKIES_ENABLED': False,
        'DOWNLOAD_TIMEOUT': 7,  # Таймаут на завантаження
    }
    exclude_words = ['wiki', 'google', 'facebook', 'yandex', 'google', 'youtube', 'javascript', '.ru', '.by', '.gov', '.edu',
                     '.kz', '.uk', '.fr', '.it', '.lt', '.at', '.uz', '.jp', '.eu', '.pl', '.ch', '.cz', '.am', '.lv',
                     '.de', '.az', '.us', '.ca', '.fi', '.no', '.hu', 'livejournal', 'blogspot', 'wordpress', 'broadwayworld'
                     ]  # Слова для виключення з посилань
    excluded_paths = ['/wiki/Help:', '/wiki/Special:', '#', '/w/']  # Шляхи, які потрібно виключити
    collected_urls = set()  # Множина для зберігання вже відвіданих доменів


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.file_path = 'D:\\Gembling\\Deepl_Python\\Deepl_Python\\Parsing\\Wikipedia\\JSON_Wiki_result\\wiki_affrica\\urls-wiki_affrica-17-01-2024.json'
        self.file_lock = asyncio.Lock()     # Блокування для синхронізації доступу до файлу
        self.urls_buffer = []            # Буфер для зберігання доменів перед записом у файл
        self.buffer_size = 20               # Максимальний розмір буфера
        self.external_urls = set()       # Множина для зберігання зовнішніх доменів
        self.load_existing_data()


    def load_existing_data(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                pass  # Створення порожнього файлу
        else:
            with open(self.file_path, 'r') as file:
                try:
                    data = json.load(file)
                    for item in data:
                        self.external_urls.add(item['url'])
                except json.JSONDecodeError:
                    pass  # Якщо файл порожній або не валідний JSON, нічого не робити


    async def write_buffer_to_file(self):
        if not self.urls_buffer:
            return

        async with self.file_lock:
            existing_data = []
            if os.path.exists(self.file_path) and os.path.getsize(self.file_path) > 0:
                async with aiofiles.open(self.file_path, 'r') as file:
                    try:
                        existing_data = json.loads(await file.read())
                    except json.JSONDecodeError:
                        existing_data = []

            existing_data.extend(self.urls_buffer)
            async with aiofiles.open(self.file_path, 'w') as file:
                # Додаємо відступи для форматування кожного об'єкта на новому рядку
                await file.write(json.dumps(existing_data, ensure_ascii=False, indent=4))

        self.urls_buffer = []


    def add_url_to_buffer(self, url):
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            url = 'http://' + url  # Додавання протоколу "http", якщо він відсутній

        # Извлечение доменного имени
        domain = re.search(r"^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)", url)
        if domain:
            domain_name = domain.group(1)
        else:
            return  # Пропускаем URL, если не удалось извлечь доменное имя
    
        # Фільтрація доменів з нестандартними символами
        if not re.match(r'^https?://[a-zA-Z0-9.-]+$', url):
            return

        if url not in self.external_urls and domain_name.count('.') == 1:
            self.external_urls.add(url)
            self.urls_buffer.append({'url': url, 'domain': domain_name})  # Зберігання даних у форматі JSON
            if len(self.urls_buffer) >= self.buffer_size:
                self.executor.submit(asyncio.run, self.write_buffer_to_file())


    def parse(self, response):
        # Отримання всіх посилань на сторінці
        links = response.css('a::attr(href)').getall()

        for link in links:
            # Перевірка, чи посилання не належить до виключених шляхів
            if not any(link.startswith(excluded_path) for excluded_path in self.excluded_paths):
                # Якщо посилання веде на внутрішню сторінку Wikipedia, йдемо за ним
                if link.startswith('/wiki/'):
                    if link not in self.collected_urls:
                        self.collected_urls.add(link)
                        yield response.follow(link, self.parse)
                else:
                    parsed_url = urlparse(link)
                    url = f"{parsed_url.scheme}://{parsed_url.netloc}"
                    if not any(word in url.lower() for word in self.exclude_words):
                        self.add_url_to_buffer(url)

# Створення та запуск процесу
process = CrawlerProcess(settings=WikipediaUrlSpider.custom_settings)
process.crawl(WikipediaUrlSpider)
process.start()