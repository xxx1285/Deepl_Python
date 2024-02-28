import pandas as pd
import pymysql
import json
from datetime import datetime
import time
import random


SQL_CONFIG = r'Parsing\Parsing_BisM\config\config_sql.json'
CSV_FILE = r'Parsing\Parsing_BisM\CSV\result7.csv'

with open(SQL_CONFIG, 'r') as f:
    configSQL = json.load(f)

# Создание словаря для сопоставления 'lang' и 'product_id' с 'resource_id'
mapping = {
    ('ru', 4): 846,     # Прямые диваны
    ('ru', 3): 847,     # Uglovie divani
    ('ru', 8): 848,     # Modulnie divani
    ('ru', 74): 849,    # Divani s otamankou
    ('ru', 5): 850,     # Dvoynie divani
    ('ru', 7): 851,     # Krovati
    ('ru', 124): 852,   # Tahta
    ('ru', 76): 858,    # Light divani
    ('ru', 75): 853,    # Krisla rozkladni
    ('ru', 6): 854,     # Kresla
    ('ru', 113): 855,   # Kuhonni kutochki
    ('ru', 112): 856,   # Pufiki
    # UA
    ('ua', 4): 821,     # Прямые диваны
    ('ua', 3): 822,     # Uglovie divani
    ('ua', 8): 823,     # Modulnie divani
    ('ua', 74): 824,    # Divani s otamankou
    ('ua', 5): 825,     # Dvoynie divani
    ('ua', 7): 826,     # Krovati
    ('ua', 124): 827,   # Tahta
    ('ua', 76): 857,    # Light divani
    ('ua', 75): 828,    # Krisla rozkladni
    ('ua', 6): 829,     # Kresla
    ('ua', 113): 830,   # Kuhonni kutochki
    ('ua', 112): 831,   # Pufiki
}

# Подключение к базе данных
connect_database = pymysql.connect(**configSQL['config_database'],
                                    port=3306,
                                    cursorclass=pymysql.cursors.DictCursor
                                    )


standart_nalashtuvannya = {'published': 0,'editedby': 0,'editedon': 0,'publishedon': 0,'publishedby': 0}
# дата UNIX на даний час для 'createdon': int(time.time()),'pub_date': int(time.time())
# Або визначити самостійно - наприклад через місяць після запуску сайта
new_create_date = {'createdon': int(time.time()),'pub_date': int(time.time())}

# Чтение данных из CSV
df = pd.read_csv(CSV_FILE, sep=';')

# Функция для вставки данных в SQL
def insert_to_sql(row):
    # Применение сопоставления для установки 'resource_id'
    lang = row['lang']
    category_id = row['category_id']
    row['resource_id'] = mapping.get((lang, category_id), None)  # Установка значения по умолчанию, если сопоставление не найдено
    row['product_id'] = row.pop('product_id')
    row['shtrihcode'] = row.pop('shtrihcode')
    # Изменение ключа 'title' на 'res_pagetitle'
    row['pagetitle'] = row.pop('pagetitle')
    row['longtitle'] = row.pop('longtitle')
    row['description'] = row.pop('description')
    row['context_key'] = row.pop('context_key')
    row['section_name'] = row.pop('section_name')
    row['lang'] = row.pop('lang')
    row['alias'] = row.pop('new_url')
    content = row.pop('technical_info')
    row['content'] = f"<p>{content}</p>"
    row['template'] = 29
    row['image'] = f"assets/images/BisM/{row['product_id']}/{row['image']}"
    # row['image'] = row.pop('image')
    row['image_galer_json'] = row.pop('image_galer_json')

    row['menuindex'] = 1
    row['published'] = 1
    row['editedon'] = 0
    row['editedby'] = 0
    row['createdby'] = 0
    row['deleted'] = 0
    row['deletedon'] = 0
    row['deletedby'] = 0
    row['publishedon'] = 0
    row['publishedby'] = 0
    row['unpublishedon'] = 0

    row['youtube'] = 0

    current_time = datetime.now()
    unix_timestamp = int(time.mktime(current_time.timetuple())) - 50000
    random_time = random.choice([500, 9000, 12300, 2850, 21336, 4670, 15700, 13820, 16820, 25700, 23820, 26820, 35700, 33820, 36820])
    new_createdon = unix_timestamp + random_time
    row['createdon'] = new_createdon

    # Виключити ключи с данными с таблицы
    keys_to_exclude = ['category_id', 'bism_url']
    # Исключение указанных ключей из row
    for key in keys_to_exclude:
        if key in row:
            del row[key]


    row_database_game = row.to_dict()

    keys = ", ".join([f"`{key}`" for key in row_database_game.keys()])
    values = tuple(row_database_game.values())
    on_duplicate_key_update = ", ".join([f"`{key}`=VALUES(`{key}`)" for key in row_database_game.keys()])

    sql_resurs = f"INSERT INTO `modx_myagh_co` ({keys}) VALUES ({', '.join(['%s'] * len(values))}) ON DUPLICATE KEY UPDATE {on_duplicate_key_update}"
    return sql_resurs, values

# Выполнение SQL-запросов для каждой строки DataFrame
with connect_database.cursor() as cursor:
    for index, row in df.iterrows():
        sql_query, data = insert_to_sql(row)
        cursor.execute(sql_query, data)
    connect_database.commit()

connect_database.close()
print("Данные успешно добавлены в базу данных.")
