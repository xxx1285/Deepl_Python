"""
    0) Перейдите на официальный сайт FFMPEG (ffmpeg.org) и скачайте последнюю версию для Windows.
        ffmpeg -version
    1)  Перейдите на страницу релизов OpenH264 на GitHub и скачайте последнюю версию библиотеки (или одну из последних, если последняя не работает).
        https://github.com/cisco/openh264/releases
    2)  Убедитесь, что файл openh264-*.dll находится в папке, указанной в переменной среды PATH или в директории вашего Python проекта.
    3)  Перезапустите вашу среду разработки и попробуйте снова выполнить свой скрипт.
"""


import cv2
import mss
import numpy as np
import time

def VideoRecorder(filename, duration, fps=24.0, region=None, top_text=""):
    """
    Записывает видео с экрана в течение заданной длительности.

    Args:
    - filename: Имя файла для сохранения видео.
    - duration: Длительность записи в секундах.
    - fps: Частота кадров в секунду.
    - region: Область экрана для записи (x, y, width, height).
    """
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(filename, fourcc, fps, (region['width'], region['height']))

    start_time = time.perf_counter()
    frame_time = 0.3 / fps
    with mss.mss() as sct:
        while time.perf_counter() - start_time < duration:
            img = sct.grab(region)
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

            font = cv2.FONT_HERSHEY_SIMPLEX

            # Добавление ВНИЗУ черной подложки с отступами
            cv2.rectangle(frame, (7, region['height'] - 290), (region['width'] - 7, region['height'] - 130), (0, 0, 255), -1)
            # Добавление ВНИЗУ текста на подложку 
            text = "FIRST DEPOSIT BONUS +500%"
            text_size = cv2.getTextSize(text, font, 1, 2)[0]
            # Вычисляем координаты X для центрирования текста
            text_x = (frame.shape[1] - text_size[0]) // 2
            text_y = region['height'] - 230  # Регулируйте координаты Y для центрирования текста
            cv2.putText(frame, text, (text_x, text_y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
            # Дополнительный текст ВНИЗУ 
            sub_text = "1win1win.com"
            sub_text_size = cv2.getTextSize(sub_text, font, 1.5, 2)[0]
            sub_text_x = (frame.shape[1] - sub_text_size[0]) // 2
            sub_text_y = region['height'] - 180  # Регулируйте координаты Y для центрирования текста
            cv2.putText(frame, sub_text, (sub_text_x, sub_text_y), font, 1.5, (255, 255, 255), 2, cv2.LINE_AA)
            # Дополнительный текст ВНИЗУ 
            sub_text = "Telegram: @BONUS100FD"
            sub_text_size = cv2.getTextSize(sub_text, font, 0.9, 2)[0]
            sub_text_x = (frame.shape[1] - sub_text_size[0]) // 2
            sub_text_y = region['height'] - 140  # Регулируйте координаты Y для центрирования текста
            cv2.putText(frame, sub_text, (sub_text_x, sub_text_y), font, 0.9, (255, 255, 255), 2, cv2.LINE_AA)

            # Добавление водяных знаков после 5-й секунды
            if time.perf_counter() - start_time > 5:

                # cv2.putText(frame, top_text, (координаты_x, координаты_y), font, размер_шрифта, (0, 255, 255), толщина_подложки, cv2.LINE_AA)

                # Черная подложка для текста
                cv2.putText(frame, top_text, (20, 80), font, 0.9, (0, 0, 0), 7, cv2.LINE_AA)
                # Красный текст поверх подложки
                cv2.putText(frame, top_text, (20, 80), font, 0.9, (0, 0, 255), 2, cv2.LINE_AA)

                # # Зеленая подложка для текста
                # cv2.putText(frame, top_text, (200, 950), font, 0.7, (0, 255, 0), 7, cv2.LINE_AA)
                # # Черный текст поверх подложки
                # cv2.putText(frame, top_text, (200, 950), font, 0.7, (0, 0, 0), 2, cv2.LINE_AA)


                # Белая обводка для черного текста
                cv2.putText(frame, top_text, (frame.shape[1] // 2 - len(top_text) * 5, frame.shape[0] // 2), font, 0.9, (255, 255, 255), 5, cv2.LINE_AA)
                # Черный текст поверх белой обводки
                cv2.putText(frame, top_text, (frame.shape[1] // 2 - len(top_text) * 5, frame.shape[0] // 2), font, 0.9, (0, 0, 0), 2, cv2.LINE_AA)

                # Желтая подложка для текста
                # cv2.putText(frame, top_text, (frame.shape[1] // 2 - len(top_text) * 5, frame.shape[0] // 2 + 148), font, 0.7, (0, 255, 255), 9, cv2.LINE_AA)
                # # Красный текст поверх подложки
                # cv2.putText(frame, top_text, (frame.shape[1] // 2 - len(top_text) * 5, frame.shape[0] // 2 + 147), font, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

                # Для правильного центрирования подложки и текста по ширине кадра, вы должны использовать размеры текста
                text_size = cv2.getTextSize(top_text, font, 0.7, 2)[0]

                # Вычисляем координаты X для центрирования текста
                text_x = (frame.shape[1] - text_size[0]) // 2

                # Желтая подложка для текста
                cv2.putText(frame, top_text, (text_x, frame.shape[0] // 2 + 148), font, 0.7, (0, 255, 255), 9, cv2.LINE_AA)
                # Красный текст поверх подложки
                cv2.putText(frame, top_text, (text_x, frame.shape[0] // 2 + 147), font, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

            out.write(frame)
            time.sleep(frame_time)

    out.release()
