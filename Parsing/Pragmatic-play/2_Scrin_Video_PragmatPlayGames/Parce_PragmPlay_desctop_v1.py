# проверка Undetect браузер - https://whoer.net/ru

import os
import csv
import time
import random
import subprocess
import traceback
from PIL import Image, ImageDraw, ImageFont
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

from threading import Thread
from llama_cpp import Llama

# from app.app_video_screenRecorder_v3 import VideoRecorder

from app.app_perefraziruem_text_NLTK_SpaCy import paraphrase_with_spacy

from app.app_Llama_v1 import app_llama
# from app.app_previu_img_ON_img_v1 import overlay_images

MY_SITE_NAME = "1win"
MY_DOMAIN_VODYANOI_ZNAK = '1win1win.com'
base_path_del = os.path.dirname(os.path.abspath(__file__))

# URLS_SLOTS = r'VideoRec_from_SiteMonitor\output_PragmaticGames\output-urls-games2.txt'
URLS_SLOTS = r'Parsing\Pragmatic-play\2_Scrin_Video_PragmatPlayGames\input\output-urls-games-08-12-2023-v2.txt'
OUTPUT_GAMES_CSV = r"Parsing\Pragmatic-play\2_Scrin_Video_PragmatPlayGames\output\output-urls-games-14-02-2024-v2.csv"
FONT_PATH = "D://Gembling//Deepl_Python//Deepl_Python//Parsing//Pragmatic-play//2_Scrin_Video_PragmatPlayGames//fonts\ProtestRiot-Regular.ttf"


BASE_PATH = "Parsing/Pragmatic-play/ResultGames/games-v1/"

MODEL_LLAMA_PATH = "D://Gembling//Deepl_Python//Deepl_Python//llama//TheBloke//llama-2-7b-chat.Q5_K_S.gguf"
model_Llama = Llama(model_path=MODEL_LLAMA_PATH, n_ctx=2048)

# Замеряем мремя
start_time = time.time()


def create_folders(url_name_game):
    """
    Создание папок
    А так было:
        output_mp3_path = f"{folder_path}/audio/"
        if not os.path.exists(os.path.dirname(output_mp3_path)):
            os.makedirs(os.path.dirname(output_mp3_path))
    """
    folders = {
        "folder_path": f"{BASE_PATH}{url_name_game}",
        "scrin_images_path": f"{BASE_PATH}{url_name_game}/images/"
    }
    for path in folders.values():
        if not os.path.exists(path):
            os.makedirs(path)
    return folders


def add_watermarks(image_path, watermark_text, font_path, font_size=35, opacity=128, angle=15, spacing=300):
    # Открытие исходного изображения
    image = Image.open(image_path)
    img_width, img_height = image.size

    # Создание изображения для водяного знака
    watermark_image = Image.new('RGBA', image.size, (0, 0, 0, 0))
    watermark_draw = ImageDraw.Draw(watermark_image)

    # Загрузка шрифта
    font = ImageFont.truetype(font_path, font_size)

    # Добавление текста водяного знака на отдельное изображение
    for x in range(0, img_width, spacing):
        for y in range(0, img_height, spacing):
            watermark_draw.text((x, y), watermark_text, fill=(255, 255, 255, opacity), font=font)

    # Поворот изображения водяного знака
    watermark_image_rotated = watermark_image.rotate(angle, expand=1)

    # Создание маски для водяного знака
    mask = watermark_image_rotated.split()[3]

    # Наложение повернутого водяного знака на исходное изображение
    image.paste(watermark_image_rotated, (0, 0), mask)

    # Сохранение результата
    image.save(image_path, format='PNG')




