
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
GOOGLE_ADRESS = 'https://www.google.com.ua/'
TXT_POISK_KEYS = 'игра авиатор 1win отзывы'
WHAT_SITE_I_SEARCH = 'aviator--game.com'
FIREFOX_DRIVER_PATH = r"D:\Gembling\Deepl_Python\Deepl_Python\SETTINGS\Mozilla\geckodriver-v0.34.0-win64\geckodriver.exe"


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
    print(emulation_settings["userAgent"])
    print(window_size)
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


def main():
    modem = ModemController("http://192.168.8.1")

    for attempt in range(5):
        driver = create_driver_with_emulation(PROXY, FIREFOX_DRIVER_PATH)
        try:
            #   Прокачка
            # driver.get("https://books.google.com/?authuser=0")
            # try:
            #     WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            # except Exception as e:
            #     print(f"Элемент <body> не найден: {e}")
            # time.sleep(3)

            # driver.get("https://google.com/")
            # driver.get("https://ifconfig.me/")
            # driver.get("https://2ip.ua/ru/")
            # driver.get("https://www.whatismybrowser.com/")
            # driver.get("https://browserleaks.com/webrtc")
            # driver.get("https://www.browserscan.net/webrtc")
            # driver.get("https://browserleaks.com/")

            # try:
            #     driver.get("https://2ip.ua/ru/")
            #     # driver.get("https://whoer.net/ru")
            #     time.sleep(5)
            # except TimeoutException:
            #     print("Страница не загрузилась за 30 секунд")
            # try:
            #     driver.get("https://time.is/")
            # except TimeoutException:
            #     print("Страница не загрузилась за 30 секунд")
            time.sleep(2)

            try:
                driver.get(GOOGLE_ADRESS)
                time.sleep(2)
                try:
                    # Ожидание, пока элемент не станет кликабельным
                    element = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea"))
                    )
                    element.click()
                    # Очистка текстового поля
                    element.clear()
                    element.send_keys(TXT_POISK_KEYS)
                    time.sleep(2)
                    element.send_keys(Keys.ENTER)
                except Exception as e:
                    print(f"С поиском GOOGLE проблема: {e}")

                time.sleep(2)
                ######################################################################################
                # Прокручуємо сторінку вниз або не більше 2 секунд
                ######################################################################################
                current_scroll_position, new_height= 0, 1
                speed = 300
                start_time = time.time()
                while current_scroll_position <= new_height:
                    if time.time() - start_time > 4:  # если прошло более 2 секунд, выходим из цикла
                        break
                    current_scroll_position += speed
                    driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
                    new_height = driver.execute_script("return document.body.scrollHeight")
                    time.sleep(0.1)
                ######################################################################################
                ######################################################################################
                try:
                    element = WebDriverWait(driver, 60).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='aviator--game.com']"))
                    )
                    time.sleep(2)
                    # Прокручиваем страницу до элемента если елемента не видно
                    driver.execute_script("arguments[0].scrollIntoView(true);", element)
                    time.sleep(5)
                    driver.execute_script("arguments[0].click();", element)
                    time.sleep(5)
                    # element1.click() 
                except Exception as e:
                    print(f"Элемент не найден: {e}")

                time.sleep(3)

                # try:
                #     element = WebDriverWait(driver, 60).until(
                #         EC.element_to_be_clickable((By.XPATH, '/html/body/header/nav/div[1]/div/ul/li[2]/a'))
                #     )
                #     element.click()
                # except Exception as e:
                #     print(f"Элемент (element_to_be_clickable((By.CSS_SELECTOR, 'https://instadivan.com/) не найден: {e}")

            except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException) as e:
                print(f"Error processing ** driver.get(address_CID) **: {e}")
        except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException) as e:
            print(f"Error ** **: {e}")

        finally:
            driver.quit()
            modem.main_restart()
            time.sleep(5)    


if __name__ == '__main__':
    main()
    print('ALL OK')