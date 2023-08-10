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
from selenium.common.exceptions import InvalidCookieDomainException, UnableToSetCookieException, TimeoutException, NoSuchElementException
# кодировка в безопастный URL
from urllib.parse import quote


# Function: Captcha
from captcha_module.captcha_img import fun_my_captcha_image
# Function: Формуэмо Частотну фразу Тайтл в Боді
from most_frequent_phrase import most_frequent_phrase_in_body

##################################################################################################################
##################################################################################################################
# База шаблонів коментарів
from comments_teplates.templ_comments_en import comments_prompt
# Links: Завантаження інструкцій
from map_instruction_Backlinks.en_comments_profile import websites
# from map_instruction_Backlinks.ru_comments_profile_web2_0 import websites
##################################################################################################################
##################################################################################################################


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


# Функція реєстрації та входу - TopicIT
def reg_topic_it(driver, url, email, password, my_site_backlink):
    base_url = "https://connect.topicit.net/authorize?redirect_uri="
    encoded_redirect_url = quote(url, safe='')
    full_url = base_url + encoded_redirect_url

    WAIT_TIME = 5

    # проходимо авторизацію на сайті TopicIT
    driver.get(full_url)
    email_keys = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-login"]/div[1]/input')))
    email_keys.send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="form-login"]/div[2]/input').send_keys(password)
    button = driver.find_element(By.XPATH, '//*[@id="form-login"]/button')
    ActionChains(driver).move_to_element(button).click().perform()

    # повертаємось на Форум та активуємось - нажимеємо на кнопку
    driver.get(url)
    driver.implicitly_wait(5)
    button_topicit_xpath = '//*[@id="topicit-connect-0"]'
    try:
        button_topicit = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, button_topicit_xpath)))
        button_topicit.click()
        time.sleep(2)
    except TimeoutException:
        driver.get(url + "/login")
        button_topicit = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, button_topicit_xpath)))
        button_topicit.click()
        time.sleep(2)
    #   в профіль додаємо url link
    add_url_in_profile(driver, url, my_site_backlink)


#   в профіль додаємо url link
def add_url_in_profile(driver, url, my_site_backlink):
    try:
        driver.get(url + "profile?mode=editprofile")
        element_xpath = '//*[@id="profile_field_3_-10"]'
        wait_for_element(driver, element_xpath)
        if "login?redirect" in driver.current_url:
            raise Exception("Login redirect detected")
        textarea_url_add = driver.find_element(By.XPATH, '//*[@id="profile_field_3_-10"]')
        textarea_url_add.clear()
        textarea_url_add.send_keys(my_site_backlink)
        #   Нажимаем кнопку - Save         
        xpath_list_btn_save = ['//*[@id="ucp"]/fieldset/input[7]', '//*[@id="ucp"]/div[2]/fieldset[5]/dl/dd/input[7]']  # Добавьте все необходимые XPATH
        for xpath in xpath_list_btn_save:
            try:
                element = driver.find_element(By.XPATH, xpath)
                element.click()
            except NoSuchElementException:
                print(f"No element with XPath {xpath} found on the page.")
            except Exception as e:
                print(f"An error with XPath {xpath}: {e}")
    except Exception as e:
        print(f"Profile add Link ERROR: {e}")
        raise e



#   функція очікування загрузки СТОРІНКИ
def wait_for_element(driver, xpath, timeout=20):
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    except TimeoutException:
        print(f"Element with xpath {xpath} did not appear within {timeout} seconds.")

#   Random li in ul by XPATH
def click_random_li_element(driver, xpath):
    refresh_url(driver)
    driver.implicitly_wait(5)
    WAIT_TIME = 10 # установите ваше ожидание здесь
    try:
        elements = WebDriverWait(driver, WAIT_TIME).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        random_element = random.choice(elements)
        random_element.click()
    except TimeoutException:
        print("Не удалось найти элементы")

