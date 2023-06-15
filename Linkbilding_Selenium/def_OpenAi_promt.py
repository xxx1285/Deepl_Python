import os
import openai
import json

import csv
import requests
from requests.exceptions import RequestException


# Нинішній розділ
current_folder = os.path.basename(os.path.dirname(__file__))

# Загружаем параметры из конфигурационного файла
with open(f'{current_folder}\\config\config_OpenAi_Key.json') as f:
    config = json.load(f)

openai.api_key = config['config_openai']['api_openai_key']


"""
    Напиши 10 идей  на Английском языке, составленных комментариев с подстановкой темы статьи и ключевого слова {game DSA}. 
    Например:f"I just got through with {title_url}, and wow, it's as gripping as playing {key_game}. 
    The future is now, and both these things prove it!". Коментарии должны быть длинной от 350 до 400 символов на игровую тематику, 
    и на простом человеческом языке с использованием структуры реальных коментарии с Reddit. Используй ключевое слово перед указанием 
    темы статьи. Конечный результат запиши в переменну в виде f строк как например comments_prompt = 
    [f"I just got through with {title_url}, and wow, it's as gripping as playing {key_game}]
"""
comments_prompt = [
    f"I just got through with {title_url}, and wow, it's as gripping as playing {key_game}. The future is now, and both these things prove it!",
    f"After reading {title_url}, I'm awestruck. Kinda like the first time I played {key_game}. Both are super innovative and open up a whole new world of possibilities.",
    f"Diving into {title_url} felt like a journey back in time. Kind of like when I revisit old levels in {key_game}. It's fascinating how much we've progressed!",
    f"The article on {title_url} was as eye-opening as the plot twists in {key_game}. Both are so full of surprises, it's impossible to predict what's coming next.",
    f"Reading {title_url} was like playing a level of {key_game} that's tough but rewarding. Both require focus and critical thinking, and boy do they keep you on your toes!",
    f"Going through {title_url} was as thrilling as winning a tough round of {key_game}. Both are breakthroughs in their own right and it's exciting to see them unfold.",
    f"The article {title_url} was as much of an adventure as a marathon session of {key_game}. The mysteries, the challenges – they both just draw you in!",
    f"Reading about {title_url} got my brain buzzing, much like the strategic gameplay in {key_game}. Both are thought-provoking and make you look at things from a whole new perspective.",
    f"{title_url} was an enlightening read. It's like {key_game} in the way it changes your outlook. They both make you think deeper and question the status quo.",
    f"Engaging with {title_url} gave me a sense of thrill akin to when I'm playing {key_game}. Both require strategy, a keen mind, and quick decision-making. It's an adrenaline rush!",
    f"{title_url} was such an engrossing read! It's like the joy I feel when I'm playing my favorite game, {key_game}. It's a great way to engage and learn new things, just like in the game!",
    f"I just had to share how much I enjoyed reading {title_url}. It made me think about the strategies and decisions I make in {key_game}, just as much as it made me ponder the future of VR.",
    f"Reading about {title_url} made me remember the excitement I had when I first played {key_game}. The thrill and competition - both are so addictive!",
    f"{title_url} is as fascinating as each level in {key_game}. The ever-changing landscapes and challenges keep me coming back for more!",
    f"I just got through with {title_url}, it felt just like mining for resources in {key_game} - intriguing and full of surprises.",
    f"I found {title_url} as enlightening as understanding the mechanics of {key_game}. Both require an open mind and a willingness to adapt to new situations.",
    f"I'm as drawn to {title_url} as I am to playing {key_game}. Both are complex yet fascinating, offering endless opportunities to learn and grow.",
    f"Reading about {title_url}, I couldn't help but reminisce about the immersive universe of {key_game}. Both provide a refreshing escape from reality.",
    f"Just like the satisfying achievement of a hard-fought victory in {key_game}, the exploration of {title_url} left me feeling accomplished, having gained new insights.",
    f"The in-depth analysis in {title_url} kept me as engaged as the intricate strategies required in {key_game}. It's amazing how technology changes our perspective, be it business or gaming!",
    f"Just like a nail-biting match in {key_game}, I found the article {title_url} equally exhilarating. It's fascinating to see how the game strategies can be related to real life scenarios.",
    f"While playing {key_game}, I stumbled upon the article {title_url}. The similarity between the game's strategy and the article's insight left me intrigued. Both are so immersive and enlightening.",
    f"I found the article {title_url} as engrossing as the gameplay in {key_game}. Both require critical thinking and strategy. It's truly fascinating to see the correlation.",
    f"The thrill of playing {key_game} is only paralleled by the insight I gained from the article {title_url}. It's amazing how gaming can be as educational as a well-researched article.",
    f"While playing {key_game}, I often find myself applying strategies I learned from articles like {title_url}. The parallels between gaming and real-life scenarios are astounding.",
    f"I find the tactical aspect of {key_game} quite similar to the strategic insights from {title_url}. Both make me think and analyze before making decisions.",
    f"The compelling strategies of {key_game} often remind me of the depth and complexity of articles like {title_url}. The more I delve into both, the more I learn.",
    f"Immersed in {key_game}, I often see myself applying the insights I got from the article {title_url}. The similarities in strategic planning are quite astounding.",
    f"The thought process in {key_game} and the insights from {title_url} are surprisingly similar. Both involve thinking ahead and adapting to new challenges.",
    f"The strategizing I do while playing {key_game} is complemented by the insights I get from articles like {title_url}. It's a perfect blend of entertainment and learning."
]




# Promt AI Zapros
def response_ai(promt_ai):
    response = openai.Completion.create(
        model="text-babbage-001",
        prompt=promt_ai,
        temperature=1.5,
        max_tokens=60,
        top_p=0.45,
        best_of=1,
        frequency_penalty=0.99,
        presence_penalty=0.90
        )
    return response['choices'][0]['text']

# Clean TEXT
def my_clean_string(string):
    string = string.replace('\n', '')
    # string = string.replace(' ', '')
    return string

# Add link <a> in TEXT
def my_clean_string(string):
    string = string.replace('\n', '')
    # string = string.replace(' ', '')
    return string

def promt_openai(site_url, title_url, random_key_poisk):
    text_open_ai = response_ai(f"Основные страны локали {loc}, укажи до 3 стран")
    print()
