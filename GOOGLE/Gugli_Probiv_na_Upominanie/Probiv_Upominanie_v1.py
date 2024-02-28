
import csv
import re
import time
import pytz
import datetime
import random
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


PROXY = "127.0.0.1:3128"  # IP:PORT или "HOST:PORT" вашего прокси-сервера
CHROME_DRIVER_PATH = r"D:\Gembling\Deepl_Python\Deepl_Python\SETTINGS\Chrome\119.0.6045.105\chromedriver.exe"

INPUT_URLS_TXT = r'D:\Gembling\Deepl_Python\Deepl_Python\GOOGLE\Gugli_Probiv_na_Upominanie\input\unique_free_domains.txt'
OUTPUT_URLS_CSV = r'D:\Gembling\Deepl_Python\Deepl_Python\GOOGLE\Gugli_Probiv_na_Upominanie\output\unique_free_domains_output5-2.csv'



def create_driver_with_emulation(PROXY, CHROME_DRIVER_PATH):
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--mute-audio")
    # Установка стратегии ожидания загрузки страницы
    # что означает, что драйвер будет ждать, пока DOM не будет загружен полностью, 
    # но не будет ждать полной загрузки всех стилей, изображений и подфреймов
    chrome_options.page_load_strategy = 'eager'
    # chrome_options.add_argument(f'--proxy-server={PROXY}')
    # опции для игнорирования ошибок сертификатов в Chrome
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")


    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors-spki-list')
    # skrivaem avtomatizatsiu brauzera
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    emulation_settings = get_device_emulation_settings()
    if "deviceName" in emulation_settings:
        chrome_options.add_experimental_option("mobileEmulation", emulation_settings)
        print(emulation_settings)
    else:
        chrome_options.add_argument(f"user-agent={emulation_settings['userAgent']}")
        print(f"user-agent={emulation_settings['userAgent']}")

    ser = Service(executable_path=CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=ser, options=chrome_options)
    driver.set_page_load_timeout(40) 
    driver.maximize_window()

    return driver


def probiv_upominanie(driver, csv_writer, lines_buffer, csv_file):
    for domain in lines_buffer:
        # driver.get(f'https://www.google.com/search?q=%22{domain}%22')
        driver.get(f'https://www.google.com/search?q=intext%3A%22{domain}%22+-site%3A{domain}')
        try:
            # Ожидание появления элемента с id 'result-stats'
            element = WebDriverWait(driver, 35).until(
                EC.presence_of_element_located((By.ID, "result-stats"))
            )
            # Получение текста элемента и очистка от HTML-кодировки
            text = element.get_attribute('innerHTML').replace('&nbsp;', '')
            # Извлечение нужной части текста с помощью регулярного выражения
            match = re.search(r"примерно ([\d,]+)", text)
            if match:
                result_count = match.group(1)
                print(f"{domain}: {result_count}")
                csv_writer.writerow([domain, result_count])  # Запись в CSV
                csv_file.flush()
            else:
                print("Количество результатов не найдено")
                csv_writer.writerow([domain, 'Не найдено'])  # Запись в CSV
                csv_file.flush()

        except Exception as e:
            print(f"Элемент <body> не найден: {e}")
            csv_writer.writerow([domain, 'Ошибка'])  # Запись в CSV
            csv_file.flush()
        time.sleep(1)



def main():
    modem = ModemController("http://192.168.8.1")

    with open(INPUT_URLS_TXT, 'r') as txt_file, open(OUTPUT_URLS_CSV, 'a', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        lines_buffer = []

        for line in txt_file:
            lines_buffer.append(line.strip())  # Удаляем символы переноса строки

            # Как только в буфере накопится 3 строки, обрабатываем их
            if len(lines_buffer) == 7:
                driver = create_driver_with_emulation(PROXY, CHROME_DRIVER_PATH)
                try:
                    probiv_upominanie(driver, csv_writer, lines_buffer, csv_file)
                except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException) as e:
                    print(f"Error ** **: {e}")

                finally:
                    driver.quit()
                    lines_buffer = []  # Очищаем буфер
                    modem.main_restart()
       
        # Обрабатываем оставшиеся строки, если они есть
        if lines_buffer:
            driver = create_driver_with_emulation(PROXY, CHROME_DRIVER_PATH)
            try:
                probiv_upominanie(driver, csv_writer, lines_buffer, csv_file)
            except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException) as e:
                print(f"Error ** **: {e}")

            finally:
                driver.quit()
                lines_buffer = []  # Очищаем буфер
                modem.main_restart()

if __name__ == '__main__':
    main()
    print('ALL OK')