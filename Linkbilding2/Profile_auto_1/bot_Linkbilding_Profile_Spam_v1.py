
import os
import re
import time
import random
import importlib.util
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


from app.app_generate_login import generate_unique_login


PROXY = "127.0.0.1:3128"  # IP:PORT или "HOST:PORT" вашего прокси-сервера
# URLS_ADRESS = r'D:\Gembling\Deepl_Python\Deepl_Python\GOOGLE\Google_mapsCID_Poxy_bot\input\CID_URLs__MebelBorispol_Freya_05-02-2024.txt'
INPUT_MY_SITES = r'Linkbilding2\Profile_auto_1\input\my_sites.txt'
URLS_ADRESS = r'Linkbilding2\Profile_auto_1\profiles_baza\Profiles.txt'
SAVE_RESULT  = r'Linkbilding2\Profile_auto_1\output\result.txt'
PROFILES_BAZA = r'Linkbilding2\Profile_auto_1\profiles_baza'
CHROME_DRIVER_PATH = r"D:\Gembling\Deepl_Python\Deepl_Python\SETTINGS\Chrome\122.0.6261.128\chromedriver.exe"


KILKIST_POSTING = 5


def get_random_urls_kilkist_posting(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Повторное добавление адресов, если их количество меньше KILKIST_POSTING
    while len(lines) < KILKIST_POSTING:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines.extend(file.readlines())
    
    return lines[:KILKIST_POSTING]

def get_random_line_inTxt(file_path):
    # случайным образом выбирает строку из текстового файла
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        random_line = random.choice(lines)
    return random_line.strip()

def get_ispolnitelniy_file_from_domain(post_url):
    # Регулярное выражение для извлечения домена из post_url
    domain_regex = r"https?://([^/]+)"
    match = re.search(domain_regex, post_url)
    if match:
        domain = match.group(1)
        print("Domain extracted from URL:", domain)

    module_path = os.path.join(PROFILES_BAZA, f"{domain}.py")
    if os.path.exists(module_path):
        module_name = f"profiles_baza.{domain}"
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    else:
        print(f"No Python file found for {domain}")
    



def create_driver_with_emulation(PROXY, CHROME_DRIVER_PATH):
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument(f'--proxy-server={PROXY}')
    # опции для игнорирования ошибок сертификатов в Chrome
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors-spki-list')
    chrome_options.add_argument('--ignore-certificate-errors')

    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--disable-software-rasterizer")
    # skrivaem avtomatizatsiu brauzera
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

    ser = Service(executable_path=CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=ser, options=chrome_options)
    # driver.set_page_load_timeout(40) 
    driver.maximize_window()

    return driver



def main():
    modem = ModemController("http://192.168.8.1")
    

    for i in range(KILKIST_POSTING):
        post_urls = get_random_urls_kilkist_posting(URLS_ADRESS)

        for post_url in post_urls:

            try:
                driver = create_driver_with_emulation(PROXY, CHROME_DRIVER_PATH)
                # try:
                #     driver.get("https://2ip.ua/ru/")
                #     # driver.get("https://whoer.net/ru")
                #     time.sleep(3)
                # except TimeoutException:
                #     print("Страница не загрузилась за 30 секунд")

                # time.sleep(1)

                unique_login = generate_unique_login()
                print(unique_login)

                #######################################################
                #######################################################
                #   Perehodimo po URL
                try:
                    my_site_url = get_random_line_inTxt(INPUT_MY_SITES)

                    password = "Dsa342343#24"

                    module = get_ispolnitelniy_file_from_domain(post_url)
                    module.process_data(driver, post_url, my_site_url, unique_login, password, SAVE_RESULT)
                    print(f"Found Python file for ")

                     ###########################################################################

                except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException) as e:
                    print(f"Error processing ** driver.get(address_CID) **: {e}")
                    continue
            except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException) as e:
                print(f"Error ** **: {e}")

            finally:
                driver.quit()
                print("#######################################")
                print(i)
                print("#######################################")
                # modem.main_restart()
                time.sleep(5)    


if __name__ == '__main__':
    main()
    print('ALL OK')