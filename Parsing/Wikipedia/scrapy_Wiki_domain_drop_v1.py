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


class WikipediaDomainSpider(scrapy.Spider):
    name = 'wikipedia_domains'
    allowed_domains = ['wikipedia.org']
    # start_urls = ['https://uk.wikipedia.org/wiki/%D0%9D%D0%BE%D0%B2%D0%B8%D0%BD%D0%B8']
    start_urls = ['https://ru.wikipedia.org/wiki/%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8']
    custom_settings = {
        'DOWNLOAD_DELAY': 1,  # Затримка між запитами
        'CONCURRENT_REQUESTS_PER_DOMAIN': 15,  # Кількість одночасних запитів на один домен
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'HTTPCACHE_ENABLED': True,
        'COOKIES_ENABLED': False,
        'DOWNLOAD_TIMEOUT': 7,  # Таймаут на завантаження
    }
    exclude_words = ['wiki', 'google', 'facebook', 'yandex', 'google', 'youtube', 'javascript', '.ru', '.by', '.gov', '.edu',
                     '.ua', '.kz', '.uk', '.fr', '.it', '.lt', '.at', '.uz', '.jp', '.eu', '.pl', '.ch', '.cz', '.am', '.lv',
                     '.de', '.az', '.us', '.ca', '.fi', '.no', '.hu', 'livejournal', 'blogspot', ]  # Слова для виключення з посилань
    excluded_paths = ['/wiki/Help:', '/wiki/Special:', '#', '/w/']  # Шляхи, які потрібно виключити
    collected_domains = set()  # Множина для зберігання вже відвіданих доменів


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.file_path = 'D:\\Gembling\\Deepl_Python\\Deepl_Python\\Parsing\\Wikipedia\\domains-ru-news.json'
        self.file_lock = asyncio.Lock()     # Блокування для синхронізації доступу до файлу
        self.domains_buffer = []            # Буфер для зберігання доменів перед записом у файл
        self.buffer_size = 20               # Максимальний розмір буфера
        self.external_domains = set()       # Множина для зберігання зовнішніх доменів
        self.load_existing_data()

    # async def write_buffer_to_file(self):
    #     async with self.file_lock:
    #         async with aiofiles.open(self.file_path, mode='a') as file:
    #             for domain_data in self.domains_buffer:
    #                 await file.write(json.dumps(domain_data) + '\n')  # Запис у форматі JSON
    #         self.domains_buffer = []

    def load_existing_data(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                pass  # Створення порожнього файлу
        else:
            with open(self.file_path, 'r') as file:
                try:
                    data = json.load(file)
                    for item in data:
                        self.external_domains.add(item['domain'])
                except json.JSONDecodeError:
                    pass  # Якщо файл порожній або не валідний JSON, нічого не робити


    async def write_buffer_to_file(self):
        if not self.domains_buffer:
            return

        async with self.file_lock:
            existing_data = []
            if os.path.exists(self.file_path) and os.path.getsize(self.file_path) > 0:
                async with aiofiles.open(self.file_path, 'r') as file:
                    try:
                        existing_data = json.loads(await file.read())
                    except json.JSONDecodeError:
                        existing_data = []

            existing_data.extend(self.domains_buffer)
            async with aiofiles.open(self.file_path, 'w') as file:
                # Додаємо відступи для форматування кожного об'єкта на новому рядку
                await file.write(json.dumps(existing_data, ensure_ascii=False, indent=4))

        self.domains_buffer = []


    def add_domain_to_buffer(self, domain):
        parsed_url = urlparse(domain)
        if not parsed_url.scheme:
            domain = 'http://' + domain  # Додавання протоколу "http", якщо він відсутній
        # Фільтрація доменів з нестандартними символами
        if not re.match(r'^https?://[a-zA-Z0-9.-]+$', domain):
            return
        if domain not in self.external_domains:
            self.external_domains.add(domain)
            self.domains_buffer.append({'domain': domain})  # Зберігання даних у форматі JSON
            if len(self.domains_buffer) >= self.buffer_size:
                self.executor.submit(asyncio.run, self.write_buffer_to_file())


    def parse(self, response):
        # Отримання всіх посилань на сторінці
        links = response.css('a::attr(href)').getall()

        for link in links:
            # Перевірка, чи посилання не належить до виключених шляхів
            if not any(link.startswith(excluded_path) for excluded_path in self.excluded_paths):
                # Якщо посилання веде на внутрішню сторінку Wikipedia, йдемо за ним
                if link.startswith('/wiki/'):
                    if link not in self.collected_domains:
                        self.collected_domains.add(link)
                        yield response.follow(link, self.parse)
                else:
                    parsed_url = urlparse(link)
                    domain = f"{parsed_url.scheme}://{parsed_url.netloc}"
                    if not any(word in domain.lower() for word in self.exclude_words):
                        self.add_domain_to_buffer(domain)

# Створення та запуск процесу
process = CrawlerProcess(settings=WikipediaDomainSpider.custom_settings)
process.crawl(WikipediaDomainSpider)
process.start()