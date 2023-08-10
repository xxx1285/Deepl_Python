import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import MoveTargetOutOfBoundsException, NoSuchElementException
import pandas as pd
import time
from PIL import Image, ImageChops, ImageOps, ImageDraw, ImageEnhance
import requests
from io import BytesIO
import os
import unicodedata
import random
import csv
import re
from unidecode import unidecode


#   ресайз фото та зменшуємо якість
def resize_and_save(image, path, quality):
    basewidth = 1000
    wpercent = (basewidth/float(image.size[0]))
    hsize = int((float(image.size[1])*float(wpercent)))
    img = image.resize((basewidth,hsize), Image.LANCZOS)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    img.save(path, 'webp', quality=quality)

#   проверить и закрыть регистрац меню
def click_on_element_if_exists(driver, admin_xpath = "//*[@id='app']/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[3]/svg"):
    try:
        driver.find_element(By.XPATH, admin_xpath).click()
        time.sleep(1)
    except NoSuchElementException:
        pass


user_agent = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
]

current_folder = os.path.basename(os.path.dirname(__file__))

chrome_options = Options()
chrome_options.add_argument(f"user-agent={random.choice(user_agent)}")
chrome_options.add_argument("--lang=en_US")
chrome_options.add_argument("--mute-audio") 
# chrome_options.add_argument("--blink-settings=imagesEnabled=false") 
chrome_options.add_argument("--disable-notifications")

ser = Service(executable_path = f"{current_folder}\\Webdriver_Chrome\\114-0-5735-90\\chromedriver.exe")

driver = uc.Chrome(service=ser, options=chrome_options)
# driver.maximize_window()
driver.set_window_size(1280, 1000)


games_data = []

driver.get('https://1whihg.top/casino/')
time.sleep(2)
# ESET antivirus
wait = WebDriverWait(driver, 25)
wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/table/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[3]/button[2]')))
driver.find_element(By.XPATH, '/html/body/div/table/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[3]/button[2]').click()
time.sleep(2)

# Выбор ТОП игор

top_game = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="casino"]/aside/div/section/main/ul[1]/li[8]/a')))
ActionChains(driver).move_to_element(top_game).click().perform()

#   прокрутка сторінки
current_scroll_position, new_height= 0, 1
speed = 1000
start_time = time.time()
while current_scroll_position <= new_height:
    if time.time() - start_time > 4:  # якщо минуло більше 4 секунд, виходимо з циклу
        break
    current_scroll_position += speed
    driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
    new_height = driver.execute_script("return document.body.scrollHeight")
    time.sleep(0.1)

games = driver.find_elements(By.CLASS_NAME, 'casino-game-item')


