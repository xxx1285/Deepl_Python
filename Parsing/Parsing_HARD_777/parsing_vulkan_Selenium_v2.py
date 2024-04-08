
import re
import os
import time
import random
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
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
MY_DOMEIN = "1wix123.com"
#########################################
URL = "https://casino-vulkan24.top/"
BASE_FOLDER = r'D:\Gembling\Deepl_Python\Deepl_Python\Parsing\Parsing_site_Vulkan\klon_vulkan4'
USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15Z (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1 (Applebot/0.1)'
ABSOLUTE_URL_NEW_PATH = r"D:\Gembling\Deepl_Python\Deepl_Python\Parsing\Parsing_site_Vulkan\klon_vulkan4"

DOMAIN = re.search('(?<=://)([^/]+)', URL).group(1)

# Создаем драйвер
def create_mobile_driver():
    # Chrome Options
    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={USER_AGENT}")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=375,812")  # Разрешение iPhone 7
    # убираем надпись о Тестовом ПО в Браузере
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Chrome Service
    ser = Service(executable_path=r"D:\Gembling\Deepl_Python\Deepl_Python\SETTINGS\Chrome\122.0.6261.128\chromedriver.exe")
    driver = webdriver.Chrome(service=ser, options=chrome_options)
    # driver.maximize_window()

    return driver

# Удаляем скрипты аналитики, iframe блоки, чистим от символов не нужных
def remove_external_scripts(soup):
    start_time = time.time()
    stop_words = ["google", "gtag", "yandex", "clarity", "datpix"]
    for script in soup.find_all("script"):
        src = script.get("src")
        if src:
            for word in stop_words:
                if word in src:
                    script.decompose()
                    break
        elif any(word in script.get_text() for word in stop_words):
            script.decompose()
        # Удаление iframe блоков
    for iframe in soup.find_all("iframe"):
        iframe.decompose()
    for source in soup.find_all('source'):
        srcset = source.get('srcset')
        if srcset:
            # Удаляем все после символов '@', '?', '#'
            srcset_cleaned = re.sub(r'[@?#].*', '', srcset)
            # Удаляем подстроки из списка ['/rsimages']
            for substring in ['/rsimages']:
                srcset_cleaned = srcset_cleaned.replace(substring, '')
            source['srcset'] = srcset_cleaned
    # Удаляем все скрипты
    # for link in soup.find_all('link'):
    #     link_href = link.get('href')
    #     if '.js' in link_href:
    #         link.decompose()

    end_time = time.time()
    print(f"{remove_external_scripts.__name__} took {end_time - start_time} seconds to complete.")
    return soup

# Прокрутка страницы чтоб подгрузились елементы
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

    # Получаем все теги link и их href
    for link in driver.find_elements(By.TAG_NAME, 'link'):
        href = link.get_attribute('href')
        if href:
            resource_urls.add(urljoin(base_url, href))

    # Получаем все теги script и их src
    for script in driver.find_elements(By.TAG_NAME, 'script'):
        src = script.get_attribute('src')
        if src:
            resource_urls.add(urljoin(base_url, src))

    # Получаем все теги source и их src
    for source in driver.find_elements(By.TAG_NAME, 'source'):
        src = source.get_attribute('src')
        if src:
            resource_urls.add(urljoin(base_url, src))

    end_time = time.time()
    print(f"{get_resource_urls.__name__} took {end_time - start_time} seconds to complete.")
    return resource_urls

# Скачиваем файлы
def download_file(url, folder):
    start_time = time.time()
    try:
        response = requests.get(url, headers={"User-Agent": USER_AGENT})
        if response.status_code == 200:
            # Очистка URL от параметров запроса и получение имени файла
            filename = os.path.basename(urlparse(url).path.split('?')[0])
            # Если имя файла пустое, пропускаем без генерации (генерируем случайное имя)
            if not filename:
                # filename = os.urandom(8).hex() + '.resource'
                print(f"Empty filename for URL: {url}. Skipping...")
                return None
            # Если имя файла содержит '@', берем только часть до '@'
            filename = filename.split('@')[0]
            filepath = os.path.join(folder, filename)
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            end_time = time.time()
            print(f"{download_file.__name__} took {end_time - start_time} seconds to complete.")
            return filepath
        else:
            print(f"Failed to download file {url}: {response.status_code}")
            return None
    except Exception as e:
        print(f"Failed to download file {url}: {e}")
        return None

# Обновление путей в HTML чтоб открывалось 
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
        # Обновляем атрибуты data-*, которые могут содержать пути к ресурсам
        # for attr in tag.attrs:
        #     if attr.startswith('data-') and isinstance(tag[attr], str):
        #         tag[attr] = update_attribute_path(tag[attr], base_folder)
    end_time = time.time()
    print(f"{update_resource_paths.__name__} took {end_time - start_time} seconds to complete.")
    return soup


# Функция для загрузки страницы и ресурсов
def download_page(url, base_folder):
    driver = create_mobile_driver()
    driver.get(url)

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
    soup = remove_external_scripts(soup)
    # Обновляем пути ресурсов
    soup = update_resource_paths(soup, base_folder)

    # Получаем все ссылки на ресурсы на странице
    resource_urls = get_resource_urls(driver, url)

    # Сохраняем ресурсы и обновляем пути в HTML
    # for resource_url in resource_urls:
    #     local_path = download_file(resource_url, base_folder)
    #     if local_path:
    #         old_path = urlparse(resource_url).path
    #         new_path = os.path.relpath(local_path, base_folder).replace('\\', '/')
    #         page_content = page_content.replace(old_path, new_path)
    # Сохраняем ресурсы
    for resource_url in resource_urls:
        if DOMAIN in resource_url:
            parsed_url = urlparse(resource_url)
            resource_path = parsed_url.path
            local_path = resource_path.lstrip('/')
            local_full_path = os.path.join(base_folder, local_path)
            os.makedirs(os.path.dirname(local_full_path), exist_ok=True)
            full_path_file = download_file(resource_url, os.path.dirname(local_full_path))
            if full_path_file:
                old_path = urlparse(resource_url).path
                new_path = os.path.relpath(full_path_file, base_folder).replace('\\', '/')
                page_content = page_content.replace(old_path, new_path)

    print('page_content = page_content')
    # Заменяем все вхождения "casino-vulkan24.top" на "fgdfgdf.com" в HTML-контенте
    page_content = page_content.replace(DOMAIN, MY_DOMEIN)
    page_content = page_content.replace('async=""', 'async')

    # Сохраняем HTML-контент
    with open(os.path.join(base_folder, 'index.html'), 'w', encoding='utf-8') as f:
        # Добавляем DOCTYPE в начало файла
        f.write('<!DOCTYPE html>\n')
        f.write(str(soup))

    # Закрываем драйвер
    driver.quit()

if __name__ == "__main__":
    download_page(URL, BASE_FOLDER)