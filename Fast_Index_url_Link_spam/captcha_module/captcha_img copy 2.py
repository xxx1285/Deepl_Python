from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import httpx
from PIL import Image
import pytesseract
from io import BytesIO

def process_image(driver, element_id):
    # Вкажіть повний шлях до виконуваного файлу tesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Знайдіть елемент зображення за його ID
    wait = WebDriverWait(driver, 10) # чекаємо до 10 секунд
    img = wait.until(EC.presence_of_element_located((By.ID, element_id))) # очікуємо, поки елемент не з'явиться

    # Отримайте абсолютний URL зображення
    img_url = img.get_attribute('src')

    # Створіть HTTP-клієнта за допомогою httpx
    client = httpx.Client()

    # Отримайте зображення від сервера
    response = client.get(img_url)

    # Відкрийте зображення за допомогою PIL
    img = Image.open(BytesIO(response.content))

    # Using OEM 3 and PSM 6  Tesseract
    custom_config = r'--oem 3 --psm 6'

    text_captcha = pytesseract.image_to_string(img, config=custom_config)

    text_captcha = text_captcha.replace('\n', '')

    return text_captcha