for idx in range(len(games)):
    idx = 35
    # try:
    number = str(idx)

    games = driver.find_elements(By.CLASS_NAME, 'casino-game-item')
    game = games[idx]
    game_img = game.find_element(By.CLASS_NAME, 'ResponsivePicture_img_N2UWA')
    img0_url = game_img.get_attribute('src')
    ActionChains(driver).move_to_element(game_img ).click().perform()
    time.sleep(5)

    screenshot = driver.get_screenshot_as_png()
    img1 = Image.open(BytesIO(screenshot))

    iframe_xpath = "//main//iframe"
    iframe = wait.until(EC.presence_of_element_located((By.XPATH, iframe_xpath)))
    iframe = driver.find_element(By.XPATH, iframe_xpath)

    iframe_url = iframe.get_attribute('src')

    # Відкриваємо нову вкладку
    driver.execute_script("window.open('');")
    # Переключаємось на вкладку
    driver.switch_to.window(driver.window_handles[-1])

    driver.get(iframe_url)
    #   проверить и закрыть регистрац меню
    time.sleep(1)
    click_on_element_if_exists(driver)
    time.sleep(13)

    title = driver.title
    if title:
        title = unicodedata.normalize('NFKD', title).encode('ASCII', 'ignore').decode()
    else:
        # Якщо title відсутнє або не знайдене, візьміть перші 15 символів iframe_url
        title = "DEL-" + iframe_url[10:20]
        title = unicodedata.normalize('NFKD', title).encode('ASCII', 'ignore').decode()

    title_alias = unidecode(title.lower())
    title_alias = re.sub(r'[^a-zA-Z0-9]+-*$' , '', re.sub(r'[^a-zA-Z0-9]+', '-', title_alias))

    # # TODO: Прокликиваем кнопку игры!!!!!!!!!!!!!!!
    # # Размер окна
    # window_width = driver.get_window_size()["width"]
    # window_height = driver.get_window_size()["height"]
    # click_x = window_width / 2
    # step = 50
    # height_limit = 400
    # game_img = driver.find_element(By.TAG_NAME, 'body')

    # for i in range(int(window_height), 0, -step):
    #     if window_height - i > height_limit:
    #         break
    #     click_y = i

    #     driver.execute_script(f"window.scrollTo(0, {window_height - click_y});")

    #     try:
    #         actions = ActionChains(driver)
    #         actions.move_to_element_with_offset(game_img, click_x, click_y)
    #         actions.click()
    #         actions.perform()
    #     except MoveTargetOutOfBoundsException:
    #         print(f"Failed to click at {click_x}, {click_y}. Skipping...")


    screenshot = driver.get_screenshot_as_png()
    img2 = Image.open(BytesIO(screenshot))

    games_data.append({'csv_id': idx, 'title': title, 'img0': f'{number}-{title_alias}/{title_alias}_slot.webp', 'img1': f'{number}-{title_alias}/1win-{title_alias}.webp', 'img2': f'{number}-{title_alias}/demo-{title_alias}-slot.webp', 'iframe': iframe_url, 'pagetitle': title, 'longtitle': title, 'description': title})

    img0 = Image.open(BytesIO(requests.get(img0_url).content))

    # улучшение контраста и яркости
    enhancer = ImageEnhance.Brightness(img0)
    img0 = enhancer.enhance(1.2)  # Увеличить яркость на 50%
    enhancer = ImageEnhance.Color(img0)
    img0 = enhancer.enhance(1.2)  # Увеличить насыщенность на 50%


    # # Применяем эффект сетки к изображению
    # img0 = apply_grid(img0, 2)
    img0 = img0.convert("RGB")

    if not os.path.exists(f'{current_folder}/img/{number}-{title_alias}'):
        os.makedirs(f'{current_folder}/img/{number}-{title_alias}')
    
    

    resize_and_save(img0, os.path.join(f'{current_folder}/img/{number}-{title_alias}', f'{title_alias}_slot.webp'), 70)
    resize_and_save(img1, os.path.join(f'{current_folder}/img/{number}-{title_alias}', f'1win-{title_alias}.webp'), 70)
    resize_and_save(img2, os.path.join(f'{current_folder}/img/{number}-{title_alias}', f'demo-{title_alias}-slot.webp'), 70)

    # except Exception as e:
    #     print(f"Виникла помилка з грою {idx}. Помилка: {e}")

    # Go back to the list after each game
    # отримуємо вікно, яке хочемо залишити відкритим
    main_window = driver.current_window_handle

    # закриваємо всі інші вікна
    for window in driver.window_handles:
        if window != main_window:
            driver.switch_to.window(window)
            driver.close()

    #   переключаємось назад на головне вікно
    driver.switch_to.window(main_window)
    driver.get('https://1whihg.top/casino/list/17')

    #   проверить и закрыть регистрац меню
    time.sleep(1)
    click_on_element_if_exists(driver)
    #   очікуємо блок ігор 
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'casino-game-item')))
    #   прокрутка сторінки
    current_scroll_position, new_height= 0, 1
    speed = 1000
    start_time = time.time()
    while current_scroll_position <= new_height:
        if time.time() - start_time > 4:  # якщо минуло більше 4 секунд, виходимо з циклу
            break
        current_scroll_position += speed
        driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
        new_height = driver.execute_script("return document.body.scrollHeight")
        time.sleep(0.1)
    time.sleep(2)



print('OK')
driver.quit()

csv_url_file = f'{current_folder}/games.csv'

with open(csv_url_file, 'w', newline='', encoding='utf-8') as file:
    field_names = ['csv_id', 'title', 'img0', 'img1', 'img2', 'iframe', 'pagetitle', 'longtitle', 'description']
    csv_writer = csv.DictWriter(file, fieldnames=field_names)
    csv_writer.writeheader()
    for game_data in games_data:
        csv_writer.writerow(game_data)
