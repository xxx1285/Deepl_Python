# проверка Undetect браузер - https://whoer.net/ru

import csv
import time
import pytz
import datetime
import random
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
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
from app.app_user_agent_Firefox_random import get_firefox_emulation_settings


PROXY = "127.0.0.1:3128"  # IP:PORT или "HOST:PORT" вашего прокси-сервера
URLS_ADRESS = r'GOOGLE\Google_mapsCID_Poxy_bot\input\output_adress_Start_NOEND_Point_v2.txt'
FIREFOX_DRIVER_PATH = r"D:\Gembling\Deepl_Python\Deepl_Python\SETTINGS\Mozilla\geckodriver-v0.34.0-win64\geckodriver.exe"

BUSINESS_PIN = [
    'ДИВАНЫ, МАТРАСЫ, КРОВАТИ 🛋️ СКЛАД магазин мягкой мебели в Борисполе. Купить кровать с матрасом - доставка в Киев. InstaDivan: вулиця Льва Толстого, 1, Бориспіль, Київська обл., 08301',
    'ДИВАНЫ, МАТРАСЫ, КРОВАТИ 🛋️ СКЛАД магазин мягкой мебели в Борисполе',
    'Купить кровать с матрасом Киев Борисполь InstaDivan',
    'Купить диван Киев Борисполь InstaDivan',
    'Магазин диванов Киев Борисполь InstaDivan',
    'диваны Борисполь InstaDivan',
    'купить диван Борисполь InstaDivan',
    'купить матрас Борисполь InstaDivan',
    'купить кровать Борисполь InstaDivan',
    'матрасы Борисполь InstaDivan',
    'кровати Борисполь InstaDivan',
    'Мебель Киев Борисполь InstaDivan',
    'Меблі Київ Бориспіль InstaDivan',
    'матраци Київ Бориспіль InstaDivan',
    'дивани Київ Бориспіль InstaDivan',
    'Бориспіль меблі InstaDivan',
    'Борисполь мебель InstaDivan',
]


def get_random_addresses(file_path, sample_size=20):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return random.sample(lines, min(sample_size, len(lines)))


def create_driver_with_emulation(PROXY, FIREFOX_DRIVER_PATH):
    firefox_options = Options()
    # Настройки user-agent для эмуляции устройств и скрытия автоматизации
    emulation_settings = get_firefox_emulation_settings()
    firefox_options.set_preference("general.useragent.override", emulation_settings["userAgent"])
    # Установка языковых предпочтений
    firefox_options.set_preference("intl.accept_languages", "ru-RU, ru, en-US, en, uk-UA, uk, fr-FR, fr, pt-PT, pt, es-ES, es")
    # Отключение уведомлений и WebRTC может раскрывать ваш IP-адрес даже при использовании VPN или прокси
    firefox_options.set_preference("dom.webnotifications.enabled", False)
    # firefox_options.set_preference("media.peerconnection.enabled", False)
    # PROXY
    # if PROXY:
    #     proxy_ip, proxy_port = PROXY.split(":")
    #     firefox_options.set_preference("network.proxy.type", 1)
    #     firefox_options.set_preference("network.proxy.http", proxy_ip)
    #     firefox_options.set_preference("network.proxy.http_port", int(proxy_port))
    #     firefox_options.set_preference("network.proxy.ssl", proxy_ip)
    #     firefox_options.set_preference("network.proxy.ssl_port", int(proxy_port))

    firefox_options.set_preference("media.volume_scale", "0.0")
    # скрывает факт использования WebDriver для управления Firefox
    firefox_options.set_preference("dom.webdriver.enabled", False)
    # Включение защиты от отслеживания
    firefox_options.set_preference("privacy.trackingprotection.enabled", True)
    # Отключение WebGL
    firefox_options.set_preference("webgl.disabled", True)
    # Отключение сохранения паролей и форм
    firefox_options.set_preference("signon.rememberSignons", False)
    firefox_options.set_preference("browser.formfill.enable", False)
    # Отключаем resistFingerprinting
    firefox_options.set_preference("privacy.resistFingerprinting", False)
    # Отключение кэша и cookies
    firefox_options.set_preference("browser.cache.disk.enable", False) 
    firefox_options.set_preference("network.cookie.cookieBehavior", 2)

    ser = Service(executable_path=FIREFOX_DRIVER_PATH)
    driver = webdriver.Firefox(service=ser, options=firefox_options)

    # Установка размера окна браузера
    window_size = emulation_settings["windowSize"].split(',')
    driver.set_window_size(int(window_size[0]), int(window_size[1]))

    # Установка часового пояса Украины "Europe/Kiev" - Южной Африки "Africa/Johannesburg"
    # https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%87%D0%B0%D1%81%D0%BE%D0%B2%D1%8B%D1%85_%D0%BF%D0%BE%D1%8F%D1%81%D0%BE%D0%B2_%D0%BF%D0%BE_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B0%D0%BC
    set_timezone(driver, "Europe/Kiev")

    # driver.maximize_window()

    return driver


