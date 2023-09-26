"""
         реализована функциональность для проверки статуса кода 200 для списка доменов с протоколом "https://". 
         Также добавлена отправка уведомлений в Telegram по завершении работы.
"""

import json
import asyncio
import httpx
from aiogram import Bot
import aiofiles  # Для асинхронной работы с файлами

# Ограничение одновременных запросов до 20
semaphore = asyncio.Semaphore(20)

# Настройка Telegram бота
with open(r'SETTINGS\telegram_bot_tokens.json', 'r') as file:
    tokens = json.load(file)
TOKEN = tokens["telegram_bot_mypyscript018"]
bot = Bot(token=TOKEN)
CHANNEL_ID = '@mypyscript018'

async def send_message(text):
    await bot.send_message(chat_id=CHANNEL_ID, text=text)

# Функция для проверки статуса кода каждого домена
async def check_domain_status(domain, output_file):
    async with semaphore:
        url = f"https://{domain}"
        try:
            async with httpx.AsyncClient(timeout=4.0) as client:  # ограничение по времени в 5 секунд
                r = await client.get(url)
                if r.status_code == 200:
                    async with aiofiles.open(output_file, 'a') as f:
                        await f.write(f"{domain}\n")
        except Exception as e:
            pass  # пропускаем домены с ошибками

# Главная функция
async def main():
    output_file = r"Links_Chistim_na_200\output_txt\result_ru_domain_seo_vladimir.txt"
    # Очистка или создание файла для успешных доменов
    open(output_file, 'w').close()

    # Список доменов из файла
    with open(r'Links_Chistim_na_200\input_txt\ru_domain_ot_seo_vladimir.txt', 'r') as f:
        domains = f.read().strip().split("\n")
    
    # Создаем список задач
    tasks = [check_domain_status(domain, output_file) for domain in domains]
    
    # Выполняем задачи асинхронно и получаем результаты
    await asyncio.gather(*tasks)
    
    await send_message("SHEF VSE ZROBLENO - sort_csv_url_by_lang")

# Точка входа
if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(bot.close())
