import os
import asyncio
import aiofiles

# Глобальные переменные
INPUT_DIRECTORY = r'GSA\Clean_dublicate_URL\input'
OUTPUT_DIRECTORY = r'GSA\Clean_dublicate_URL\output'
MAX_CONCURRENT_TASKS = 5  # Ограничение на количество одновременных асинхронных задач
CHUNK_SIZE = 500000  # Количество строк для обработки за один раз

def extract_domain(url):
    start = url.find("://") + 3
    end = url.find("/", start)
    if end == -1:
        return url[start:]
    else:
        return url[start:end]

async def process_file_chunk(lines, seen_domains, output_file, duplicates_file):
    for line in lines:
        url = line.strip()
        domain = extract_domain(url)
        
        if domain not in seen_domains:
            seen_domains.add(domain)
            await output_file.write(url + '\n')
        else:
            await duplicates_file.write(url + '\n')

async def process_file(input_file_path, output_file_path, duplicates_file_path, semaphore):
    async with semaphore:
        seen_domains = set()
        async with aiofiles.open(input_file_path, 'r', encoding='utf-8', errors='ignore') as input_file, \
             aiofiles.open(output_file_path, 'w', encoding='utf-8') as output_file, \
             aiofiles.open(duplicates_file_path, 'w', encoding='utf-8') as duplicates_file:

            while True:
                lines = []
                for _ in range(CHUNK_SIZE):
                    line = await input_file.readline()
                    if not line:
                        break
                    lines.append(line)
                
                if not lines:
                    break
                
                await process_file_chunk(lines, seen_domains, output_file, duplicates_file)

async def process_files():
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.makedirs(OUTPUT_DIRECTORY)

    semaphore = asyncio.Semaphore(MAX_CONCURRENT_TASKS)
    tasks = []

    for filename in os.listdir(INPUT_DIRECTORY):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(INPUT_DIRECTORY, filename)
            output_filename = f"unique00_{filename}"
            duplicates_filename = f"duplicates00_{filename}"
            output_file_path = os.path.join(OUTPUT_DIRECTORY, output_filename)
            duplicates_file_path = os.path.join(OUTPUT_DIRECTORY, duplicates_filename)
            task = process_file(input_file_path, output_file_path, duplicates_file_path, semaphore)
            tasks.append(task)

    await asyncio.gather(*tasks)

async def main():
    await process_files()

if __name__ == "__main__":
    asyncio.run(main())