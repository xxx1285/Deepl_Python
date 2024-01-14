# проверка Undetect браузер - https://whoer.net/ru
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, \
                                        ElementClickInterceptedException, InvalidArgumentException

from app.app_user_agent_random import get_device_emulation_settings
import sys
sys.path.append('D:\\Gembling\\Deepl_Python\\Deepl_Python')
from Proxy.Restart_modem.E3372_Restart_control_clas_v1 import ModemController


PROXY = "127.0.0.1:3128"  # IP:PORT или "HOST:PORT" вашего прокси-сервера
# URLS_SLOTS = r'VideoRec_from_SiteMonitor\output_PragmaticGames\output-urls-games2.txt'
# URLS_ADRESS = r'GOOGLE\Google_mapsCID_Poxy_bot\input\output_result_CIT_URLs.txt'
URLS_ADRESS = r'GOOGLE\Google_mapsCID_Poxy_bot\input\output_result_CIT_URLs_only_borispol.txt'
# Создаем экземпляр класса с указанием базового URL модема
modem = ModemController("http://192.168.8.1")


def create_driver_with_emulation():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument(f'--proxy-server={PROXY}')
    # опции для игнорирования ошибок сертификатов в Chrome
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors-spki-list')

    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    emulation_settings = get_device_emulation_settings()
    if "deviceName" in emulation_settings:
        chrome_options.add_experimental_option("mobileEmulation", emulation_settings)
        print(emulation_settings)
    else:
        chrome_options.add_argument(f"user-agent={emulation_settings['userAgent']}")
        print(f"user-agent={emulation_settings['userAgent']}")

    ser = Service(executable_path=r"D:\Gembling\Deepl_Python\Deepl_Python\SETTINGS\Chrome\119.0.6045.105\chromedriver.exe")
    driver = webdriver.Chrome(service=ser, options=chrome_options)
    driver.set_page_load_timeout(40) 
    driver.maximize_window()

    return driver


def open_urls_and_click_button():
    with open(URLS_ADRESS, mode='r', encoding='utf-8') as file:
        lines = file.readlines()

    # меняем ip
    # modem.main_restart()
    
    # Выбор 5 случайных строк
    random_lines = random.sample(lines, 10)
    # random_lines = lines

    count = 0
    for line in random_lines:
        if count < 200:
            driver = create_driver_with_emulation()
            # прогреваем
            # try:
            #     driver.get("https://www.youtube.com/results?search_query=e3372h-607+port")
            # except TimeoutException:
            #     print("Страница не загрузилась за 30 секунд")
            try:
                driver.get("https://books.google.com/?authuser=0")
            except TimeoutException:
                print("Страница не загрузилась за 30 секунд")

            # try:
            #     driver.get("https://ifconfig.me/")
            # except TimeoutException:
            #     print("Страница не загрузилась за 30 секунд")
                
            # driver.get("https://google.com/")
            # driver.get("https://ifconfig.me/")
            # driver.get("https://www.whatismybrowser.com/")
            # driver.get("https://browserleaks.com/webrtc")
            # driver.get("https://www.browserscan.net/webrtc")
            # driver.get("https://browserleaks.com/")
            try:
                driver.get("https://2ip.ua/ru/")
            except TimeoutException:
                print("Страница не загрузилась за 30 секунд")
            # try:
            #     driver.get("https://time.is/")
            # except TimeoutException:
            #     print("Страница не загрузилась за 30 секунд")
            time.sleep(2)

            # переход на нужный нам url со списка
            new_url = line.strip()  # Удаление пробельных символов, включая символ новой строки
            try:
                driver.get(new_url)
                time.sleep(5)
            except TimeoutException:
                print("Страница не загрузилась за 30 секунд")
            time.sleep(5)

            
            flag = False

            # Если CID Кликаем и переходим на сайт !!!!!!!!!CID
            try:
                element = WebDriverWait(driver, 60).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="https://instadivan.com/"]'))
                ) 
                element.click()
                time.sleep(3)
                element = WebDriverWait(driver, 60).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/header/nav/div[1]/div/ul/li[2]/a'))
                )
                element.click()
                flag = True  # Клик прошел успешно
                # меняем ip
                driver.quit()
                modem.main_restart()
            except (TimeoutException, NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
                # меняем ip
                driver.quit()
                modem.main_restart()
                continue  # Переход к следующей итерации цикла

            # Если MAP Кликаем и переходим на сайт !!!!!!!!!MAPS
            # меняем ip
            driver.quit()
            modem.main_restart()


            # Если клик был успешен, перейти к следующему URL
            if flag:
                driver.quit()
                continue

            # Увеличиваем счетчик
            count += 1
        
        else:
            break


if __name__ == '__main__':
    open_urls_and_click_button()
    print("All Good")