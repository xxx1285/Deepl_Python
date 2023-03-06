# import os
import time
import random
import re
import json
import pymysql
from bs4 import BeautifulSoup
import transliterate
# import datetime
import deepl


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

xren = 0

# SQL Зчитуємо параметри з конфігураційного файлу
with open(r'SQL_clon_modx_resourse\configs\config_sql_Deepl.json') as f:
    config = json.load(f)


"""
    modx_context_setting                настройки контекстов (catalog id, site_start, site_url, nazva)
    modx_site_content                   ресурсы сайта
    modx_site_tmplvar_contentvalues     VNIMANIE - BABEL
    modx_games_co                       MIGX content Resourses
"""
my_tables = ['modx_context_setting', 'modx_site_content', 'modx_site_tmplvar_contentvalues',
             'modx_games_co']
# my_tables_str = ", ".join(my_tables)

# Контексти з якого копіюємо
context_web = 'web'
# Контексти та мови для перекладу
context_and_lang = ["ru","es","pl","pt","fr","id","el","de","tr","hu","uk","it","ro","bg","fi","et","lv","nl"]

# Поля що потрібно перекласти
translate_name = ['pagetitle','longtitle','description','menutitle']
dont_translate = ['Aviator', 'The dog house']

standart_nalashtuvannya = {
    'published': 0,
    'editedby': 0,
    'editedon': 0,
    'publishedon': 0,
    'publishedby': 0
}
# дата UNIX на даний час
new_create_date = {
    'createdon': int(time.time()),
    'pub_date': int(time.time())
}


try:
    # Приєднуємось до бази для Export SQL
    connect_database = pymysql.connect(**config['config_database'],
                                       port=3306,
                                       cursorclass=pymysql.cursors.DictCursor
                                       )
    print("\n*************************************\
            \n--> Succesfully connect - " + config['config_database']['database'])

    # Ініціалізуємо Deepl API key
    translator = deepl.Translator(config['config_deepl']['deepl_api_key'])
    print("--> Deepl API - OK \n*************************************")

    with connect_database.cursor() as my_cursor:
        # Выбор всех строк таблицы modx_site_content, где context = 'web' id = 75
        my_cursor.execute(f"SELECT * FROM modx_site_content WHERE `context_key` = '{context_web}' \
                            AND (`id` = 75 OR `template` IN (6,7,19))")
        rows_database = my_cursor.fetchall()

        # перебираємо контексти (язики) - lang
        for lang in context_and_lang:
            # перебираємо кожен вибраний рядок в SQL таблиці
            for row in rows_database:

                # Клонуємо рядок
                new_row = row.copy()

                # Змінюємо context на поточне значення мови
                new_row['context_key'] = lang

                for key, value in standart_nalashtuvannya.items():
                    new_row[key] = value
                # {**new_row, **{key: value for key, value in standart_nalashtuvannya.items()}}

                # randon секунди дати UNIX
                random_time = random.choice([15150, 18300, 21500, 23700, 40320])

                new_create_date['createdon'] = new_create_date['createdon'] + random_time
                new_row['createdon'] = new_create_date['createdon']

                new_create_date['pub_date'] = new_create_date['pub_date'] + random_time
                new_row['pub_date'] = new_create_date['pub_date']
                print(type(new_row))

                # Перекладаємо поля використовуючи DEEPL
                for name in translate_name:
                    # Замінюємо входження зі списку dont_translate на тег <keep>
                    for word in dont_translate:
                        new_row[name] = new_row[name].replace(word, f"<keep>{word}</keep>")

                    translate = translator.translate_text(new_row[name], tag_handling='xml', ignore_tags='keep', target_lang=lang)
                    new_row[name] = str(translate)
                    new_row[name] = new_row[name].replace("<keep>", "").replace("</keep>", "")

                TODO: АлИАС

                TODO: Якщо Parent not 0 ???????????   або  Якщо is folder ???????

                TODO: настройка контекста

                TODO: Babel

                TODO: modx_games_co








                # for i in new_row:
                #     print(i, new_row[i])

                # print("3333")


                xren += 1
                print(str(xren) + ' - ' +str(new_row['pub_date']) + ' - ' + str(datetime.datetime.fromtimestamp(new_row['pub_date'])))
                # print(datetime.datetime.fromtimestamp(new_row['pub_date']))





        #     # Загальний список значень для таблиці
        #     all_values = []

        #     # перебираємо кожен рядок таблиці
        #     for row in rows:
        #         # values = ', '.join([f"'{value.hex()}'" if isinstance(value, bytes) else f"'{value}'" for value in row.values()])
        #         # формируємо список значень для кожного рядка
        #         values = []
        #         for value in row.values():
        #             # Якщо значення є NULL, додати до списку значення 'NULL'
        #             if value is None:
        #                 values.append('NULL')
        #             elif isinstance(value, bytes):
        #                 value = value.hex()
        #                 values.append(f"'{value}'")
        #             # Якщо значення є рядком, додати до списку лапки з екрануванням лапок всередині рядка
        #             elif isinstance(value, str):
        #                 # values.append("'" + value.replace("'", "\\'") + "'")
        #                 # value = value.replace("'", "\\'").replace('"', '\\"')
        #                 value = value.replace("'", "\\'")
        #                 values.append(f"'{value}'")
        #             # Якщо значення є числом, додати до списку без лапок
        #             elif isinstance(value, (int, float)):
        #                 values.append(f"{value}")
        #             else:
        #                 values.append(f"'{value}'")
        #             # добавляем значение в список значений

        #         # объединяем список значений в строку, разделяя их запятыми
        #         values = ', '.join(values)

        #         # об'єднуємо список полів до таблиці
        #         fields = ', '.join([f"`{key}`" for key in row.keys()])

        #         # Добаляємо значення в Загальний список значень для таблиці
        #         all_values.append(f"({values})")

        #     # об'єднуємо загальий список значень таблиці розділяючи комами та з нової
        #     all_values = ', \n'.join(all_values)

        #     # fields = ', '.join([f"`{key}`" for key in row.keys()])
        #     #     # insert_query = f"INSERT INTO `{table}` ({fields}) VALUES ({values});\n"
        # # insert_query = f"INSERT INTO `{table}` ({fields}) VALUES\n{all_values};\n"


except Exception as ex:
    print("Connection refused...")
    print(ex)
finally:
    connect_database.close()
    print("Connection Export CLOSE")
