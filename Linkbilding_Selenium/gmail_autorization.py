import os
import time
import json
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidCookieDomainException, UnableToSetCookieException, TimeoutException

# Gmail - функція для входу
def gmail_autoriz_fun(driver, email, password):
    # Инициализация объекта WebDriverWait
    my_wait = WebDriverWait(driver, 10)  # ожидание до 10 секунд
    
    # Ищем все элементы div с атрибутом data-email на странице
    elements = driver.find_elements(By.CSS_SELECTOR, "div[data-email]")

    # Проходимся по каждому элементу в списке
    for element in elements:
        # Проверяем, соответствует ли значение атрибута data-email нашей переменной email
        if element.get_attribute("data-email") == email:
            # Если да, то получаем родительский элемент
            parent_element = element.find_element(By.XPATH, "..")
            
            # Используем ActionChains для клика по родительскому элементу
            ActionChains(driver).move_to_element(parent_element).click().perform()
            break  # Если элемент найден и клик выполнен, то выходим из цикла

    if "https://accounts.google.com/AccountChooser/" in driver.current_url:
        # Чекаємо доки не зявиться поле пароль
        pass_xpath = '//*[@id="password"]/div[1]/div/div[1]/input'
        password_input = my_wait.until(EC.presence_of_element_located((By.XPATH, pass_xpath)))

        # Введення пароля
        password_input.send_keys(password)
        # Знаходимо кнопку - далі
        next_button_pass = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span')
        ActionChains(driver).move_to_element(next_button_pass).click(next_button_pass).perform()
        time.sleep(3)
