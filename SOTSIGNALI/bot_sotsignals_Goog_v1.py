
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
URLS_ADRESS = r'D:\Gembling\Deepl_Python\Deepl_Python\SOTSIGNALI\del\test.txt'
CHROME_DRIVER_PATH = r"D:\Gembling\Deepl_Python\Deepl_Python\SETTINGS\Chrome\119.0.6045.105\chromedriver.exe"

KILKIST_SOTSSIGNALS = 200000
SPAM_SOTSIGNAL_ON_SITE = 'https://mxim.in/'



def get_random_address(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return random.choice(lines).strip()


def create_driver_with_emulation(PROXY, CHROME_DRIVER_PATH):
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--mute-audio")
    # chrome_options.add_argument(f'--proxy-server={PROXY}')
    # опции для игнорирования ошибок сертификатов в Chrome
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors-spki-list')
    # skrivaem avtomatizatsiu brauzera
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    # otkluchaem kartinki
    chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

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

    for i in range(KILKIST_SOTSSIGNALS):
        address_Sotsignal = get_random_address(URLS_ADRESS)
        print(f"Sotssignal: {address_Sotsignal}")
        # address_Sotsignal = 'https://t.me/'
        driver = create_driver_with_emulation(PROXY, CHROME_DRIVER_PATH)
        try:
            
            try:
                driver.get(address_Sotsignal)
                WebDriverWait(driver, 70).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            except TimeoutException as e:
                print(f"TimeoutException: {address_Sotsignal}  - {e}")
            except Exception as e:
                print(f"Інша помилка при пошуку {address_Sotsignal}: {e}")

            # Находим все элементы ссылок на странице
            links = driver.find_elements(By.XPATH, "//a[@href]")
            
            clickable_link = None
            # Перебираем элементы, ищем первый кликабельный
            # Перебираем элементы, ищем первый кликабельный
            for link in links:
                href = link.get_attribute('href')
                disabled = link.get_attribute('disabled')  # Получаем атрибут disabled
                onclick = link.get_attribute('onclick')  # Получаем атрибут onclick

                # Проверяем, что ссылка отображается, активна, не содержит 'javascript' в href, не отключена и не имеет атрибута onclick
                if link.is_displayed() and link.is_enabled() and 'javascript' not in href and not disabled and not onclick:
                    clickable_link = link
                    break  # Прерываем цикл, так как нашли подходящую кликабельную ссылку


            if clickable_link:
                
                # Получаем текущий href элемента
                current_href = clickable_link.get_attribute('href')
                print(f"a href: {current_href}")
                
                # Ваш новый URL, который вы хотите подставить вместо существующего href
                new_href = SPAM_SOTSIGNAL_ON_SITE
                
                # Используем JavaScript для изменения href у выбранной ссылки
                driver.execute_script("arguments[0].setAttribute('href', arguments[1])", clickable_link, new_href)
                
                # Кликаем по ссылке после изменения href
                clickable_link.click()
                print("Click OK")
                time.sleep(20)
            else:
                print("На странице не найдено кликабельных ссылок.")
            
        except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException) as e:
            print(f"Error ** **: {e}")
        except Exception as e:
            print(f"Error *№№№№* **: {e}")

        finally:
            driver.quit()
            print("##############################################################")
            print(f"№{i} -  {address_Sotsignal}")
            print("##############################################################")
            modem.main_restart()
            time.sleep(5)    


if __name__ == '__main__':
    main()
    print('ALL OK')