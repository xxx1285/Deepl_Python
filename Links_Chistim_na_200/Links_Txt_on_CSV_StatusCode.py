import json
import asyncio
import httpx
import aiofiles  # Для асинхронной работы с файлами
import csv


INPUT_URLS_TXT = r"D:\Gembling\Deepl_Python\Deepl_Python\SITEMAP\output\sitemap_url_onlyfans-models-sitemap1-2024-04-08.txt"
OUTPUT_URLS_STATUS_CODE_CSV = r"Links_Chistim_na_200\output_txt\sitemap_url_onlyfans-models-sitemap1-2024-04-08.csv"

# Ограничение одновременных запросов до 20
semaphore = asyncio.Semaphore(100)

# Функция для проверки статуса кода каждого домена
async def check_domain_status(url, output_file):
    async with semaphore:
        try:
            async with httpx.AsyncClient() as client:  # ограничение по времени в 5 секунд  httpx.AsyncClient(timeout=1.0)
                r = await client.get(url)
                status_code = r.status_code
                async with aiofiles.open(output_file, 'a') as f:
                    writer = csv.writer(f)
                    await writer.writerow([url, status_code])
        except Exception as e:
            pass  # пропускаем домены с ошибками

# Главная функция
async def main():
    # Список доменов из файла
    with open(INPUT_URLS_TXT, 'r') as f:
        domains = f.read().strip().split("\n")

    # Создаем список задач
    tasks = []
    count = 0
    async with aiofiles.open(OUTPUT_URLS_STATUS_CODE_CSV, 'w') as f:
        writer = csv.writer(f)
        await writer.writerow(["URL", "Status Code"])

        for domain in domains:
            tasks.append(check_domain_status(domain, OUTPUT_URLS_STATUS_CODE_CSV))
            count += 1

            # Записываем строки в CSV файл после каждых 1000 строк
            if count % 100 == 0:
                await asyncio.gather(*tasks)
                tasks = []  # Сбрасываем список задач

        # Записываем оставшиеся строки в CSV файл
        if tasks:
            await asyncio.gather(*tasks)

# Точка входа
if __name__ == "__main__":
    asyncio.run(main())
