import os
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options
 

s = Service(executable_path = r"Linkbilding_Selenium\Webdriver_Chrome\113-0-5672\chromedriver.exe")

chrome_options = webdriver.ChromeOptions()

# Options
user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36']
chrome_options.add_argument(f"user-agent={random.choice(user_agent)}")  # User-agent
chrome_options.add_argument("--blink-settings=imagesEnabled=false")     # Отключение отображения изображений (опционально)
chrome_options.add_argument("--disable-notifications")                  # Отключение уведомлений (опционально)

# Driver
driver = webdriver.Chrome(service=s, options=chrome_options)



url = "https://www.blogger.com/about/?bpli=1"
# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
# driver = webdriver.Chrome(executable_path=r"Linkbilding_Selenium\Webdriver_Chrome\113-0-5672\chromedriver.exe")

try:
    driver.maximize_window()
    driver.get(url=url)
    time.sleep(5)
    create_akaunt = driver.find_element(By.XPATH, '//*[@id="maincontent"]/section[1]/header/a')
    time.sleep(3)
    ActionChains(driver).move_to_element(create_akaunt).click().perform()
    time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()