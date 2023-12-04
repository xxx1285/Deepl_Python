# проверка Undetect браузер - https://whoer.net/ru

import os
import csv
import time
import random
import subprocess
import traceback
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, \
                                        ElementClickInterceptedException, InvalidArgumentException

from threading import Thread
from app.app_video_screenRecorder_v3 import VideoRecorder
from app.app_audioText_on_audioMUS_v1 import audioTextSpeach_on_audioMusic
from app.app_delete_old_BIG_video import delete_files_from_list
from app.app_perefraziruem_text_NLTK_SpaCy import paraphrase_with_spacy

MY_SITE_NAME = "1win1win.com"

# URLS_SLOTS = r'VideoRec_from_SiteMonitor\output_PragmaticGames\output-urls-games2.txt'
URLS_SLOTS = r'VideoRec_from_SiteMonitor\2_Scrin_Video_PragmatPlayGames\input\output-urls-games-02-12-2023.txt'
OUTPUT_GAMES_CSV = "VideoRec_from_SiteMonitor/output_PragmaticGames/output_games3.csv"


BASE_PATH = "VideoRec_from_SiteMonitor/output_PragmaticGames/games-v2/"
BG_MUS_NO_AUTHOR = "D:\\Gembling\\Deepl_Python\\Deepl_Python\\SETTINGS\\Music-no-author"

LIST_VIDEO_TO_DELETE = r"VideoRec_from_SiteMonitor\2_Scrin_Video_PragmatPlayGames\output\video_to_delete.txt"
BASE_PATH_LIST_VIDEO_TO_DEL = "D://Gembling//Deepl_Python//Deepl_Python//"



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
        "video_path": f"{BASE_PATH}{url_name_game}/video",
        "scrin_images_path": f"{BASE_PATH}{url_name_game}/images/",
        "audio_path": f"{BASE_PATH}{url_name_game}/audio/"
    }
    for path in folders.values():
        if not os.path.exists(path):
            os.makedirs(path)
    return folders


