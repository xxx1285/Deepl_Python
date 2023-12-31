# проверка Undetect браузер - https://whoer.net/ru
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, \
                                        ElementClickInterceptedException, InvalidArgumentException

from app.app_user_agent_random import get_device_emulation_settings
import sys
sys.path.append('D:\\Gembling\\Deepl_Python\\Deepl_Python')
from Proxy.Restart_modem.E3372_Restart_control_clas_v1 import ModemController


PROXY = "127.0.0.1:3128"  # IP:PORT или "HOST:PORT" вашего прокси-сервера
# URLS_SLOTS = r'VideoRec_from_SiteMonitor\output_PragmaticGames\output-urls-games2.txt'
URLS_ADRESS = r'GOOGLE\Google_mapsCID_Poxy_bot\input\output_borispol_adress_txt.txt'
# URLS_ADRESS = r'GOOGLE\Google_mapsCID_Poxy_bot\input\output_borispol_adress_Instadivan_txt.txt'
# Создаем экземпляр класса с указанием базового URL модема
modem = ModemController("http://192.168.8.1")


def create_driver_with_emulation():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument(f'--proxy-server={PROXY}')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    emulation_settings = get_device_emulation_settings()
    if "deviceName" in emulation_settings:
        chrome_options.add_experimental_option("mobileEmulation", emulation_settings)
        print(emulation_settings)
    else:
        chrome_options.add_argument(f"user-agent={emulation_settings['userAgent']}")
        print(f"user-agent={emulation_settings['userAgent']}")

    ser = Service(executable_path=r"D:\Gembling\Deepl_Python\Deepl_Python\SETTINGS\Chrome\119.0.6045.105\chromedriver.exe")
    driver = webdriver.Chrome(service=ser, options=chrome_options)
    driver.set_page_load_timeout(20) 
    driver.maximize_window()

    return driver


def open_urls_and_click_button():
    with open(URLS_ADRESS, mode='r', encoding='utf-8') as file:
        lines = file.readlines()

    # меняем ip
    modem.main_restart()
    
    # Выбор 5 случайных строк
    # random_lines = random.sample(lines, 5)
    random_lines = lines

    count = 0
    for line in random_lines:
        if count < 200:
            driver = create_driver_with_emulation()
            # прогреваем
            try:
                driver.get("https://books.google.com/?authuser=0")
            except TimeoutException:
                print("Страница не загрузилась за 30 секунд")

            # try:
            #     driver.get("https://ifconfig.me/")
            # except TimeoutException:
            #     print("Страница не загрузилась за 30 секунд")

            try:
                driver.get("https://2ip.ua/ru/")
            except TimeoutException:
                print("Страница не загрузилась за 30 секунд")

            # try:
            #     driver.get("https://artsandculture.google.com/")
            # except TimeoutException:
            #     print("Страница не загрузилась за 30 секунд")

            # try:
            #     driver.get("https://time.is/")
            # except TimeoutException:
            #     print("Страница не загрузилась за 30 секунд")

            time.sleep(2)

            # переход на нужный нам url со списка
            new_url = line.strip()  # Удаление пробельных символов, включая символ новой строки
            try:
                driver.get(new_url)
                time.sleep(15)
            except TimeoutException:
                print("Страница не загрузилась за 30 секунд")
            finally:
                # меняем ip
                driver.quit()
                modem.main_restart()

            # Увеличиваем счетчик
            count += 1
        
        else:
            break


if __name__ == '__main__':
    open_urls_and_click_button()
    print("All Good")