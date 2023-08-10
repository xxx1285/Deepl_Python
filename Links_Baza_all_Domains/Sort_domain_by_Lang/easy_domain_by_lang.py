# Достаем язык сьраницы
import httpx
from bs4 import BeautifulSoup
from langdetect import detect
import asyncio

async def fetch_and_detect_language(url):
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        title_text = soup.title.string
        lang = detect(title_text)
        return lang

# Создаем новую сопрограмму и выполняем ее
url = "https://bdfeu.ukraine7.com/login"
loop = asyncio.get_event_loop()
language = loop.run_until_complete(fetch_and_detect_language(url))

print(language)