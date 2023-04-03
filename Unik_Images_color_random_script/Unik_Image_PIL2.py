from PIL import Image, ImageEnhance
import os
import random
import shutil

# Путь к папке с фото
image_path = r'Unik_Images_color_random_script\all_images\images_unik'

# Количество каталогов, которые нужно создать
num_dirs = 10

# Создание новых каталогов
for i in range(num_dirs):
    new_dir = image_path + str(i+1)
    if not os.path.exists(new_dir):
        shutil.copytree(image_path, new_dir)

# Обработка фото в каждом каталоге
for i in range(num_dirs):
    current_dir = image_path + str(i+1)
    for root, dirs, files in os.walk(current_dir):
        # Генерация фильтра
        filter_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for filename in files:
            # Если это фото в формате webp, то генерируем новое изображение
            if filename.endswith(".webp"):
                # Открываем фото
                with Image.open(os.path.join(root, filename)) as image:
                    # Создаем новое изображение с фильтром
                    filtered_image = Image.new("RGB", image.size, filter_color)

                    # Наложение фильтра на изображение
                    alpha = 0.2  # Настройка глубины наложения
                    blended_image = Image.blend(image, filtered_image, alpha)

                    # Увеличение красочности цветов, не совпадающих с фильтром
                    color_enhancer = ImageEnhance.Color(blended_image)
                    color_factor = 1.5  # Настройка уровня увеличения красочности
                    enhanced_image = color_enhancer.enhance(color_factor)

                    # Сохранение нового изображения
                    new_filename = os.path.splitext(filename)[0] + ".webp"
                    new_filepath = os.path.join(root, new_filename)
                    with open(new_filepath, "wb") as f:
                        enhanced_image.save(f, "webp")
