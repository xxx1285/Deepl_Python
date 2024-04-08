from TTS.api import TTS
from pydub import AudioSegment
import io
import os
import random

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)


def audioTextSpeach_on_audioMusic(text_in_audio, lang='en', audio_path=""):

    bg_music_folder = r"SETTINGS\Music-no-author"
    # Выбор случайного MP3 файла из указанного каталога
    bg_music_files = [f for f in os.listdir(bg_music_folder) if f.endswith('.mp3')]
    name_random_mus_file = random.choice(bg_music_files)
    random_bg_music_path = os.path.join(bg_music_folder, name_random_mus_file)
    print(random_bg_music_path)
    bg_music_audio = AudioSegment.from_mp3(random_bg_music_path)[13000:]

    if text_in_audio and len(text_in_audio) >= 100:
        speaker_wav = r"VideoRec_from_SiteMonitor\2_Scrin_Video_PragmatPlayGames\audio\714085__strangehorizon__zephy_like_a_fly.wav"
        text_in_audio_result = r"VideoRec_from_SiteMonitor\2_Scrin_Video_PragmatPlayGames\audio\result_del.wav"
        tts.tts_to_file(text=text_in_audio,
                file_path=text_in_audio_result,
                speaker_wav=speaker_wav,
                language="en")

        speech_audio = AudioSegment.from_file(text_in_audio_result, format="wav")

        # Уменьшение громкости фоновой музыки
        bg_music_audio = bg_music_audio - 22  # Уменьшаем громкость на 10 дБ

        # Обрезка фоновой музыки до длительности речи
        bg_music_audio = bg_music_audio[:len(speech_audio)]

        # Наложение речи на фоновую музыку
        combined_audio = speech_audio.overlay(bg_music_audio)
        # Удаляем голос по тексту WAV
        os.remove(text_in_audio_result)
    else:
        combined_audio = bg_music_audio

    # Экспорт итогового файла
    if not os.path.exists(audio_path):
        os.makedirs(audio_path)
    output_path = os.path.join(audio_path, 'output.mp3')
    combined_audio.export(output_path, format='mp3')

    return name_random_mus_file