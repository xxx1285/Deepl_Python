import os
import time
import random
from datetime import datetime
import undetected_chromedriver as uc    # Undetected Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidCookieDomainException, UnableToSetCookieException, TimeoutException


# Function: Captcha
from captcha_module.captcha_img import fun_my_captcha_image
# Function: Формуэмо Частотну фразу Тайтл в Боді
# from most_frequent_phrase import most_frequent_phrase_in_body
# База шаблонів коментарів для публікації
from templ_comments.comments_prompt import comments_prompt
# Links: Завантаження інструкцій для простановки беклинків
from templ_map_instruction_Backlinks.map_instruction_backlinks import map_instruction_backlinks


# USER-AGENT
user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36']


# Нинішній розділ
current_folder = os.path.basename(os.path.dirname(__file__))
# Дата - вивод в форматі: 10-06-2023
current_date = datetime.now()
formatted_date = current_date.strftime('%d-%m-%Y')


#######################################################################################
#   Ссылки что нужно проспамить
#######################################################################################
with open(f'{current_folder}\\backlinks_url\\backlinks_url.txt', 'r') as input_file:
    urls = input_file.readlines()


# Функція для виконання інструкцій для простановки беклинків
def execute_instructions(driver, url, instructions, comment_prompt):
    my_wait = WebDriverWait(driver, 10)  # ожидание до 10 секунд

    # Перехід до веб-сайту
    driver.get(url)
    time.sleep(2)

    # # Текст з тега <title>
    # title_text = driver.title
    # # Извлекаем текст из body
    # body_text = driver.find_element(By.CSS_SELECTOR, "body").text
    # # Отримуємо самий частотний вираз біграмми і триграмми
    # frequent_phrase_title = most_frequent_phrase_in_body(title_text, body_text)


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
def process_instructions():
    # Chrome Options
    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={random.choice(user_agent)}")
    chrome_options.add_argument("--disable-notifications")
    # Chrome Service
    ser = Service(executable_path = f"{current_folder}\\Webdriver_Chrome\\114-0-5735-90\\chromedriver.exe")
    # Ініціалізуємо веб-драйвер Chrome
    driver = uc.Chrome(service=ser, options=chrome_options)
    driver.maximize_window()


    # Для каждого URL из backlinks_url.txt
    for backlink_url in urls:
        #   удаляем лишние пробелы и символы новой строки
        backlink_url = backlink_url.strip()
        #   Мій Чистий Сайт без "https://" i  "/"
        clean_site_url = backlink_url.split("//")[1].split("/")[0]
        #   створюємо тег А з беклінком
        url_a_href = f'<a href="{backlink_url}" title="{clean_site_url}" target="_blank">{clean_site_url}</a>'


        #   Вибираємо випадковим чином 3 промпти для коментарів зі списку.
        selected_prompts = random.sample(comments_prompt, 3)
        #   Форматуємо вибрані промпти з вашою url.
        for prompt in selected_prompts:
            comment_prompt = prompt.format(backlink_url=url_a_href)                 # заменить {backlink_url} на url_a_href


            # выберите три случайных URL и их инструкции без повторения
            chosen_items = random.sample(list(map_instruction_backlinks.items()), 3)
            for url, instructions in chosen_items:
                execute_instructions(driver, url, instructions, comment_prompt)

    # Закриваємо драйвер
    driver.quit()


if __name__ == '__main__':
    process_instructions()