def set_timezone(driver, timezone):
    tz = pytz.timezone(timezone)
    now = datetime.datetime.now(tz)
    timezone_offset = now.strftime('%z')
    script = f"return new Date().toLocaleString('en-US', {{timeZone: '{timezone}'}});"
    driver.execute_script(script)
    driver.execute_script(f"Date.prototype.getTimezoneOffset = function(){{return {timezone_offset[:-2]}}};")



# Функция для загрузки cookies (пример)
def load_social_media_cookies(driver):
    driver.get("https://example.com") # URL социальной сети
    # Здесь код для загрузки cookies


def main():

    modem = ModemController("http://192.168.8.1")
    addresses = get_random_addresses(URLS_ADRESS)

    for address in addresses:
        driver = create_driver_with_emulation(PROXY, FIREFOX_DRIVER_PATH)
        try:
            driver.get("https://books.google.com/?authuser=0")
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            except Exception as e:
                print(f"Элемент <body> не найден: {e}")
            time.sleep(3)

            driver.get("https://whoer.net/ru")
            # driver.get("https://google.com/")
            # driver.get("https://ifconfig.me/")
            # driver.get("https://www.whatismybrowser.com/")
            # driver.get("https://browserleaks.com/webrtc")
            # driver.get("https://www.browserscan.net/webrtc")
            # driver.get("https://browserleaks.com/")
            
            driver.get("https://2ip.ua/ru/")
            
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            except Exception as e:
                print(f"Элемент <body> не найден: {e}")
            time.sleep(3)

            try:
                driver.get(address)
                try:
                    WebDriverWait(driver, 50).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "tactile-searchbox-input")))
                except Exception as e:
                    print(f"Элемент (tactile-searchbox-input) не найден: {e}")
                time.sleep(3)

                inputs = driver.find_elements(By.CLASS_NAME, "tactile-searchbox-input")
                if len(inputs) > 1:
                    input_field = inputs[1]  # Получаем второй элемент, если он существует
                else:
                    print("Второй элемент 'tactile-searchbox-input' не найден.")
                    continue
                time.sleep(4)
                input_field.click()
                random_pin = random.choice(BUSINESS_PIN)
                time.sleep(3)

                input_field.send_keys(random_pin)
                time.sleep(3)
                input_field.send_keys(Keys.ENTER)
                time.sleep(10)
                # Ищем кнопку с атрибутом aria-label равным "Парковки"
                button_parkovka = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Парковки"]')
                time.sleep(4)
                button_parkovka.click()
                time.sleep(10)
                # Возвращаемся назад на предыдущую страницу
                driver.back()
                time.sleep(5)
                print(random_pin)


            except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException) as e:
                print(f"Error processing {address}: {e}")

        finally:
            driver.quit()
            modem.main_restart()
            time.sleep(5)

if __name__ == '__main__':
    main()
    print('ALL OK')
