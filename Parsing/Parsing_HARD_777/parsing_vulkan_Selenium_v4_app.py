
import re
import os
import time
import random
import aiohttp
import aiofiles
import asyncio
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from unidecode import unidecode
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, \
                                        ElementClickInterceptedException, InvalidArgumentException
#########################################
from app.app_remove_scripts_symbols_other   import  app_remove_external_scripts

#########################################
#########################################
MY_DOMEIN = "1wix123.com"
# MY_DOMEIN = r'D:\Gembling\Deepl_Python\Deepl_Python\Parsing\Parsing_site_Vulkan\klon_vulkan5'
#########################################
# Старт url для парсинга
#########################################
URLS_SITE_PARSING_TXT = r'Parsing\Parsing_HARD_777\input_urls\allurls.txt'
URL = "https://aqua-park.kz/"
# URL = "https://casino-vulkan24.top/"
DOMAIN = re.search('(?<=://)([^/]+)', URL).group(1)
#########################################
# Куда сохраняем
#########################################
BASE_FOLDER = r'D:\Gembling\Deepl_Python\Deepl_Python\Parsing\Parsing_HARD_777\output_parse_sites\klon_aqua-park_1'
#########################################
USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15Z (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1 (Applebot/0.1)'
#########################################
# Каталог для сохранения изображений с сети
FILES_WWW = 'images-www'
FILES_EXTENSIONS = ['png', 'jpg', 'jpeg', 'webp', 'gif', 'svg', 'ico', 'css', 'js']


# Создаем драйвер
def create_mobile_driver():
    # Chrome Options
    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={USER_AGENT}")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=375,812")  # Разрешение iPhone 7
    # chrome_options.add_argument("--headless")  # Запуск Chrome в безголовом режиме
    # Отключение автоматических редиректов
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--disable-site-isolation-trials')
    # убираем надпись о Тестовом ПО в Браузере
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Chrome Service
    ser = Service(executable_path=r"D:\Gembling\Deepl_Python\Deepl_Python\SETTINGS\Chrome\122.0.6261.128\chromedriver.exe")
    driver = webdriver.Chrome(service=ser, options=chrome_options)
    # driver.maximize_window()

    return driver

# УДАЛЯЕМ все пустые каталоги вкнце
def remove_empty_directories(directory):
    for dirpath, dirnames, filenames in os.walk(directory, topdown=False):
        for dirname in dirnames:
            dir_full_path = os.path.join(dirpath, dirname)
            if not os.listdir(dir_full_path):
                print(f"Removing empty directory: {dir_full_path}")
                os.rmdir(dir_full_path)

# Прокрутка страницы чтоб подгрузились елементы Вниз и ВВерх
def scroll_to_bottom(driver):
    ######################################################################################
    # Прокручуємо сторінку вниз або не більше 7 секунд
    ######################################################################################
    time.sleep(5)
    current_scroll_position, new_height= 0, 7
    speed = 50
    start_time = time.time()
    while current_scroll_position <= new_height:
        if time.time() - start_time > 7:  # если прошло более 2 секунд, выходим из цикла
            break
        current_scroll_position += speed
        driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
        new_height = driver.execute_script("return document.body.scrollHeight")
        time.sleep(0.05)
    # Возвращаемся обратно в самый верх страницы
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)


# Получаем ссылки на ресурсы
def get_resource_urls(driver, base_url):
    start_time = time.time()
    resource_urls = set()

    # Регулярное выражение для удаления хвостов URL-адресов
    tail_pattern = re.compile(r'[#@?].*$')

    # Получаем все теги img и их src и srcset
    for img in driver.find_elements(By.TAG_NAME, 'img'):
        src = img.get_attribute('src')
        if src:
            resource_urls.add(urljoin(base_url, src))
        srcset = img.get_attribute('srcset')
        if srcset:
            # Разбиваем srcset на отдельные ссылки и добавляем их
            parts = srcset.split(',')
            for part in parts:
                src_url = part.strip().split(' ')[0]
                resource_urls.add(urljoin(base_url, src_url))
    
    # Словарь соответствия между тегом и его атрибутом для URL
    tag_attribute_mapping = {
        'link': 'href',
        'script': 'src',
        'source': 'src',
        'use': 'xlink:href'
    }

    for tag_name, attr_name in tag_attribute_mapping.items():
        elements = driver.find_elements(By.TAG_NAME, tag_name)
        
        for element in elements:
            attr_value = element.get_attribute(attr_name)
            if attr_value:
                # чистим от хвостов
                cleaned_url = re.sub(tail_pattern, '', attr_value)
                resource_urls.add(urljoin(base_url, cleaned_url))

    # Регулярное выражение для проверки расширений
    allowed_extensions = ['png', 'jpg', 'jpeg', 'webp', 'gif', 'svg', 'ico', 'js', 'css']
    resource_urls = [url for url in resource_urls if any(url.endswith(ext) for ext in allowed_extensions)]

    end_time = time.time()
    print(f"{get_resource_urls.__name__} took {end_time - start_time} seconds to complete.")
    return resource_urls
