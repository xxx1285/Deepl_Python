from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import httpx
import cv2
import numpy as np
from PIL import Image
import pytesseract
from io import BytesIO

def fun_my_captcha_image(driver, element_XPATH):
    # Вкажіть повний шлях до виконуваного файлу tesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Знайдіть елемент зображення за його ID
    wait = WebDriverWait(driver, 10) # чекаємо до 10 секунд
    img = wait.until(EC.presence_of_element_located((By.XPATH, element_XPATH))) # очікуємо, поки елемент не з'явиться

    # Отримайте абсолютний URL зображення
    img_url = img.get_attribute('src')

    # Створіть HTTP-клієнта за допомогою httpx
    client = httpx.Client()

    # Отримайте зображення від сервера
    response = client.get(img_url)

    # Завантажте зображення як масив NumPy
    nparr = np.frombuffer(response.content, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert the image to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply some image processing methods
    # Note: these methods may need to be tweaked depending on the specific CAPTCHA images you are working with
    gray = cv2.medianBlur(gray, 3)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Convert processed image back to PIL Image
    img = Image.fromarray(gray)

    # Using OEM 3 and PSM 6  Tesseract
    custom_config = r'--oem 3 --psm 10'

    text_captcha = pytesseract.image_to_string(img, config=custom_config)

    text_captcha = text_captcha.replace('\n', '')

    return text_captcha