import imageio
import os
import random
import subprocess

def convert_gif_to_video(gif_path, output_video_path):
    # Команда для конвертации GIF в MP4 с использованием FFmpeg
    cmd = ['ffmpeg', '-i', gif_path, '-movflags', 'faststart', '-pix_fmt', 'yuv420p', '-vf', 'scale=trunc(iw/2)*2:trunc(ih/2)*2', output_video_path]
    try:
        subprocess.run(cmd, check=True)
        print(f"Видео {output_video_path} успешно создано.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при конвертации {gif_path} в видео: {e}")

def create_gif(directory, output_filename):
    # Получаем список всех файлов в каталоге и фильтруем, исключая те, что содержат "0.jpg"
    files = [f for f in os.listdir(directory) if f.endswith('.jpg') and '0.jpg' not in f]

    # Случайно перемешиваем список файлов
    random.shuffle(files)

    # Создаем GIF анимацию
    with imageio.get_writer(output_filename, mode='I', duration=600.1) as writer:
        for i in range(10):  # Создаем 20 кадров для 10-секундной анимации при 0.5 секунды на кадр
            file_path = os.path.join(directory, random.choice(files))  # Выбираем случайный файл
            image = imageio.imread(file_path)  # Читаем изображение
            writer.append_data(image)  # Добавляем изображение в GIF

    print(f"GIF анимация создана и сохранена как '{output_filename}'")
    # Путь к выходному видео файлу
    output_video_path = output_filename.replace('.gif', '.mp4')
    convert_gif_to_video(output_filename, output_video_path)

def process_directories(parent_directory):
    # Получаем список всех поддиректорий в указанной директоyрии
    directories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d))]

    # Для каждой директории создаем GIF анимацию
    for directory in directories:
        images_directory_path = os.path.join(parent_directory, directory, "images")
        # Проверяем, существует ли подкаталог 'images'
        if os.path.exists(images_directory_path):
            gif_filename = f"{directory}.gif"  # Имя файла GIF
            full_gif_path = os.path.join(images_directory_path, gif_filename)  # Полный путь к файлу GIF
            create_gif(images_directory_path, full_gif_path)
        else:
            print(f"В директории '{directory}' отсутствует подкаталог 'images'")
        print("ok")

# Пример использования функции
parent_directory_path = r'Parsing\Pragmatic-play\ResultGames\games-v1'
process_directories(parent_directory_path)
