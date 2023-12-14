import os
import subprocess

def app_video_merge_banner_niz(main_video_path, overlay_video_path, output_path):
    """Накладывает видео на основное видео с заданными размерами и позицией."""
    try:
        # Установка высоты основного видео
        main_video_height = 960  # Предполагаемая высота основного видео

        # Изменение размера накладываемого видео
        resized_overlay_video_path = f"{overlay_video_path}_resized.mp4"
        resize_cmd = f'ffmpeg -i "{overlay_video_path}" -vf "scale=540:-2" "{resized_overlay_video_path}"'
        subprocess.run(resize_cmd, shell=True, check=True)

        # Получение размеров измененного накладываемого видео
        probe_cmd_overlay = f'ffprobe -v error -select_streams v:0 -show_entries stream=height -of csv=s=x:p=0 "{resized_overlay_video_path}"'
        process_overlay = subprocess.run(probe_cmd_overlay, shell=True, text=True, capture_output=True, check=True)
        overlay_video_height = int(process_overlay.stdout.strip())

        # Расчет позиции наложения
        overlay_y_position = main_video_height - overlay_video_height  # Накладываемое видео в низу основного видео

        # Команда для наложения видео
        overlay_cmd = f'ffmpeg -i "{main_video_path}" -i "{resized_overlay_video_path}" -filter_complex \
        "[0:v][1:v]overlay=0:{overlay_y_position}:shortest=1[out]" -map "[out]" -map 0:a? "{output_path}"'
        subprocess.run(overlay_cmd, shell=True, check=True)

        # Удаление временного файла
        os.remove(resized_overlay_video_path)
    except Exception as e:
        print(f"Ошибка при наложении видео: {e}")