#############################################################
# Транслитерация названия файлов
############################################################# 
def transliter_resource_name(resource_url):
    # Транслитерация символов и букв в названии файлов
    filename_resource = os.path.basename(urlparse(resource_url).path.split('?')[0])
    filename_resource_decode = unidecode(filename_resource)
    filename_resource_decode = re.sub(r'[^\w.-]', '0', filename_resource_decode)
    return filename_resource_decode
#############################################################
# Ограничение асинхронного скачивания и записи файлов до 10
############################################################# 
# semaphore = asyncio.Semaphore(5)
#############################################################
# Скачиваем асинхронно файлы
############################################################# 
def download_file_async(url, folder, transliter_name_file):
    try:
        response = requests.get(url, headers={'User-Agent': USER_AGENT})
        if response.status_code == 200:
            # Очистка URL от параметров запроса и получение имени файла
            file_extension = os.path.splitext(transliter_name_file)[1]
            
            # Проверяем, является ли расширение запрещенным
            forbidden_extensions = [".webmanifest", ".pdf", ".apk"]  # Добавьте сюда нужные расширения
            if file_extension in forbidden_extensions:
                print(f"Skipping download of file with forbidden extension: {transliter_name_file}")
                return None
            # Если имя файла пустое, пропускаем без генерации (генерируем случайное имя)
            if not transliter_name_file:
                print(f"Empty transliter_name_file for URL: {url}. Skipping...")
                return None
            # Если содержит '@', берем только часть до '@'
            folder = folder.split('@')[0]
            # filepath = os.path.join(folder, transliter_name_file)
            # with aiofiles.open(folder, 'wb') as f:
            #     for chunk in response.content.iter_any():
            #         await f.write(chunk)
            with open(folder, 'wb') as f:
                f.write(response.content)
            return folder
        else:
            print(f"Failed to download file {url}: {response.status_code}")
            return None
    except Exception as e:
        print(f"Failed to download file {url}: {e}")
        return None

#############################################################
# Обновление путей в HTML чтоб открывалось на компе !!!!!!!!!
############################################################# 
def update_resource_paths(soup, base_folder):
    start_time = time.time()
    
    def update_attribute_path(attribute_value, base_folder):
        if not attribute_value.startswith('http') and not attribute_value.startswith('//'):
            resource_path = urlparse(attribute_value).path
            resource_path, extension = os.path.splitext(resource_path)
            absolute_path = os.path.join(base_folder, resource_path.lstrip('/')) + extension
            return absolute_path.replace('\\', '/')
        return attribute_value
    
    for tag in soup.find_all(True):
        # Обновляем атрибут src
        if tag.has_attr('src'):
            tag['src'] = update_attribute_path(tag['src'], base_folder)

        if tag.has_attr('srcset'):
            tag['srcset'] = update_attribute_path(tag['srcset'], base_folder)

        # Обновляем атрибут href
        href_tags = ['link']
        if tag.name in href_tags and tag.has_attr('href'):
            tag['href'] = update_attribute_path(tag['href'], base_folder)

        # Обновляем атрибут srcset для изображений
        if tag.name == 'img' and tag.has_attr('srcset'):
            updated_srcset = []
            for srcset_part in tag['srcset'].split(','):
                srcset_url, *descriptor = srcset_part.strip().split(' ', 1)
                updated_srcset_url = update_attribute_path(srcset_url, base_folder)
                updated_srcset.append(f"{updated_srcset_url} {' '.join(descriptor)}")
            tag['srcset'] = ', '.join(updated_srcset)

        # Обновляем стили с URL
        if tag.has_attr('style'):
            style_value = tag['style']
            updated_style = re.sub(r'url\(([^)]+)\)', lambda match: f'url({update_attribute_path(match.group(1), base_folder)})', style_value)
            tag['style'] = updated_style

        # Обновляем стили с URL
        if tag.has_attr('style'):
            style_value = tag['style']
            # Используйте модифицированную версию регулярного выражения для обработки кавычек
            updated_style = re.sub(r'url\((["\']?)([^)"\']+)\1\)', 
                           lambda match: f'url("{update_attribute_path(match.group(2), base_folder)}")', 
                           style_value)
            tag['style'] = updated_style

    end_time = time.time()
    print(f"{update_resource_paths.__name__} took {end_time - start_time} seconds to complete.")
    return soup
