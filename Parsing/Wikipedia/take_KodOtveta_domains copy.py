import asyncio
import aiohttp
import json
from aiohttp import TCPConnector
import socket


# Асинхронная функция для получения статуса ответа от сайта
async def fetch_status(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            return response.status
    except asyncio.TimeoutError:
        return "ERROR-TIME"
    except aiohttp.ClientConnectorError as e:
        if isinstance(e.os_error, socket.gaierror):
            print(f"{url}: ERROR-DNS {e}")
            return "ERROR-DNS"
        elif isinstance(e.os_error, OSError):
            if e.os_error.winerror == 64:
                print(f"{url}: ERROR-NETWORK-NAME-UNAVAILABLE {e}")
                return "ERROR-NETWORK-NAME-UNAVAILABLE"
            else:
                print(f"{url}: ERROR-CONNECT {e}")
                return "ERROR-CONNECT"
        else:
            return "ERROR-CONNECT"
    except Exception as e:
        print(f"Ошибка при запросе к {url}: {e}")
        return "ERROR"

# Основная асинхронная функция
async def main(json_file, output_folder):
    # Чтение JSON-файла для получения списка URL
    with open(json_file, 'r') as file:
        sites = json.load(file)

    # Настройки для игнорирования SSL ошибок и установки пользовательского агента
    connector = TCPConnector(ssl=False)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

    # Создаем сессию для асинхронных HTTP запросов
    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
        # Создаем список задач
        # tasks = [fetch_status(session, site['domain']) for site in sites]

        # доп перевірка на довжину та останній сивол в кінці
        tasks = []
        for site in sites:
            url = site['url']
            # Проверяем длину URL и последний символ
            if len(url) >= 15 and not url.endswith('.'):
                task = fetch_status(session, url)
                tasks.append(task)

        semaphore = asyncio.Semaphore(20)  # Ограничиваем количество одновременных задач

        async def sem_task(task):
            async with semaphore:
                return await task

        # Запускаем задачи с ограничением и собираем результаты
        statuses = await asyncio.gather(*(sem_task(task) for task in tasks))

        # Обработка кодов ответов и запись в файлы
        for status in set(statuses):
            # Создаем или дописываем файл для каждого статуса
            with open(f"{output_folder}/{status}.txt", 'a') as file:
                for url, url_status in zip(sites, statuses):
                    if url_status == status:
                        file.write(url['domain'] + '\n')

# Запуск асинхронного main
json_file = r'Parsing\Wikipedia\JSON_Wiki_result\test_2.json'
output_folder = r'Parsing\Wikipedia\kod_otveta_domains'
asyncio.run(main(json_file, output_folder))
