

# import undetected_chromedriver as uc    # Undetected Chrome
from PIL import Image
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

            # BTN 18 Years
            try:
                driver.find_element(By.XPATH, '//*[@id="game_pop"]/div[3]/a[1]/span').click()
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
            # driver.fullscreen_window()  # полноекранный режим
            driver.set_window_size(390, 844)
            time.sleep(5)

            # Координаты для клика
            x_to_click = 1620
            y_to_click = 700

            # # Добавление визуального маркера клика на страницу с помощью JavaScript
            # script = f"""
            # var body = document.querySelector('body');
            # var clickIndicator = document.createElement('div');
            # clickIndicator.style.position = 'absolute';
            # clickIndicator.style.left = '{x_to_click}px';
            # clickIndicator.style.top = '{y_to_click}px';
            # clickIndicator.style.width = '5px';
            # clickIndicator.style.height = '5px';
            # clickIndicator.style.backgroundColor = 'green';
            # clickIndicator.style.zIndex = '10000';
            # body.appendChild(clickIndicator);
            # """
            # driver.execute_script(script)
            actions = ActionChains(driver)
            actions.move_by_offset(x_to_click, y_to_click).click().perform()
            time.sleep(2)

            # Сброс положения курсора (перемещение обратно к начальной точке)
            actions = ActionChains(driver)
            actions.move_by_offset(-x_to_click, -y_to_click).perform()

            #################################################################
            #   PLAY BTN - igraem nazhimaya knopku
            #################################################################
            x_to_play = 1460
            y_to_play = 950

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
                    driver.get_screenshot_as_file(screenshot_path)

                    # Конвертация в JPEG
                    image = Image.open(screenshot_path)
                    jpeg_screenshot_path = f"{folder_path}/image_{url_name_game}_{i}.jpg"
                    image.convert('RGB').save(jpeg_screenshot_path, "JPEG")

                    # Удаление временного файла PNG
                    os.remove(screenshot_path)

        except (TimeoutException, NoSuchElementException) as e:
            print(f"Ошибка при обработке URL {url}: {e}")

    driver.quit()

# Замените 'output-my.txt' на путь к вашему файлу и укажите правильный путь к текущей папке
open_urls_and_click_button(r'VideoRec_from_SiteMonitor\2_Scrin_Video_PragmatPlayGames\output\output-urls-games.txt')
