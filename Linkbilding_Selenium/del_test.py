"""
    Функция принимает строку, удаляет все нерелевантные символы, 
    вычисляет математическое выражение и возвращает результат.
"""

from selenium.webdriver.common.by import By
import re


def captcha_calculate_mathematic_XPATH(driver, xpath):

    # Отримуємо текст з веб-сторінки
    element = driver.find_element(By.XPATH, xpath)
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