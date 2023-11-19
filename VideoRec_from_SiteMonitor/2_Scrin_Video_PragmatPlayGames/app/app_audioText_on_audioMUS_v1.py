from gtts import gTTS
from pydub import AudioSegment
import io
import os
import random



def audioTextSpeach_on_audioMusic(text_in_audio, lang='en', output_mp3_path="", bg_music_folder=""):
    # Создание аудио из текста
    tts = gTTS(text_in_audio, lang=lang, tld='co.in', lang_check=False)
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    speech_audio = AudioSegment.from_file(audio_fp, format="mp3")


    # Выбор случайного MP3 файла из указанного каталога
    bg_music_files = [f for f in os.listdir(bg_music_folder) if f.endswith('.mp3')]
    random_bg_music_path = os.path.join(bg_music_folder, random.choice(bg_music_files))
    bg_music_audio = AudioSegment.from_mp3(random_bg_music_path)

    # Уменьшение громкости фоновой музыки
    bg_music_audio = bg_music_audio - 20  # Уменьшаем громкость на 10 дБ

    # Обрезка фоновой музыки до длительности речи
    bg_music_audio = bg_music_audio[:len(speech_audio)]

    # Наложение речи на фоновую музыку
    combined_audio = speech_audio.overlay(bg_music_audio)

    # Экспорт итогового файла
    if not os.path.exists(output_mp3_path):
        os.makedirs(output_mp3_path)
    output_path = os.path.join(output_mp3_path, 'output.mp3')
    combined_audio.export(output_path, format='mp3')
