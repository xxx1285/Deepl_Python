# проверка Undetect браузер - https://whoer.net/ru

import os
import csv
import time
import json
import random
import urllib.parse
import googlemaps
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, \
                                        ElementClickInterceptedException, InvalidArgumentException


import sys
sys.path.append('D:\\Gembling\\Deepl_Python\\Deepl_Python')
from Proxy.Restart_modem.E3372_Restart_control_clas_v1 import ModemController
from app.app_user_agent_Chrome_random import get_device_emulation_settings


URLS_ADRESS = r'GOOGLE\Google_Maps_Marshrut_BOT\output\output_FOOL_adress_InstadivFrayameb_v1.txt'
CHROME_DRIVER_PATH = r"D:\Gembling\Deepl_Python\Deepl_Python\SETTINGS\Chrome\120.0.6099.109\chromedriver.exe"

PROXY = "127.0.0.1:3128"  # IP:PORT или "HOST:PORT" вашего прокси-сервера

def get_random_addresses(file_path, sample_size=50):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return random.sample(lines, min(sample_size, len(lines)))
    # return lines


def create_driver_with_emulation():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--mute-audio")
    # chrome_options.add_argument(f'--proxy-server={PROXY}')
    # опции для игнорирования ошибок сертификатов в Chrome
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors-spki-list')

    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # chrome_options.add_argument(f"user-agent={random.choice(user_agent)}")  
    emulation_settings = get_device_emulation_settings()
    if "deviceName" in emulation_settings:
        chrome_options.add_experimental_option("mobileEmulation", emulation_settings)
        print(emulation_settings)
    else:
        chrome_options.add_argument(f"user-agent={emulation_settings['userAgent']}")
        print(f"user-agent={emulation_settings['userAgent']}")

    ser = Service(executable_path=CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=ser, options=chrome_options)
    # driver.set_page_load_timeout(40) 
    driver.maximize_window()

    return driver

def main():

    modem = ModemController("http://192.168.8.1")
    addresses = get_random_addresses(URLS_ADRESS)

    for address in addresses:
        driver = create_driver_with_emulation()
        try:
            driver.get("https://books.google.com/?authuser=0")
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            except Exception as e:
                print(f"Элемент <body> не найден: {e}")
            time.sleep(3)

            # driver.get("https://whoer.net/ru")
            driver.get("https://2ip.ua/ru/")
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            except Exception as e:
                print(f"Элемент <body> не найден: {e}")
            time.sleep(3)

            try:
                driver.get(address)
                time.sleep(10)
                # Ищем кнопку с атрибутом aria-label равным "Парковки"
                button_parkovka = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Парковки"]')
                time.sleep(4)
                button_parkovka.click()
                time.sleep(6)
                # Возвращаемся назад на предыдущую страницу
                driver.back()
                time.sleep(5)

            except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException) as e:
                print(f"Error processing {address}: {e}")

        finally:
            driver.quit()
            modem.main_restart()
            time.sleep(5)

if __name__ == '__main__':
    main()
    print('ALL OK')
