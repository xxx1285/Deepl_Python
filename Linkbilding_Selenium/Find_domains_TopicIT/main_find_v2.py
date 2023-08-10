import ssl
import httpx
import asyncio
import os
# from urllib.parse import urlparse, urlunparse

# создайте семафор перед началом проверки доменов
semaphore = asyncio.Semaphore(25)  # ограничивает количество одновременно выполняющихся запросов до 50


async def get_status_and_content(url):
    try:
        timeout = httpx.Timeout(6.0)  # total timeout
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.get(url)
            # response = await client.get(url, follow_redirects=True)
            return response.status_code, response.text, url
    except (httpx.HTTPError, httpx.RequestError, ssl.SSLError, ssl.SSLCertVerificationError, httpx.TimeoutException) as err:
        print(f"Error {url}: {str(err)}")
        return None, "", url

async def check_domain(domain):
    async with semaphore:  # использование семафора для ограничения количества одновременно выполняющихся запросов
        for prefix in ('https://', 'http://'):
            url = f'{prefix}{domain}'
            status_code, content, valid_url = await get_status_and_content(url)
            if status_code == 200:
                if 'https://connect.topicit.net/' in content:
                    print(f"Found match in {url}")
                    return valid_url
                else:
                    _, content, valid_url = await get_status_and_content(url + "/login")
                    if 'https://connect.topicit.net/' in content:
                        print(f"Found match in {url}/admin")
                        return valid_url
        return None


async def process_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r') as f:
                print(filename)
                domains = f.read().splitlines()
                results = await asyncio.gather(*(check_domain(domain) for domain in domains))
                with open(r"Linkbilding_Selenium\Find_domains_TopicIT\valid_urls.txt", "a") as outfile:
                    for url in results:
                        if url:
                            outfile.write(url + '\n')

# Нинішній розділ
current_folder = os.path.basename(os.path.dirname(__file__))

directory = f'Linkbilding_Selenium\\{current_folder}\\del1' # Change to your directory

asyncio.run(process_files_in_directory(directory))
