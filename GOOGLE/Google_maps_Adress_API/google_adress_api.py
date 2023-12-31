import json
import googlemaps
import urllib.parse
import csv


###################################################################
# задаємо стартову адресу
# origin = "ФИТНЕС-КЛУБ FIJI SPORT CLUB. Премиум-класс. Бассейн, фитнес центр, зал рядом с метро: Октябрьское поле, Полежаевская., 3-я Хорошевская ул., 21А, Москва, 123298"
# start_adress = "КУХНИ НА ЗАКАЗ FREYAMEBEL. Магазин кухонной мебели, диванов и кроватей с матрасами в Борисполе: вулиця Льва Толстого, 1, Бориспіль, Київська обл., 08301"
start_adress = "ДИВАНЫ, МАТРАСЫ, КРОВАТИ 🛋️ СКЛАД магазин мягкой мебели в Борисполе. Купить кровать с матрасом - доставка в Киев. InstaDivan: вулиця Льва Толстого, 1, Бориспіль, Київська обл., 08301"

# "КУХНИ НА ЗАКАЗ FREYAMEBEL. Магазин кухонной мебели, диванов и кроватей с матрасами в Борисполе"
# Кухни на заказ FreyaMebel || Магазин мебели Борисполь. Магазин кухонь под заказ и выставка диванов и кроватей с матрасами в многоетажном доме номер 1 на Толстого: вулиця Льва Толстого, 1, Бориспіль, Київська обл., 08301
###################################################################


input_file = r'GOOGLE\Google_maps_Adress_API\input\input_borispol_adress.txt'  # Шлях до вашого txt-файлу
output_file_csv = r'GOOGLE\Google_maps_Adress_API\input\output_borispol_adress_Instadivan.csv'
output_file_txt = r'GOOGLE\Google_maps_Adress_API\input\output_borispol_adress_Instadivan_txt.txt'

# SQL Зчитуємо параметри з конфігураційного файлу
with open(r'GOOGLE\Google_maps_Adress_API\config\api_key.json') as f:
    config = json.load(f)

# створюємо об'єкт клієнта Google Maps
gmaps = googlemaps.Client(key=config['google_api_key'])
start_adress_coords = gmaps.geocode(start_adress)[0]['geometry']['location']

num = 1

with open(input_file, 'r', encoding='utf-8') as file:
    lines_data = file.readlines()



# CSV !!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# with open(output_file_csv, 'w', newline='', encoding='utf-8') as file:
#     field_names = ['csv_id', 'start_adress', 'end_adress', 'new_url', 'a_link_new_url']
#     csv_writer = csv.DictWriter(file, fieldnames=field_names, delimiter=';')
#     csv_writer.writeheader()
    
#     for end_adress in lines_data:
#         # destination = "Киев, " + end_adress[0]
#         # отримуємо координати для заданих адрес
#         # start_adress_coords = gmaps.geocode(start_adress)[0]['geometry']['location']
#         end_adress_coords = gmaps.geocode(end_adress)[0]['geometry']['location']

#         # отримуємо маршрут між двома адресами
#         # routes = gmaps.directions(start_adress=start_adress, destination=destination, mode="driving")

#         # формуємо URL-посилання з адресами, координатами та маршрутом
#         # url = f"https://www.google.com/maps/dir/{start_adress.replace(' ', '+')}/{destination.replace(' ', '+')}/@{start_adress_coords['lat']},{start_adress_coords['lng']},{destination_coords['lat']},{destination_coords['lng']}/data=!3m1!4b1!4m2!4m1!3e0"

