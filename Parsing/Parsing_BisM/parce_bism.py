import os
import json
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import pandas as pd
import io
from PIL import Image


BASE_URL = "https://www.bis-m.ua"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
SAVE_RESULT_CSV = r"Parsing\Parsing_BisM\CSV\result.csv"
BISM_IMAGES = r"Parsing\Parsing_BisM\images"

# Асинхронная функция для получения HTML контента
async def fetch(session, url, semaphore):
    async with semaphore, session.get(url, headers=HEADERS) as response:
        return await response.text()

# Асинхронная функция для парсинга ссылок на подразделы
async def parse_section_links(session, url, semaphore):
    html = await fetch(session, url, semaphore)
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', class_='product_link')
    return [BASE_URL + link['href'] for link in links]

# Асинхронная функция для парсинга товаров в подразделе
async def parse_items(session, url, semaphore):
    html = await fetch(session, url, semaphore)
    soup = BeautifulSoup(html, 'html.parser')
    item_links = soup.find_all('div', class_='image_block')
    return [BASE_URL + link.a['href'] for link in item_links]

# Асинхронная функция для cкачивания и преобразования картинок
async def download_image(session, url, save_path):
    async with session.get(url) as response:
        image_data = await response.read()
        image = Image.open(io.BytesIO(image_data))
        if image.format != 'JPEG':
            image = image.convert('RGB')
        image.save(save_path, 'JPEG')

# Асинхронная функция для парсинга данных товара
async def parse_item_data(session, url, semaphore):
    html = await fetch(session, url, semaphore)
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h1').text.strip()
    price = soup.find('span', id='block_price').text.strip().split()[0]
    # product_id
    product_id_input = soup.find('input', {'id': 'product_id'})
    product_id = product_id_input['value'] if product_id_input else 'Не найдено product_id'
    # category_id
    category_id_input = soup.find('input', {'id': 'category_id'})
    category_id = category_id_input['value'] if category_id_input else 'Не найдено category_id'
    # Извлечение последней части URL и создание папки
    product_name = url.rstrip('/').split('/')[-1]  # Получаем последнюю часть URL
    product_folder_path = os.path.join(BISM_IMAGES, product_name)
    os.makedirs(product_folder_path, exist_ok=True)  # Создаем папку, если ее нет

    # Получение и сохранение изображений
    image_links = soup.find_all('a', class_='lightbox wfpopup wf-zoom-image')
    image_filenames = []
    for idx, link in enumerate(image_links, start=1):
        image_url = link['href']
        image_name = f"{product_name}-image-{idx}.jpg"
        image_path = os.path.join(product_folder_path, image_name)
        await download_image(session, image_url, image_path)
        image_filenames.append(f"{product_name}/{image_name}")  # Добавляем путь к папке к имени файла

    img1 = image_filenames[0] if image_filenames else None
    img_all = json.dumps(image_filenames[1:]) if len(image_filenames) > 1 else json.dumps([])

    return {'product_id': product_id, 'category_id': category_id, 'title': title, 'price': price, 'img1': img1, 'img_all': img_all}

# Асинхронный основной метод
async def main():
    async with aiohttp.ClientSession() as session:
        semaphore = asyncio.Semaphore(5)  # Ограничение в 5 одновременных запросов
        sections = await parse_section_links(session, f'{BASE_URL}/ru/katalog-bis-m', semaphore)


        products = []
        for section_url in sections:
            item_urls = await parse_items(session, section_url, semaphore)
            for url in item_urls:
                data = await parse_item_data(session, url, semaphore)
                products.append(data)
                print(f"Собраны данные: {data}")

        df = pd.DataFrame(products)
        df.to_csv(SAVE_RESULT_CSV, index=False)
        print("Данные сохранены в файл 'catalog.csv'.")

# Запуск асинхронного кода
if __name__ == '__main__':
    asyncio.run(main())
