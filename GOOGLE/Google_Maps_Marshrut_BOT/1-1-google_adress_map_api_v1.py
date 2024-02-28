import json
import googlemaps
import urllib.parse
import csv


###################################################################
# задаємо стартову адресу
# origin = "ФИТНЕС-КЛУБ FIJI SPORT CLUB. Премиум-класс. Бассейн, фитнес центр, зал рядом с метро: Октябрьское поле, Полежаевская., 3-я Хорошевская ул., 21А, Москва, 123298"
# start_adress = "КУХНИ НА ЗАКАЗ FREYAMEBEL. Магазин кухонной мебели, диванов и кроватей с матрасами в Борисполе: вулиця Льва Толстого, 1, Бориспіль, Київська обл., 08301"

# start_adress = "ДИВАНЫ, МАТРАСЫ, КРОВАТИ 🛋️ СКЛАД магазин мягкой мебели в Борисполе. Купить кровать с матрасом - доставка в Киев. InstaDivan: вулиця Льва Толстого, 1, Бориспіль, Київська обл., 08301"
start_adress = "КУХНИ НА ЗАКАЗ 🛋️ МЕБЕЛЬ КИЕВ БОРИСПОЛЬ FREYAMEBEL. Склад мебели: диваны, кровати, матрасы в Борисполе. Кухні на замовлення: вулиця Льва Толстого, 1, Бориспіль, Київська обл., 08301"

# Кухни на заказ FreyaMebel || Магазин мебели Борисполь. Магазин кухонь под заказ и выставка диванов и кроватей с матрасами в многоетажном доме номер 1 на Толстого: вулиця Льва Толстого, 1, Бориспіль, Київська обл., 08301
###################################################################


input_file = r'GOOGLE\Google_Maps_Marshrut_BOT\input\input_borispol_adress_v2.txt'  # Шлях до вашого txt-файлу
output_file_txt = r'GOOGLE\Google_Maps_Marshrut_BOT\output\output_FOOL_adress_InstadivFrayameb_v1.txt'

# SQL Зчитуємо параметри з конфігураційного файлу
with open(r'GOOGLE\Google_maps_Adress_API\config\api_key.json') as f:
    config = json.load(f)

# створюємо об'єкт клієнта Google Maps
gmaps = googlemaps.Client(key=config['google_api_key'])
start_adress_coords = gmaps.geocode(start_adress)[0]['geometry']['location']

num = 1

with open(input_file, 'r', encoding='utf-8') as file:
    lines_data = file.readlines()



# TXT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
with open(output_file_txt, 'a', encoding='utf-8') as file:
    for end_adress in lines_data:

        if len(end_adress) < 10:
            continue

        end_adress_coords = gmaps.geocode(end_adress)[0]['geometry']['location']

        new_url = "https://www.google.com/maps/dir/" + urllib.parse.quote(end_adress) + "/" + urllib.parse.quote(start_adress) + "/@" + str(end_adress_coords['lat']) + "," + str(end_adress_coords['lng']) + "," + str(start_adress_coords['lat']) + "," + str(start_adress_coords['lng']) + "0?entry=ttu"
        # new_url = "https://www.google.com/maps/dir/" + urllib.parse.quote(end_adress) + "//@" + str(end_adress_coords['lat']) + "," + str(end_adress_coords['lng']) + ",12z?entry=ttu"

        file.write(new_url + '\n')

print("All GOOD")
