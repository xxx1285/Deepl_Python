
import csv
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
URLS_ADRESS = r'D:\Gembling\Deepl_Python\Deepl_Python\GOOGLE\Google_slots_games\input\redici-URL-1win-officialsite_store.txt'
CHROME_DRIVER_PATH = r"D:\Gembling\Deepl_Python\Deepl_Python\SETTINGS\Chrome\122.0.6261.128\chromedriver.exe"


KILKIST_POSESHENIY = 500


def get_random_address(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return random.choice(lines).strip()


def create_driver_with_emulation(PROXY, CHROME_DRIVER_PATH):
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument(f'--proxy-server={PROXY}')
    # опции для игнорирования ошибок сертификатов в Chrome
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



def main():
    modem = ModemController("http://192.168.8.1")
    

    for i in range(KILKIST_POSESHENIY):
        driver = create_driver_with_emulation(PROXY, CHROME_DRIVER_PATH)
        addresses_CID = get_random_address(URLS_ADRESS)

        try:
            #######################################################
            #   Прокачка
            #######################################################
            # driver.get("https://books.google.com/?authuser=0")
            # try:
            #     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            # except Exception as e:
            #     print(f"Элемент <body> не найден: {e}")

            # time.sleep(3)

            try:
                driver.get("https://2ip.ua/ru/")
                # driver.get("https://whoer.net/ru")
                time.sleep(3)
            except TimeoutException:
                print("Страница не загрузилась за 30 секунд")

            time.sleep(1)

            # driver.get("https://google.com/")
            # driver.get("https://ifconfig.me/")
            # driver.get("https://2ip.ua/ru/")
            # driver.get("https://www.whatismybrowser.com/")
            # driver.get("https://browserleaks.com/webrtc")
            # driver.get("https://www.browserscan.net/webrtc")
            # driver.get("https://browserleaks.com/")
            # driver.get("https://time.is/")
            
            #######################################################
            #######################################################
            #   Perehodimo po_CID
            try:
                driver.get(addresses_CID)

                urls_to_try = [
                    'https://1win-officialsite.store/'
                ]

                element_found = None

                for url in urls_to_try:
                    try:
                        element = WebDriverWait(driver, 40).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, f'a[href="{url}"]'))
                        )
                        element_found = element
                        print(f"Click URL: {url}")
                        break  # Выходим из цикла, если элемент найден
                    except TimeoutException:
                        print(f"Элемент с URL {url} не найден или не доступен для клика.")
                    except Exception as e:
                        print(f"Інша помилка при пошуку {url}: {e}")


                if element_found:
                    # Прокрутка страницы к элементу
                    # time.sleep(4)
                    # driver.execute_script("arguments[0].scrollIntoView(true);", element_found)
                    time.sleep(4)  # Пауза для обеспечения времени на прокрутку и отрисовку элемента
                    element_found.click()
                    # Нажатие на элемент с помощью JavaScript
                    # driver.execute_script("arguments[0].click();", element_found)
                    time.sleep(4)
                else:
                    print("Ни один из элементов не был найден.")

                
                ###########################################################################
                #   Внутрішній CLICK
                ###########################################################################
                # try:
                #     # шукаємо всі ссилки в <nav>
                #     all_links = driver.find_elements(By.CSS_SELECTOR, "nav a")
                #     # Фильтруем ссылки, чтобы оставить только кликабельные и видимые
                #     clickable_links = [link for link in all_links if driver.execute_script("return arguments[0].offsetParent !== null", link) and link.is_displayed()]
                #     time.sleep(3)
                #     # Проверяем, есть ли кликабельные ссылки
                #     if clickable_links:
                #         # Выбираем случайную ссылку из отфильтрованного списка
                #         random_link = random.choice(clickable_links)
                #         random_link.click()
                #         time.sleep(7)
                #     else:
                #         print("Кликабельные и видимые ссылки не найдены")
                # except Exception as e:
                #     print(f"ERROR Внутрішній CLICK {url}: {e}")

                ###########################################################################

            except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException) as e:
                print(f"Error processing ** driver.get(address_CID) **: {e}")
        except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException) as e:
            print(f"Error ** **: {e}")

        finally:
            driver.quit()
            print("#######################################")
            print(i)
            print("#######################################")
            modem.main_restart()
            time.sleep(5)    


if __name__ == '__main__':
    main()
    print('ALL OK')