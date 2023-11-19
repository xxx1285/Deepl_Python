import cv2
from PIL import ImageGrab
import numpy as np
import time

class ScreenRecorder:
    def __init__(self, filename, framerate=20.0, resolution=(1170, 2532)):
        self.filename = filename
        self.framerate = framerate
        self.resolution = resolution
        self.is_recording = False
        self.out = None

    def start_recording(self):
        # Определение кодека и создание объекта VideoWriter
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Используйте 'XVID', если 'mp4v' не работает
        self.out = cv2.VideoWriter(self.filename, fourcc, self.framerate, self.resolution)

        self.is_recording = True
        while self.is_recording:
            img = ImageGrab.grab()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            frame_resized = cv2.resize(frame, self.resolution)
            self.out.write(frame_resized)
            time.sleep(1 / self.framerate)

    def stop_recording(self):
        self.is_recording = False
        if self.out is not None:
            self.out.release()
