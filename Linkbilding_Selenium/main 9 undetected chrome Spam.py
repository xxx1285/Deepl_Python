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
from baza_links.spam_comments import websites

# Function: Captcha
from captcha_img import fun_my_captcha_image
# Function: Формуэмо Частотну фразу Тайтл в Боді
from most_frequent_phrase import most_frequent_phrase_in_body


# База шаблонів коментарів
from baza_template_comments.templ_comments_en import comments_prompt


# Нинішній розділ
current_folder = os.path.basename(os.path.dirname(__file__))

# Дата - вивод в форматі: 10-06-2023
current_date = datetime.now()
formatted_date = current_date.strftime('%d-%m-%Y')

# EMAIL Google
with open(f'{current_folder}\\email\\spam.json') as json_file:
    email_json = json.load(json_file)

# USER-AGENT
user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36']

# Функція для виконання інструкцій
def execute_instructions(driver, url, instructions, **email_json_info):
    my_wait = WebDriverWait(driver, 10)  # ожидание до 10 секунд

    # Мій Чистий Сайт без "https://" i  "/"
    site_url = email_json_info['site_url']                  # Базовий url
    site_link = email_json_info['site_link']                # url для продвижения
    clean_site_url = site_url.split("//")[1].split("/")[0]

    # Перехід до веб-сайту
    driver.get(url)
    time.sleep(2)

    # Текст з тега <title>
    title_text = driver.title
    # Извлекаем текст из body
    body_text = driver.find_element(By.CSS_SELECTOR, "body").text
    # Отримуємо самий частотний вираз біграмми і триграмми
    frequent_phrase_title = most_frequent_phrase_in_body(title_text, body_text)


    rand_spam = str(random.randint(1, 9999))
    my_author = email_json_info['author']
    my_spam_author = f"{my_author} {rand_spam}"
    my_spam_email = f"{rand_spam}sdfefef@gmaild.com"
    my_spam_comment = f"{rand_spam} 只玩最好的游戏，使用防毒面具，{rand_spam} 方便的赌场 - <a href='https://vavadat5.fun/' title='{rand_spam} 和田市'>和田市</a>"

    for _ in range(3):  # Вводим цикл для повторения до 3 раз
        for instruction in instructions:
            action, code = list(instruction.items())[0]

            # Виконуємо код інструкції, використовуючи exec. Зауважте, що це може бути потенційно небезпечно,
            # якщо інструкції не є надійними, оскільки exec виконує будь-який переданий йому код.
            try:
                exec(code)
                time.sleep(1)
            except Exception as e:
                print(f"Error {url} - '{action}'")
                driver.get(url)
                continue
        
        # Обновляем страницу и ждем ее загрузки
        time.sleep(1)
        driver.refresh()


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

    # TODO: Виконуємо інструкції для кожного URL по простановці беклінків
    for _ in range(1500):
        for url, instructions in websites.items():
            execute_instructions(driver, url, instructions, **email_json_info)


    # Закриваємо драйвер
    driver.quit()


# Використовуємо бібліотеку multiprocessing, щоб запустити обробку інструкцій для кожної електронної пошти паралельно
if __name__ == '__main__':
    with Pool(5) as p:
        p.map(process_instructions, email_json.values())
