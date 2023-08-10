from PIL import Image, ImageSequence
import numpy as np
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pil_image = Image.open(r'D:\DEL\index(1).gif')

frames = [f.copy() for f in ImageSequence.Iterator(pil_image)]

frames = [np.array(f.convert('L')) for f in frames]

# Стекаем все кадры вместе, создавая трехмерный массив
stacked_frames = np.stack(frames, axis=-1)

# Выбираем медианное значение для каждого пикселя во всех кадрах
median_frame = np.median(stacked_frames, axis=-1)

# Конвертируем обратно в PIL.Image для использования pytesseract
median_frame = Image.fromarray(median_frame.astype(np.uint8))

custom_config = r'--oem 3 --psm 6'
text_captcha = pytesseract.image_to_string(median_frame, config=custom_config)

text_captcha = text_captcha.replace('\n', '')

print(text_captcha)
