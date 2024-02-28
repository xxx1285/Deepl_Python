import os
from PIL import Image

def process_and_save_image(image_path):
    # Загрузка изображения
    image = Image.open(image_path)
    original_width, original_height = image.size
    
    # Проверка и обрезка размеров изображения до 1620x1080, если необходимо
    if original_width == 1920 and original_height == 1080:
        left = (original_width - 1620) / 2
        top = 0
        right = left + 1620
        bottom = original_height
        image = image.crop((left, top, right, bottom))
    
    # Изменение размера изображения до 240x160
    new_image = image.resize((480, 320))
    # Сохранение изображения в том же каталоге с новым названием
    # Удаление "0" перед расширением и добавление "_mini"
    base, extension = os.path.splitext(image_path)
    if base.endswith("0"):
        base = base[:-1]  # Удаление "0" в конце названия файла
    new_image_path = f"{base}480x.webp"
    new_image.convert('RGB').save(new_image_path, "WEBP", quality=30)

    print(f'Processed mini image saved as: {new_image_path}')

def process_images_in_directories(parent_directory):
    # Перебор всех поддиректорий в указанной директории
    for root, dirs, files in os.walk(parent_directory):
        for file in files:
            # Проверка на соответствие условию "0.jpg" в конце имени файла
            if file.endswith("0.jpg"):
                full_file_path = os.path.join(root, file)
                print(f"Processing: {full_file_path}")
                # Применение функции обработки к изображению
                process_and_save_image(full_file_path)

# Пример использования
parent_directory_path = r'Parsing\Pragmatic-play\ResultGames\games-v1'  # Замените на путь к вашему каталогу
process_images_in_directories(parent_directory_path)
