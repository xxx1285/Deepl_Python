#!/usr/bin/python3

# python /home/vilmebel/dynamiteminergames.com/www/Youtube-API/youtube-api-video.py
# CRON: /usr/bin/python3.10 /home/vilmebel/dynamiteminergames.com/www/Youtube-API/youtube-api-video.py

import datetime
import pandas as pd
import os
import httplib2
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run_flow

# Налаштування OAuth 2.0
# Путь к JSON-ключу служебного аккаунта
# key_path = r"/home/vilmebel/dynamiteminergames.com/www/my_geoipRedirect/json_key/gambling-traker-geoip-ee529f94c112.json"
CLIENT_SECRETS_FILE = r"/home/vilmebel/dynamiteminergames.com/www/Youtube-API/json_key/client_secret_75919922252-md40qq7of31jc7jvlsbo2e8mrtp96ud1.apps.googleusercontent.com.json"
SCOPES = ['https://www.googleapis.com/auth/youtube.upload',
          'https://www.googleapis.com/auth/youtube.readonly']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
CSV_ALL_VIDEOS = r'/home/vilmebel/dynamiteminergames.com/www/Youtube-API/csv/output_games.csv'
GAMES_VIDEO_CATALOG = r'/home/vilmebel/dynamiteminergames.com/www/Youtube-API/video/games-v1/'

# Функція для ініціалізації YouTube API
def get_authenticated_service():
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=SCOPES)
    storage = Storage(f"/home/vilmebel/dynamiteminergames.com/www/Youtube-API/{API_SERVICE_NAME}-{API_VERSION}.dat")
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
def upload_video(youtube, video_file, title, text_game=""):

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

    response = insert_request.execute()
    print(f"Video slot - {title}. Video ID: {response['id']}")

# Головна функція
def main():
    youtube = get_authenticated_service()
    df = pd.read_csv(CSV_ALL_VIDEOS, delimiter=';', quotechar='"')

    for index, row in df.iterrows():
        video_file = GAMES_VIDEO_CATALOG + row['alias'] + '/video/video-' + row['alias'] + '.mp4'
        title = row['title_game']
        text_game = row['text_game']

        # Завантаження відео
        success = upload_video(youtube, video_file, title, text_game)

        if success:
            # Видалення рядка після успішної публікації
            df.drop(index, inplace=True)
        else:
            print(f"Помилка під час завантаження відео: {title}")
        break  # Залиште цей рядок для публікації лише одного відео

    # Збереження оновленого CSV файлу
    df.to_csv(CSV_ALL_VIDEOS, sep=';', quotechar='"', index=False)

if __name__ == '__main__':
    main()
