import os
import json
import random
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import pandas as pd
import io
from PIL import Image

from llama_cpp import Llama
from app.app_llama_v1 import app_llama


BASE_URL = "https://www.bis-m.ua"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
SAVE_RESULT_CSV = r"Parsing\Parsing_BisM\CSV\result5.csv"
BISM_IMAGES = r"Parsing\Parsing_BisM\images"

MODEL_LLAMA_PATH = "D://Gembling//Deepl_Python//Deepl_Python//llama//TheBloke//llama-2-7b-chat.Q5_K_S.gguf"
model_Llama = Llama(model_path=MODEL_LLAMA_PATH, n_ctx=2048)

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
        # Проверяем наличие прозрачности
        if image.mode in ("RGBA", "LA") or (image.mode == "P" and "transparency" in image.info):
            # Создаем новое изображение с белым фоном
            background = Image.new("RGB", image.size, (255, 255, 255))
            # Накладываем PNG изображение на фон
            background.paste(image, mask=image.split()[3])  # 3 - это альфа-канал
            background.save(save_path, 'JPEG')
        else:
            image.save(save_path, 'JPEG')


#############################################################################################
#  Llama Генератс
#############################################################################################
def check_and_update_text_game_Llama(model_Llama, title, text_game):
    for _ in range(3):
        text_game_Llama = app_llama(model_Llama, title, text_game)
        if len(text_game_Llama) > 150:
            break
    return text_game_Llama



# Асинхронная функция для парсинга данных товара
async def parse_item_data(session, url, semaphore):
    html = await fetch(session, url, semaphore)
    soup = BeautifulSoup(html, 'lxml')
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
    # NEW URL
    new_url = product_name + '-' + product_id

    # Получение и сохранение изображений
    image_links = soup.find_all('a', class_='lightbox jcepopup')
    image_filenames = []
    for idx, link in enumerate(image_links, start=1):
        image_url = link['href']
        image_name = f"image-{product_name}-{product_id}-{idx}.jpg"
        image_path = os.path.join(product_folder_path, image_name)
        await download_image(session, image_url, image_path)
        image_filenames.append(f"{product_name}/{image_name}")  # Добавляем путь к папке к имени файла

    img1 = image_filenames[0] if image_filenames else None
    img_all = json.dumps(image_filenames[1:]) if len(image_filenames) > 1 else json.dumps([])

    # Находим блок по его уникальному классу или id
    # block = soup.select_one('#comjshop > form > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(4) > div')
    block = soup.select_one('.jshop .block_efg')
    
    if block:
        extra_fields_elements = block.find_all('div', class_='extra_fields_el')
        random.shuffle(extra_fields_elements)  # Перемешиваем элементы
        technical_info = '\n'.join(element.get_text(strip=True) for element in extra_fields_elements)
        technical_info = technical_info.replace(":", ": ")
    else:
        technical_info = ''

    ai_text_Llama = check_and_update_text_game_Llama(model_Llama, title, technical_info)

    return {'product_id': product_id, 'category_id': category_id, 'title': title, 'price': price, 'img1': img1, 'img_all': img_all, 'technical_info': technical_info, 'ai_text_Llama': ai_text_Llama, 'bism_url': url, 'new_url': new_url}

# Асинхронный основной метод
async def main():
    async with aiohttp.ClientSession() as session:
        semaphore = asyncio.Semaphore(7)  # Ограничение в 5 одновременных запросов
        sections = await parse_section_links(session, f'{BASE_URL}/ru/katalog-bis-m', semaphore)


        products = []
        for section_url in sections:
            item_urls = await parse_items(session, section_url, semaphore)
            for url in item_urls:
                # if len(products) >= 3:
                    # break  # Прерываем внутренний цикл, если уже собрано 5
                data = await parse_item_data(session, url, semaphore)
                if data['img1']:
                    products.append(data)
                    print(f"Собраны данные: {data}")

        df = pd.DataFrame(products)
        df.to_csv(SAVE_RESULT_CSV, sep=';', index=False)
        print("Данные сохранены в файл 'catalog.csv'.")

# Запуск асинхронного кода
if __name__ == '__main__':
    asyncio.run(main())
