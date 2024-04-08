from PIL import Image
import os
import random

def overlay_images(base_image_path, overlay_images_directory, output_path):
    # Открываем основное изображение
    base_image = Image.open(base_image_path)

    # Получаем список PNG файлов в указанной директории
    overlay_files = [f for f in os.listdir(overlay_images_directory) if f.endswith('.png')]
    if not overlay_files:
        raise ValueError("В директории нет PNG файлов")

    # Случайным образом выбираем файл для наложения
    overlay_image_path = os.path.join(overlay_images_directory, random.choice(overlay_files))
    overlay_image = Image.open(overlay_image_path)

    # Масштабируем его до ширины 300 пикселей, сохраняя пропорции
    base_width = 400
    wpercent = (base_width / float(overlay_image.size[0]))
    hsize = int((float(overlay_image.size[1]) * float(wpercent)))
    overlay_image_resized = overlay_image.resize((base_width, hsize), Image.Resampling.LANCZOS)


    # Располагаем поверх основного изображения, центрируем по ширине и отступаем от низа на 10 пикселей
    base_image.paste(overlay_image_resized, ((base_image.width - overlay_image_resized.width) // 2, base_image.height - overlay_image_resized.height - 5), overlay_image_resized)

    # Сохраняем результат
    # base_image.save(output_path)
    base_image.convert('RGB').save(output_path, "JPEG", quality=70)