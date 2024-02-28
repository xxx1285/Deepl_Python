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


class ForbesUrlSpider(scrapy.Spider):
    name = 'globo'
    allowed_urls = ['globo.com']
    start_urls = ['https://oglobo.globo.com/']
    custom_settings = {
        'DOWNLOAD_DELAY': 1,  # Затримка між запитами
        'CONCURRENT_REQUESTS_PER_URL': 25,  # Кількість одночасних запитів на один домен
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'HTTPCACHE_ENABLED': False,
        'COOKIES_ENABLED': False,
        'DOWNLOAD_TIMEOUT': 7,  # Таймаут на завантаження
    }
    exclude_words = ['wiki', 'google', 'forbes', '.gov', '.edu', 'livejournal', 'blogspot', 'wordpress', 'broadwayworld', 
                     'facebook', 'yandex', 'youtube', 'twitter', 'linkedin', 'lemonde', 'terra.com.br',
                     '.ru', '.by', '.kz', '.uk', '.fr', '.it', '.lt', '.at', '.uz', '.jp', '.eu', '.pl', '.ch', '.cz', 
                     '.am', '.lv', '.de', '.az', '.us', '.ca', '.fi', '.no', '.hu'
                     ]  # Слова для виключення з посилань
    excluded_paths = ['/home_', 'account.', '#', '@', 'twitter-com.', 'translate.goog', 'amazon.com']  # Шляхи, які потрібно виключити


    collected_urls = set()  # Множина для зберігання вже відвіданих доменів


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.file_path = 'D:\\Gembling\\Deepl_Python\\Deepl_Python\\Parsing\\Poisk-Dropov\\Brazil\\Result_JSON\\2-urls-globo.com-v1.json'
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


    def add_url_to_buffer(self, url, link):
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
            self.urls_buffer.append({'url': url, 'domain': domain_name, 'parce_link': link})  # Зберігання даних у форматі JSON
            if len(self.urls_buffer) >= self.buffer_size:
                self.executor.submit(asyncio.run, self.write_buffer_to_file())


    def parse(self, response):
        # Отримання всіх посилань на сторінці
        links = response.css('a::attr(href)').getall()

        for link in links:
            # Перевірка, чи посилання не належить до виключених шляхів
            if not any(link.startswith(excluded_path) for excluded_path in self.excluded_paths):
                # Якщо посилання веде на внутрішню сторінку Wikipedia, йдемо за ним
                if 'globo' in link:
                    if link not in self.collected_urls:
                        self.collected_urls.add(link)
                        yield response.follow(link, self.parse)
                else:
                    parsed_url = urlparse(link)
                    url = f"{parsed_url.scheme}://{parsed_url.netloc}"
                    if not any(word in url.lower() for word in self.exclude_words):
                        self.add_url_to_buffer(url, link)

# Створення та запуск процесу
process = CrawlerProcess(settings=ForbesUrlSpider.custom_settings)
process.crawl(ForbesUrlSpider)
process.start()