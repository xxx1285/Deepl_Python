from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def wait_for_page_load(driver, check_frequency=3, timeout=10):
    """
    Функция ожидает полной загрузки страницы.
    driver - экземпляр WebDriver.
    check_frequency - частота проверки в секундах.
    timeout - время ожидания в секундах (по умолчанию 10 секунд).
    """
    try:
        WebDriverWait(driver, timeout, poll_frequency=check_frequency).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )
    except TimeoutException:
        print("Время ожидания истекло после {} секунд, пока страница полностью не загрузилась".format(timeout))
