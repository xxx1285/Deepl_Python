"""
    Функция принимает строку, удаляет все нерелевантные символы, 
    вычисляет математическое выражение и возвращает результат.
"""

from selenium.webdriver.common.by import By
import re


def fun_my_captcha_calculate_mathematic(driver, captcha_xpath):

    # Отримуємо текст з веб-сторінки
    element = driver.find_element(By.XPATH, captcha_xpath)
    text = element.text

    # Видаляємо все символи, що не відносяться до чисел і "(,),=,+,-,*,/"
    clean_text = re.sub("[^0-9\(\)\+\-\*/]", "", text)

    # Перевіряємо, чи не відсутній текст після очищення
    if not clean_text:
        raise ValueError('Немає тексту для обчислення після очищення')

    # Здійснюємо математичну операцію
    try:
        result = eval(clean_text)
    except SyntaxError:
        raise SyntaxError('Помилка у тексті для обчислення. Перевірте його.')

    return result