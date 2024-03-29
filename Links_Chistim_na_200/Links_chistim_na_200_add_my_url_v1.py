import os
import re
import asyncio  # Для асинхронного програмування
import httpx
from bs4 import BeautifulSoup
import aiofiles  # Для асинхронної роботи з файлами

# Установка SelectorEventLoop для Windows
# if os.name == 'nt':
#     loop = asyncio.SelectorEventLoop()
#     asyncio.set_event_loop(loop)


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

old_domain = "treatallergicdisorder.com"
new_domain = "dynamiteminergames.com"
# Створюємо семафор, який обмежує кількість одночасних асинхронних операцій до 5
semaphore = asyncio.Semaphore(21)

input_file = r"Links_Chistim_na_200\input_txt\redici_treatallergicdisorder_com.txt" 
output_file = f"Links_Chistim_na_200//output_txt//output_my_redik_a_{new_domain}.txt"
# Флаг для блокировки записи в файл
write_lock = asyncio.Lock()


# Функція для обробки окремого URL
async def check_links_and_save(url, output_file):
    # Використовуємо семафор для контролю одночасних завдань
    async with semaphore:
        try:
            # Створюємо асинхронний HTTP клієнт
            async with httpx.AsyncClient(timeout=10.0) as client:
                r = await client.get(url, headers=headers)  # Здійснюємо GET запит до URL

                # Якщо отримано відповідь 200 OK
                if r.status_code == 200:
                    # Парсимо HTML за допомогою BeautifulSoup
                    soup = BeautifulSoup(r.text, 'lxml')
                    # Знаходимо всі теги <a> на сторінці
                    anchors = soup.find_all('a')

                    # Перевіряємо кожний тег <a> на наявність "lion" у href
                    for a in anchors:
                        href = a.get('href', "")
                        if new_domain in href:
                            # Якщо "lion" знайдено в href, зберігаємо цей URL у вигляді {url}\n або <a href="..."></a> у вихідний файл
                            async with write_lock, aiofiles.open(output_file, 'a') as f:
                                # await f.write(f'{url}\n')
                                await f.write(f'<a href="{url}">{url}</a>\n')
                            # Прерываем цикл после первой успешной записи
                            break
        # Виведення помилки у випадку виникнення проблеми при обробці URL
        except Exception as e:
            print(f"Error processing {url}. Error: {e}")

# Функція для обробки файлу з URL
async def process_file(input_file , output_file):
    # Відкриваємо вхідний файл і читаємо всі URL
    with open(input_file, 'r') as file:
        urls = [line.replace(old_domain, new_domain).strip() for line in file.readlines()]

    # Створюємо список завдань для обробки кожного URL
    tasks = [check_links_and_save(url, output_file) for url in urls]

    # Виконуємо всі завдання асинхронно
    await asyncio.gather(*tasks)
    print("Ok-ALL")

# Запускаємо головну функцію, зазначивши шлях до вхідного та вихідного файлу
if __name__ == "__main__":
    asyncio.run(process_file(input_file, output_file))
    print("Vse - Ok")
