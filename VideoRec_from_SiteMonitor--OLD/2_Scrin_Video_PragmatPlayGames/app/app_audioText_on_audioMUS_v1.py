from gtts import gTTS
from pydub import AudioSegment
import io
import os
import random



def audioTextSpeach_on_audioMusic(text_in_audio, lang='en', audio_path=""):

    bg_music_folder = r"SETTINGS\Music-no-author"
    # Выбор случайного MP3 файла из указанного каталога
    bg_music_files = [f for f in os.listdir(bg_music_folder) if f.endswith('.mp3')]
    name_random_mus_file = random.choice(bg_music_files)
    random_bg_music_path = os.path.join(bg_music_folder, name_random_mus_file)
    print(random_bg_music_path)
    bg_music_audio = AudioSegment.from_mp3(random_bg_music_path)[13000:]

    if text_in_audio and len(text_in_audio) >= 100:
        # Создание аудио из текста
        tts = gTTS(text_in_audio, lang=lang, tld='ca', lang_check=False)
        # Language code --- https://gtts.readthedocs.io/en/latest/module.html
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        speech_audio = AudioSegment.from_file(audio_fp, format="mp3")

        # Уменьшение громкости фоновой музыки
        bg_music_audio = bg_music_audio - 15  # Уменьшаем громкость на 10 дБ

        # Обрезка фоновой музыки до длительности речи
        bg_music_audio = bg_music_audio[:len(speech_audio)]

        # Наложение речи на фоновую музыку
        combined_audio = speech_audio.overlay(bg_music_audio)
    else:
        combined_audio = bg_music_audio

    # Экспорт итогового файла
    if not os.path.exists(audio_path):
        os.makedirs(audio_path)
    output_path = os.path.join(audio_path, 'output.mp3')
    combined_audio.export(output_path, format='mp3')

    return name_random_mus_file
