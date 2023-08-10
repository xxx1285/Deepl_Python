import ssl
import httpx
import asyncio
import os

# Создаём семафор для ограничения количества одновременно выполняющихся запросов до 20
semaphore = asyncio.Semaphore(10)  

class BufferedWriter:
    def __init__(self, filename, buffer_size):
        self.buffer = []  # Внутренний буфер для хранения URL
        self.filename = filename  # Имя файла для записи URL
        self.buffer_size = buffer_size  # Максимальный размер буфера

    # Метод для добавления URL в буфер и записи буфера в файл, если достигнут максимальный размер
    async def write(self, url):
        if url:
            self.buffer.append(url)
            if len(self.buffer) >= self.buffer_size:
                await self.flush()  # Очистка буфера и запись URL в файл

    # Метод для очистки буфера и записи URL в файл
    async def flush(self):
        with open(self.filename, "a") as outfile:
            for url in self.buffer:
                outfile.write(url + '\n')
        self.buffer = []  # Очистка буфера после записи в файл

# Асинхронная функция для получения статуса и содержимого URL
async def get_status_and_content(url):
    try:
        timeout = httpx.Timeout(6.0)  # Устанавливаем таймаут запроса
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.get(url)  # Выполняем запрос
            return response.status_code, response.text, url  # Возвращаем статус, содержимое и URL
    except (httpx.HTTPError, httpx.RequestError, httpx.InvalidURL, ssl.SSLError, ssl.SSLCertVerificationError, httpx.TimeoutException) as err:
        print(f"Error {url}: {str(err)}")
        return None, "", url  # В случае ошибки возвращаем None статус, пустое содержимое и URL

# Асинхронная функция для проверки домена
async def check_domain(domain, writer):
    async with semaphore:  # Используем семафор для ограничения одновременных запросов
        for prefix in ('https://', 'http://'):  # Проходим по обоим протоколам
            url = f'{prefix}{domain}'  # Формируем URL
            status_code, content, valid_url = await get_status_and_content(url)  # Получаем статус, содержимое и URL
            if status_code is not None and status_code == 200:  # Если статус 200 и не None
                if 'topicit.net' in content:  # Если нужная нам строка есть в содержимом
                    print(f"Found ==> {url}")
                    await writer.write(valid_url)  # Добавляем URL в буфер
                    return
                else:  # Если строка не найдена, проверяем другой URL
                    _, content, valid_url = await get_status_and_content(url + "/login")
                    if 'topicit.net' in content:
                        print(f"Found ==> {url}/login")
                        await writer.write(valid_url)
                        return

# Асинхронная функция для обработки файлов в директории
async def process_files_in_directory(directory):
    writer = BufferedWriter(r"Linkbilding_Selenium\Find_domains_TopicIT\valid_urls.txt", 5)  # Создаем экземпляр буферизованного писателя
    for filename in os.listdir(directory):  # Проходим по всем файлам в директории
        if filename.endswith(".txt"):  # Если файл имеет расширение .txt
            with open(os.path.join(directory, filename), 'r') as f:  # Открываем файл
                print(filename)
                domains = f.read().splitlines()  # Считываем домены
                # Запускаем проверку для каждого домена
                await asyncio.gather(*(check_domain(domain, writer) for domain in domains))

    await writer.flush()  # Записываем остаток буфера в файл

# Текущая папка
current_folder = os.path.basename(os.path.dirname(__file__))

directory = f'Linkbilding_Selenium\\{current_folder}\\del1' # Измените на вашу директорию

asyncio.run(process_files_in_directory(directory))  # Запускаем основную функцию
