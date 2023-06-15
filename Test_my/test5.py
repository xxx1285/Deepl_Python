import httpx
from PIL import Image
import pytesseract










# Укажите полный путь к исполняемому файлу tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

im = r"Test_my\lc_ep1.png"
# Используем Tesseract для распознавания текста
text = pytesseract.image_to_string(im)
print(text)
print(text)
