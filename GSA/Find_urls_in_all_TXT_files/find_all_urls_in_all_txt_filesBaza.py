import asyncio
import aiofiles
import os

FIND_URLS = ".ph/"
EXCLUDED_PATTERNS = ['?q=', '?url', '?http', '=http', '/http']

async def process_file(filename, output_file, semaphore):
    try:
        async with aiofiles.open(filename, 'r') as file:
            async for line in file:
                if FIND_URLS in line and not any(pattern in line for pattern in EXCLUDED_PATTERNS):
                    async with semaphore:
                        async with aiofiles.open(output_file, 'a') as out_file:
                            await out_file.write(line)
    except Exception as e:
        print(f"Error processing {filename}: {e}")

async def search_files(directory, output_file, semaphore):
    tasks = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            tasks.append(process_file(file_path, output_file, semaphore))
            if len(tasks) >= 10:
                await asyncio.gather(*tasks)
                tasks = []
    if tasks:
        await asyncio.gather(*tasks)

async def main():
    directory = r"D:\Gembling\GSA\GSA_site_list_Telegram_TEST\Verified"  # Укажите путь к каталогу
    output_file = r"GSA\Find_urls_in_all_TXT_files\output\output.txt"  # Укажите имя выходного файла
    semaphore = asyncio.Semaphore(10)
    async with aiofiles.open(output_file, 'w') as out_file:
        await out_file.write("")  # Очищаем содержимое файла перед началом записи
    await search_files(directory, output_file, semaphore)

if __name__ == "__main__":
    asyncio.run(main())