#   Отримуємо driver для сторінки (при переході на нову сторінку - перезагружаємо драйвер) 
#   Однако при обычной навигации (например, переход на другую страницу по ссылке) это обычно не требуется.
def refresh_url(driver):
    current_url = driver.current_url
    driver.get(current_url)


# Функція для виконання інструкцій
def execute_instructions(driver, url, instructions, **email_json_info):
    my_wait = WebDriverWait(driver, 10)  # ожидание до 10 секунд
    # Мій Чистий Сайт без "https://" i  "/"
    clean_site_url = email_json_info['site_url'].split("//")[1].split("/")[0]
    # Параметри розпаковані з JSON
    my_site_backlink = email_json_info['site_backlink'] 
    my_author = email_json_info['author']
    my_email =  email_json_info['email']
    my_password_fictiv =  email_json_info['password_fictiv']

    # Перехід до веб-сайту
    driver.get(url)
    time.sleep(2)

    # # COOKIES LOAD - Завантажуємо файли cookie
    load_cookies(driver, my_email)
    time.sleep(1)
    driver.refresh()

    ######################################################################################
    # Прокручуємо сторінку вниз або не більше 2 секунд
    ######################################################################################
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
    ######################################################################################
    ######################################################################################

    # TODO:     COMMENT     COMMENT     COMMENT
    # Отримуємо самий частотний вираз біграмми і триграмми, для логіки побудови коментаря   
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
    ######################################################################################
    ######################################################################################

    try:
        # реєстрація Topic IT
        reg_topic_it(driver, url, my_email, my_password_fictiv, my_site_backlink)
        # інструкції для кожного сайту
        for instruction in instructions:
            action, code = list(instruction.items())[0]
            # Виконуємо код інструкції, використовуючи exec. Зауважте, що це може бути потенційно небезпечно,
            try:
                exec(code)
            except Exception as e:
                print(f"Error {url} - '{action}': {e}")
                driver.get(url)
                continue
        print(f"OK for - {url}")
        # Обновляем страницу и ждем ее загрузки
        time.sleep(2)
        driver.refresh()
        time.sleep(2)

        # Перевіряємо наявність мого URL сайту на сторінці
        
        if clean_site_url in driver.page_source:
            # Додаємо URL до файлу, якщо текст знайдено
            with open(f'{current_folder}\\Final_result_links\\{clean_site_url}_{formatted_date}.txt', 'a') as file:
                file.write(f"{url}\n")
            # break  # Если "author" найден, прерываем цикл
        else:
            print(f"Url not found, retrying for {url}")
        
        if clean_site_url not in driver.page_source:
            print(f"!!!! Failed to find URL in {url} after 3 attempts")
    
    except Exception as e:
        print(f"Profile add Link ERROR: {e}")
    

# Функція для обробки інструкцій
def main_process_instructions(email_json_info):
    # логін з вхідного словника
    email = email_json_info["email"]

    # Chrome Options
    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={random.choice(user_agent)}")
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")
    chrome_options.add_argument("--disable-notifications")
    # Chrome Service
    ser = Service(executable_path = f"{current_folder}\\Webdriver_Chrome\\114-0-5735-90\\chromedriver.exe")
    driver = uc.Chrome(service=ser, options=chrome_options)
    driver.maximize_window()

    # TODO: Виконуємо інструкції для кожного URL по простановці беклінків
    for url, instructions in websites.items():

        current_url = driver.current_url
        print(current_url)

        execute_instructions(driver, url, instructions, **email_json_info)
        # Зберігаємо файли cookie
        save_cookies(driver, email)
        driver.refresh()    # Оновлюємо сторінку
        time.sleep(2)       # чекаємо, поки сторінка завантажиться

    # Закриваємо драйвер
    driver.quit()

# Без multiprocessing
if __name__ == '__main__':
    for email_info in email_json.values():
        main_process_instructions(email_info)