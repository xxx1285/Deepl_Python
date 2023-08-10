from selenium.webdriver.common.by import By
import httpx
from PIL import Image
import pytesseract
from io import BytesIO

def compare_texts(text_captcha, text2):
    # Припущення: порівняння включає лише пробіли на початку і в кінці тексту
    return text_captcha.strip() == text2.strip() 

def process_image(driver, element_id, max_checks=3):
    # Вкажіть повний шлях до виконуваного файлу tesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Знайдіть елемент зображення за його ID
    img = driver.find_element(By.ID, element_id)

    # Отримайте абсолютний URL зображення
    img_url = img.get_attribute('src')

    # Створіть HTTP-клієнта за допомогою httpx
    client = httpx.Client()

    # Отримайте зображення від сервера
    response = client.get(img_url)

    # Відкрийте зображення за допомогою PIL
    img = Image.open(BytesIO(response.content))

    checks = 0
    while checks < max_checks:
        text_captcha = pytesseract.image_to_string(img)
        print(text_captcha)
        text2 = pytesseract.image_to_string(img)
        print(text2)
        if compare_texts(text_captcha, text2):
            print(text_captcha)
            return text_captcha  # повернути текст, якщо два розпізнавання збігаються
        checks += 1
    return None  # повернути None, якщо після max_checks спроб текст все ще не збігається
