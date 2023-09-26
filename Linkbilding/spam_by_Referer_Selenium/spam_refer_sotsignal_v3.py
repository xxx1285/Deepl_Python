import time
import random
from selenium_driverless.sync import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium_driverless.types.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType
# from cdp_socket.socket import CDPSocket


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



    screen_sizes_desktop = [(1366, 768),(1920, 1080),(1280, 800),(1440, 900),(1600, 900),(2560, 1440),(3840, 2160),(1024, 768),  
        (1280, 1024),(1680, 1050),(1152, 864),(1280, 720),(1360, 768),(1600, 1200),(1920, 1200),(2560, 1080),(3440, 1440)
        ]
    width, height = random.choice(screen_sizes_desktop)

    ua = UserAgent(browsers=['edge', 'chrome', 'firefox'])

        
    # Chrome Options
    options = webdriver.ChromeOptions()
    # options.add_argument(f"user-agent={random.choice(user_agents)}")
    # options.add_argument(f"--user-agent={random.choice(user_agents)}")
    # options.add_argument(f"--user-agent={ua.random}")
    options.add_argument(f"--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36")
    # options.add_argument("--user-agent=Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
    # options.add_argument("--headless")
    options.add_argument(f"--window-size={width},{height}")
    options.add_argument("--accept-lang=ru-RU2,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6")
    # options.add_argument(f"referer={random.choice(referers)}")
    # options.add_argument("--disable-notifications")
    # options.add_argument("--mute-audio")
    # options.add_argument("--test-type=no")
    # IGNORE SSL
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--disable-blink-features")
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # prefs = {"profile.managed_default_content_settings.images": 2}
    # options.add_experimental_option("prefs", prefs)


    driver = webdriver.Chrome(options=options)
    # driver.maximize_window()
        # Установка размера окна
    # driver.set_window_size(1520, 1080)
    time.sleep(3)
    driver.maximize_window()
    # перемещаем окно в левый верхний угол основного монитора 
    # driver.set_window_position(0, 0)


    # url = "https://twitter.com/brodieseo/status/1692051660171075967?s=46&t=MAyjtXoQ8UDGQsucT8lERw"
    # url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
    # url = "https://bot.sannysoft.com/"  # proverka na bota
    # Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36

    # url = "https://whoer.net/"  # proverka na bota
    url = "https://medium.com/"
    # url = "https://httpbin.org/headers" # headers
    # driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    #     "source": """
    #         const newProto = navigator.__proto__
    #         delete newProto.webdriver
    #         navigator.__proto__ = newProto
    #         """
    #     })


    driver.get(url)

    ######################################
    # Сloudflare.com
    time.sleep(2)
    if any("cloudflare.com" in iframe.get_attribute('src') for iframe in driver.find_elements(By.TAG_NAME, 'iframe')):
        driver.switch_to.frame(next(iframe for iframe in driver.find_elements(By.TAG_NAME, 'iframe') if "cloudflare.com" in iframe.get_attribute('src')))
    ######################################

    # Находит первый элемент <p> на странице
    element = driver.find_element(By.TAG_NAME, 'a').click()

    # Получение текущего текста элемента
    current_text = element.text

    # Разделение текста на слова и подсчет первых трех слов
    first_three_words = " ".join(current_text.split(" ")[:3])

    # Замена первых трех слов на HTML-ссылку
    new_text = current_text.replace(first_three_words, '<a id="revolclick" href="https://the-dog-house.org/ru/" target="_blank">Игра дог хаус</a>')

    # Используем JavaScript для обновления HTML содержимого элемента
    driver.execute_script("arguments[0].innerHTML = arguments[1];", element, new_text)
    
    element = driver.find_element(By.ID, 'revolclick').click()
    print('1')

if __name__ == '__main__':
    main()


    