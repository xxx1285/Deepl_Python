import os
import json
import random
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import pandas as pd
import io
from PIL import Image


BASE_URL = "https://www.bis-m.ua"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
SAVE_RESULT_CSV = r"Parsing\Parsing_BisM\CSV\result7.csv"
BISM_IMAGES = r"Parsing\Parsing_BisM\images"

# Асинхронная функция для получения HTML контента
async def fetch(session, url, semaphore):
    async with semaphore, session.get(url, headers=HEADERS) as response:
        return await response.text()

# # Асинхронная функция для парсинга ссылок на подразделы
# async def parse_section_links(session, url, semaphore):
#     html = await fetch(session, url, semaphore)
#     soup = BeautifulSoup(html, 'html.parser')
#     links = soup.find_all('a', class_='product_link')
#     return [BASE_URL + link['href'] for link in links]

# Асинхронная функция для парсинга ссылок на подразделы
async def parse_section_links(session, url, semaphore):
    html = await fetch(session, url, semaphore)
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find_all('a', class_='product_link')
    return [(BASE_URL + link['href'], link.find('h5').text.strip()) for link in links]


# Асинхронная функция для парсинга товаров в подразделе
async def parse_items(session, url, semaphore):
    html = await fetch(session, url, semaphore)
    soup = BeautifulSoup(html, 'lxml')
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


# Асинхронная функция для парсинга данных товара
async def parse_item_data(session, url, semaphore, section_name):
    html = await fetch(session, url, semaphore)
    soup = BeautifulSoup(html, 'lxml')
    pagetitle = soup.find('h1').text.strip()
    price = soup.find('span', id='block_price').text.strip().split()[0]
    # LANG
    lang = soup.html.get('lang', '')
    if lang in ['ru', 'ru-RU', 'ru-ua']:
        lang = 'ru'
        context_key = 'ru'
        longtitle = pagetitle + ' Цена - ' + price + ' грн Купить в Киеве, фото, от производителя'
        description = 'Доставка &#128715; по Украине адресная в наличии на складе Киев Борисполь Одесса Механизм Еврокнижка Лучшее предложение на рынке ' + section_name
    else:
        lang = 'ua'
        context_key = 'web'
        longtitle = pagetitle + ' Ціна - ' + price + ' грн Купити Київ Бориспіль, від виробника'
        description = "Доставка &#128715; по Україні адресна в наявності на складі Київ Бориспіль Одеса Механізм Єврокнижка Краща пропозиція на ринку " + section_name
    # product_id
    product_id_input = soup.find('input', {'id': 'product_id'})
    product_id = product_id_input['value'] if product_id_input else 'Не найдено product_id'
    # category_id
    category_id_input = soup.find('input', {'id': 'category_id'})
    category_id = category_id_input['value'] if category_id_input else 'Не найдено category_id'
    # Извлечение последней части URL и создание папки
    product_name = url.rstrip('/').split('/')[-1]  # Получаем последнюю часть URL
    product_folder_path = os.path.join(BISM_IMAGES, product_id)
    os.makedirs(product_folder_path, exist_ok=True)  # Создаем папку, если ее нет
    # NEW URL
    new_url = product_name + '-' + product_id + '-' + lang
    # Shtrihcode
    shtrihcode = product_id + '-' + category_id

    # Получение и сохранение изображений
    image_links = soup.find_all('a', class_='lightbox jcepopup')
    image_filenames = []
    for idx, link in enumerate(image_links, start=1):
        image_url = link['href']
        # image_name = f"image-{product_name}-{product_id}-{idx}.jpg"
        image_name = image_url.rsplit('/', 1)[-1].rsplit('.', 1)[0] + ".jpg"
        image_path = os.path.join(product_folder_path, image_name)
        await download_image(session, image_url, image_path)
        image_filenames.append(image_name)

    image = image_filenames[0] if image_filenames else None
    # Создание JSON-структуры для img_all
    img_all_json = []
    for i, image_name in enumerate(image_filenames[1:], start=1):
        img_all_json.append({
            "MIGX_id": str(i),
            "description": f"{pagetitle} {i}",
            "image": f"assets/images/BisM/{product_id}/{image_name}"
        })

    image_galer_json = json.dumps(img_all_json, ensure_ascii=False)

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
    
    return {'lang': lang, 'context_key': context_key, 'category_id': category_id, 'section_name': section_name, 'product_id': product_id, 'shtrihcode': shtrihcode, 'pagetitle': pagetitle, 'longtitle': longtitle, 'description': description, 'price': price, 'image': image, 'image_galer_json': image_galer_json, 'technical_info': technical_info, 'bism_url': url, 'new_url': new_url}

# Асинхронный основной метод
async def main():
    async with aiohttp.ClientSession() as session:
        semaphore = asyncio.Semaphore(20)  # Ограничение в 5 одновременных запросов

        # Собираем разделы для RU
        sections_ru = await parse_section_links(session, f'{BASE_URL}/ru/katalog-bis-m', semaphore)
        # Собираем разделы для UA
        sections_ua = await parse_section_links(session, f'{BASE_URL}/ua/katalog-bis-m', semaphore)
        # Объединяем разделы
        all_sections = sections_ru + sections_ua

        products = []
        for section_url, section_name in all_sections:
            item_urls = await parse_items(session, section_url, semaphore)
            for url in item_urls: 
                # if len(products) >= 3:
                    # break  # Прерываем внутренний цикл, если уже собрано 5
                data = await parse_item_data(session, url, semaphore, section_name)
                if data['image']:
                    products.append(data)
                    print(f"Собраны данные: {data}")

        df = pd.DataFrame(products)
        df.to_csv(SAVE_RESULT_CSV, sep=';', index=False)
        print("Данные сохранены в файл 'catalog.csv'.")

# Запуск асинхронного кода
if __name__ == '__main__':
    asyncio.run(main())
