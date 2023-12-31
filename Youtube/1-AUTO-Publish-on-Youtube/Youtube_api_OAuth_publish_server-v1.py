#!/usr/bin/python3

# python /home/vilmebel/dynamiteminergames.com/www/Youtube-API/youtube-api-video-v1.py
# CRON: /usr/bin/python3.10 /home/vilmebel/dynamiteminergames.com/www/Youtube-API/youtube-api-video-v1.py
# pip install --user oauth2client            install on HOSTONG
# Права доступа к скрипту должны быть 750 или rwxr-x—.
# Права доступа к каталогу, в котором размещён скрипт, должны быть 750 или rwxr-x—.

import datetime
import pandas as pd
import os
import random
import httplib2
import asyncio
import httpx
import json
from aiogram import Bot
from aiogram.types import FSInputFile
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Налаштування OAuth 2.0
CLIENT_SECRETS_FILE = r"/home/vilmebel/dynamiteminergames.com/www/Youtube-API/channel-IvanDombro/json_key/client_secret_75919922252-md40qq7of31jc7jvlsbo2e8mrtp96ud1.apps.googleusercontent.com.json"
SCOPES = ['https://www.googleapis.com/auth/youtube.upload',
          'https://www.googleapis.com/auth/youtube.readonly',
          'https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
CSV_ALL_VIDEOS = r'/home/vilmebel/dynamiteminergames.com/www/Youtube-API/channel-IvanDombro/csv/output_games7.csv'
GAMES_CATALOG = r'/home/vilmebel/dynamiteminergames.com/www/Youtube-API/channel-IvanDombro/games/games-v7'
OAUTH_TOKEN = r'/home/vilmebel/dynamiteminergames.com/www/Youtube-API/channel-IvanDombro/json_key/token-v2.json'
TELEGRAM_BOT_TOKEN = r'/home/vilmebel/dynamiteminergames.com/www/TELEGRAM-BOT/telegram_bot_tokens.json'
POPULAR_HASHTAGS = r'/home/vilmebel/dynamiteminergames.com/www/Youtube-API/channel-IvanDombro/tags/popular_hashtags.txt'

# Настройка Telegram бота
with open(TELEGRAM_BOT_TOKEN, 'r') as file:
    tokens = json.load(file)
TOKEN = tokens["telegram_bot_mypyscript018"]
bot = Bot(token=TOKEN)
CHANNEL_ID = '@mypyscript018'

# Telegram fuction TEXT
async def send_Telegram_message(text):
    await bot.send_message(chat_id=CHANNEL_ID, text=text)
# Telegram fuction VIDEO and Caption
async def send_Telegram_video(video_file, caption):
    if os.path.exists(video_file):
        video = FSInputFile(video_file)
        await bot.send_video(chat_id=CHANNEL_ID, video=video, caption=caption)
    else:
        await bot.send_message(chat_id=CHANNEL_ID, text=f"Error: File does not exist at {video_file}")

# текущее время
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M")

###########################################################################################
# HASHTAGS
###########################################################################################
def convert_title_with_Tags(title):
    # Convert Title with TAGS
    exclude = {'stake', 'slots', 'staking', 'playing', 'slot'}
    words = title.split()
    first_word = next(("#" + word.lower() for word in words if len(word) >= 3 and word.lower() not in exclude), "#1win")
    return first_word

def select_4_hashtags():
    # выбираем хештеги со списка
    hashtags = [
        "stake", "slot", "staking", "playing", "casino", 
        "jackpot", "winning", "casinoLife", "the day before review", "BigWin", 
        "brents slot channel", "slot machine secrets", "slot machine big win", "ho slot cars", "lightning link slot", 
        "the big payback slot", "lock it link slot machine", "top dollar slot machine wins", "new slot machine",
        "bigprizes", "wheel of fortune slot machine", "brian christopher slot", "slot machine bonus", "casinoplay",
        "quick hits slot machine jackpot", "slot wins", "kuri slot", "live slot play", "slot lover",
        "slot machine wins", "high limit slot jackpots", "jackpot slot machine", "CasinoOnline", "SlotStrategy",
        "ng slot", "wild life slot machine", "biggest slot machine win ever", "top dollar slot machine wins", "VegasSlots", "JackpotParty",
        "CasinoRoyale", "slot machine jackpot", "slot lady", "slot queen", "akafuji slot", "buffalo gold slot machine", "slot cats",
        "slot videos", "slot machines"
    ]
    return random.sample(hashtags, 4)

def select_random_tags_from_txt_file(filename, number_of_lines=4):
    # выбираем хештеги с файла TXT популярных тегов
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        # Удаление возможных пробелов и переносов строк в конце каждой строки
        lines = [line.strip() for line in lines]
        # Проверка, достаточно ли строк в файле для выбора
        if len(lines) < number_of_lines:
            raise ValueError(f"Файл содержит только {len(lines)} строк(и), что меньше запрашиваемых {number_of_lines}.")
        # Выбор случайных строк
        random_lines = random.sample(lines, number_of_lines)
        return random_lines
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{filename}' не найден.")
    except Exception as e:
        raise Exception(f"Произошла ошибка: {e}")
    
def tags_from_title(title):
    # создаем хештеги с Title разбивая на фразы
    words = title.split()
    titles = [' '.join(words[:i]) for i in range(len(words), 0, -1) if len(words[i-1]) > 3]
    return titles

####################################################################################
####################################################################################

def generate_random_title(title):
    title_upper = title.upper()
    templates = [
        f"🔥 Hot Streaks in {title_upper} Beat the Odds",
        f"{title_upper} The Game Awards 2023 Showdown",
        f"Avatar Frontiers of {title_upper}",
        f"Genshin Impact 4.3 {title_upper} Adventure",
        f"Lethal Company {title_upper} Edition",
        f"Fortnite Movement in {title_upper}",
        f"Jimmy Carter's {title_upper} Quest",
        f"Dragon's Dogma Dark Arisen in {title_upper}",
        f"{title_upper} Journey Through the World of M5 Championship",
        f"{title_upper} vs Eagles The Ultimate Challenge",
        f"Explore the Depths of {title_upper} with Animal Trailer Reaction",
        f"Survive the {title_upper} in Telangana Election 2023",
        f"France vs Gibraltar The {title_upper} Challenge",
        f"Suicide Squad in {title_upper} Justice League Gameplay",
        f"Spotify Wrapped The {title_upper} Soundtrack Edition",
        f"{title_upper} The Artful Dodger's Heist",
        f"Worlds 2023 Finals The Ultimate {title_upper} Battle",
        f"House of the Dragon Season 2 The {title_upper} Saga",
        f"{title_upper} vs. Godzilla Battle for the New Empire",
        f"The {title_upper} Thanksgiving Parade Adventure",
        f"Dream Allegations The {title_upper} Mystery",
        f"Liverpool vs Crystal Palace in {title_upper} Showdown",
        f"Godzilla Minus One Atomic Breath {title_upper} Challenge",
        f"Kitsune Mysteries in {title_upper} World",
        f"Sparking Zero {title_upper} Quest",
        f"{title_upper} and the Portugal vs Iceland Face-off",
        f"Survival Squad {title_upper} Operation",
        f"Lethal Company Funny Moments in {title_upper}",
        f"{title_upper} Meet the Suicide Squad Kill the Justice League",
        f"Thanksgiving Parade Through {title_upper} Land",
        f"The Lethal Company Lore of {title_upper}",
        f"{title_upper} in the World of Avatar Frontiers of Pandora",
        f"Rise of the Ronin The {title_upper} Chronicles",
        f"Man United vs Galatasaray The {title_upper} Cup",
        f"Barcelona Girona Rivalry in {title_upper}",
        f"{title_upper} The Ultimate Thanksgiving Parade Quest",
        f"Godzilla x Kong The {title_upper} Empire",
        f"Fortnite Lego Adventure with {title_upper}",
        f"The Artful Dodger Strikes in {title_upper}",
        f"Sam Altman's {title_upper} Universe",
        f"{title_upper} and the Mystery of Gemini Remix Rumble",
        f"Cybertruck Delivery Event in the World of {title_upper}",
        f"The {title_upper} Game Awards Reaction Challenge",
        f"T1 vs WBG The Epic {title_upper} Showdown",
        f"Andre 3000 Flute in {title_upper} Symphony",
        f"Animal Movie Review The {title_upper} Critique",
        f"Last of Us 2 Remastered in {title_upper} Apocalypse",
        f"Kitsune Fruit Hunt in {title_upper} Fantasy",
        f"Please Donate Giveaway in the Realm of {title_upper}",
        f"Welcome to Samdalri The {title_upper} Journey",
        f"The Archies Review Inside {title_upper} World",
        f"Chill Kill Adventure with {title_upper}",
        f"Fortnite Chapter 5 The {title_upper} Saga",
        f"King of the Table 9 {title_upper} Championship",
        f"Lethal Company All Monsters in {title_upper}",
        f"{title_upper} and the Formula 1 Las Vegas Race",
        f"The {title_upper} Christmas Fireplace Experience",
        f"Survivor Series 2023 The {title_upper} Battle Royale",
        f"Rick and Morty Season 7 in {title_upper} Madness",
        f"F1 Vegas Grand Prix in {title_upper} Speed",
        f"LUXURIOUS {title_upper} 💎 1WIN LUXURY STAKES",
        f"EXPLOSIVE {title_upper} 🎃 1WIN MEGA PRIZES",
        f"ENERGIZING {title_upper} ⚡ 1WIN WINNING STREAK",
        f"LUCKY {title_upper} 🍀 1WIN LUCKY SPINS",
        f"EXPLORE {title_upper} 🎃 1WIN SLOT EXPLORER",
        f"KINGDOM {title_upper} 👑 1WIN KING OF SLOTS",
        f"STRATEGY {title_upper} 🏆 1WIN WINNING TACTICS",
        f"{title_upper} 🌟 EXCITING JACKPOT CHASE",
        f"{title_upper} 💰 THRILLING BIG WIN THRILLS",
        f"{title_upper} 🔥 ADVENTURE SPIN MANIA",
        f"{title_upper} 💎 LUXURIOUS LUXURY STAKES",
        f"{title_upper} 🎃 EXPLOSIVE MEGA PRIZES",
        f"{title_upper} ⚡ ENERGIZING WINNING STREAK",
        f"{title_upper} 🍀 LUCKY LUCKY SPINS",
        f"{title_upper} 🎰 VIBRANT SLOT SAGA",
        f"{title_upper} 💥 BURSTING BIG SCORE",
        f"{title_upper} 🚀 BLAST OFF BIG WINS | PRAGMATIC PLAY",
        f"{title_upper} 🏝 TROPICAL TREASURE HUNT | PRAGMATIC PLAY",
        f"{title_upper} 🎇 SPARKLING VICTORY RUSH | PRAGMATIC PLAY",
        f"{title_upper} 🍾 CHAMPAGNE SHOWERS OF WINS | PRAGMATIC PLAY",
        f"{title_upper} 💎 DIAMOND RICHES BONANZA | PRAGMATIC PLAY",
        f"{title_upper} 🔑 KEYS TO FORTUNE | PRAGMATIC PLAY",
        f"{title_upper} 🌞 SUNSHINE OF SUCCESS | PRAGMATIC PLAY",
        f"{title_upper} 🍀 FIELD OF FORTUNES | PRAGMATIC PLAY",
        f"{title_upper} 🌟 GALACTIC GOLD RUSH | PRAGMATIC PLAY",
        f"{title_upper} 🍭 SWEET SWEEPSTAKES | PRAGMATIC PLAY",
    ]
    return random.choice(templates)

# обрізаємо тайтл та текст по останньому слову по переданному ліміту
def truncate_to_last_word(s, max_length):
    if not s:  # Check if the string is empty
        return s
    if len(s) <= max_length:
        return s
    truncate_index = s.rfind(' ', 0, max_length)
    return s if truncate_index == -1 else s[:truncate_index]

# перетворюємо список url адрес відео в рядок
def create_video_list_string(video_urls):
    # Проверяем, не пуст ли список
    if not video_urls:
        return ""
    random_urls = random.sample(video_urls, min(5, len(video_urls)))
    video_list_str = "\n".join(random_urls)
    return video_list_str

# Youtube Thumb Images - Zastavka
def upload_thumbnail(youtube, video_id, thumbnail_file):
    thumbnail_request = youtube.thumbnails().set(
        videoId=video_id,
        media_body=MediaFileUpload(thumbnail_file, chunksize=-1, resumable=True)
    )
    thumbnail_request.execute()

# Функція для ініціалізації YouTube API
def get_authenticated_service():
    credentials = None
    # Проверка наличия файла с сохраненными учетными данными
    if os.path.exists(OAUTH_TOKEN):
        credentials = Credentials.from_authorized_user_file(OAUTH_TOKEN, SCOPES)
    # Если нет сохраненных учетных данных или они недействительны
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_local_server(port=8080)
        # Сохранение учетных данных для следующего запуска
        with open(OAUTH_TOKEN, 'w') as token:
            token.write(credentials.to_json())

    youtube = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

    # Отримання інформації про канал
    channel_request = youtube.channels().list(
        part="snippet,contentDetails",
        id="UCIby7wMrI7gNhZlXzoiNbMQ"
    )
    channel_response = channel_request.execute()

    if 'items' in channel_response and len(channel_response['items']) > 0:
        channel_name = channel_response['items'][0]['snippet']['title']
        print(f"Авторизовано на каналі: {channel_name}")

        # Отримання ID основного плейлисту каналу
        playlist_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        # Отримання відео з плейлисту
        video_urls = []
        playlist_request = youtube.playlistItems().list(
            playlistId=playlist_id,
            part="snippet",
            maxResults=7
        )

        while playlist_request:
            playlist_response = playlist_request.execute()

            for item in playlist_response['items']:
                video_id = item['snippet']['resourceId']['videoId']
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                video_urls.append(video_url)

            playlist_request = youtube.playlistItems().list_next(playlist_request, playlist_response)

        # Тут video_urls містить список URL-адрес відео
        print(f"Знайдено {len(video_urls)} відео на каналі.")
    else:
        print("Інформація про канал не знайдена.")

    return youtube, video_urls


# Функція для завантаження відео
async def upload_video(youtube, video_file, img_prevue_file, title, text_game="", video_urls=None):
    new_title = generate_random_title(title)
    new_title = truncate_to_last_word(new_title, 100)

    # Додавання списку URL до опису відео
    additional_description = ""
    if video_urls:
        additional_description = create_video_list_string(video_urls)
    new_description = (new_title + " " + convert_title_with_Tags(title) + "\n\n\n" + truncate_to_last_word(text_game, 500) + "\n\nPlay slot " + title + " https://1win1win.com/\n\n" +
                    additional_description)
    
    # теги без решетки в конце
    selected_hashtags = select_4_hashtags()
    select_random_tags_from_txt = select_random_tags_from_txt_file(POPULAR_HASHTAGS)
    tags_from_title_list = tags_from_title(new_title)

    new_tag = tags_from_title_list + selected_hashtags + select_random_tags_from_txt

    body = {
        'snippet': {
            'title': new_title,
            'description': new_description,
            # "tags": ["surfing", "Santa Cruz"],
            'tags': new_tag,
            'categoryId': '22',
            'defaultLanguage': 'en',
            'defaultAudioLanguage': 'en'
        },
        'status': {
            'privacyStatus': 'public',
            'selfDeclaredMadeForKids': False,
        }
    }

    # Виклик API для завантаження відео
    insert_request = youtube.videos().insert(
        part=",".join(body.keys()),
        body=body,
        media_body=MediaFileUpload(video_file, chunksize=-1, resumable=True)
    )

    try:
        # Завантажити відео
        response = insert_request.execute()
        # ЗАГРУЗКА ЗАСТАВКИ
        if response and 'id' in response:
            video_id = response['id']
            upload_thumbnail(youtube, video_id, img_prevue_file)

        await send_Telegram_video(video_file, f"{title}\n\n{new_title}\n\n{formatted_time}")
        return True
    except Exception as e:
        print(f"Помилка під час завантаження відео: {title}\n{e}")
        await send_Telegram_message(f"ERROR завантаження відео: {title}\n{e}")
        return False

# Головна функція
async def main():
    youtube, video_urls = get_authenticated_service()
    df = pd.read_csv(CSV_ALL_VIDEOS, delimiter=';', quotechar='"')

    for index, row in df.iterrows():
        video_file = GAMES_CATALOG + "/" + row['alias'] + '/video/' + row['alias'] + '.mp4'
        img_prevue_file = GAMES_CATALOG + "/" + row['alias'] + '/images/image-slot-' + row['alias'] + '-0.jpg'
        title = row['title_game']
        if len(row['text_game_Llama_1000_and_nachalo']) < 100:
            text_game = row['text_game']
        else:
            text_game = row['text_game_Llama_1000_and_nachalo']

        # Завантаження відео
        success = await upload_video(youtube, video_file, img_prevue_file, title, text_game, video_urls)

        if success:
            # Видалення рядка після успішної публікації
            df.drop(index, inplace=True)
        else:
            print(f"Помилка під час завантаження відео: {title}")
        break  # Залиште цей рядок для публікації лише одного відео

    # Збереження оновленого CSV файлу
    df.to_csv(CSV_ALL_VIDEOS, sep=';', quotechar='"', index=False)
    await bot.close()

if __name__ == '__main__':
    asyncio.run(main())