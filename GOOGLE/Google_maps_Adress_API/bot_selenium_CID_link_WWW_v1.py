# проверка Undetect браузер - https://whoer.net/ru

import os
import csv
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, \
                                        ElementClickInterceptedException, InvalidArgumentException


base_path_del = os.path.dirname(os.path.abspath(__file__))

# URLS_SLOTS = r'VideoRec_from_SiteMonitor\output_PragmaticGames\output-urls-games2.txt'
URLS_ADRESS = r'Google_maps_Adress_API\output\output_result_CIT_URLs.txt'

# https://families.google/familylink/?utm_source=google&utm_medium=pref-page&hl=ru-UA&authuser=0


def open_urls_and_click_button():
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


    # IP-адрес: 154.6.130.11
    # Время: 2023-12-23T21:19:22Z
    # URL: https://google.com/

    # Chrome Service
    ser = Service(executable_path=r"D:\Gembling\Deepl_Python\Deepl_Python\SETTINGS\Chrome\119.0.6045.105\chromedriver.exe")
    driver = webdriver.Chrome(service=ser, options=chrome_options)
    driver.maximize_window()

    # JavaScript для подмены времени
    script = """
    var baseTime = new Date();
    baseTime.setHours(baseTime.getHours() + 2); // Добавляем 2 часа

    Date = class extends Date {
    constructor() {
        super();
        return new Date(baseTime.getTime() + (new Date().getTime() - baseTime.getTime()));
    }
    };
    """
    driver.execute_script(script)

    # Открываем файл для чтения TXT
    with open(URLS_ADRESS, mode='r', encoding='utf-8') as file:
        # Счетчик для ограничения количества итераций
        count = 0
        # Перебор строк в файле CSV
        for line in file:
            if count < 20:

                # прогреваем
                # driver.get("https://books.google.com/?authuser=0")
                # driver.get("https://artsandculture.google.com/")
                # azenv.net  - proxy чекер
                driver.get("https://time.is/")
                time.sleep(2)

                new_url = line.strip()  # Удаление пробельных символов, включая символ новой строки
                driver.get(new_url)
                time.sleep(3)

                # BTN 18 Years
                flag = False
                try:
                    element = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[9]/div[2]/div/div[2]/async-local-kp/div/div/div[1]/div/g-sticky-content-container/div/block-component/div/div[1]/div/div/div/div[1]/div/div/div[5]/c-wiz/div/div/div/div[1]/a/div/div'))
                    )
                    element.click()
                    time.sleep(3)
                    element = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[20]/div/div/div/div/div[3]/div/span[2]/button/span/span'))
                    )
                    element.click()
                    flag = True  # Клик прошел успешно
                except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
                    pass
                # Если клик был успешен, перейти к следующему URL
                if flag:
                    driver.quit()
                    continue

                # BTN Cookies close
                try:
                    driver.find_element(By.XPATH, '//*[@id="wt-cli-accept-all-btn"]').click()
                except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
                    pass

                # try:
                #     # Название и Описание игры
                #     title_game = driver.find_element(By.CLASS_NAME, "game-details__title").text
                #     title_game = title_game.replace("™", "").replace("®", "")
                #     text_game = driver.find_element(By.CLASS_NAME, "game-details__description").text
                #     text_game = text_game.replace("™", "").replace("®", "")
                #     url_name_game = url.strip('/').split('/')[-1]
                # except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
                #     pass
                
                



                x_to_click = 270
                y_to_click = 650

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
                # Увеличиваем счетчик
                count += 1
            
            else:
                break

    driver.quit()

if __name__ == '__main__':
    open_urls_and_click_button()