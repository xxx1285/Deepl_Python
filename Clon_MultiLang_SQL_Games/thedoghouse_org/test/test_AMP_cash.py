import requests
import json

# список URL, для яких потрібно отримати URL для AMP
urls = ['https://aviator--game.com/', 'https://aviator--game.com/aviator-game-strategies-and-prediction-methods.html']

# параметри запиту до API
url = 'https://acceleratedmobilepageurl.googleapis.com/v1/ampUrls:batchGet'
# https://console.cloud.google.com/apis/dashboard?authuser=4&hl=ru&project=alert-height-304110&supportedpurview=project
params = {'key': 'AIzaSyAPtOlja-Wjq6y1X799XIesG09WP7pqV3Y'}

# створення JSON-об'єкту для передачі у тілі запиту
data = json.dumps({'urls': urls})

# виклик методу API з використанням бібліотеки requests
response = requests.post(url, params=params, data=data)

# отримання URL для AMP з відповіді API
amp_urls = [item['ampUrl'] for item in response.json()['ampUrls']]

print(amp_urls)  # ['https://aviator--game.com/?amp=1', 'https://aviator--game.com/aviator-game-strategies-and-prediction-methods.html?amp=1']
print(response.text)
