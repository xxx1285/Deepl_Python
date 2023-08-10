import asyncio
import httpx
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import pandas as pd

class AsyncParser:
    def __init__(self, max_req):
        # Инициализируем семафор с максимальным числом одновременных запросов, чтобы предотвратить перегрузку сервера.
        self.semaphore = asyncio.Semaphore(max_req)
        # Используем set (множества), чтобы избежать дубликатов при сохранении внутренних и внешних ссылок.
        self.internal_links = set()  
        self.external_links = set()

    async def fetch(self, url):
        # Используем наш семафор в этой асинхронной функции.
        async with self.semaphore:  
            async with httpx.AsyncClient() as client:
                try:
                    # Выполняем HTTP GET запрос к заданному URL.
                    response = await client.get(url)
                    return response
                except Exception as e:
                    print(f"An error occurred while fetching {url}.", e)
                    return

    async def parse_links(self, url):
        # Вызываем fetch для получения HTML страницы по указанному URL.
        response = await self.fetch(url)
        if response is None:
            return
        # Используем BeautifulSoup для парсинга HTML.
        soup = BeautifulSoup(response.text, 'html.parser')
        # Определяем базовый URL (без пути), чтобы понять, является ли ссылка внутренней или внешней.
        base_url = urlparse(url).scheme + '://' + urlparse(url).netloc
        for link in soup.find_all('a'):
            href = link.get('href')
            if href is not None:
                if base_url in href:
                    # Если ссылка является внутренней, сохраняем ее в self.internal_links.
                    self.internal_links.add(href)
                elif 'http' in href:
                    # Если ссылка является внешней, сохраняем ее в self.external_links.
                    self.external_links.add(href)

    async def parse_csv(self, file_path):
        # Используем pandas для чтения CSV файла.
        data = pd.read_csv(file_path)
        tasks = []
        for site in data['site']:
            # Для каждого сайта в CSV файле создаем задачу для парсинга ссылок.
            task = asyncio.ensure_future(self.parse_links(site))  
            tasks.append(task)
        # Ожидаем завершения всех задач перед тем, как продолжить.
        await asyncio.gather(*tasks)  

    async def write_links(self, file_path):
        with open(file_path, 'w', newline='') as f:
            writer = pd.writer(f)
            # Записываем все внешние ссылки в CSV файл.
            writer.writerows([link] for link in self.external_links)

async def main():
    # Создаем экземпляр нашего асинхронного парсера с максимальным количеством одновременных запросов, равным 5.
    parser = AsyncParser(5)
    # Парсим URL-ы из CSV файла и собираем внешние ссылки.
    await parser.parse_csv('websites.csv')
    # Записываем собранные внешние ссылки в новый CSV файл.
    await parser.write_links('external_links.csv')

if __name__ == "__main__":
    # Используем asyncio.run для запуска нашего асинхронного кода.
    asyncio.run(main())  



russian,spanish,polish,portuguese,french,indonesian,greek,german,turkish,hungarian,ukrainian,italian,romanian,bulgarian,finnish,estonian,lithuanian,latvian,dutch,czech,danish,japanese,norwegian,slovak,slovenian,swedish,azerbaijani,kazakh,arabic,uzbek