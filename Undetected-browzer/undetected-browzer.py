import os
import csv
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, \
                                        ElementClickInterceptedException, InvalidArgumentException

user_agent = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Linux x86_64; Android 10; O) AppleWebKit/537.36 (KHTML, like Gecko) Orbita/118.0.0.0 Mobile Safari/537.36',
    # Добавьте дополнительные пользовательские агенты по желанию
]

# Chrome Options
chrome_options = Options()
chrome_options.add_argument(f"user-agent={random.choice(user_agent)}")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")  # Добавляем режим инкогнито
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Скрытие признаков автоматизации
# убираем надпись о Тестовом ПО в Браузере
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

# емулируем как мобильное устройство
# mobile_emulation = { "deviceName": "iPhone 12 Pro" }
# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
mobile_emulation = {
"deviceMetrics": { "width": 540, "height": 960, "pixelRatio": 2.0 },
"userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

# Настройка языка браузера на итальянский
chrome_options.add_argument("--lang=it")

# Chrome Service
ser = Service(executable_path=r"D:\Gembling\Deepl_Python\Deepl_Python\SETTINGS\Chrome\119.0.6045.105\chromedriver.exe")
driver = webdriver.Chrome(service=ser, options=chrome_options)
driver.maximize_window()
print("ggg")