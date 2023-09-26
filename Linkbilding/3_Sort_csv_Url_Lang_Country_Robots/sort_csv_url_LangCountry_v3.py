import httpx
import csv
import json
import re
import os
import asyncio
import gc  # Для сборки мусора
from aiogram import Bot
from bs4 import BeautifulSoup
import pycountry

from system_lang_dict.dict__all_domain_zona import country_to_domain  # Импортируем словарь из другого файла


# Обмежуємо кількість одночасних запитів до 5
semaphore = asyncio.Semaphore(20)


################################################################
# TELEGRAM BOT
with open(r'SETTINGS\telegram_bot_tokens.json', 'r') as file:
    tokens = json.load(file)
TOKEN = tokens["telegram_bot_mypyscript018"]
bot = Bot(token=TOKEN)
CHANNEL_ID = '@mypyscript018'
async def send_message(text):
    await bot.send_message(chat_id=CHANNEL_ID, text=text)
################################################################


def get_language_name(lang_code):
    """
    Визначити мову за її кодом.
    """
    try:
        return pycountry.languages.get(alpha_2=lang_code).name
    except AttributeError:
        return lang_code
    
def get_country_name(country_code):
    """
    Визначити країну за її кодом.
    """
    try:
        return pycountry.countries.get(alpha_2=country_code).name
    except AttributeError:
        return country_code


async def fetch_html(url: str) -> (str, str):
    """
    Асинхронно завантажує HTML сторінку.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    async with semaphore:
        async with httpx.AsyncClient(timeout=15.0) as client:
            resp = None  # Ініціалізація resp тут
            try:
                resp = await client.get(url, headers=headers)
                await asyncio.sleep(1)
                resp.raise_for_status()  # Викликає помилку, якщо отриманий статус відповіді є помилковим
                return resp.text, "OK"
            except Exception as e:  # Обробка інших можливих помилок
                print(f"Помилка при завантаженні {url}. Помилка: {e}")
                if resp:
                    return "", resp.status_code
                else:
                    return "", "Error without response"


async def process_urls_chunk(urls_chunk, rows_chunk, output_filename):
    results = await asyncio.gather(*[fetch_html(url) for url in urls_chunk])

    with open(output_filename, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Domain', 'URL', 'Category', 'Language', 'Country', 'Status_code'])

        for (_, status), row in zip(results, rows_chunk):
            domain = row['Domain'].split('//')[-1].split('/')[0]
            tld = domain.split('.')[-1]
            country_from_dict = [k for k, v in country_to_domain.items() if v == tld]

            html, _ = await fetch_html(row['Domain'])
            soup = BeautifulSoup(html, 'lxml')
            lang_country_element = soup.find('html')

            if lang_country_element:
                lang_country_str = lang_country_element.get('lang', '').replace('_', '-')
                parts = lang_country_str.split('-')
                
                if len(parts) >= 1:
                    row['Language'] = get_language_name(parts[0].lower())
                
                if country_from_dict:
                    row['Country'] = country_from_dict[0]
                elif len(parts) >= 2:
                    row['Country'] = get_country_name(parts[1].upper())

            row['Status_code'] = status
            writer.writerow(row)
    # Очистка переменных и вызов сборщика мусора
    del urls_chunk, rows_chunk
    gc.collect()


async def main():
    """
    Головна асинхронна функція.
    """
    input_filename = r"Linkbilding\Async_sort_CSV_url_by_Lang\input\extracted_urls6.csv"
    output_filename = r"Linkbilding\Async_sort_CSV_url_by_Lang\output\result_urls6-3.csv"

    # Створення заголовка вихідного файлу
    with open(output_filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Domain', 'URL', 'Category', 'Language', 'Country', 'Status_code'])
        writer.writeheader()

    chunk_size = 20
    with open(input_filename, 'r') as f:
        reader = csv.DictReader(f)
        urls_chunk, rows_chunk = [], []

        for row in reader:
            urls_chunk.append(row['Domain'])
            rows_chunk.append(row)
            if len(urls_chunk) >= chunk_size:
                await process_urls_chunk(urls_chunk, rows_chunk, output_filename)
                urls_chunk, rows_chunk = [], []

        if urls_chunk:
            await process_urls_chunk(urls_chunk, rows_chunk, output_filename)
    
    # Telegram Povidomlennya
    current_file = os.path.basename(__file__)
    await send_message(text=f"SHEF VSE ZROBLENO - {current_file}")

if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(bot.close())
