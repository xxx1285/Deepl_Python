import os
import re
import json
import time
import scrapy
from scrapy.crawler import CrawlerProcess
from urllib.parse import urlparse
from twisted.internet.error import TimeoutError, TCPTimedOutError
import asyncio
import aiofiles
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
import sys

sys.path.append('D:\\Gembling\\Deepl_Python\\Deepl_Python')
from Proxy.Restart_modem.E3372_Restart_control_clas_v1 import ModemController


# Глобальні змінні для зберігання зібраних URL-адрес
GLOBAL_COLLECTED_URLS = set()
GLOBAL_EXTERNAL_URLS = set()
# для зберігання URL, які потрібно відвідати
GLOBAL_PENDING_URLS = ['https://www.reddit.com/r/gaming/', 'https://www.reddit.com/t/minecraft/', 'https://www.reddit.com/t/the_real_housewives_of_atlanta/']

class ForbesUrlSpider(scrapy.Spider):
    name = 'reddit.com_1'   # ключ для пошуку внутрішніх сторінок по яким ходить паук
    allowed_urls = ['reddit.com']
    start_urls = GLOBAL_PENDING_URLS
    # start_urls = ['https://www.reddit.com/r/gaming/', 'https://www.reddit.com/search/?q=game&type=link&cId=989a24f8-7da1-4820-bede-beb5b9386ca8&iId=36d9e2f3-14d1-4665-bae8-adba1f439c6d',
    #               'https://www.reddit.com/t/minecraft/', 'https://www.reddit.com/t/the_real_housewives_of_atlanta/', 'https://www.reddit.com/t/nba/']
    custom_settings = {
        'DOWNLOAD_DELAY': 1,  # Затримка між запитами
        'CONCURRENT_REQUESTS_PER_URL': 25,  # Кількість одночасних запитів на один домен
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'HTTPCACHE_ENABLED': True,
        'COOKIES_ENABLED': False,
        'DOWNLOAD_TIMEOUT': 7,  # Таймаут на завантаження
    }
    exclude_words = ['wiki', 'google', 'forbes', '.gov', '.edu', 'livejournal', 'blogspot', 'wordpress', 'broadwayworld', 
                     'facebook', 'yandex', 'youtube', 'twitter', 'linkedin', 'lemonde', 'shopping'
                     '.ru', '.by', '.kz', '.uk', '.fr', '.it', '.lt', '.at', '.uz', '.jp', '.eu', '.pl', '.ch', '.cz', 
                     '.am', '.lv', '.de', '.az', '.us', '.ca', '.fi', '.no', '.hu'
                     ]  # Слова для виключення з посилань
    excluded_paths = ['/home_', 'account.', '#', '@', 'twitter-com.', 'translate.goog', 'redditinc', 'ads.']  # Шляхи, які потрібно виключити


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.file_path = 'D:\\Gembling\\Deepl_Python\\Deepl_Python\\Parsing\\Wikipedia\\JSON_Wiki_result\\reddit\\urls-reddit.com-v3.json'
        self.file_lock = asyncio.Lock()     # Блокування для синхронізації доступу до файлу
        self.urls_buffer = []            # Буфер для зберігання доменів перед записом у файл
        self.buffer_size = 20               # Максимальний розмір буфера
        self.collected_urls = GLOBAL_COLLECTED_URLS     # Множина для зберігання вже відвіданих доменів
        self.external_urls = GLOBAL_EXTERNAL_URLS       # Множина для зберігання зовнішніх доменів
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
                if 'reddit' in link:
                    if link not in self.collected_urls:
                        self.collected_urls.add(link)
                        GLOBAL_PENDING_URLS.add(link)
                        yield response.follow(link, self.parse)
                        GLOBAL_PENDING_URLS.clear()
                else:
                    parsed_url = urlparse(link)
                    url = f"{parsed_url.scheme}://{parsed_url.netloc}"
                    if not any(word in url.lower() for word in self.exclude_words):
                        self.add_url_to_buffer(url)



def run_spider():
    process = CrawlerProcess(settings=ForbesUrlSpider.custom_settings)
    process.crawl(ForbesUrlSpider)
    process.start()

def spider_with_modem_restart():
    while True:
        # Запускаємо павука у окремому процесі
        spider_process = multiprocessing.Process(target=run_spider)
        spider_process.start()
        spider_process.join(timeout=1000)  # Чекаємо 10 хвилин 600

        # Якщо павук все ще працює, примусово завершуємо процес
        if spider_process.is_alive():
            spider_process.terminate()
            spider_process.join()
            print("************   Якщо павук все ще працює, примусово завершуємо процес")

        # Виконуємо дії з перезапуску модему
        # Перезагрузка модема
        modem_controller = ModemController("http://192.168.8.1")
        modem_controller.main_restart()
        print("**********************************************************************")
        print("************   Модем перезагружен")
        print("**********************************************************************")

        # Даємо час для оновлення IP
        time.sleep(10)

if __name__ == "__main__":
    spider_with_modem_restart()