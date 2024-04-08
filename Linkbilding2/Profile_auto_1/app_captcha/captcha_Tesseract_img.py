import cv2
import os
import numpy as np
import pytesseract
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import httpx


def captcha_tesseract_image(driver, element_XPATH):
    # Укажите полный путь к исполняемому файлу Tesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Найдите элемент изображения по его XPATH
    wait = WebDriverWait(driver, 10)
    img = wait.until(EC.presence_of_element_located((By.XPATH, element_XPATH)))

    # Получаем абсолютный URL изображения
    img_url = img.get_attribute('src')

    # Создаем HTTP-клиент
    client = httpx.Client()

    # Получаем изображение от сервера
    response = client.get(img_url)

    # Сохраняем изображение локально
    image_path = r"Linkbilding2\Profile_auto_1\234234.png"
    with open(image_path, 'wb') as f:
        f.write(response.content)

    # Чтение изображения с альфа-каналом
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # Создание маски для прозрачных пикселей
    alpha_channel = image[:, :, 3]
    mask = alpha_channel == 0

    # Замена прозрачных пикселей на зеленый цвет
    image[mask] = [0, 255, 0, 255]

    # Расширение изображения
    border_size = 5
    image = cv2.copyMakeBorder(image, border_size, border_size, border_size, border_size, cv2.BORDER_CONSTANT, value=[0, 255, 0, 255])

    # Сохранение обработанного изображения
    output_path = r"Linkbilding2\Profile_auto_1\test.png"
    cv2.imwrite(output_path, image)

    # Распознавание текста на изображении
    recognized_text = pytesseract.image_to_string(output_path)

    recognized_text = recognized_text.replace('\n', '')

    # Удаление временного файла
    os.remove(image_path)
    os.remove(output_path)

    return recognized_text
