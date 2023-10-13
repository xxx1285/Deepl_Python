from PIL import Image
import os
import piexif

# Шлях до основної папки, де знаходяться вкладені папки з зображеннями
main_folder_path = r"D:\Gembling\ALL-CASINO-IMAGES\gatesofolympus_club"

# Якість, яку ви хочете встановити для зображень
target_quality = 55

# Значення для Artist and copyright
author = "Garry Dranik"
copyright_value = "https://gatesofolympus.club/"

# Перебираємо всі папки та підпапки у основній папці
for root, dirs, files in os.walk(main_folder_path):
    for filename in files:
        if filename.endswith(".jpg"):  # Перевіряємо, чи файл має розширення .jpg
            # Формуємо повний шлях до файлу
            filepath = os.path.join(root, filename)

            # Відкриваємо зображення
            img = Image.open(filepath)

            # Перевіряємо, чи існують Exif метадані
            exif_info = img.info.get("exif")

            # Якщо Exif метадані існують, завантажуємо їх
            if exif_info:
                exif_dict = piexif.load(exif_info)
                exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "Interop": {}, "1st": {}, "thumbnail": None}
            else:
                exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "Interop": {}, "1st": {}, "thumbnail": None}

            # Додаємо інформацію про авторські права до Exif метаданих
            exif_dict["0th"][piexif.ImageIFD.Artist] = author
            exif_dict["0th"][piexif.ImageIFD.Copyright] = copyright_value
            # exif_dict["Exif"][piexif.ExifIFD.Copyright] = copyright_value

            # Створюємо рядок байтів з оновленими Exif метаданими
            exif_bytes = piexif.dump(exif_dict)
            
            # Додаємо Exif метадані до зображення та зберігаємо його
            # img.save(filepath, format="JPEG", quality=target_quality, exif=exif_bytes)
            img.save(filepath, format="JPEG", exif=exif_bytes)

print("!!!!!!!!!! змінено успішно.")
