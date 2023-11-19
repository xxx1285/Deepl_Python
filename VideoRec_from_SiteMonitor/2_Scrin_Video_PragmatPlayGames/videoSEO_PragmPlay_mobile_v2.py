

# import undetected_chromedriver as uc    # Undetected Chrome
from PIL import Image
import pyautogui  # Добавлено для создания скриншотов
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

from threading import Thread
# from app.app_video_screenRecorder_v2 import ScreenRecorder



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
    mobile_emulation = { "deviceName": "iPhone 12 Pro" }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # mobile_emulation = {
    # "deviceMetrics": { "width": 390, "height": 844, "pixelRatio": 3.0 },
    # "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    # }
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

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
            time.sleep(7)

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

            # Находим iframe DEMO Game
            iframe = driver.find_element(By.ID, "iframe")
            iframe_src = iframe.get_attribute("src")
            print(iframe_src)

            driver.get(iframe_src)
            driver.fullscreen_window()  # полноекранный режим

            # Добавление визуального маркера клика на страницу с помощью JavaScript
            # script = f"""
            # var body = document.querySelector('body');
            # var clickIndicator = document.createElement('div');
            # clickIndicator.style.position = 'absolute';
            # clickIndicator.style.left = '200px';
            # clickIndicator.style.top = '600px';
            # clickIndicator.style.width = '5px';
            # clickIndicator.style.height = '5px';
            # clickIndicator.style.backgroundColor = 'green';
            # clickIndicator.style.zIndex = '10000';
            # body.appendChild(clickIndicator);
            # """
            # driver.execute_script(script)









            time.sleep(5)

            # Координаты для клика
            x_to_click = 200
            y_to_click = 600

            actions = ActionChains(driver)
            actions.move_by_offset(x_to_click, y_to_click).click().perform()
            time.sleep(2)

            # Сброс положения курсора (перемещение обратно к начальной точке)
            actions = ActionChains(driver)
            actions.move_by_offset(-x_to_click, -y_to_click).perform()

            #################################################################
            #   PLAY BTN - igraem nazhimaya knopku
            #################################################################
            x_to_play = 200
            y_to_play = 600

            # Scrinshot settings - Получаем размеры и положение окна браузера
            window_rect = driver.get_window_rect()
            x = window_rect['x']
            y = window_rect['y']
            width = window_rect['width']
            height = window_rect['height']

            # VIDEO REC
            import cv2
            import numpy as np
            import pyautogui
            from moviepy.editor import VideoFileClip

            class ScreenRecorder:
                def __init__(self, output_path):
                    self.output_path = output_path
                    self.recording = False
                    self.out = None

                def start_recording(self):
                    self.recording = True
                    # Получение размера экрана
                    screen_size = pyautogui.size()
                    # Создание объекта VideoWriter
                    fourcc = cv2.VideoWriter_fourcc(*"XVID")
                    self.out = cv2.VideoWriter(self.output_path, fourcc, 20.0, screen_size)

                    while self.recording:
                        # Захват изображения экрана
                        img = pyautogui.screenshot()
                        frame = np.array(img)
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        self.out.write(frame)

                def stop_recording(self):
                    self.recording = False
                    self.out.release()
                    cv2.destroyAllWindows()

            # Функция для изменения размера видео
            def resize_video(input_path, output_path, new_width, new_height):
                clip = VideoFileClip(input_path)
                resized_clip = clip.resize(newsize=(new_width, new_height))
                resized_clip.write_videofile(output_path, codec='libx264')








            video_path = f"VideoRec_from_SiteMonitor/2_Scrin_Video_PragmatPlayGames/output/video/{url_name_game}.mp4"
            video_recorder = ScreenRecorder(video_path)
            video_recorder.start_recording()

            # Клики с нажатием играть и скриншотами
            for i in range(10):  # 30 раз для 15 секунд, если пауза 0.5 секунды
                actions = ActionChains(driver)
                actions.move_by_offset(x_to_play, y_to_play).click().perform()
                actions.move_by_offset(-x_to_play, -y_to_play).perform()
                time.sleep(2.3)

                # Сохранение скриншота с уникальным именем
                # Путь к папке для скриншотов
                folder_path = f"VideoRec_from_SiteMonitor/2_Scrin_Video_PragmatPlayGames/output/scrinshot-img/{url_name_game}"
                # Создание папки, если она еще не существует
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                if i < 4:
                    screenshot_path = f"{folder_path}/image_{url_name_game}_{i}.png"

                    screenshot_img = driver.find_element(By.CLASS_NAME, "loading-holder")
                    # driver.get_screenshot_as_file(screenshot_path
                    screenshot_img.screenshot(screenshot_path)
                    # screenshot = pyautogui.screenshot()
                    # screenshot = pyautogui.screenshot(region=(x, y, width, height))
                    # screenshot.save(screenshot_path)

                    # Конвертация в JPEG и обрезка
                    image = Image.open(screenshot_path)
                    width, height = image.size
                    # Обрезка для получения квадрата 1:1 с отступом сверху на 100 пикселей
                    crop_rectangle = (0, 90, width,90 + width)  # (left, upper, right, lower)
                    cropped_image = image.crop(crop_rectangle)

                    jpeg_screenshot_path = f"{folder_path}/image_{url_name_game}_{i}.jpg"
                    cropped_image.convert('RGB').save(jpeg_screenshot_path, "JPEG")

                    # Удаление временного файла PNG
                    os.remove(screenshot_path)

            # video_recorder.stop_recording()
            video_recorder.stop_recording()
            # Изменение размера записанного видео
            resized_video_path = f"VideoRec_from_SiteMonitor/2_Scrin_Video_PragmatPlayGames/output/video/{url_name_game}.mp4"
            resize_video(video_path, resized_video_path, 1170, 2532)

            print("4444")

        except (TimeoutException, NoSuchElementException) as e:
            print(f"Ошибка при обработке URL {url}: {e}")

    driver.quit()

# Замените 'output-my.txt' на путь к вашему файлу и укажите правильный путь к текущей папке
open_urls_and_click_button(r'VideoRec_from_SiteMonitor\2_Scrin_Video_PragmatPlayGames\output\output-urls-games.txt')
