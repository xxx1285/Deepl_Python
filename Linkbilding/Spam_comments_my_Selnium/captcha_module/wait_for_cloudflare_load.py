"""
    Функция, которая проверяет наличие "Cloudflare" элемента на странице и затем ожидает его исчезновения
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def wait_for_cloudflare_to_disappear(driver):
    try:
        # Проверяем наличие элемента на странице 
        driver.find_element(By.XPATH, '//*[@id="footer-text"]/a[contains(text(), "Cloudflare")]')
        # Если элемент найден, ждем его исчезновения
        WebDriverWait(driver, 15).until(
            EC.invisibility_of_element_located((By.XPATH, '//*[@id="footer-text"]/a[contains(text(), "Cloudflare")]'))
        )
    except NoSuchElementException:
        print("Элемент Cloudflare не найден на странице.")
    except TimeoutException:
        print("Элемент Cloudflare не исчез в течение 15 секунд.")