#         # new_url = "https://www.google.com/maps/dir/" + urllib.parse.quote(start_adress) + "/" + urllib.parse.quote(destination) + "/@" + str(start_adress_coords['lat']) + "," + str(start_adress_coords['lng']) + "," + str(destination_coords['lat']) + "," + str(destination_coords['lng']) + "/data=!3m1!4b1!4m2!4m1!3e0"
#         # print(new_url)
#         # https://www.google.com/maps/dir/%D0%B2%D1%83%D0%BB%D0%B8%D1%86%D1%8F+%D0%A2%D0%BE%D0%BF%D0%BE%D0%BB%D0%B5%D0%B2%D0%B0,+%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BF%D1%96%D0%BB%D1%8C,+%D0%9A%D0%B8%D1%97%D0%B2%D1%81%D1%8C%D0%BA%D0%B0+%D0%BE%D0%B1%D0%BB./%D0%9A%D1%83%D1%85%D0%BD%D0%B8+%D0%BD%D0%B0+%D0%B7%D0%B0%D0%BA%D0%B0%D0%B7+FreyaMebel+%7C%7C+%D0%9C%D0%B0%D0%B3%D0%B0%D0%B7%D0%B8%D0%BD+%D0%BC%D0%B5%D0%B1%D0%B5%D0%BB%D0%B8+%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C,+%D1%83%D0%BB%D0%B8%D1%86%D0%B0+%D0%9B%D1%8C%D0%B2%D0%B0+%D0%A2%D0%BE%D0%BB%D1%81%D1%82%D0%BE%D0%B3%D0%BE,+%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C,+%D0%9A%D0%B8%D0%B5%D0%B2%D1%81%D0%BA%D0%B0%D1%8F+%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C/@50.3481944,30.9214562,14z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x40d4e8d01f74aab3:0xaccb1036d6c47dd1!2m2!1d30.9320891!2d50.333396!1m5!1m1!1s0x40d4e9521d2e0e93:0xb84dffbf89cb35ab!2m2!1d30.9390607!2d50.3637429!3e0?entry=ttu
#         # https://www.google.com/maps/dir/%D0%B2%D1%83%D0%BB%D0%B8%D1%86%D1%8F+%D0%93%D0%B0%D0%B3%D0%B0%D1%80%D1%96%D0%BD%D0%B0,+5,+%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BF%D1%96%D0%BB%D1%8C,+%D0%9A%D0%B8%D1%97%D0%B2%D1%81%D1%8C%D0%BA%D0%B0+%D0%BE%D0%B1%D0%BB.,+%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0,+08301/%D0%9A%D0%A3%D0%A5%D0%9D%D0%98+%D0%9D%D0%90+%D0%97%D0%90%D0%9A%D0%90%D0%97+FREYAMEBEL.+%D0%9C%D0%B0%D0%B3%D0%B0%D0%B7%D0%B8%D0%BD+%D0%BA%D1%83%D1%85%D0%BE%D0%BD%D0%BD%D0%BE%D0%B9+%D0%BC%D0%B5%D0%B1%D0%B5%D0%BB%D0%B8,+%D0%B4%D0%B8%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2+%D0%B8+%D0%BA%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%B9+%D1%81+%D0%BC%D0%B0%D1%82%D1%80%D0%B0%D1%81%D0%B0%D0%BC%D0%B8+%D0%B2+%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D0%B5,+%D0%B2%D1%83%D0%BB%D0%B8%D1%86%D1%8F+%D0%9B%D1%8C%D0%B2%D0%B0+%D0%A2%D0%BE%D0%BB%D1%81%D1%82%D0%BE%D0%B3%D0%BE,+1,+%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BF%D1%96%D0%BB%D1%8C,+%D0%9A%D0%B8%D1%97%D0%B2%D1%81%D1%8C%D0%BA%D0%B0+%D0%BE%D0%B1%D0%BB.,+%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0,+08301/@50.3702092,30.9404359,15z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x40d4e63e0f899e21:0x2baef8d9ea40925a!2m2!1d30.9624106!2d50.3769806!1m5!1m1!1s0x40d4e9521d2e0e93:0xb84dffbf89cb35ab!2m2!1d30.9390607!2d50.3637429!3e0?entry=ttu
#         # new_url = "https://www.google.com/maps/dir/" + urllib.parse.quote(end_adress) + "/" + urllib.parse.quote(start_adress) + "/@" + str(end_adress_coords['lat']) + "," + str(end_adress_coords['lng']) + "," + str(start_adress_coords['lat']) + "," + str(start_adress_coords['lng']) + "/data=!3m1!4b1!4m2!4m1!3e0"
#         new_url = "https://www.google.com/maps/dir/" + urllib.parse.quote(end_adress) + "/" + urllib.parse.quote(start_adress) + "/@" + str(end_adress_coords['lat']) + "," + str(end_adress_coords['lng']) + "," + str(start_adress_coords['lat']) + "," + str(start_adress_coords['lng']) + "0?entry=ttu"
#         a_link_new_url = f'<a href="{new_url}">{end_adress[:25]} - Мебель Кухни Диваны Борисполь Freya</a>'
#         print(new_url)

#         # CSV Запис
#         csv_writer.writerow({'csv_id': num,
#                 'start_adress': start_adress,
#                 'end_adress': end_adress,
#                 'new_url': new_url,
#                 'a_link_new_url': a_link_new_url
#                 })
#         num += 1


# TXT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
with open(output_file_txt, 'w', encoding='utf-8') as file:
    for end_adress in lines_data:
        end_adress_coords = gmaps.geocode(end_adress)[0]['geometry']['location']

        new_url = "https://www.google.com/maps/dir/" + urllib.parse.quote(end_adress) + "/" + urllib.parse.quote(start_adress) + "/@" + str(end_adress_coords['lat']) + "," + str(end_adress_coords['lng']) + "," + str(start_adress_coords['lat']) + "," + str(start_adress_coords['lng']) + "0?entry=ttu"

        file.write(new_url + '\n')

print("All GOOD")
