

# import undetected_chromedriver as uc    # Undetected Chrome
from PIL import Image
# import pyautogui  # Добавлено для создания скриншотов
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
import time
import random
import os
# import moviepy.editor as mp
# import mss
from moviepy.editor import VideoFileClip, AudioFileClip
import subprocess

from threading import Thread
from app.app_video_screenRecorder_v3 import VideoRecorder
from app.app_audioText_on_audioMUS_v1 import audioTextSpeach_on_audioMusic

MY_SITE_NAME = "0000.com"



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
    ser = Service(executable_path=r"C:\Gembling\Deepl_Python\Deepl_Python\SETTINGS\Chrome\109.0.5414.25\chromedriver.exe")
    driver = webdriver.Chrome(service=ser, options=chrome_options)
    # driver = uc.Chrome(headless=True,use_subprocess=False)
    driver.maximize_window()

    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file.readlines()]

    for url in urls:
        try:
            driver.get(url)
            time.sleep(8)

            # BTN Cookies close
            try:
                driver.find_element(By.XPATH, '//*[@id="wt-cli-accept-all-btn"]').click()
            except NoSuchElementException:
                pass
            except ElementNotInteractableException:
                pass

            # Название и Описание игры
            title_game = driver.find_element(By.CLASS_NAME, "game-details__title").text
            title_game = title_game.replace("™", "")
            text_game = driver.find_element(By.CLASS_NAME, "game-details__description").text
            text_game = text_game.replace("™", "")
            url_name_game = url.strip('/').split('/')[-1]

            # Create folder game - Создание папки, если она еще не существует
            folder_path = f"VideoRec_from_SiteMonitor/2_Scrin_Video_PragmatPlayGames/output/games/{url_name_game}"
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Находим iframe DEMO Game
            iframe = driver.find_element(By.ID, "iframe")
            iframe_src = iframe.get_attribute("src")
            driver.get(iframe_src)
            driver.fullscreen_window()  # полноекранный режим
            time.sleep(5)


            #################################################################
            #   Закрываем баннер и приступаем к игре
            #################################################################
            x_to_click = 270 #200
            y_to_click = 750 #600
            actions = ActionChains(driver)
            actions.move_by_offset(x_to_click, y_to_click).click().perform()
            time.sleep(2)
            # Сброс положения курсора (перемещение обратно к начальной точке)
            actions = ActionChains(driver)
            actions.move_by_offset(-x_to_click, -y_to_click).perform()


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
            video_path = f"{folder_path}/video/{url_name_game}-777.mp4"
            if not os.path.exists(os.path.dirname(video_path)):
                os.makedirs(os.path.dirname(video_path))
            #webm mkv mp4
            # x, y, width, height = 0, 0, 390, 844  # Пример значений для iPhone 12 Pro 390*844 - 1170, 2532
            x, y, width, height = 0, 0, 540, 960
            region = {"top": y, "left": x, "width": width, "height": height}
            video_thread = Thread(target=VideoRecorder, args=(video_path, 40, 24.0, region, MY_SITE_NAME))   #35, 4.0
            video_thread.start()


            #################################################################
            # Клики с нажатием играть и скриншотами
            #################################################################
            for i in range(10):  # 30 раз для 15 секунд, если пауза 0.5 секунды
                actions = ActionChains(driver)
                actions.move_by_offset(x_to_play, y_to_play).click().perform()
                actions.move_by_offset(-x_to_play, -y_to_play).perform()
                time.sleep(3)

                # Сохранение скриншота с уникальным именем
                scrin_images_path = f"{folder_path}/scrin-images/"
                if not os.path.exists(os.path.dirname(scrin_images_path)):
                    os.makedirs(os.path.dirname(scrin_images_path))


                if i < 4:
                    screenshot_path = f"{scrin_images_path}/image_{url_name_game}_{i}.png"

                    screenshot_img = driver.find_element(By.CLASS_NAME, "loading-holder")
                    # driver.get_screenshot_as_file(screenshot_path
                    screenshot_img.screenshot(screenshot_path)


                    # Конвертация в JPEG и обрезка
                    image = Image.open(screenshot_path)
                    width, height = image.size
                    # Обрезка для получения квадрата 1:1 с отступом сверху на 100 пикселей
                    # crop_rectangle = (0, 90, width,90 + width)  # (left, upper, right, lower)
                    crop_rectangle = (0, 0, width, width)
                    cropped_image = image.crop(crop_rectangle)

                    jpeg_screenshot_path = f"{scrin_images_path}/image_{url_name_game}_{i}.jpg"
                    cropped_image.convert('RGB').save(jpeg_screenshot_path, "JPEG")

                    # Удаление временного файла PNG
                    os.remove(screenshot_path)

            time.sleep(1)
            video_thread.join()

            #################################################################
            # Аудио с текста и накладываем музыку
            #################################################################
            bg_music_folder = "SETTINGS/Music-no-author"
            output_mp3_path = f"{folder_path}/audio/"
            if not os.path.exists(os.path.dirname(output_mp3_path)):
                os.makedirs(os.path.dirname(output_mp3_path))
            text_in_audio = text_game[:500]
            audioTextSpeach_on_audioMusic(text_in_audio, lang='en', output_mp3_path=output_mp3_path, bg_music_folder=bg_music_folder)


            # Путь к аудиофайлу, который был создан
            audio_file = f"{output_mp3_path}/output.mp3"
            final_video_path = f"{folder_path}/video/final_video.mp4"
            # Объединение видео и аудио
            # video_clip = VideoFileClip(video_path)
            # audio_clip = AudioFileClip(audio_file)
            # final_clip = video_clip.set_audio(audio_clip)
            # final_clip.write_videofile(final_video_path, codec='libx264', audio_codec='aac')

            # Команда для FFmpeg
            ffmpeg_cmd = f'ffmpeg -i {video_path} -i {audio_file} -c:v copy -c:a aac -strict experimental {final_video_path}'
            # Запуск FFmpeg
            subprocess.run(ffmpeg_cmd, shell=True)



            # Удаление исходного видеофайла
            # if os.path.exists(video_path):
            #     os.remove(video_path)

            print("4444")

        except (TimeoutException, NoSuchElementException) as e:
            print(f"Ошибка при обработке URL {url}: {e}")

    driver.quit()

# Замените 'output-my.txt' на путь к вашему файлу и укажите правильный путь к текущей папке
open_urls_and_click_button(r'VideoRec_from_SiteMonitor\2_Scrin_Video_PragmatPlayGames\output\output-urls-games.txt')
