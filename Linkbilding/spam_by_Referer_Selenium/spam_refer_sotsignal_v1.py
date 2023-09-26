import time
import random
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType


def main():
    # Загрузка списка URL
    with open(r'Linkbilding\spam_by_Referer_Selenium\urls_txt\test.txt', 'r') as f:
        urls = [line.strip() for line in f]

    # Загрузка списка User-Agent
    with open(r'Linkbilding\spam_by_Referer_Selenium\referer_useragent_txt\user-agent.txt', 'r') as f:
        user_agents = [line.strip() for line in f]

    # Загрузка списка Referer
    with open(r'Linkbilding\spam_by_Referer_Selenium\referer_useragent_txt\referer.txt', 'r') as f:
        referers = [line.strip() for line in f]



        
    # Chrome Options
    chrome_options = Options()
    # chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")
    chrome_options.add_argument("--user-agent=Mozilla/5.22")
    chrome_options.add_argument("--accept-lang=ru-RU2,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6")
    # chrome_options.add_argument(f"referer={random.choice(referers)}")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--test-type=no")
    # IGNORE SSL
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors')


    chrome_options.add_argument("--disable-blink-features")
    # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])



    # Chrome Service
    ser = Service(executable_path = r"D:\Gembling\Deepl_Python\Deepl_Python\SETTINGS\Chrome\117.0.5938.62\chromedriver.exe")
    driver = uc.Chrome(service=ser, options=chrome_options)
    driver.maximize_window()


    # url = "https://httpbin.org/headers"
    # url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
    url = "https://bot.sannysoft.com/"  # proverka na bota
    # driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    #     "source": """
    #         const newProto = navigator.__proto__
    #         delete newProto.webdriver
    #         navigator.__proto__ = newProto
    #         """
    #     })
    # driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {'headers': {'Referer': 'https://22-referer.com', 'Test-Header': 'TestValue'}})


    driver.get(url)
    print('1')

if __name__ == '__main__':
    main()


    