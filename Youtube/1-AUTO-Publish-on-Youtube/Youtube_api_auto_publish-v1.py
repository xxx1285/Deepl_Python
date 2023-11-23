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
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run_flow

# Налаштування OAuth 2.0
CLIENT_SECRETS_FILE = r"C:\Gembling\Deepl_Python\Deepl_Python\Youtube\1-AUTO-Publish-on-Youtube\client_secret_75919922252-0secpp8nn50huglm8fb7qbafqpcrkidv.apps.googleusercontent.com.json"
SCOPES = ['https://www.googleapis.com/auth/youtube.upload',
          'https://www.googleapis.com/auth/youtube.readonly']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
CSV_ALL_VIDEOS = r'Youtube\1-AUTO-Publish-on-Youtube\input\output_games.csv'

# Настройка Telegram бота
with open(r'SETTINGS\telegram_bot_tokens.json', 'r') as file:
    tokens = json.load(file)
TOKEN = tokens["telegram_bot_mypyscript018"]
bot = Bot(token=TOKEN)
CHANNEL_ID = '@mypyscript018'

async def send_message(text):
    await bot.send_message(chat_id=CHANNEL_ID, text=text)

# Функція для ініціалізації YouTube API
def get_authenticated_service():
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=SCOPES)
    storage = Storage(f"Youtube//1-AUTO-Publish-on-Youtube//{API_SERVICE_NAME}-{API_VERSION}.dat")
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage)

    youtube = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

    # Отримання інформації про канал
    request = youtube.channels().list(
        part="snippet",
        mine=True
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

    new_title = "SLOT 🎃 " + title + " DEMO - Strategy For Profit - Stake #stake #slots #staking #playing"
    new_description = text_game[:350]
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
        video_file = row['video_src']
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
    # Закриваємо сесію бота Телеграм
    await bot.close()


if __name__ == '__main__':
    asyncio.run(main())
