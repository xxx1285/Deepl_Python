"""
    0) Перейдите на официальный сайт FFMPEG (ffmpeg.org) и скачайте последнюю версию для Windows.
        ffmpeg -version
    1)  Перейдите на страницу релизов OpenH264 на GitHub и скачайте последнюю версию библиотеки (или одну из последних, если последняя не работает).
        https://github.com/cisco/openh264/releases
    2)  Убедитесь, что файл openh264-*.dll находится в папке, указанной в переменной среды PATH или в директории вашего Python проекта.
    3)  Перезапустите вашу среду разработки и попробуйте снова выполнить свой скрипт.
"""


import cv2
import pyautogui
import numpy as np
import time

def VideoRecorder(filename, duration, fps=20.0, region=None, top_text=""):
    """
    Записывает видео с экрана в течение заданной длительности.

    Args:
    - filename: Имя файла для сохранения видео.
    - duration: Длительность записи в секундах.
    - fps: Частота кадров в секунду.
    - region: Область экрана для записи (x, y, width, height).
    """
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')    #mp4v  X264    'avc1', или 'h264' VP90   (Good --- X264 (.mkv))
    out = cv2.VideoWriter(filename, fourcc, fps, (region[2], region[3]))

    start_time = time.perf_counter()

    frame_time = 0.5 / fps
    while time.perf_counter() - start_time < duration:
        img = pyautogui.screenshot(region=region)
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Добавление текста "Hello" после 5-й секунды
        if time.perf_counter() - start_time > 5:
            font = cv2.FONT_HERSHEY_SIMPLEX

            # Черная подложка для текста
            cv2.putText(frame, top_text, (10, 50), font, 0.7, (0, 0, 0), 7, cv2.LINE_AA)
            # Красный текст поверх подложки
            cv2.putText(frame, top_text, (10, 50), font, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

            # Белая обводка для черного текста
            cv2.putText(frame, top_text, (frame.shape[1] // 2 - len(top_text) * 5, frame.shape[0] // 2), font, 0.7, (255, 255, 255), 4, cv2.LINE_AA)
            # Черный текст поверх белой обводки
            cv2.putText(frame, top_text, (frame.shape[1] // 2 - len(top_text) * 5, frame.shape[0] // 2), font, 0.7, (0, 0, 0), 2, cv2.LINE_AA)



        out.write(frame)
        time.sleep(frame_time)

    out.release()
