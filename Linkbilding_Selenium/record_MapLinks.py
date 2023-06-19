import os
import json
import time
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


###############################################################################
###############################################################################

record_url = "https://mail.google.com"

###############################################################################
###############################################################################

# Нинішній розділ
current_folder = os.path.basename(os.path.dirname(__file__))

# Дата - вивод в форматі: 10-06-2023
current_date = datetime.now()
formatted_date = current_date.strftime('%d-%m-%Y')

# USER-AGENT
user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36']


# Ініціалізуємо веб-драйвер Chrome
# Chrome Options
chrome_options = Options()
chrome_options.add_argument(f"user-agent={random.choice(user_agent)}")          # User-agent
# chrome_options.add_argument("--blink-settings=imagesEnabled=false")           # Отключение отображения изображений (опционально)
chrome_options.add_argument("--disable-notifications")                          # Отключение уведомлений (опционально)
# Chrome Service
ser = Service(executable_path = f"{current_folder}\\Webdriver_Chrome\\114-0-5735-90\\chromedriver.exe")
driver = uc.Chrome(service=ser, options=chrome_options)                         # Undetected Chrome
driver.maximize_window()

driver.get(record_url)

actions = []

def click_element(xpath):
    global actions
    driver.find_element(By.XPATH, xpath).click()
    actions.append({"click": f'driver.find_element(By.XPATH, "{xpath}").click()'})

def send_keys_element(xpath, keys):
    global actions
    driver.find_element(By.XPATH, xpath).send_keys(keys)
    actions.append({"send_keys": f'driver.find_element(By.XPATH, "{xpath}").send_keys("{keys}")'})

# Все действия, которые вы хотите выполнить, должны быть обернуты функциями
click_element('//*[@id="submit"]')
send_keys_element('//*[@id="email"]', 'test@example.com')

# После того, как все действия выполнены, вы можете сохранить их в формате JSON
import json
with open(f'{current_folder}\\record_links\\{formatted_date}.json', 'a') as f:
    json.dump(actions, f)