# Клики с нажатием играть и скриншотами
def take_screenshots(driver, start_index, num_screenshots, x_to_play, y_to_play, url_name_game, scrin_images_path, crop_required=True):
    if not crop_required:
        success = True  # Флаг успешности операции
        try:
            # Просто конвертация в формат .JPG и накладка Превью картинки
            img_screenshot_path_glavn_png = f"{scrin_images_path}image-slot-{url_name_game}-0.png"
            driver.get_screenshot_as_file(img_screenshot_path_glavn_png)
            # Наложение водяных знаков
            add_watermarks(img_screenshot_path_glavn_png, MY_DOMAIN_VODYANOI_ZNAK, FONT_PATH)
            # Конвертация в JPEG
            image = Image.open(img_screenshot_path_glavn_png)
            img_screenshot_path_glavn_jpg = f"{scrin_images_path}image-slot-{url_name_game}-0.jpg"
            image.convert('RGB').save(img_screenshot_path_glavn_jpg, "JPEG", quality=70)
            # Удаление временного файла PNG
            os.remove(img_screenshot_path_glavn_png)
        except Exception as e:
            print(f"Ошибка при обработке изображения: {e}")
            success = False
    elif crop_required:
        success = True  # Флаг успешности операции
        for i in range(start_index, start_index + num_screenshots):
            try:
                # Сохранение скриншота с уникальным именем
                time.sleep(15)
                scrin_images_file_png = f"{scrin_images_path}image-slot-{url_name_game}-{i}.png"
                driver.get_screenshot_as_file(scrin_images_file_png)
                # Наложение водяных знаков
                add_watermarks(scrin_images_file_png, MY_DOMAIN_VODYANOI_ZNAK, FONT_PATH)
                # Открытие исходного изображения
                image = Image.open(scrin_images_file_png)

                # Обрезка изображения до 1024x576, если оно больше
                if image.width > 1024 or image.height > 576:
                    # Вычисление новых размеров, сохраняя пропорции
                    new_width = 1024
                    new_height = int((new_width / image.width) * image.height)
                    if new_height > 576:
                        new_height = 576
                        new_width = int((new_height / image.height) * image.width)

                    # Обрезка изображения
                    image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

                # Конвертация в JPEG
                scrin_images_file_jpg = f"{scrin_images_path}image-slot-{url_name_game}-{i}.jpg"
                image.convert('RGB').save(scrin_images_file_jpg, "JPEG", quality=60)
                # image.convert('RGB').save(img_screenshot_path, "WEBP", quality=30)

                # Удаление временного файла PNG
                os.remove(scrin_images_file_png)

                # Отправка нажатия клавиши пробел

                # # Добавление визуального маркера клика на страницу с помощью JavaScript
                # script = f"""
                # var body = document.querySelector('body');
                # var clickIndicator = document.createElement('div');
                # clickIndicator.style.position = 'absolute';
                # clickIndicator.style.left = '1500px';
                # clickIndicator.style.top = '950px';
                # clickIndicator.style.width = '15px';
                # clickIndicator.style.height = '15px';
                # clickIndicator.style.backgroundColor = 'green';
                # clickIndicator.style.zIndex = '10000';
                # body.appendChild(clickIndicator);
                # """
                # driver.execute_script(script)


                ActionChains(driver).send_keys(Keys.SPACE).perform()
                ActionChains(driver).send_keys(Keys.SPACE).perform()
                time.sleep(2)
                #######################################################
                #   Якщо пробіл не спрацював - то клікаємо
                #######################################################
                # Создание цепочки действий для клика
                actions = ActionChains(driver)
                actions.move_by_offset(1500, 950).click().perform()
                # Сброс положения курсора
                actions = ActionChains(driver)
                actions.move_by_offset(-1500, -950).perform()

                time.sleep(1)
            except Exception as e:
                print(f"Ошибка при обработке изображения: {e}")
                success = False
    return success



