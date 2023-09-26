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
from urllib.parse import quote  # обробки URL-адрес з нестандартними символами


from system_lang_dict.dict__all_domain_zona import country_to_domain  # Импортируем словарь из другого файла
from proverka_robors_txt.proverka_robots_txt_v5 import is_url_indexed


# Обмежуємо кількість одночасних запитів до 5
semaphore = asyncio.Semaphore(30)


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
    Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.110 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)
    Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    }

    url = quote(url, safe=':/?&=')  # Закодувати URL-адрес з нестандартними символами

    async with semaphore:
        async with httpx.AsyncClient(verify=False, timeout=35.0) as client:
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

    index_results = await asyncio.gather(*[is_url_indexed(row['Domain'], row['URL']) for row in rows_chunk])

    with open(output_filename, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Domain', 'URL', 'Category', 'Lang_Prefix', 'Language', 'Country', 'Status_code', 'Indexing'])


        for (html_content, status), row, indexing_status in zip(results, rows_chunk, index_results):
            domain = row['Domain'].split('//')[-1].split('/')[0]
            tld = domain.split('.')[-1]
            country_from_dict = [k for k, v in country_to_domain.items() if v == tld]

            # Изменение тут: используем html_content вместо нового вызова fetch_html
            soup = BeautifulSoup(html_content, 'lxml')
            lang_country_element = soup.find('html')

            if lang_country_element:
                lang_country_str = lang_country_element.get('lang', '').replace('_', '-')
                parts = lang_country_str.split('-')
                
                if len(parts) >= 1:
                    row['Language'] = get_language_name(parts[0].lower())
                    row['Lang_Prefix'] = parts[0].lower()  # Сохраняем первые две буквы
                
                if country_from_dict:
                    row['Country'] = country_from_dict[0]
                elif len(parts) >= 2:
                    row['Country'] = get_country_name(parts[1].upper())

            row['Status_code'] = status
            row['Indexing'] = indexing_status
            writer.writerow(row)

    # Очистка переменных и вызов сборщика мусора
    del urls_chunk, rows_chunk
    gc.collect()


async def main():
    """
    Головна асинхронна функція.
    """
    input_filename = r"Linkbilding\3_Sort_csv_Url_Lang_Country_Robots\input\extracted_urls_3.csv"
    output_filename = r"Linkbilding\3_Sort_csv_Url_Lang_Country_Robots\output\result_urls_3_1.csv"

    # Створення заголовка вихідного файлу
    with open(output_filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Domain', 'URL', 'Category', 'Lang_Prefix', 'Language', 'Country', 'Status_code', 'Indexing'])
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
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_until_complete(bot.close())
