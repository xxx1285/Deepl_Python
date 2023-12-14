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
from aiogram.types import InputFile
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Налаштування OAuth 2.0
CLIENT_SECRETS_FILE = r"/home/vilmebel/dynamiteminergames.com/www/Youtube-API/json_key/client_secret_75919922252-md40qq7of31jc7jvlsbo2e8mrtp96ud1.apps.googleusercontent.com.json"
SCOPES = ['https://www.googleapis.com/auth/youtube.upload',
          'https://www.googleapis.com/auth/youtube.readonly',
          'https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
CSV_ALL_VIDEOS = r'/home/vilmebel/dynamiteminergames.com/www/Youtube-API/csv/output_games.csv'
GAMES_CATALOG = r'/home/vilmebel/dynamiteminergames.com/www/Youtube-API/video/games-v1'
OAUTH_TOKEN = r'/home/vilmebel/dynamiteminergames.com/www/Youtube-API/json_key/token-v2.json'
TELEGRAM_BOT_TOKEN = r'/home/vilmebel/dynamiteminergames.com/www/TELEGRAM-BOT/telegram_bot_tokens.json'
# YOUTUBE_ZASTAVKA_THUMB_JPG = r'Youtube\1-AUTO-Publish-on-Youtube\test\zastavka-test.jpg'

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
    video = InputFile(video_file)
    await bot.send_video(chat_id=CHANNEL_ID, video=video, caption=caption)

# текущее время
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M")

# TAGS add new TAG from Titile
def find_first_long_word(sentence):
    exclude = {'stake', 'slots', 'staking', 'playing', 'slot'}
    words = sentence.split()
    first_word = next(("#" + word.lower() for word in words if len(word) >= 3 and word.lower() not in exclude), "#1win")
    return first_word

def select_hashtags():
    # hashtags
    hashtags = [
        "#stake", "#slots", "#staking", "#playing", "#casino", "#gaming", 
        "#jackpot", "#winning", "#casinoLife", "#LuckySpin", "#BigWin", 
        "#PlayNow", "#CasinoGames", "#fortune", "#OnlineCasino", "#gamble", 
        "#casinoslots", "#slotmachine", "#casinofun", "#slotsaction",
        "#bigprizes", "#gambling", "#luckywin", "#slotstrategies", "#casinoplay",
        "#topslot", "#slotadventure", "#casinowins", "#epicplay", "#hotstreak",
        "#highwins", "#electricplay", "#casinonight", "#slotthrills", "#winningnight",
        "#Lucky", "#SlotGames", "#SlotKing", "#CasinoOnline", "#SlotStrategy",
        "#FreeSpins", "#Bonus", "#MegaWin", "#SlotFun", "#VegasSlots", "#JackpotParty",
        "#CasinoRoyale", "#Bet", "#Riches", "#Treasure", "#Money", "#Gold", "#LuckyCharm",
        "#SpinToWin", "#Winner", "#Betting", "#stake", "#slots", "#staking", "#playing", "#slot"
    ]

    # Randomly select 4 unique hashtags
    return random.sample(hashtags, 4)

def generate_random_title(title):
    title_upper = title.upper()
    templates = [
        f"EXCITING {title_upper} 🌟 1WIN JACKPOT CHASE",
        f"THRILLING {title_upper} 💰 1WIN BIG WIN THRILLS",
        f"ADVENTURE {title_upper} 🔥 1WIN SPIN MANIA",
        f"LUXURIOUS {title_upper} 💎 1WIN LUXURY STAKES",
        f"EXPLOSIVE {title_upper} 🎃 1WIN MEGA PRIZES",
        f"ENERGIZING {title_upper} ⚡ 1WIN WINNING STREAK",
        f"LUCKY {title_upper} 🍀 1WIN LUCKY SPINS",
        f"EPIC {title_upper} 🌟 1WIN EPIC WINS",
        f"AMAZING {title_upper} 🎃 1WIN AMAZING WINS",
        f"TOP {title_upper} 🥇 1WIN TOP JACKPOTS",
        f"FRENZIED {title_upper} 🌟 1WIN SPIN FRENZY",
        f"RICH {title_upper} 🤑 1WIN RICHES HUNT",
        f"MAGICAL {title_upper} 🌟 1WIN MAGIC SPINS",
        f"WINNING {title_upper} 💰 1WIN WINNING SECRETS",
        f"CHAMPION {title_upper} 🏆 1WIN CHAMPION PLAY",
        f"UNFORGETTABLE {title_upper} 🎃 1WIN SLOT ADVENTURE",
        f"HOT {title_upper} 🔥 1WIN HOT STREAK",
        f"JOURNEY {title_upper} 🎃 1WIN SLOT ADVENTURE",
        f"HOT {title_upper} 🔥 1WIN HOT STREAK",
        f"ELECTRIC {title_upper} ⚡ 1WIN ELECTRIC WINS",
        f"MOONLIGHT {title_upper} 🌙 1WIN NIGHT THRILLS",
        f"CHALLENGE {title_upper} 🔥 1WIN ODDS CHALLENGE",
        f"DISCOVERY {title_upper} 🌟 1WIN MAGIC WINS",
        f"QUEST {title_upper} 💰 1WIN JACKPOT QUEST",
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
        f"{title_upper} 🌟 EPIC EPIC WINS",
        f"{title_upper} 🎃 AMAZING AMAZING WINS",
        f"{title_upper} 🥇 TOP TOP JACKPOTS",
        f"{title_upper} 🌟 FRENZIED SPIN FRENZY",
        f"{title_upper} 🤑 RICH RICHES HUNT",
        f"{title_upper} 🌟 MAGICAL MAGIC SPINS",
        f"{title_upper} 🚀 DYNAMIC WIN EXPLOSION",
        f"{title_upper} 💫 SPECTACULAR LUCKY BREAK",
        f"{title_upper} 🌈 COLOURFUL SLOT FANTASY",
        f"{title_upper} 🌟 GLITTERING PRIZE FRENZY",
        f"{title_upper} 🔮 MYSTICAL FORTUNE HUNT",
        f"{title_upper} 🎉 CELEBRATORY MEGA WINS",
        f"{title_upper} 🌙 NIGHTTIME JACKPOT ADVENTURE",
        f"{title_upper} ⭐ STAR-STUDDED WINNING GALORE",
        f"{title_upper} 💸 FLASHY MONEY SPREE",
        f"{title_upper} 🎲 DAZZLING GAMBLING THRILLS",
        f"{title_upper} 🏆 CHAMPION'S GOLDEN TROPHY",
        f"{title_upper} 🎰 VIBRANT SLOT SAGA",
        f"{title_upper} 💥 BURSTING BIG SCORE",
        f"{title_upper} 🌠 BRILLIANT STREAKS | PRAGMATIC PLAY",
        f"{title_upper} ✨ GOLDEN WINS AWAITS | PRAGMATIC PLAY",
        f"{title_upper} 🎯 TARGET HUGE REWARDS | PRAGMATIC PLAY",
        f"{title_upper} 💥 EXPLORE EPIC WINS | PRAGMATIC PLAY",
        f"{title_upper} 🔥 FLAMING HOT PRIZES | PRAGMATIC PLAY",
        f"{title_upper} 🌪 WHIRLWIND OF FORTUNE | PRAGMATIC PLAY",
        f"{title_upper} 💫 SPIN INTO ORBIT | PRAGMATIC PLAY",
        f"{title_upper} 🎈 SKY-HIGH JACKPOTS | PRAGMATIC PLAY",
        f"{title_upper} 🌐 GLOBAL WINNING SPINS | PRAGMATIC PLAY",
        f"{title_upper} ⚡ ELECTRIC WINS | PRAGMATIC PLAY",
        f"{title_upper} 🧲 MAGNETIC MEGA WINS | PRAGMATIC PLAY",
        f"{title_upper} 🚀 BLAST OFF BIG WINS | PRAGMATIC PLAY",
        f"{title_upper} 🏝 TROPICAL TREASURE HUNT | PRAGMATIC PLAY",
        f"{title_upper} 🎇 SPARKLING VICTORY RUSH | PRAGMATIC PLAY",
        f"{title_upper} 🍾 CHAMPAGNE SHOWERS OF WINS | PRAGMATIC PLAY",
        f"{title_upper} 💎 DIAMOND RICHES BONANZA | PRAGMATIC PLAY",
        f"{title_upper} 🌌 COSMIC CASH BLAST | PRAGMATIC PLAY",
        f"{title_upper} 🎰 REEL THRILL SPINS | PRAGMATIC PLAY",
        f"{title_upper} 🎢 ROLLERCOASTER OF REWARDS | PRAGMATIC PLAY",
        f"{title_upper} ⏳ TIMELESS TREASURES CHASE | PRAGMATIC PLAY",
        f"{title_upper} 🌊 OCEAN OF OPPORTUNITY | PRAGMATIC PLAY",
        f"{title_upper} 🔑 KEYS TO FORTUNE | PRAGMATIC PLAY",
        f"{title_upper} 🌞 SUNSHINE OF SUCCESS | PRAGMATIC PLAY",
        f"{title_upper} 🍀 FIELD OF FORTUNES | PRAGMATIC PLAY",
        f"{title_upper} 🌟 GALACTIC GOLD RUSH | PRAGMATIC PLAY",
        f"{title_upper} 🍭 SWEET SWEEPSTAKES | PRAGMATIC PLAY",
        f"$1 200 000 🔥 {title_upper} SLOT PRAGMATIC PLAY",
        f"$1 070 000 {title_upper} 🍾 COSMIC CASH SLOT PRAGMATIC PLAY",
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
    video_list_str = ""
    for url in video_urls:
        video_list_str += f"{url}\n"
    return video_list_str

# # Youtube Thumb Images - Zastavka
# def upload_thumbnail(youtube, video_id, thumbnail_file):
#     request = youtube.thumbnails().set(
#         videoId=video_id,
#         media_body=MediaFileUpload(thumbnail_file)
#     )
#     response = request.execute()
#     print(f"Thumbnail uploaded for video id {video_id}")

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
    tag_from_name = find_first_long_word(title)
    selected_hashtags = select_hashtags()
    new_title = generate_random_title(title) + " " + tag_from_name + " " + " ".join(selected_hashtags)
    new_title = truncate_to_last_word(new_title, 100)
    # Додавання списку URL до опису відео
    additional_description = ""
    if video_urls:
        additional_description = create_video_list_string(video_urls)
    new_description = (truncate_to_last_word(text_game, 500) + "\n\nPlay slot " + title + " https://1win1win.com/\n" +
                    tag_from_name + " " + " ".join(selected_hashtags) + "\n\n" + additional_description)
    # теги без решетки в конце
    new_tag = [tag.strip('#') for tag in selected_hashtags]
    additional_tag = random.choice(['stake', 'slots', 'staking', 'playing'])
    new_tag = new_tag.append(additional_tag)
    print(new_title)

    body = {
        'snippet': {
            'title': new_title,
            'description': new_description,
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
        # video_id = response['id']
        # thumbnail_file = 'path_to_your_thumbnail.jpg'  # Укажите путь к файлу миниатюры
        # upload_thumbnail(youtube, video_id, thumbnail_file)
        print(f"Video slot - {title}. Video ID: {response['id']}")
        
        await send_Telegram_video(video_file, f"{title}\n\n Успішно завантажено - {formatted_time}")
        # await send_Telegram_message(f"{title}/n Успішно завантажено {formatted_time}")
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
        img_prevue_file = GAMES_CATALOG + "/" + row['alias'] + '/images/image-' + row['alias'] + '-0.jpg'
        title = row['title_game']
        text_game = row['text_game']

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