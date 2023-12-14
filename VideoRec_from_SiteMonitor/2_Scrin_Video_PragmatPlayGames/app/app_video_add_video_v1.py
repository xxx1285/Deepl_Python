import os
import subprocess
import random

# Все функции, например:
def get_random_video_from_directory(directory):
    """Выбирает случайный видео файл из заданной директории."""
    video_files = [f for f in os.listdir(directory) if f.endswith(('.mp4', '.mkv', '.avi'))]
    return os.path.join(directory, random.choice(video_files)) if video_files else None


def cut_7_second_clip(video_path, output_path):
    """Обрезает 7-секундный фрагмент видео."""
    try:
        cmd = f'ffmpeg -ss 00:00:00 -i "{video_path}" -t 7 -c copy "{output_path}"'
        subprocess.run(cmd, shell=True, check=True)
    except Exception as e:
        print(f"Ошибка при обрезке видео: {e}")


def merge_videos(main_video_path, clip_video_path, output_path):
    """Объединяет два видео файла в один."""
    try:
        cmd = f'ffmpeg -i "{main_video_path}" -i "{clip_video_path}" -filter_complex \
        "[0:v]scale=540:960:force_original_aspect_ratio=decrease,pad=540:960:(ow-iw)/2:(oh-ih)/2,setsar=1[v0]; \
        [1:v]scale=540:960:force_original_aspect_ratio=decrease,pad=540:960:(ow-iw)/2:(oh-ih)/2,setsar=1[v1]; \
        [v0][v1]concat=n=2:v=1:a=0[out]" -map "[out]" "{output_path}"'
        subprocess.run(cmd, shell=True, check=True)
    except Exception as e:
        print(f"Ошибка при объединении видео: {e}")