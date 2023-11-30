#!/usr/bin/python3

# python /home/vilmebel/dynamiteminergames.com/www/Youtube-API/youtube-api-video.py
# CRON: /usr/bin/python3.10 /home/vilmebel/dynamiteminergames.com/www/Youtube-API/youtube-api-video.py
# pip install --user oauth2client            install on HOSTONG
# Права доступа к скрипту должны быть 750 или rwxr-x—.
# Права доступа к каталогу, в котором размещён скрипт, должны быть 750 или rwxr-x—.

import datetime
import pandas as pd
import os
import httplib2
import asyncio
import httpx
import json
from aiogram import Bot
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

# Налаштування OAuth 2.0
SERVICE_ACCOUNT_FILE = r"/home/vilmebel/dynamiteminergames.com/www/Youtube-API/json_key/load-youtube-slots-api-v1-9454c48658ca.json"
SCOPES = ['https://www.googleapis.com/auth/youtube.upload',
          'https://www.googleapis.com/auth/youtube.readonly']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
CSV_ALL_VIDEOS = r'/home/vilmebel/dynamiteminergames.com/www/Youtube-API/csv/output_games.csv'
GAMES_VIDEO_CATALOG = r'/home/vilmebel/dynamiteminergames.com/www/Youtube-API/video/games-v1/'

# Настройка Telegram бота
with open(r'/home/vilmebel/dynamiteminergames.com/www/TELEGRAM-BOT/telegram_bot_tokens.json', 'r') as file:
    tokens = json.load(file)
TOKEN = tokens["telegram_bot_mypyscript018"]
bot = Bot(token=TOKEN)
CHANNEL_ID = '@mypyscript018'

async def send_message(text):
    await bot.send_message(chat_id=CHANNEL_ID, text=text)

def find_first_long_word(sentence):
    exclude = {'stake', 'slots', 'staking', 'playing', 'slot'}
    words = sentence.split()
    first_word = next(("#" + word.lower() for word in words if len(word) >= 3 and word.lower() not in exclude), "#1win")
    return first_word

# Функція для ініціалізації YouTube API
def get_authenticated_service():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    youtube = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

    # Отримання інформації про канал
    request = youtube.channels().list(
        part="snippet",
        id="UCIby7wMrI7gNhZlXzoiNbMQ"
    )
    response = request.execute()

    if 'items' in response and len(response['items']) > 0:
        channel_name = response['items'][0]['snippet']['title']
        print(f"Авторизовано на каналі: {channel_name}")
    else:
        print("Інформація про канал не знайдена.")

    return youtube


# Функція для завантаження відео
async def upload_video(youtube, video_file, title, text_game=""):
    tag_from_name = find_first_long_word(title)
    new_title = "SLOT 🎃 " + title + " DEMO - Strategy For Profit - Stake #stake #slots #staking #playing " + tag_from_name
    new_description = text_game[:350]
    print(video_file)
    print(new_title)
    body = {
        'snippet': {
            'title': new_title,
            # 'description': new_description,
            'tags': ['stake', 'slots', 'staking', 'playing'],
            'categoryId': '22'
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
        response = insert_request.execute()
        print(f"Video slot - {title}. Video ID: {response['id']}")
        await send_message(f"Успішно завантажено відео: {title}")
        return True
    except Exception as e:
        print(f"Помилка під час завантаження відео: {title}\n{e}")
        await send_message(f"ERROR завантаження відео: {title}\n{e}")
        return False

# Головна функція
async def main():
    youtube = get_authenticated_service()
    df = pd.read_csv(CSV_ALL_VIDEOS, delimiter=';', quotechar='"')

    for index, row in df.iterrows():
        video_file = GAMES_VIDEO_CATALOG + row['alias'] + '/video/video-' + row['alias'] + '.mp4'
        title = row['title_game']
        text_game = row['text_game']

        # Завантаження відео
        success = await upload_video(youtube, video_file, title, text_game)

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
