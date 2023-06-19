import os
import time
import json
import random
from datetime import datetime
import undetected_chromedriver as uc    # Undetected Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidCookieDomainException, UnableToSetCookieException, TimeoutException


# Multiprotcessing
from multiprocessing import Pool
# Links: Завантаження інструкцій
from baza_backlinks.en_comments_web2_0 import websites
# Function: Gmail
from module_gmail.gmail_login import login_to_gmail
from module_gmail.gmail_autorization import gmail_autoriz_fun
# Function: Captcha
from module_captcha.captcha_img import fun_my_captcha_image
from module_captcha.captcha_calculate_mathematic import fun_my_captcha_calculate_mathematic
from module_captcha.wait_for_cloudflare_load import wait_for_cloudflare_to_disappear
# Function: Формуэмо Частотну фразу Тайтл в Боді
from most_frequent_phrase import most_frequent_phrase_in_body
# Function: Функція очікування загрузки сайта 
from def_wait_for_page_load import wait_for_page_load


# База шаблонів коментарів
from comments_teplates.templ_comments_en import comments_prompt


# Нинішній розділ
current_folder = os.path.basename(os.path.dirname(__file__))

# Дата - вивод в форматі: 10-06-2023
current_date = datetime.now()
formatted_date = current_date.strftime('%d-%m-%Y')

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
                    if 'expiry' in cookie:
                        del cookie['expiry']
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
def execute_instructions(driver, url, instructions, **email_json_info):
    my_wait = WebDriverWait(driver, 10)  # ожидание до 10 секунд

    # Мій Чистий Сайт без "https://" i  "/"
    clean_site_url = email_json_info['site_url'].split("//")[1].split("/")[0]

    # Параметри розпаковані з JSON
    my_site_backlink = email_json_info['site_backlink'] 
    my_author = email_json_info['author']
    my_email =  email_json_info['email']

    # Перехід до веб-сайту
    driver.get(url)
    wait_for_cloudflare_to_disappear(driver)
    print("5 sek")
    wait_for_page_load(driver, check_frequency=1, timeout=10)

    # Прокручуємо сторінку вниз або не більше 2 секунд
    current_scroll_position, new_height= 0, 1
    speed = 300
    start_time = time.time()
    while current_scroll_position <= new_height:
        if time.time() - start_time > 2:  # если прошло более 2 секунд, выходим из цикла
            break
        current_scroll_position += speed
        driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
        new_height = driver.execute_script("return document.body.scrollHeight")
        time.sleep(0.1)

    # Отримуємо самий частотний вираз біграмми і триграмми    
    title_text = driver.title                                           # Текст з тега <title> сайта
    body_text = driver.find_element(By.CSS_SELECTOR, "body").text       # Извлекаем текст из body
    frequent_phrase_title = most_frequent_phrase_in_body(title_text, body_text)

    # Випадковий ключове слово з поля "keys": ["House", "slot game"] та підставляємо в тег <a>
    random_key_poisk = random.choice(email_json_info["keys"])
    a_href_key_poisk = f'<a href="{my_site_backlink}" title="{random_key_poisk}">{random_key_poisk}</a>'

    # Создаем коментарий
    # comment_ai = promt_openai(site_url, title_url, random_key_poisk)
    my_new_comment = random.choice(comments_prompt)
    my_new_comment = my_new_comment.format(title_url=frequent_phrase_title, key_game=a_href_key_poisk)

    for _ in range(3):  # Вводим цикл для повторения до 3 раз
        for instruction in instructions:
            action, code = list(instruction.items())[0]

            # Виконуємо код інструкції, використовуючи exec. Зауважте, що це може бути потенційно небезпечно,
            # якщо інструкції не є надійними, оскільки exec виконує будь-який переданий йому код.
            try:
                exec(code)
            except Exception as e:
                print(f"Error {url} - '{action}': {e}")
                driver.get(url)
                continue
        print(f"OK for - {url}")
        print(my_new_comment)
        
        # Повторно заходим на страницу - таким образом обновляя ее 33
        driver.get(url)
        # driver.refresh()
        wait_for_page_load(driver, check_frequency=1, timeout=10)

        # Перевіряємо наявність мого URL сайту на сторінці
        
        if clean_site_url in driver.page_source:
            # Додаємо URL до файлу, якщо текст знайдено
            with open(f'{current_folder}\\result_links_txt\\{clean_site_url}_{formatted_date}.txt', 'a') as file:
                file.write(f"{url}\n")
            break  # Если "author" найден, прерываем цикл
        else:
            print(f"Url not found, retrying for {url}")
    
    if clean_site_url not in driver.page_source:
        print(f"!!!! Failed to find URL in {url} after 3 attempts")
    

# Функція для обробки інструкцій
def process_instructions(email_json_info):
    # логін і пароль з вхідного словника
    email = email_json_info["email"]
    password = email_json_info["password"]

    # Ініціалізуємо веб-драйвер Chrome
    # Chrome Options
    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={random.choice(user_agent)}")          # User-agent
    # chrome_options.add_argument("--blink-settings=imagesEnabled=false")           # Отключение отображения изображений (опционально)
    chrome_options.add_argument("--disable-notifications")                          # Отключение уведомлений (опционально)
    # Chrome Service
    ser = Service(executable_path = f"{current_folder}\\Webdriver_Chrome\\114-0-5735-90\\chromedriver.exe")
    driver = uc.Chrome(service=ser, options=chrome_options)                         # Undetected Chrome
    driver.maximize_window()                                                        # Chrome Вікно відкрити максимально

    # TODO: GMAIL - Переходимо на сторінку Gmail
    storinka_gmail_vhid = "https://mail.google.com"
    driver.get(storinka_gmail_vhid)
    
    # COOKIES LOAD - Завантажуємо файли cookie
    load_cookies(driver, email)
    time.sleep(1)
    # Оновлюємо сторінку
    driver.refresh()
    time.sleep(2)

    # Якщо поточний URL не "mail.google.com" виконуємо вхід
    if storinka_gmail_vhid not in driver.current_url:
        login_to_gmail(driver, email, password)
        # Зберігаємо файли cookie після входу в gmail
        save_cookies(driver, email)
        driver.refresh()    # Оновлюємо сторінку
        time.sleep(3)

    # TODO: Виконуємо інструкції для кожного URL по простановці беклінків
    for url, instructions in websites.items():
        execute_instructions(driver, url, instructions, **email_json_info)
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