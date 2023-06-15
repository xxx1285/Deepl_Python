import os
import time
import json
from random import choice
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidCookieDomainException, UnableToSetCookieException, TimeoutException

# Multiprotcessing
from multiprocessing import Pool
# Завантаження інструкцій
from baza_links.web2_0 import websites
# Gmail
from gmail_login import login_to_gmail
from gmail_autorization import gmail_autoriz_fun
from captcha_img import process_image


# Нинішній розділ
current_folder = os.path.basename(os.path.dirname(__file__))

# EMAIL Google
with open(f'{current_folder}\\email\\email.json') as json_file:
    email_json = json.load(json_file)

# USER-AGENT
user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36']

# TODO: COOKIES
# cookies- Шлях до файлу з куками
COOKIES_FOLDER_PATH = os.path.join(current_folder, 'cookies')
# cookies- Функція для завантаження cookies
def load_cookies(driver, email):
    try:
        cookie_file = os.path.join(COOKIES_FOLDER_PATH, f'{email}.json')
        if os.path.exists(cookie_file):
            with open(cookie_file, 'r') as file:
                cookies = json.load(file)
                for cookie in cookies:
                    # if 'expiry' in cookie:
                    #     del cookie['expiry']
                    try:
                        driver.add_cookie(cookie)
                        print(f'Cookies loaded for {email}.')
                    except (InvalidCookieDomainException, UnableToSetCookieException) as e:
                        print((f"Error loading cookies for {email}: {e}"))
                        continue
            
    except (OSError, IOError):
        print(f"No cookie file found for {email}.")

# cookies- Функція для збереження cookies
def save_cookies(driver, email):
    cookie_file = os.path.join(COOKIES_FOLDER_PATH, f'{email}.json')
    # Зберігаємо файли cookie у вигляді набору, щоб видалити дублікати
    cookies_set = {json.dumps(cookie) for cookie in driver.get_cookies()}
    # Перетворюємо набір назад у список
    cookies_list = [json.loads(cookie) for cookie in cookies_set]
    with open(cookie_file, 'w') as file:
        json.dump(cookies_list, file)
    print(f'Cookies saved for {email}.')


# Функція для виконання інструкцій
def execute_instructions(driver, email, password, author, url, instructions):
    # Перехід до веб-сайту
    driver.get(url)
    my_wait = WebDriverWait(driver, 10)  # ожидание до 10 секунд

    for instruction in instructions:
        action, code = list(instruction.items())[0]

        # Виконуємо код інструкції, використовуючи exec. Зауважте, що це може бути потенційно небезпечно,
        # якщо інструкції не є надійними, оскільки exec виконує будь-який переданий йому код.
        try:
            exec(code)
        except Exception as e:
            print(f"Error executing instruction '{action}': {e}")
            continue
    print(f"Completed instructions for {url}")


# Функція для обробки інструкцій
def process_instructions(email_json_info):
    # Витягуємо логін і пароль з вхідного словника
    email = email_json_info["login"]
    password = email_json_info["password"]
    author = email_json_info["author"]

    # Инициализация веб-драйвера Firefox
    # Firefox Options
    firefox_options = FirefoxOptions()
    firefox_options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    firefox_options.set_preference("general.useragent.override", choice(user_agent))  # User-agent
    firefox_options.set_preference("dom.webnotifications.enabled", False)  # Disable notifications
    firefox_options.set_preference("fission.bfcacheInParent", False)  # Fission setting
    firefox_options.set_preference("fission.webContentIsolationStrategy", 0)  # Fission setting
    # Firefox Service
    ser = Service(executable_path = f"{current_folder}\\Webdriver_Firefox\\geckodriver.exe")  # Please, update the path to geckodriver.exe file

    # Firefox Driver - Create a Firefox WebDriver
    driver = webdriver.Firefox(service=ser, options=firefox_options)
    # Chrome Вікно відкрити максимально
    driver.maximize_window()

    # TODO: GMAIL - Переходимо на сторінку Gmail
    storinka_gmail_vhid = "https://mail.google.com"
    driver.get(storinka_gmail_vhid)
    
    # COOKIES LOAD - Завантажуємо файли cookie
    load_cookies(driver, email)
    time.sleep(1)
    # Оновлюємо сторінку
    driver.refresh()
    time.sleep(3)

    # Якщо поточний URL не "mail.google.com" виконуємо вхід
    if storinka_gmail_vhid not in driver.current_url:
        login_to_gmail(driver, email, password)
        # Зберігаємо файли cookie після входу в gmail
        save_cookies(driver, email)
        driver.refresh()    # Оновлюємо сторінку
        time.sleep(3)

    # TODO: Виконуємо інструкції для кожного URL
    for url, instructions in websites.items():
        execute_instructions(driver, email, password, author, url, instructions)
        # Зберігаємо файли cookie
        save_cookies(driver, email)
        driver.refresh()    # Оновлюємо сторінку
        time.sleep(2)       # чекаємо, поки сторінка завантажиться

    # Закриваємо драйвер
    driver.quit()


# Використовуємо бібліотеку multiprocessing, щоб запустити обробку інструкцій для кожної електронної пошти паралельно
# if __name__ == '__main__':
#     with Pool(5) as p:
#         p.map(process_instructions, email_json.values())

# Без multiprocessing
if __name__ == '__main__':
    for email_info in email_json.values():
        process_instructions(email_info)