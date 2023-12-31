import os
import random
import string
import json

# Пути к каталогам с изображениями
people_images_dir = r'D:\Gembling\GAMES\player_img_80_80'
casino_images_dir = r'D:\Gembling\GAMES\casino_img_80_80'
SAVE_JSON = r"JSON_scripts\create_json_Win_in_games\output\output_gatesof.json"

def get_file_names(directory):
    """ Получение всех имен файлов из указанной директории """
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def generate_random_name(names_start_list, names_end_list):
    """ Генерация случайного имени """
    name_start = random.choice(names_start_list)
    name_end = random.choice(names_end_list)
    # random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
    return f"{name_start}***{name_end}"

def generate_random_win():
    """ Генерация случайного выигрыша """
    win = random.randint(100, 800)
    if win > 600:
        win = win - (win % 10)
    return str(win)


# Получение списков имен файлов из каталогов
people_images = get_file_names(people_images_dir)
casino_images = get_file_names(casino_images_dir)

# Список имен для генерации имени человека
names_start_list = ['Noa', 'Fat', 'Bla', 'Ant', 'Han', 'Sha', 'Ais', 'Lis', 'Koj', 'Kof', 'Dav', 'Oli', 'Olu', 
              'Dra', 'Ada', 'Kai', 'Lun', 'Fal', 'Nin', 'Idr', 'Wol', 'Zac', 'San', 'Yus', 'Haw', 'Ale', 
              'Ros', 'Ass', 'Pat', 'Vic', 'Uly', 'Emi', 'Rob', 'Mas', 'Inf', 'Kat', 'Seb', 'Jag', 'Sop', 
              'Keh', 'Bet', 'Pre', 'Leo', 'Mav', 'Kim', 'Xav', 'Yar', 'Rav', 'Isa', 'Zoe', 'Fin', 'Hen', 
              'Mia', 'Pho', 'Joh', 'Iri', 'Xen', 'Ash', 'Don', 'Ben', 'Jam', 'Vor', 'Nor', 'Qui', 'And', 
              'Uma', 'Tho', 'Par', 'Ami', 'Eli', 'Chr', 'Eag', 'Wiz', 'Wil', 'Dia', 'Kar', 'Pau', 'Sar', 
              'Jos', 'Dje', 'Pan', 'War', 'Chi', 'Jes', 'Yaw', 'Lia', 'Tig', 'Cha', 'Pen', 'Rya', 'Mar', 
              'Aur', 'Ric', 'Cyc', 'Vio', 'Sni', 'Tar', 'Ste', 'Bel', 'Mat']
names_end_list = ['777', '8LI', '3Pi', 'TOR', 'HAH', 'sha', '969', '555', '212', 'K13', 'DDD', 'oli', 'olu', 
                'dra', '997', '787', '777', 'FAX', '0in', 'ili', 'WwW', 'zac', 'san', 'usa', 'chu', 'lex', 
                'D777', 'X:)', 'pat1', 'vic7', 'uly88', 'e0m7i', '7b77', 'lDas', '1Inf', 'kKat', 'Seb9', 'kag:)', 'SoSo', 
                'Keh', 'Bet', 'Pre', 'Leo', 'Mav', 'Kim', 'Xav', 'Yar', 'Rav', 'Isa', 'Zoe', 'Fin', 'Hen', 
                'Z1Pz', 'R2D2', 'L33T', 'Pwn4', 'G4me', 'K3n0', 'B0ss', 'N1nj', 'H4wk', '888', '000', 'F:)',
                'V3ga', 'R0kz', 'M3ch', 'Zyx4', 'Q8Ti', 'J4Xx', 'W1zZ', 'E1Te', 'S1m0', '888', '000', 'D:)',
                'Ufo3', 'Y2Kz', 'B4tz', 'F1zZ', 'O3Oz', 'X9Xx', 'T2T2', 'M1M1', 'V8V8', '888', '000', 'J:)',
                'K9K9', 'Q5Q5', 'Z0R0', 'L7L7', 'G3G3', 'J7J7', 'F5F5', 'H2Oo', 'M0M0', '888', '000', 'D:)',
                'N1N1', 'O2O2', 'P3P3', 'R1R1', '777', '777', '777', '777', '777', '888', '888', '888']
european_countries = [
    "Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", 
    "Bulgaria", "Denmark", "Estonia", "Finland", "France",
    "Georgia", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kazakhstan",
    "Latvia", "Lithuania", "Luxembourg", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Russia",
    "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey",
    "Ukraine", "United Kingdom", "India", "Japan", "Kyrgyzstan", "Nepal", 
    "Russia", "Saudi Arabia", "Tajikistan", "Turkey", "Turkmenistan",
    "United Arab Emirates", "Uzbekistan", "Canada"
]


# Генерация 1000 объектов
json_data = []
for _ in range(30):
    people_images2 = random.choice(people_images)
    two_list_people_images = ['incognito-man.png', people_images2, people_images2]

    entry = {
        "person_img": random.choice(two_list_people_images),
        "countries": random.choice(european_countries),
        "person_name": generate_random_name(names_start_list, names_end_list),
        "casino_catalog_img": random.choice(casino_images),
        "how_win": generate_random_win()
    }
    json_data.append(entry)

# Конвертирование списка в JSON
json_output = json.dumps(json_data, indent=4)

with open(SAVE_JSON, 'w') as file:
    file.write(json_output)

# Вывод первых 500 символов для примера
print(json_output[:500])