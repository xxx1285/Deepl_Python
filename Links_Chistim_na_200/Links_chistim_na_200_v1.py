import asyncio
import httpx
from bs4 import BeautifulSoup
import re

chto_ishem = "treatallergicdisorder"
MAX_CONCURRENT_REQUESTS = 7  # Максимальное количество одновременных запросов

async def fetch_url(session, url):
    try:
        response = await session.get(url)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(f"Error fetching URL {url}: {e}")
    return None


async def process_urls_batch(session, urls, output_file):
    tasks = [fetch_url(session, url) for url in urls]
    responses = await asyncio.gather(*tasks)
    
    for content, original_url in zip(responses, urls):
        if content:
            soup = BeautifulSoup(content, 'html.parser')
            for a_tag in soup.find_all('a'):
                href = a_tag.get('href')
                if href and chto_ishem in href:
                    output_file.write(f'<a href="{original_url}">{original_url}</a>\n')

async def main():
    async with httpx.AsyncClient() as session:
        with open(r'Links_Chistim_na_200\input_txt\input.txt', 'r') as input_file:
            # urls = [line.strip() for line in input_file if '<a' in line]
            urls = [re.search(r'href="([^"]+)"', line).group(1) for line in input_file if '<a' in line]
            
        with open(r'Links_Chistim_na_200\output_txt\outpu.txt', 'a') as output_file:
            for i in range(0, len(urls), MAX_CONCURRENT_REQUESTS):
                batch = urls[i:i + MAX_CONCURRENT_REQUESTS]
                await process_urls_batch(session, batch, output_file)

if __name__ == "__main__":
    asyncio.run(main())
