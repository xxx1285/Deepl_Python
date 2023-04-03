

import urllib.parse
import json
import googlemaps
import urllib.parse
import csv


###################################################################
# задаємо стартову адресу
origin = "ФИТНЕС-КЛУБ FIJI SPORT CLUB. Премиум-класс. Бассейн, фитнес центр, зал рядом с метро: Октябрьское поле, Полежаевская., 3-я Хорошевская ул., 21А, Москва, 123298"
###################################################################


# SQL Зчитуємо параметри з конфігураційного файлу
with open(r'C:\Gembling\Deepl_Python\Deepl_Python\Google_Adress_API\config\config.json') as f:
    config = json.load(f)

# створюємо об'єкт клієнта Google Maps
gmaps = googlemaps.Client(key=config['google_api_key'])
# отримуємо координати першої адреси яка не змінна
origin_coords = gmaps.geocode(origin)[0]['geometry']['location']

num = 1


with open(r'Google_Adress_API\doc\adress_in.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=';', quotechar=' ')
    # збереження даних у CSV файл
    with open(r'Google_Adress_API\doc\adress_out_2.csv', 'w', newline='', encoding='utf-8') as new_csv:
        field_names = ['csv_id', 'baza_adress', 'end_adress', 'new_url']
        csv_writer = csv.DictWriter(new_csv, fieldnames=field_names)
        csv_writer.writeheader()
        for row in data:
            destination = "Москва, " + row[0]
            # отримуємо координати для заданих адрес
            # origin_coords = gmaps.geocode(origin)[0]['geometry']['location']
            destination_coords = gmaps.geocode(destination)[0]['geometry']['location']

            # отримуємо маршрут між двома адресами
            routes = gmaps.directions(origin=origin, destination=destination, mode="driving")

            # формуємо URL-посилання з адресами, координатами та маршрутом
            # url = f"https://www.google.com/maps/dir/{origin.replace(' ', '+')}/{destination.replace(' ', '+')}/@{origin_coords['lat']},{origin_coords['lng']},{destination_coords['lat']},{destination_coords['lng']}/data=!3m1!4b1!4m2!4m1!3e0"

            # new_url = "https://www.google.com/maps/dir/" + urllib.parse.quote(origin) + "/" + urllib.parse.quote(destination) + "/@" + str(origin_coords['lat']) + "," + str(origin_coords['lng']) + "," + str(destination_coords['lat']) + "," + str(destination_coords['lng']) + "/data=!3m1!4b1!4m2!4m1!3e0"
            # print(new_url)

            new_url = "https://www.google.com/maps/dir/" + urllib.parse.quote(destination) + "/" + urllib.parse.quote(origin) + "/@" + str(destination_coords['lat']) + "," + str(destination_coords['lng']) + "," + str(origin_coords['lat']) + "," + str(origin_coords['lng']) + "/data=!3m1!4b1!4m2!4m1!3e0"
            print(new_url)

            # CSV Запис
            csv_writer.writerow({'csv_id': num,
                    'baza_adress': origin,
                    'end_adress': destination,
                    'new_url': new_url
                    })
            num += 1
print("All GOOD")
