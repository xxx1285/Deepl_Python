import json
import googlemaps
import urllib.parse


input_file = r'GOOGLE\Google_Maps_Marshrut_BOT\input\input_borispol_adress_v2-test.txt'
output_file_txt = r'GOOGLE\Google_Maps_Marshrut_BOT\input\output_borispol_adress_Instadivan_txt_3.txt'

# Google Maps - Конфиг и обьект клиента
with open(r'GOOGLE\Google_maps_Adress_API\config\api_key.json') as f:
    config = json.load(f)
gmaps = googlemaps.Client(key=config['google_api_key'])

# Створюємо список адрес з вхідного файла
with open(input_file, 'r', encoding='utf-8') as file:
    lines_data = file.readlines()

# new_url = "https://www.google.com/maps/dir//" + urllib.parse.quote(start_adress) + "/@" + str(start_adress_coords['lat']) + "," + str(start_adress_coords['lng']) + "0?entry=ttu"
# print(new_url)

#############################################################
# Обробка і збереження в TXT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
with open(output_file_txt, 'a', encoding='utf-8') as file:
    for adress in lines_data:

        if len(adress) < 10:
            continue

        adress_coords = gmaps.geocode(adress)[0]['geometry']['location']

        # new_url = "https://www.google.com/maps/dir/" + urllib.parse.quote(adress) + "/" + urllib.parse.quote(start_adress) + "/@" + str(adress_coords['lat']) + "," + str(adress_coords['lng']) + "," + str(start_adress_coords['lat']) + "," + str(start_adress_coords['lng']) + "0?entry=ttu"
        new_url = "https://www.google.com/maps/dir/" + urllib.parse.quote(adress) + "//@" + str(adress_coords['lat']) + "," + str(adress_coords['lng']) + ",13z?entry=ttu"

        file.write(new_url + '\n')

print("All GOOD")





# address_coords = gmaps.geocode(address)[0]['geometry']['location']
# # new_url = "https://www.google.com/maps/dir/" + urllib.parse.quote(start_adress) + "//@" + str(start_adress_coords['lat']) + "," + str(start_adress_coords['lng']) + "/?entry=ttu"
# new_url = f"https://www.google.com/maps/dir/{urllib.parse.quote(address)}//@{address_coords['lat']},{address_coords['lng']}/?entry=ttu"
