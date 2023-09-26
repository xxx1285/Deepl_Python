import time
import random
# import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType


devices = {
    "iPhoneX1": {
        "deviceName": "iPhone X",
        "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        "touch": True,
        "mobile": True,
        "orientation": "portrait",
        "clientHints": {"platform": "iPhone", "mobile": True}
    },
    "iPhoneX2": {
        "deviceName": "iPhone X",
        "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
        "touch": True,
        "mobile": True,
        "orientation": "portrait",
        "clientHints": {"platform": "iPhone", "mobile": True}
    },
    "iPhoneX3": {
        "deviceName": "iPhone X",
        "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
        "touch": True,
        "mobile": True,
        "orientation": "portrait",
        "clientHints": {"platform": "iPhone", "mobile": True}
    },
    "GalaxyS91": {
        "deviceName": "Samsung Galaxy S9",
        "deviceMetrics": {"width": 360, "height": 740, "pixelRatio": 4.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
        "touch": True,
        "mobile": True,
        "orientation": "portrait",
        "clientHints": {"platform": "Android", "mobile": True}
    },
    "GalaxyS92": {
        "deviceName": "Samsung Galaxy S9",
        "deviceMetrics": {"width": 360, "height": 740, "pixelRatio": 4.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 9.0; SM-G960F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.85 Mobile Safari/537.36",
        "touch": True,
        "mobile": True,
        "orientation": "portrait",
        "clientHints": {"platform": "Android", "mobile": True}
    },
    "GalaxyS93": {
        "deviceName": "Samsung Galaxy S9",
        "deviceMetrics": {"width": 360, "height": 740, "pixelRatio": 4.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 10.0; SM-G960F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36",
        "touch": True,
        "mobile": True,
        "orientation": "portrait",
        "clientHints": {"platform": "Android", "mobile": True}
    }
}



options.add_argument("--accept-language=en;q=0.9,ru;q=0.8,es;q=0.7,pl;q=0.6,pt;q=0.5,fr;q=0.4,el;q=0.3,de;q=0.2,tr;q=0.1,hu;q=0.05,uk;q=0.04,it;q=0.03,ro;q=0.02,bg;q=0.01,fi;q=0.005,et;q=0.004,lt;q=0.003,lv;q=0.002,nl;q=0.001,cs;q=0.0005,da;q=0.0004,ja;q=0.0003,nb;q=0.0002,sk;q=0.0001")

accept_language_variations = [
    'en;q=0.9,ru;q=0.8,fr;q=0.7,de;q=0.6,es;q=0.5,pt;q=0.4,el;q=0.3,pl;q=0.2,tr;q=0.1',
    'en;q=0.9,ru;q=0.8,pt;q=0.7,fr;q=0.6,de;q=0.5,el;q=0.4,es;q=0.3,pl;q=0.2,hu;q=0.1',
    'en;q=0.9,ru;q=0.8,pl;q=0.7,es;q=0.6,pt;q=0.5,fr;q=0.4,el;q=0.3,de;q=0.2,tr;q=0.1',
    'en;q=0.9,ru;q=0.8,el;q=0.7,pt;q=0.6,fr;q=0.5,de;q=0.4,es;q=0.3,pl;q=0.2,hu;q=0.1',
    'en;q=0.9,ru;q=0.8,de;q=0.7,el;q=0.6,pt;q=0.5,fr;q=0.4,es;q=0.3,pl;q=0.2,tr;q=0.1',
    'en;q=0.9,ru;q=0.8,es;q=0.7,de;q=0.6,el;q=0.5,pt;q=0.4,fr;q=0.3,pl;q=0.2,hu;q=0.1',
    'en;q=0.9,ru;q=0.8,fr;q=0.7,pt;q=0.6,de;q=0.5,el;q=0.4,es;q=0.3,pl;q=0.2,tr;q=0.1',
    'en;q=0.9,ru;q=0.8,pt;q=0.7,el;q=0.6,fr;q=0.5,de;q=0.4,es;q=0.3,pl;q=0.2,hu;q=0.1',
    'en;q=0.9,ru;q=0.8,pl;q=0.7,pt;q=0.6,es;q=0.5,fr;q=0.4,el;q=0.3,de;q=0.2,tr;q=0.1',
    'en;q=0.9,ru;q=0.8,el;q=0.7,de;q=0.6,pt;q=0.5,fr;q=0.4,es;q=0.3,pl;q=0.2,hu;q=0.1'
]


screen_sizes = [
    (1366, 768),  # Ноутбуки
    (1920, 1080), # Лаптопы и стационарные мониторы
    (1280, 800),  # Ноутбуки
    (1440, 900),  # Ноутбуки
    (1600, 900),  # Лаптопы
    (2560, 1440), # Стационарные мониторы
    (3840, 2160), # 4K мониторы
    (1024, 768),  # Старые мониторы и ноутбуки
    (1280, 1024), # Старые мониторы
    (1680, 1050), # Лаптопы и мониторы
    (1152, 864),  # Старые мониторы
    (1280, 720),  # HD мониторы и ТВ
    (1360, 768),  # Ноутбуки и ТВ
    (1600, 1200), # Старые мониторы
    (1920, 1200), # Мониторы
    (2560, 1080), # Ультраширокие мониторы
    (3440, 1440)  # Ультраширокие мониторы
]

chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)


# Chrome Service
ser = Service(executable_path = r"D:\Gembling\Deepl_Python\Deepl_Python\SETTINGS\Chrome\Chrome_116_0_5845_96\chromedriver.exe")
driver = webdriver.Chrome(service=ser, options=chrome_options)
driver.maximize_window()


# url = "https://twitter.com/brodieseo/status/1692051660171075967?s=46&t=MAyjtXoQ8UDGQsucT8lERw"
# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
# url = "https://bot.sannysoft.com/"  # proverka na bota
url = "https://httpbin.org/headers"

driver.get(url)
print("ffff")