#############################################################
#############################################################
# Функция для получения имени файла из URL с учетом вложенности страниц
def get_filename_from_url(url):
    parsed_url = urlparse(url)
    if parsed_url.path in ['', '/']:
        return 'index.html'
    else:
        # Разделяем путь на компоненты
        path_components = parsed_url.path.strip('/').split('/')
        # Если путь содержит один компонент, это конечный адрес страницы
        if len(path_components) == 1:
            filename = path_components[-1].replace('.html', '') + '.html'
        # В противном случае, это вложенная страница и требуется создать каталоги
        else:
            # Первый компонент всегда корневой каталог
            directory = path_components[0]
            # Создаем итератор для последовательности каталогов
            directories = iter(path_components[:-1])
            # Пропускаем первый компонент, так как это корневой каталог
            next(directories)
            # Перебираем оставшиеся компоненты, создавая каталоги
            for dir_name in directories:
                directory = os.path.join(directory, dir_name)
                os.makedirs(directory, exist_ok=True)
            # Имя файла будет равно последнему компоненту пути
            filename = path_components[-1].replace('.html', '') + '.html'
            # Добавляем в имя файла путь к каталогу
            filename = os.path.join(directory, filename)
        return filename
#############################################################
############################################################# 
# Функция для загрузки страницы и ресурсов
def download_page_async(driver, url, base_folder, filename):

    if url.endswith(('.apk', '.app', '.xml', '.php')):
        print(f"Skipping page {url} due to file extension")
        return
    
    response = requests.get(url, headers={'User-Agent': USER_AGENT})
    if response.status_code != 200:
        print(f"Skipping page {url} due to non-200 status code")
        return
        
    driver.get(url)

    # Предотвращение редиректов с помощью JavaScript
    driver.execute_script("window.stop();")

    # Ожидание загрузки страницы
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    except TimeoutException:
        print("Timed out waiting for page to load")
        driver.quit()
        return
    
    # Прокрутка страницы до конца
    scroll_to_bottom(driver)
    time.sleep(4)

    # Получаем содержимое страницы
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'lxml')
    soup = app_remove_external_scripts(soup)
    # Обновляем пути ресурсов
    soup = update_resource_paths(soup, base_folder)
    


    # Получаем все ссылки на ресурсы на странице
    resource_urls = get_resource_urls(driver, url)

    # Создаем асинхронные задачи для скачивания файлов и обновления путей в HTML
    tasks = []
    urls_www = {}

    for resource_url in resource_urls:
        parsed_url = urlparse(resource_url)
        if DOMAIN not in resource_url and parsed_url.path.split('.')[-1] in FILES_EXTENSIONS:
            # если ссылки на внешние ресурсы тогда сохранить ...
            transliter_name_file = transliter_resource_name(resource_url)
            local_path = os.path.join(FILES_WWW, transliter_name_file)
            # local_full_path = os.path.join(base_folder, local_path)
            local_full_path = os.path.join(base_folder, local_path)
            urls_www[resource_url] = local_path
        elif DOMAIN in resource_url:
            transliter_name_file = transliter_resource_name(resource_url)
            resource_path = parsed_url.path
            local_path = resource_path.lstrip('/')
            old_filename = os.path.basename(local_path)
            local_path = local_path.replace(old_filename, transliter_name_file)
            local_full_path = os.path.join(base_folder, local_path)
            urls_www[resource_url] = local_path
        else:
            continue
        

        os.makedirs(os.path.dirname(local_full_path), exist_ok=True)
        download_file_async(resource_url, local_full_path, transliter_name_file )

    # Обновляем пути в HTML (ЛОКАЛЬНЫЕ АДРЕСА НА КОМПЕ)
    # for resource_url, local_file in zip(resource_urls, downloaded_files):
    #     if DOMAIN in resource_url and local_file:
    #         old_path = urlparse(resource_url).path
    #         new_path = os.path.relpath(local_file, base_folder).replace('\\', '/')
    #         page_content = page_content.replace(old_path, new_path)

    # Заменяем вхождения в HTML-контенте
    page_content = str(soup)
    for key, value in urls_www.items():
        # Заменяем внешние ссылки на ресурсы внутренними скаченными адресами
        page_content = page_content.replace(key, value)
    page_content = page_content.replace('async=""', 'async')
    page_content = page_content.replace(DOMAIN, MY_DOMEIN)

    # Создаем каталоги и папки для html структуры
    local_full_html_path = os.path.join(base_folder, filename)
    os.makedirs(os.path.dirname(local_full_html_path), exist_ok=True)
    # Сохраняем HTML-контент

    with open(local_full_html_path, 'w', encoding='utf-8') as f:
        # Добавляем DOCTYPE в начало файла
        f.write('<!DOCTYPE html>\n')
        f.write(page_content)
        # Явно закрываем файл
        f.close()
        # f.write(str(soup))




# Функция для чтения URL-адресов из файла
def read_urls_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]
    
def main():
        # Получаем список URL-адресов из файла
        urls_to_parse = read_urls_from_file(URLS_SITE_PARSING_TXT)

        driver = create_mobile_driver()

        for url in urls_to_parse:
            filename = get_filename_from_url(url)
            download_page_async(driver, url, BASE_FOLDER, filename)


        # Закрываем драйвер
        driver.quit()
        # Удаляем все пустые каталоги
        remove_empty_directories(BASE_FOLDER)

# # Запуск асинхронного приложения
# asyncio.run(main())
if __name__ == "__main__":
    main()