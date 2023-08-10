import asyncio
import httpx
from bs4 import BeautifulSoup
import re
import os
import urllib.parse
import langid

# Задайте пределы для анализа сайта
MAX_OUTBOUND_LINKS = 50
MIN_TEXT_LENGTH = 200
CONCURRENT_LIMIT = 10  

# Визначаємо назву поточної директорії
current_folder = os.path.basename(os.path.dirname(__file__))

# Функция для парсинга контента страницы
async def analyze_site(semaphore, client, url):
    async with semaphore:  
        try:
            r = await client.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')

            # Извлечение домена из URL
            netloc = urllib.parse.urlparse(url).netloc

            # Проверка на спам:
            # 1. Количество внешних ссылок (может быть признаком спама)
            outbound_links = [a['href'] for a in soup.find_all('a', href=True) 
                            if urllib.parse.urlparse(a['href']).netloc != netloc]
            # 2. Количество слов в тексте страницы (слишком мало может быть признаком недостаточного содержания)
            text_content = re.findall(r'\b\w+\b', soup.get_text())

            # Если сайт кажется хорошим для обратной ссылки, определяем язык первых 100 символов
            if len(outbound_links) < MAX_OUTBOUND_LINKS and len(text_content) > MIN_TEXT_LENGTH:
                language = langid.classify(soup.get_text()[:100])[0]
                print(f"{language}_{url}")
                # Записываем URL в файл в зависимости от определенного языка
                with open(f'{current_folder}\\result\\{language}_urls.txt', 'a') as f:
                    f.write(url + '\n')

        except Exception as e:
            print(f"Error while analyzing {url}: {str(e)}")

# Основная функция
async def main():
    semaphore = asyncio.Semaphore(CONCURRENT_LIMIT)  # Создаем семафор
    async with httpx.AsyncClient(timeout=30.0) as client:

        # Получение списка файлов в директории
        files = os.listdir(f"{current_folder}\\proverit")

        for file in files:
            # Проверяем, что это текстовый файл
            if file.endswith('.txt'):
                # Получение списка URL из файла
                with open(f"{current_folder}\\proverit\\{file}", "r") as file:
                    urls = [line.strip() for line in file]

                tasks = (analyze_site(semaphore, client, url) for url in urls)
                await asyncio.gather(*tasks)

# Запуск асинхронного цикла событий
asyncio.run(main())