# Клики с нажатием играть и скриншотами
def take_screenshots(driver, start_index, num_screenshots, x_to_play, y_to_play, url_name_game, scrin_images_path, crop_required=True):
    success = True  # Флаг успешности операции
    for i in range(start_index, start_index + num_screenshots):
    # 30 раз для 15 секунд, если пауза 0.5 секунды
        if x_to_play != 0:
            actions = ActionChains(driver)
            actions.move_by_offset(x_to_play, y_to_play).click().perform()
            actions.move_by_offset(-x_to_play, -y_to_play).perform()
            time.sleep(3)
        # Сохранение скриншота с уникальным именем
        scrin_images_file = f"{scrin_images_path}image-slot-{url_name_game}-{i}.png"

        try:
            screenshot_img = driver.find_element(By.CLASS_NAME, "loading-holder")
            # driver.get_screenshot_as_file(scrin_images_file
            screenshot_img.screenshot(scrin_images_file)
        except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
            print(f"Элемент 'loading-holder' для {url_name_game} не найден. Делаем <canvas>.")
            try:
                # Находим элемент canvas и делаем его скриншот
                canvas = driver.find_element(By.TAG_NAME, "canvas")
                canvas.screenshot(scrin_images_file)
            except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
                print(f"Элемент <canvas> также не найден {url_name_game}.")
                success = False
                break
        try:
            # Конвертация в JPEG и обрезка
            image = Image.open(scrin_images_file)
            if crop_required:
                # Обрезка изображения и сохранение в формате .webp
                width, height = image.size
                crop_rectangle = (0, 0, width, width)
                image = image.crop(crop_rectangle)
                img_screenshot_path = f"{scrin_images_path}image-slot-{url_name_game}-{i}.webp"
                image.convert('RGB').save(img_screenshot_path, "WEBP", quality=30)
            else:
                # Просто конвертация в формат .jpg
                img_screenshot_path = f"{scrin_images_path}image-slot-{url_name_game}-{i}.jpg"
                image.convert('RGB').save(img_screenshot_path, "JPEG", quality=70)
            # Удаление временного файла PNG
            os.remove(scrin_images_file)
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

    # емулируем как мобильное устройство
    # mobile_emulation = { "deviceName": "iPhone 12 Pro" }
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    mobile_emulation = {
    "deviceMetrics": { "width": 540, "height": 960, "pixelRatio": 2.0 },
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    # Chrome Service
    ser = Service(executable_path=r"D:\Gembling\Deepl_Python\Deepl_Python\SETTINGS\Chrome\119.0.6045.105\chromedriver.exe")
    driver = webdriver.Chrome(service=ser, options=chrome_options)
    driver.maximize_window()


    # Reed all games from parce TXT file
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file.readlines()]

    # Создаем и открываем CSV файл для записи
    fieldnames = ['#', 'title_game', 'alias', 'text_game', 'text_game_NLTK', 'text_game_NLTK_1000_and_nachalo', 'iframe_url', 
                'video_src', 'image_0', 'image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6', 'url_original', 
                'name_random_mus_file']
    with open(OUTPUT_GAMES_CSV, mode='a', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Эту строку нужно закомментировать - это заголовки которые при "a" не добавляются
        # writer.writeheader()
        url_counter = 1

        for url in urls:
            try:
                driver.get(url)
                time.sleep(8)

                # BTN 18 Years
                flag = False
                try:
                    element = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="game_pop"]/div[3]/a[1]/span'))
                    )
                    element.click()
                    flag = True  # Клик прошел успешно
                except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
                    pass
                # Если клик был успешен, перейти к следующему URL
                if flag:
                    continue

                # BTN Cookies close
                try:
                    driver.find_element(By.XPATH, '//*[@id="wt-cli-accept-all-btn"]').click()
                except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
                    pass

                try:
                    # Название и Описание игры
                    title_game = driver.find_element(By.CLASS_NAME, "game-details__title").text
                    title_game = title_game.replace("™", "").replace("®", "")
                    text_game = driver.find_element(By.CLASS_NAME, "game-details__description").text
                    text_game = text_game.replace("™", "").replace("®", "")
                    url_name_game = url.strip('/').split('/')[-1]
                except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
                    pass
                
                # Изминенный текст с использованием NLTK
                text_game_NLTK = paraphrase_with_spacy(text_game)
                # Приставка под текст и аудио где в начале ключевое слово
                pristavka_nachalo_text = title_game + " is available on the " + MY_SITE_NAME + " website\n"

                text_game_NLTK_1000_and_nachalo = pristavka_nachalo_text + text_game_NLTK[:1000]

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
                    time.sleep(12)
                except InvalidArgumentException:
                    print(f"Невірний URL iframe, пропускаємо: {iframe_src}")
                    continue  # Пропустити цю ітерацію циклу


                #################################################################
                #   Закрываем баннер и приступаем к игре
                #################################################################
                # # Добавление визуального маркера клика на страницу с помощью JavaScript
                # script = f"""
                # var body = document.querySelector('body');
                # var clickIndicator = document.createElement('div');
                # clickIndicator.style.position = 'absolute';
                # clickIndicator.style.left = '270px';
                # clickIndicator.style.top = '650px';
                # clickIndicator.style.width = '5px';
                # clickIndicator.style.height = '5px';
                # clickIndicator.style.backgroundColor = 'green';
                # clickIndicator.style.zIndex = '10000';
                # body.appendChild(clickIndicator);
                # """
                # driver.execute_script(script)

                x_to_click = 270
                y_to_click = 650

                # Скрин главной страницы
                time.sleep(1)
                success = take_screenshots(driver, 0, 1, 0, 0, url_name_game, scrin_images_path, crop_required=False)
                if not success:
                    continue

                for i in range(3):
                    # Создание цепочки действий для клика
                    actions = ActionChains(driver)
                    actions.move_by_offset(x_to_click, y_to_click).click().perform()
                    # Сброс положения курсора
                    actions = ActionChains(driver)
                    actions.move_by_offset(-x_to_click, -y_to_click).perform()
                    # Увеличение Y-координаты для следующего клика
                    y_to_click += 80  # Например, увеличивать на 30 каждый раз

                time.sleep(2)


                #################################################################
                #   PLAY BTN - igraem nazhimaya knopku
                #################################################################
                x_to_play = 270
                y_to_play = 750

                # Scrinshot settings - Получаем размеры и положение окна браузера
                # window_rect = driver.get_window_rect()
                # x = window_rect['x']
                # y = window_rect['y']
                # width = window_rect['width']
                # height = window_rect['height']

                # VIDEO REC
                video_path = folders['video_path']
                video_path_file = f"{video_path}/{url_name_game}-777del.mp4"

                
                #webm mkv mp4
                # x, y, width, height = 0, 0, 390, 844  # Пример значений для iPhone 12 Pro 390*844 - 1170, 2532
                x, y, width, height = 0, 0, 540, 960
                region = {"top": y, "left": x, "width": width, "height": height}
                video_thread = Thread(target=VideoRecorder, args=(video_path_file, 30, 24.0, region, MY_SITE_NAME))   #35, 4.0
                video_thread.start()


                #################################################################
                # Робимо скріни та кліки по кнопці (driver, start_index, num_screenshots, x_to_play, y_to_play, url_name_game)
                #################################################################
                success = take_screenshots(driver, 1, 7, x_to_play, y_to_play, url_name_game, scrin_images_path, crop_required=True)
                if not success:
                    # Обработка ситуации, пропуск оставшейся части цикла
                    continue

                time.sleep(1)
                video_thread.join()

                #################################################################
                # Аудио с текста и накладываем музыку
                #################################################################
                audio_path = folders['audio_path']
                name_random_mus_file = audioTextSpeach_on_audioMusic(text_game_NLTK_1000_and_nachalo, lang='en', audio_path=audio_path)


                # Путь к аудиофайлу, который был создан
                audio_file = f"{audio_path}output.mp3"
                final_video_path = f"{folders['folder_path']}/video/{url_name_game}.mp4"
                # Объединение видео и аудио
                # video_clip = VideoFileClip(video_path)
                # audio_clip = AudioFileClip(audio_file)
                # final_clip = video_clip.set_audio(audio_clip)
                # final_clip.write_videofile(final_video_path, codec='libx264', audio_codec='aac')

                # Команда для FFmpeg
                # ffmpeg_cmd = f'ffmpeg -i {video_path} -i {audio_file} -c:v copy -c:a aac -strict experimental {final_video_path}'
                ffmpeg_cmd = f'ffmpeg -i {video_path_file} -i {audio_file} -c:v libx264 -crf 23 -preset faster -c:a aac -b:a 128k -strict experimental {final_video_path}'
                # Запуск FFmpeg
                subprocess.run(ffmpeg_cmd, shell=True, check=True)

                # Запись данных в CSV
                row_data = {
                    '#': url_counter,
                    'title_game': title_game,
                    'alias': url_name_game,
                    'text_game': text_game,
                    'text_game_NLTK': text_game_NLTK,
                    'text_game_NLTK_1000_and_nachalo': text_game_NLTK_1000_and_nachalo,
                    'iframe_url': iframe_src,
                    'video_src': f"{url_name_game}/video/{url_name_game}.mp4",  # Путь к видеофайлу final_video_path
                    # Пути к изображениям (пример)
                    'image_0': f"{url_name_game}/images/image-slot-{url_name_game}-0.jpg",
                    'image_1': f"{url_name_game}/images/image-slot-{url_name_game}-1.jpg",
                    'image_2': f"{url_name_game}/images/image-slot-{url_name_game}-2.jpg",
                    'image_3': f"{url_name_game}/images/image-slot-{url_name_game}-3.jpg",
                    'image_4': f"{url_name_game}/images/image-slot-{url_name_game}-4.jpg",
                    'image_5': f"{url_name_game}/images/image-slot-{url_name_game}-5.jpg",
                    'url_original': url,  # Исходный URL
                    'name_random_mus_file': name_random_mus_file
                }

                writer.writerow(row_data)
                csv_file.flush()  # Принудительная запись данных в файл
                url_counter += 1

                time.sleep(5)
                # Удаление исходного видеофайла - Попытка удаления файла
                # Предполагаем, что у вас есть переменная video_path для пути к видеофайлу
                def add_path_to_delete_file(path, LIST_VIDEO_TO_DELETE):
                    with open(LIST_VIDEO_TO_DELETE, "a") as file:  # "a" для добавления в конец файла
                        file.write(path + "\n")  # Добавление пути к файлу с новой строки


                add_path_to_delete_file(video_path_file, LIST_VIDEO_TO_DELETE)

                print(title_game)



            except (TimeoutException, NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, InvalidArgumentException) as e:
                print(f"Ошибка при обработке URL {url}: {e}")
                traceback.print_exc()  # Печать полной трассировки стека

        driver.quit()

    # Видаляємо старі та великі відео
    try:
        delete_files_from_list(LIST_VIDEO_TO_DELETE, BASE_PATH_LIST_VIDEO_TO_DEL)
    except Exception as e:
        print(f"Произошла ошибка при удалении файлов: {e}")

# Замените 'output-my.txt' на путь к вашему файлу и укажите правильный путь к текущей папке
open_urls_and_click_button(URLS_SLOTS)
