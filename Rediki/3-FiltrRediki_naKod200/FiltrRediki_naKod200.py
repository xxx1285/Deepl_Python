import aiohttp
import asyncio
import re
from aiohttp import ClientSession

async def fetch(url, session, redirect_count=0, original_url=None):
    if original_url is None:
        original_url = url  # Зберігаємо оригінальний URL при першому виклику

    try:
        # Виконуємо GET-запит до URL без перенаправлень
        async with session.get(url, allow_redirects=False) as response:
            # Перевіряємо код відповіді
            if response.status == 200:
                text = await response.text()
                # Шукаємо "777.com" в атрибутах href усіх посилань
                if re.search(r'href="[^"]*777\.com[^"]*"', text):
                    return original_url, 'accepted'
                else:
                    # Немає посилань на "777.com" на сторінці
                    return original_url, 'no 777.com link'
            elif response.status in [301, 302, 305, 307, 308]:
                if redirect_count < 6:  # Перевірка ліміту редиректів
                    new_url = response.headers.get('Location')
                    if new_url:
                        print(f"Редирект {url} до {new_url}")
                        return await fetch(new_url, session, redirect_count + 1, original_url)  # Інкрементуємо лічильник редиректів
                    else:
                        return original_url, 'redirect without location'
                else:
                    return original_url, 'redirect loop'  # Досягнуто ліміт редиректів
            else:
                # Код відповіді не відповідає нашим критеріям
                return original_url, f'unexpected status code {response.status}'
    except Exception as e:
        print(f"Помилка при запиті URL {url}: {e}")
        return original_url, 'error'

async def bound_fetch(sem, url, session):
    # Використовуємо семафор для обмеження кількості одночасних запитів
    async with sem:
        return await fetch(url, session)

async def run(urls):
    tasks = []
    # Обмежуємо кількість одночасних запитів до 10
    sem = asyncio.Semaphore(20)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
    conn = aiohttp.TCPConnector(ssl=False)  # Вимкнення перевірки SSL

    # Створюємо сесію aiohttp із вказаними заголовками
    async with ClientSession(headers=headers, connector=conn) as session:
        for url in urls:
            # Створюємо і додаємо завдання в список завдань
            task = asyncio.ensure_future(bound_fetch(sem, url, session))
            tasks.append(task)

        # Чекаємо завершення всіх запитів і фільтруємо відповіді
        responses = await asyncio.gather(*tasks)
        return responses

def read_urls_from_file(input_filename):
    # Читаємо URL з вхідного файлу
    with open(input_filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

def write_urls_to_file(urls, output_filename, rejected_filename):
    # Записуємо URL, що відповідають умовам, у вихідний файл
    # та URL, що не відповідають умовам, у файл із відхиленими URL
    with open(output_filename, 'w', encoding='utf-8') as accepted_file, \
         open(rejected_filename, 'w', encoding='utf-8') as rejected_file:
        for url, status in urls:
            if status == 'accepted':
                accepted_file.write(url + '\n')
            else:
                rejected_file.write(f"{url} - {status}\n")

if __name__ == "__main__":
    input_filename = r'GSA\FiltrRediki_naKod200\input\redici-3-res.txt'  # Замініть на шлях до вашого вхідного файлу
    output_filename = r'GSA\FiltrRediki_naKod200\output\redici-3-res-Good.txt'  # Замініть на шлях до вашого вихідного файлу для прийнятих URL
    rejected_filename = r'GSA\FiltrRediki_naKod200\output\redici-3-res-No.txt'  # Замініть на шлях до файлу для відхилених URL

    urls = read_urls_from_file(input_filename)

    loop = asyncio.get_event_loop()
    # Виконуємо асинхронну обробку URL
    result_urls = loop.run_until_complete(run(urls))

    # Записуємо результати у файли
    write_urls_to_file(result_urls, output_filename, rejected_filename)
