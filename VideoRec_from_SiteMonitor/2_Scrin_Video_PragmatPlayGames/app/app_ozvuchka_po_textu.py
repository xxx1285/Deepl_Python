# text_to_speech.py
from gtts import gTTS
from pydub import AudioSegment
import io
import os

def text_to_speech_and_duration(text, lang='en', output_folder='VideoRec_from_SiteMonitor/2_Scrin_Video_PragmatPlayGames/output'):
    tts = gTTS(text, lang=lang, tld='co.in', lang_check=False)
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)

    audio = AudioSegment.from_file(audio_fp, format="mp3")
    duration_seconds = len(audio) / 1000.0

    ###################
    # Убедитесь, что папка для вывода существует
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_path = os.path.join(output_folder, 'output.mp3')
    audio.export(output_path, format='mp3')
    #######################

    return audio, duration_seconds


# Используйте функцию
text = "Unlock the treasures of Ancient Egypt with Nile Fortune. Played across 5×3 reels, this Egyptian-inspired slot features symbols such as the eye of Horus, Bastet and more. These must form a matched combination across 20 paylines to award a win. Mystery modifiers boost win potential and provide three varying features, including adding random Wilds to the gameboard, expanding the reels to become a 5×6 game grid and adding a multiplier to the matrix. \
        What to expect: \
        At least three Scatters are required to gain access to the free spins round and can award up to 20 free spins \
        A retrigger can be granted for landing an additional three scatters in the bonus, providing even more opportunity to create a win \
        The multiplier modifier has been upgraded in the free spins round, further boosting win potential."
audio, duration = text_to_speech_and_duration(text)
print(f"Длительность аудио: {duration} секунд")
