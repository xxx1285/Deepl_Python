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
    chrome_options.add_argument(f"--user-agent={random.choice(user_agents)}")
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
    ser = Service(executable_path = r"D:\Gembling\Deepl_Python\Deepl_Python\SETTINGS\Chrome\Chrome_116_0_5845_96\chromedriver.exe")
    driver = uc.Chrome(service=ser, options=chrome_options)
    driver.maximize_window()


    # url = "https://twitter.com/brodieseo/status/1692051660171075967?s=46&t=MAyjtXoQ8UDGQsucT8lERw"
    # url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
    url = "https://bot.sannysoft.com/"  # proverka na bota
    # driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    #     "source": """
    #         const newProto = navigator.__proto__
    #         delete newProto.webdriver
    #         navigator.__proto__ = newProto
    #         """
    #     })


    driver.get(url)
    # Находит первый элемент <p> на странице
    element = driver.find_element(By.TAG_NAME, 'a')

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


    