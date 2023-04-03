from PIL import Image
import os
import random
import shutil


# Шлях до папки з фото
image_path = r'Unik_Images_color_random_script\images_unik'


# Кількість каталогів, які потрібно створити
num_dirs = 10

# Створення нових каталогів
for i in range(num_dirs):
    new_dir = image_path + str(i+1)
    if not os.path.exists(new_dir):
        shutil.copytree(image_path, new_dir)

# Перебір фото в кожному каталозі
for i in range(num_dirs):
    current_dir = "images_unik" + str(i+1)
    for root, dirs, files in os.walk(current_dir):
        for filename in files:
            # Якщо це фото у форматі webp, то генеруємо нові зображення
            if filename.endswith(".webp"):
                # Відкриваємо фото
                with Image.open(os.path.join(root, filename)) as image:
                    # Генерація нових зображень
                    for j in range(10):
                        # Генерація нового зображення
                        new_image = Image.new("RGB", image.size, "white")
                        pixels = new_image.load()
                        for x in range(image.size[0]):
                            for y in range(image.size[1]):
                                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                                pixels[x,y] = color

                        # Збереження нового зображення
                        new_filename = os.path.splitext(filename)[0] + "_" + str(j+1) + ".webp"
                        new_filepath = os.path.join(root, new_filename)
                        with open(new_filepath, "wb") as f:
                            new_image.save(f, "webp")
