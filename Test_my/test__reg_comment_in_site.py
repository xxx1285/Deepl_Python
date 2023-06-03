import time
from selenium import webdriver

# Открытие текстового документа для чтения
with open(r'Test_my\baza_domen_txt\data.txt', 'r') as f:
    data = f.readlines()

# Запуск браузера
driver = webdriver.Chrome()
driver.maximize_window()

# Перебор страниц из базы сайтов
for url in data:
    driver.get(url)
    time.sleep(3) # Задержка для загрузки страницы
    
    # Ввод имени
    name_input = driver.find_element_by_xpath('//input[@name="name"]')
    name_input.send_keys(data[0])
    
    # Ввод электронной почты
    email_input = driver.find_element_by_xpath('//input[@name="email"]')
    email_input.send_keys(data[1])
    
    # Ввод ссылки на сайт
    website_input = driver.find_element_by_xpath('//input[@name="website"]')
    website_input.send_keys(data[2])
    
    # Ввод комментария
    comment_input = driver.find_element_by_xpath('//textarea[@name="comment"]')
    comment_input.send_keys('Отличный сайт!')
    
    # Отправка комментария
    submit_button = driver.find_element_by_xpath('//input[@type="submit"]')
    submit_button.click()
    
# Закрытие браузера
driver.quit()