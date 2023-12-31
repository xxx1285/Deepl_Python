import requests
import json
import googlemaps
import urllib.parse

# INSTADIVAAN = 8207621176809025478
# FRAYAMEBEL = 13280552074301093291
CID_MY_COMPANY = 8207621176809025478

# SQL Зчитуємо параметри з конфігураційного файлу
with open(r'del_old_materials\Google_maps_Adress_API\config\api_key.json') as f:
    config = json.load(f)

# створюємо об'єкт клієнта Google Maps
api_key = config['google_api_key']

#  клацни правой клавишой по карте и выбери ЧТО ЗДЕСЬ ( внизу будут координаты) latitude, longitude = 30.952025
#  центр Борисполя 
coordinate = '50.350868,30.952025'
keyword = ['кухні на замовлення бориспіль', 'диваны Борисполь', 'мебель Борисполь']
# type_place = ['cafe', 'bank', 'beauty_salon', 'car_wash', 'clothing_store', 'electronics_store', 'hair_care', 
#               'supermarket', 'store', 'shopping_mall', 'restaurant', 'park']

def get_cid_from_coordinates(coordinate, keyword, api_key):
    # Используем Google Places API для поиска местоположения по координатам
    baza_cids = []
    for key in keyword:
        encoded_key = urllib.parse.quote(key.encode('utf-8'))
        places_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword={encoded_key}&location={coordinate}&radius=2500&key={api_key}"
        places_response = requests.get(places_url).json()
        if places_response['status'] != 'OK':
            return "Ошибка поиска местоположений: " + places_response['status']
        for place in places_response['results']:
            # place_ids.append(place['place_id'])
            place_id = place['place_id']
            details_place_id = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={api_key}"
            details_place_id_response = requests.get(details_place_id).json()
            if details_place_id_response['status'] != 'OK':
                return "Ошибка получения деталей местоположения: " + details_place_id_response['status']

            # CID обычно содержится в URL страницы местоположения на Google Maps
            cid = details_place_id_response['result']['url'].split('=')[1]
            baza_cids.append(cid)


def urls_from_cid(baza_cids):
    resolt = f"https://www.google.com/search?q=your+keyword+here&oq=your+keyword+here&rldimm=000000taregtCID00000&rlst=f#rlfi=hd:;si:0000YOURCID00000000"

    return cid


cid = get_cid_from_coordinates(coordinate, keyword, api_key)
print(cid)



# https://maps.googleapis.com/maps/api/place/nearbysearch/json
#   ?keyword=cafe
#   &location=50.363814,30.938732
#   &radius=1500
#   &key=AIzaSyAGU6x_TcuG8zY6ABGf0yoo1PdFLttW1iQ

# import urllib.parse

# original_str = "кухні на замовлення бориспіль"
# encoded_str = urllib.parse.quote(original_str.encode('utf-8'))
 
# print(encoded_str)


