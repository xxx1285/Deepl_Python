import os
import time
import csv
import json
from datetime import datetime
import random
import asyncio
from aiogram import Bot
import undetected_chromedriver as uc    # Undetected Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

# Function: Captcha
from captcha_module.captcha_img import fun_my_captcha_image
# Function: Формуэмо Частотну фразу Тайтл в Боді
from most_frequent_phrase import most_frequent_phrase_in_body
# База шаблонів коментарів
from comments_teplates.templ_comments_en import comments_prompt
# Links: Завантаження інструкцій та де ставити коментарі
from spam_baza_TIR2.spam_baza_TIR2_v1 import map_TIR2_comments

######################################################################################
######################################################################################
name = "Online1win"
email = "1win1win121@gmail.com"
keywords = "1win, 1win online, 1win casino, 1win official site, 1win com"
######################################################################################
######################################################################################


# Проверка !!!!!!
# map_TIR2_comments = {
#     "https://blogs.helsinki.fi": {
#         "urls": [
#             "/sosiologia-varjo-opas/129-2/",
#             "/sosiologia-varjo-opas/152-2/",
#             "/sosiologia-varjo-opas/140-2/",
#             "/sosiologia-varjo-opas/231-2/",
#             "/sosiologia-varjo-opas/136-2/",
#             "/sosiologia-varjo-opas/6321-2/",
#             "/sosiologia-varjo-opas/harj/"
#         ],
#         "selenium_actions": [
#             """a2 = driver.find_element(By.XPATH, '//*[@id="comment"]').click()""",
#             """a3 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
#             """x2 = driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinDeclineAll"]').click()""",
#             """a4 = driver.find_element(By.XPATH, '//*[@id="author"]').click()""",
#             """a5 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
#             """a6 = driver.find_element(By.XPATH, '//*[@id="email"]').click()""",
#             """a7 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
#             """a8 = driver.find_element(By.XPATH, '//*[@id="url"]').click()""",
#             """a9 = driver.find_element(By.XPATH, '//*[@id="url"]').send_keys(www)""",
#             """a10 = driver.find_element(By.XPATH, '//*[@id="submit"]').click()"""
#         ]
#     }
# }


# USER-AGENT
user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36']
# Нинішній розділ
current_folder = os.path.basename(os.path.dirname(__file__))
# Дата - вивод в форматі: 10-06-2023
current_date = datetime.now()
formatted_date = current_date.strftime('%d-%m-%Y')


# Сайти ТИР 1 які потрібно проспам в коментах
with open(f'Linkbilding\\{current_folder}\\url_TIR1\\TIR1.txt', 'r') as tir1_file:
    tir1_urls = [line.strip() for line in tir1_file]


# Загрузка токенов ТЕЛЕГРАМ из файла
async def send_message(text):
    with open(r'SETTINGS\telegram_bot_tokens.json', 'r') as file:
        tokens = json.load(file)
    CHANNEL_ID = '@mypyscript018'
    TOKEN = tokens["telegram_bot_mypyscript018"]
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHANNEL_ID, text=text)
    await bot.close()


def create_link_tag(tir1_url):
    """ створюємо посилання в тегу <a> з ключевою фразою"""
    keyword = random.choice(keywords.split(", ")).strip()
    return f'<a href="{tir1_url}">{keyword}</a>'


def create_random_comment(driver, link_tag):
    """ створюємо коментар """
    try:
        title_text = driver.title
        body_element = driver.find_element(By.TAG_NAME, 'header')
        body_text = body_element.text[:1000]
    except NoSuchElementException:
        title_text = "Best world game"
        body_text = "Best world game"
    
    title_url = most_frequent_phrase_in_body(title_text, body_text)
    comment = random.choice(comments_prompt)
    return comment.format(title_url=title_url, key_game=link_tag)



def generate_urls(map_dict, num_keys=5):
    """
    Генерує випадкові повні URL TIR2 на основі доменів та їх URL-закінчень зі словника map_dict.
    
    :param map_dict: Словник, де ключ - це домен, а значення - інформація про URL-закінчення та selenium дії.
    :param num_keys: Кількість доменів, які потрібно вибрати.
    :return: Список кортежів, де перший елемент - це повний URL, а другий - домен.
    """
    random_domains = random.sample(list(map_dict.keys()), min(len(map_dict), num_keys))
    generated_data = []
    for domain in random_domains:
        chosen_url_endings = map_dict[domain]['urls']
        random_url_endings = random.choice(chosen_url_endings)
        full_url = domain + random_url_endings
        generated_data.append((full_url, domain))
            
    return generated_data


def check_link_presence(driver, link_url):
    """Перевіряє наявність посилання на сторінці"""
    try:
        driver.find_element(By.CSS_SELECTOR, f"a[href*='{link_url}']")
        return True
    except NoSuchElementException:
        return False


def execute_selenium_actions(driver, tir1_url, tir2_url, actions):
    my_wait = WebDriverWait(driver, 40)
    driver.get(tir2_url)
    ######################################################################################
    # Прокручуємо сторінку вниз або не більше 2 секунд
    ######################################################################################
    current_scroll_position, new_height= 0, 1
    speed = 300
    start_time = time.time()
    try:
        while current_scroll_position <= new_height:
            if time.time() - start_time > 2:  # если прошло более 2 секунд, выходим из цикла
                break
            current_scroll_position += speed
            driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
            new_height = driver.execute_script("return document.body.scrollHeight")
            time.sleep(0.1)
    except:
        pass
    ######################################################################################
    ######################################################################################
    try:
        www = tir1_url
        link_tag = create_link_tag(tir1_url)
        comment = create_random_comment(driver, link_tag)

        for action in actions:
            time.sleep(1)
            exec(action)
    except Exception as e:
        asyncio.run(send_message(text=f"ERROR: {tir2_url}"))
        print(f"Error {tir2_url} with action '{action}': {e}")



def main():
    # Chrome Options
    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={random.choice(user_agent)}")
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")
    chrome_options.add_argument("--disable-notifications")
    # Chrome Service
    ser = Service(executable_path = f"Linkbilding\\{current_folder}\\Webdriver_Chrome\\114-0-5735-90\\chromedriver.exe")
    driver = uc.Chrome(service=ser, options=chrome_options)
    driver.maximize_window()

    
    # Ініціалізація csv файла
    with open(f'Linkbilding\\{current_folder}\\result.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        # Записуємо заголовок
        csvwriter.writerow(['formatted_date', 'tir1_url', 'tir2_url', 'link_present'])
        
        for tir1_url in tir1_urls:
            tir2_urls = generate_urls(map_TIR2_comments)
            for tir2_url, tir2_domain in tir2_urls:
                actions = map_TIR2_comments[tir2_domain]['selenium_actions']
                execute_selenium_actions(driver, tir1_url, tir2_url, actions)
                time.sleep(10)
                driver.get(tir2_url)
                time.sleep(3)

                # Перевірка наявності посилання tir1_url на сторінці tir2_url
                link_present = check_link_presence(driver, tir1_url)
                
                # Записуємо результат в csv файл
                csvwriter.writerow([formatted_date, tir1_url, tir2_url, link_present])
    
    
    asyncio.run(send_message(text="OK - Spam komments ZROBLENO"))
    driver.quit()

if __name__ == "__main__":
    main()