def open_urls_and_click_button(file_path):
    # Список пользовательских агентов
    user_agent = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        # Добавьте дополнительные пользовательские агенты по желанию
    ]

    # Chrome Options
    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={random.choice(user_agent)}")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--mute-audio")
    # убираем надпись о Тестовом ПО в Браузере
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Chrome Service
    ser = Service(executable_path=r"D:\Gembling\Deepl_Python\Deepl_Python\SETTINGS\Chrome\119.0.6045.105\chromedriver.exe")
    driver = webdriver.Chrome(service=ser, options=chrome_options)
    driver.maximize_window()


    # Reed all games from parce TXT file
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file.readlines()]

    # Создаем и открываем CSV файл для записи
    fieldnames = ['#', 'title_game', 'alias', 'text_game', 'text_game_Llama_1000_and_nachalo', 'iframe_url', 
                'image_0', 'image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6', 'url_original' 
                ]
    with open(OUTPUT_GAMES_CSV, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Эту строку нужно закомментировать - это заголовки которые при "a" не добавляются
        writer.writeheader()
        url_counter = 1

        for url in urls:
            try:
                driver.get(url)
                time.sleep(3)

                # BTN 18 Years
                try:
                    element = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="game_pop"]/div[3]/a[1]/span'))
                    )
                    element.click()
                except (TimeoutException, NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
                    pass

                # BTN Cookies close
                try:
                    driver.find_element(By.XPATH, '//*[@id="wt-cli-accept-all-btn"]').click()
                except (TimeoutException, NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
                    pass

                try:
                    # Название и Описание игры
                    title_game = driver.find_element(By.CLASS_NAME, "game-details__title").text
                    title_game = title_game.replace("™", "").replace("®", "")
                    text_game = driver.find_element(By.CLASS_NAME, "game-details__description").text
                    text_game = text_game.replace("™", "").replace("®", "")
                    url_name_game = url.strip('/').split('/')[-1]
                except (TimeoutException, NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
                    pass

                #############################################################################################
                #  Llama Генератс
                #############################################################################################
                def check_and_update_text_game_Llama(model_Llama, text_game):
                    for _ in range(3):
                        text_game_Llama = app_llama(model_Llama, text_game)
                        if len(text_game_Llama) > 150:
                            break
                    else:
                        text_game_NLTK = paraphrase_with_spacy(text_game)
                        text_game_Llama = text_game_NLTK
                    return text_game_Llama
                
                text_game_Llama = check_and_update_text_game_Llama(model_Llama, text_game)

                text_game_Llama_1000_and_nachalo = title_game + " on " + MY_SITE_NAME + "\n" + text_game_Llama[:930]

                # Инициализация каталогов
                folders = create_folders(url_name_game)
                scrin_images_path = folders['scrin_images_path']

                # Находим iframe DEMO Game
                try:
                    iframe = driver.find_element(By.ID, "iframe")
                    iframe_src = iframe.get_attribute("src")
                    if not iframe_src:  # якщо src є None або порожнім
                        iframe_src = iframe.get_attribute("data-src")
                    if iframe_src and iframe_src.startswith("http"):
                        driver.get(iframe_src)
                    else:
                        print(f"Недійсний URL iframe: {iframe_src}")
                        continue  # Пропустити цю ітерацію циклу
                    driver.fullscreen_window()
                    time.sleep(15)
                except InvalidArgumentException:
                    print(f"Невірний URL iframe, пропускаємо: {iframe_src}")
                    continue  # Пропустити цю ітерацію циклу


                #################################################################
                #   Скрин главной страницы для превью
                #################################################################
                # driver.maximize_window()
                # time.sleep(1)
                # driver.fullscreen_window()
                time.sleep(3)

                take_screenshots(driver, 0, 1, 0, 0, url_name_game, scrin_images_path, crop_required=False)

                x_to_click = 960
                y_to_click = 880

                # Создание цепочки действий для клика
                actions = ActionChains(driver)
                actions.move_by_offset(x_to_click, y_to_click).click().perform()
                # Сброс положения курсора
                actions = ActionChains(driver)
                actions.move_by_offset(-x_to_click, -y_to_click).perform()
                # Отправка нажатия клавиши пробел
                ActionChains(driver).send_keys(Keys.SPACE).perform()
                ActionChains(driver).send_keys(Keys.SPACE).perform()
                time.sleep(2)


                #################################################################
                #   PLAY BTN - igraem nazhimaya knopku
                #################################################################
                x_to_play = 0
                y_to_play = 0

                #################################################################
                # Робимо скріни та кліки по кнопці (driver, start_index, num_screenshots, x_to_play, y_to_play, url_name_game)
                #################################################################
                success = take_screenshots(driver, 1, 6, x_to_play, y_to_play, url_name_game, scrin_images_path, crop_required=True)
                if not success:
                    # Обработка ситуации, пропуск оставшейся части цикла
                    continue
                time.sleep(1)
                

                # Запись данных в CSV
                row_data = {
                    '#': url_counter,
                    'title_game': title_game,
                    'alias': url_name_game,
                    'text_game': text_game,
                    'text_game_Llama_1000_and_nachalo': text_game_Llama_1000_and_nachalo,
                    'iframe_url': iframe_src,
                    # Пути к изображениям (пример)
                    'image_0': f"{url_name_game}/images/image-slot-{url_name_game}-0.jpg",
                    'image_1': f"{url_name_game}/images/image-slot-{url_name_game}-1.jpg",
                    'image_2': f"{url_name_game}/images/image-slot-{url_name_game}-2.jpg",
                    'image_3': f"{url_name_game}/images/image-slot-{url_name_game}-3.jpg",
                    'image_4': f"{url_name_game}/images/image-slot-{url_name_game}-4.jpg",
                    'image_5': f"{url_name_game}/images/image-slot-{url_name_game}-5.jpg",
                    'image_6': f"{url_name_game}/images/image-slot-{url_name_game}-6.jpg",
                    'url_original': url  # Исходный URL
                }

                writer.writerow(row_data)
                csv_file.flush()  # Принудительная запись данных в файл
                url_counter += 1

                time.sleep(2)

                print(title_game)

                end_time = time.time()
                vremya_raboti = end_time - start_time
                print(vremya_raboti)



            except (TimeoutException, NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, InvalidArgumentException) as e:
                print(f"Ошибка при обработке URL {url}: {e}")
                traceback.print_exc()  # Печать полной трассировки стека

        driver.quit()


end_time = time.time()
vremya_raboti = end_time - start_time
print(vremya_raboti)


# Замените 'output-my.txt' на путь к вашему файлу и укажите правильный путь к текущей папке
open_urls_and_click_button(URLS_SLOTS)