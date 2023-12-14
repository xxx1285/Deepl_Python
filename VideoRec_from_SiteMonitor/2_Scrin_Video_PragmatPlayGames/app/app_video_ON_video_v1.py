import os
import subprocess
import random

def app_video_random_video_emotsiya(directory):
    """Выбирает случайный видео файл из заданной директории."""
    video_files = [f for f in os.listdir(directory) if f.endswith(('.mp4', '.mkv', '.avi', '.mov'))]
    return os.path.join(directory, random.choice(video_files)) if video_files else None

def app_video_resize(video_path, output_path, width, height):
    captions = ["Paris", "Berlin", "Rome", "Madrid",
    "Amsterdam", "Prague", "Vienna", "Moscow", "Athens",
    "Dublin", "Brussels", "Warsaw", "Lisbon", "Oslo", "Helsinki", "Stockholm", "Copenhagen", "Budapest", "Istanbul"
    "Helsinki", "Stockholm", "Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa"]
    caption = random.choice(captions)
    """Уменьшает видео до заданного размера."""
    try:

        cmd = (
            f'ffmpeg -i "{video_path}" '
            f'-vf "scale={width}:{height}, '
            f'drawtext=text=\'{caption}\':fontcolor=white:fontsize=20:x=(w-text_w)/2:y=h-30" '
            f'"{output_path}"'
        )


        subprocess.run(cmd, shell=True, check=True)
    except Exception as e:
        print(f"Ошибка при изменении размера видео: {e}")


# def app_video_merge_videos(main_video_path, overlay_video_path, output_path):
#     """Накладывает уменьшенное видео на основное видео."""
#     try:
#         overlay_duration = 6
#         overlay_end_time = 7 + overlay_duration  # Например, если накладываемое видео длится 5 секунд

#         cmd = f'ffmpeg -i "{main_video_path}" -i "{overlay_video_path}" -filter_complex \
#         "[0:v][1:v]overlay=W-w-5:550:enable=\'between(t,7,12)\'[out]" -map "[out]" -map 0:a? "{output_path}"'
#         subprocess.run(cmd, shell=True, check=True)
#     except Exception as e:
#         print(f"Ошибка при наложении видео: {e}")

def app_video_merge_videos(main_video_path, overlay_video_path, output_path):
    """Накладывает уменьшенное видео на основное видео."""
    try:
        # Добавление петли к накладываемому видео, чтобы предотвратить замерзание кадра
        loop_cmd = f'ffmpeg -stream_loop 3 -i "{overlay_video_path}" -c copy "{overlay_video_path}_looped.mp4"'

        # Команда для наложения видео
        overlay_cmd = f'ffmpeg -i "{main_video_path}" -i "{overlay_video_path}_looped.mp4" -filter_complex \
        "[0:v][1:v]overlay=W-w-5:350:enable=\'between(t,7,12)\'[out]" -map "[out]" -map 0:a? "{output_path}"'
        

        # Выполнение команд
        subprocess.run(loop_cmd, shell=True, check=True)
        subprocess.run(overlay_cmd, shell=True, check=True)

        # Удаление временного файла с петлёй
        os.remove(f"{overlay_video_path}_looped.mp4")
    except Exception as e:
        print(f"Ошибка при наложении видео: {e}")