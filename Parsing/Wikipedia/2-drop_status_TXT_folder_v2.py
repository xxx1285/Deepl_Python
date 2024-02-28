import asyncio
import aiohttp
import json
from aiohttp import TCPConnector
import socket
import whois
import re
import os


# Асинхронная функция для получения статуса ответа от сайта
async def fetch_status(session, url, domain):
    try:
        async with session.get(url, timeout=25) as response:
            # print(f"{url}: 200")
            return {"fetch_status": response.status}
    except asyncio.TimeoutError:
        print(f"{url}: ERROR-TIME")
        return {"fetch_status": "ERROR-TIME"}
    except aiohttp.ClientConnectorError as e:
        
        if isinstance(e.os_error, socket.gaierror):
            print(f"{url}: ERROR-DNS {e}")
            whois_domain_status = await whois_domain(domain)
            return {"fetch_status": "ERROR-DNS", "whois_domain_status": whois_domain_status}
        elif isinstance(e.os_error, OSError):
            whois_domain_status = await whois_domain(domain)
            if e.os_error.winerror == 64:
                print(f"{url}: ERROR-NETWORK-NAME-UNAVAILABLE {e}")
                return {"fetch_status": "ERROR-NETWORK-NAME-UNAVAILABLE", "whois_domain_status": whois_domain_status}
            else:
                print(f"{url}: ERROR-ClientConnectorError {e}")
                return {"fetch_status": "ERROR-ClientConnectorError", "whois_domain_status": whois_domain_status}
        else:
            return {"fetch_status": "ERROR-CONNECT"}
    except Exception as e:
        print(f"Ошибка при запросе к {url}: {e}")
        return {"fetch_status": "ERROR"}

async def main(folder_path, output_file):
    json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
    unique_domains = set()  # Множество для хранения уникальных доменов


    for json_file in json_files:
        full_path = os.path.join(folder_path, json_file)

        # Check if file is empty or invalid and handle it
        if os.stat(full_path).st_size == 0:
            print(f"File {json_file} is empty, skipping...")
            continue

        try:
            with open(full_path, 'r') as file:
                sites = json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error reading {json_file}: {e}")
            continue
        
        # (list comprehension
        # Очистка списка sites от элементов, не соответствующих условиям
        # filtered_sites = [site for site in sites if len(site['url']) >= 15 and not site['url'].endswith('.') and site['domain'].count('.') == 1]

        filtered_sites = [site for site in sites if 'url' in site and 'domain' in site and 
                          len(site['url']) >= 15 and not site['url'].endswith('.') and site['domain'].count('.') == 1]

        # Записываем уникальные домены в один txt-файл
        with open(output_file, 'w') as outfile:
            for domain in unique_domains:
                outfile.write(domain + '\n')

        connector = TCPConnector(ssl=False)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

        # Список для хранения сайтов с результатом "ERROR-DNS"
        error_dns_sites = []
        
        async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
            semaphore = asyncio.Semaphore(20)  # Ограничение количества одновременных задач
            tasks = []

            for site in filtered_sites:
                url = site['url']
                domain = site['domain']
                ######################################
                # url = site['domain']
                # domain = re.search(r"^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)", url)
                # if domain:
                #     domain = domain.group(1)
                # else:
                #     domain = url
                ##############################################
                task = sem_task(session, semaphore, url, domain)
                tasks.append(task)

            # Асинхронно выполняем все задачи и получаем результаты
            results = await asyncio.gather(*tasks)

            # Сопоставление URL со статусами и фильтрация
            for site, result in zip(filtered_sites, results):
                fetch_status = result.get("fetch_status")
                if fetch_status == "ERROR-DNS" or fetch_status == "ERROR-NETWORK-NAME-UNAVAILABLE" or fetch_status == "ERROR-ClientConnectorError":
                    # Если статус сайта равен "ERROR-DNS", добавляем его в список error_dns_sites
                    whois_domain_status = result.get("whois_domain_status")
                    if whois_domain_status == "FREE":
                        error_dns_sites.append({**site, **result})

            # Записываем результаты в новый JSON-файл
            with open(output_json, 'w') as outfile:
                # Форматирование данных в JSON и запись в файл
                json.dump(error_dns_sites, outfile, ensure_ascii=False, indent=4)

# Асинхронная функция, оборачивающая вызов fetch_status с использованием семафора
async def sem_task(session, semaphore, url, domain):
    async with semaphore:  # Ожидание доступности ресурса семафора
        # Вызов функции fetch_status и возвращение ее результата
        return await fetch_status(session, url, domain)
    
async def whois_domain(domain):
    try:
        w = whois.whois(domain)
        if w.status:
            return "Registration"
        else:
            return "FREE"
    except whois.parser.PywhoisError:
        return "FREE"
    except Exception as e:
        return "ERRORRR"

folder_path = r'Parsing\Wikipedia\New_Drops'  # Путь к исходному JSON-файлу
output_folder = r'Parsing\Wikipedia\New_Drops\res'  # Путь для нового JSON-файла
asyncio.run(main(folder_path, output_folder))