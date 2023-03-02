import json
from bs4 import BeautifulSoup
import pymysql


# функція що очищає або добавляє екранування - JSON
def my_clean_string(string, escape=True):
    if escape:
        # Замінюємо спеціальні символи на їх екрановані еквіваленти
        string = string.replace('/', '\/')
    else:
        # Видаляємо екранування спеціальних символів
        string = string.replace('\\', '')
        string = string.replace('\n', '')
        string = string.replace('\t', '')
        string = string.replace('&nbsp;', '')
    return string

# SQL Зчитуємо параметри з конфігураційного файлу
with open(r'Python_JSON\configs\config_baza_mysql.json') as f:
    config = json.load(f)

# Експорт таблиць
my_tables = ['modx_site_content']

my_json = [
    {
        "MIGX_id":"1",
        "h2_title":"How to play Aviator game",
        "description":"<p>The essence of the on , namely:<\/p>\n\n<ol>\n\t<li>At the beginning of the Aviator the ;<\/li>\n\t<li>And the most, until button and take the win.<\/li>\n<\/ol>\n\n<p>You see how you don't to fly away.<\/p>\n\n<p>It is important to know fly, your bet.&nbsp;<\/p>\n",
        "alt_img":"aviator game, win 70x plane is fly, bet you money in casino Aviator game",
        "image":"online-game-Aviator\/Aviator-game-win-70x-online-1win.webp"
    },
    {
        "MIGX_id":"2",
        "h2_title":"Aviator game",
        "description":"<h3>1. Betting on the Aviator game<\/h3>\n\n<p>For multiply our bet.<\/p>\n\n<p>In the game the second bet)<\/p>\n",
        "alt_img":"Betting 10 Aviator",
        "image":"images\/gameplay\/button-in-Aviator-Game-1.webp"
    }
]

try:
    # Попытаемся распарсить строку как JSON
    json.loads(my_json)
    print("1")
except ValueError:
    try:
        # Если не удалось распарсить строку как JSON, попробуем распарсить ее как HTML
        soup = BeautifulSoup(asdf, 'html.parser')
        print("2")
    except:
        # Если не удалось распарсить строку как JSON или HTML, значит это обычная строка без тегов
        if "<" not in asdf and ">" not in asdf:
            print("3")

for item in my_json:
    print(f"\nItem {item['MIGX_id']}:")
    for key, value in item.items():
        if key != "MIGX_id":
            # value = value.replace('\\', '').replace('\n', '').replace('\t', '')
            # value = clean_string(value, escape=False)
            print(f"{key}: {value}")
            value = my_clean_string(value, escape=False)
            print(f"{key} 44: {value}")
