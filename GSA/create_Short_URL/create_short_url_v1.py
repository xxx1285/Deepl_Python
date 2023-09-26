import csv
import asyncio
from datetime import datetime
import httpx
import random
from service_short_api import TINYURL, REBRANDLY, OWO

# Количество параллельных запросов
MAX_CONCURRENT_REQUESTS = 10

# Функция для сокращения URL-адреса с использованием API случайно выбранного сервиса
async def shorten_url(url, client, service_settings):

    selected_service = random.choice([TINYURL, REBRANDLY, OWO])

    

    # Отправляем POST-запрос к API выбранного сервиса
    response = await client.post(service_settings["base_url"], json=payload)

    # Проверяем статус-код ответа
    if response.status_code == 200:
        result = response.json()
        if "shortUrl" in result:
            return result["shortUrl"]  # Возвращаем сокращенный URL-адрес
    return None

# Основная функция для обработки URL и сохранения результатов в CSV
async def process_urls(input_file, output_file, service_settings):
    async with httpx.AsyncClient() as client:
        with open(input_file, "r") as file:
            urls = file.read().splitlines()

        data = []  # Список для хранения результатов

        async def process_url(url):
            nonlocal data
            # Сокращаем URL-адрес и добавляем результат в список
            shortened_url = await shorten_url(url, client, service_settings)
            if shortened_url:
                data.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), url, shortened_url])

        tasks = []  # Список для хранения задач

        for url in urls:
            if len(tasks) >= MAX_CONCURRENT_REQUESTS:
                # Асинхронно выполняем задачи, когда их достаточно
                await asyncio.gather(*tasks)
                tasks.clear()
            tasks.append(process_url(url))

        if tasks:
            # Завершаем оставшиеся задачи
            await asyncio.gather(*tasks)

        # Зберігаем данные в CSV-файл
        with open(output_file, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Дата", "Оригинальный URL", "Сокращенный URL"])
            csv_writer.writerows(data)

if __name__ == "__main__":
    input_file = "urls.txt"     # Укажите имя вашего файла с URL
    output_file = "output.csv"  # Укажите имя файла для результатов

    asyncio.run(process_urls(input_file, output_file))
