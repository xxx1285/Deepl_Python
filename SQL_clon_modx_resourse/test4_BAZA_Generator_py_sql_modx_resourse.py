
# v.0.0.1
# import os
import time
import random
import re
import json
import pymysql
from bs4 import BeautifulSoup
from unidecode import unidecode
import datetime
import deepl
import csv
import os


# функція що додає екранування - JSON
def my_add_ekran_string(string):
    string = string.replace('/', '\\/')
    string = string.replace('"', '\\"')
    string = string.replace("'", "\\'")
    return string

# функція що видаляє екранування та символи - JSON
def my_clean_ekran_string(string):
    string = string.replace('\n', '')
    string = string.replace('\t', '')
    string = string.replace('&nbsp;', '')
    return string


# SQL Зчитуємо параметри з конфігураційного файлу
with open(r'SQL_clon_modx_resourse\configs\config_sql_Deepl.json') as f:
    config = json.load(f)


# TODO:сайт для якого обробляємо - з слешем вкінці
my_site = "https://gatesofolympus.club/"
site_name = "Gates of Olympus"
# футер настройка - перекласти на багато мов
footer_allrights = 'All rights to the "Gates of Olympus" brand, trademark and game are owned by Pragmatic play'

csv_url_file = r"SQL_clon_modx_resourse\csv\gatesofolympus_club.csv"  # !!!!!! СТВОРИ ВРУЧНУ ФАЙЛ

"""
#############################################
    >>>>    modx_site_content
##############################################
"""
# Контекст по замовчуванням (web == en) та з якого копіюємо
context_web = 'web'

# TODO: id шаблона AMP - та id каталога AMP
amp_templates = 7
amp_catalog = 14
# TODO: Контексти та мови для перекладу
context_and_lang = ["ru"]
# context_and_lang = ["ru","es","pl","pt-br","fr","id","el","de","tr","hu","uk","it","ro","bg","fi","et",
#                     "lt","lv","nl","cs","da","ja","nb","sk","sl","sv"]
# web,ru,es,pl,pt-br,fr,id,el,de,tr,hu,uk,it,ro,bg,fi,et,lt,lv,nl,cs,da,ja,nb,sk,sl,sv,az,kk,ar,uz


# Словник звязаних між собою EN Контекста та інших Ресурсів
dict_id_clon_resouses = {}

# Не змінювати - базове налаштування - стартовий ID
start_id = 0

# Поля що потрібно перекласти
translate_name = ['pagetitle','menutitle']
# translate_name = ['pagetitle','longtitle','description','menutitle']

# TODO: Слова які не потрібно перекладати 'Aviator', 'The dog house', 'Gates of Olympus'
dont_translate = ['Aviator', 'The dog house', 'Gates of Olympus', 'Pragmatic play']

# Стандартні налаштувавання бази
standart_nalashtuvannya = {'published': 0,'editedby': 0,'editedon': 0,'publishedon': 0,'publishedby': 0, 'properties': 'NULL'}

# дата UNIX на даний час для 'createdon': int(time.time()),'pub_date': int(time.time())
# Або визначити самостійно - наприклад через місяць після запуску сайта
new_create_date = {'createdon': int(time.time()),'pub_date': int(time.time())}


"""
############################################
    >>>>    modx_context_setting
#############################################
"""
cazino_catalog_id = 6
locale_alternate = {'bg': '[[$bg_BG]]', 'cs': '[[$cs_CZ]]', 'da': '[[$da_DK]]', 'de': '[[$de_DE]]', 'el': '[[$el_GR]]',
                    'en': '[[$en_UK]]', 'es': '[[$es_ES]]', 'et': '[[$et_EE]]', 'fi': '[[$fi_FI]]', 'fr': '[[$fr_FR]]',
                    'hu': '[[$hu_HU]]', 'id': '[[$id_ID]]', 'it': '[[$it_IT]]', 'ja': '[[$ja_JP]]', 'lt': '[[$lt_LT]]',
                    'lv': '[[$lv_LV]]', 'nb': '[[$nb_NO]]', 'nl': '[[$nl_NL]]', 'pl': '[[$pl_PL]]', 'pt-br': '[[$pt_BR]]',
                    'ro': '[[$ro_RO]]', 'ru': '[[$ru_RU]]', 'sk': '[[$sk_SK]]', 'sl': '[[$sl_SL]]', 'sv': '[[$sv_SE]]',
                    'tr': '[[$tr_TR]]', 'uk': '[[$uk_UA]]',
                    'ar': '[[$ar_EG]]', 'az': '[[$az_AZ]]', 'kk': '[[$kk_KZ]]', 'uz': '[[$uz_UZ]]'
               }

"""
##################################################################
    >>>>    BABEL BABEL BABEL - modx_site_tmplvar_contentvalues
##################################################################
"""
babel_baza_dict = {}  # словник контекстів та звязаних id


# try:
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

    # Мах id в таблиці
    # lambda x: x['id']: це анонімна (lambda) функція, яка приймає на вхід один аргумент x
    # (в нашому випадку, словник зі списку freadf) і повертає значення за ключем 'id'.
    # Ми створюємо цю функцію, щоб вказати, які значення ми хочемо порівнювати під час пошуку максимального значення
    max_id = max(rows_database, key=lambda x: x['id'])['id']

    # CSV створюємо файл для запису
    csv_id = 0
    with open(csv_url_file, 'w', newline='', encoding='utf-8') as file:
        field_names = ['csv_id', 'id', 'lang', 'menutitle', 'pubdate', 'pubdatetime', 'url']
        csv_writer = csv.DictWriter(file, fieldnames=field_names)
        csv_writer.writeheader()

        # перебираємо контексти (язики) - lang
        for lang in context_and_lang:

            # ################################################################################################
            # # TODO: modx_site_content
            # ################################################################################################

            # Структура id з new id щоб зробити (вложения) вкладення в структуру - та для AMP
            struktura_id_map = {}

            # Структура для внутрішньої перелінковки - {id: alias, new_id, new_alias}
            struktura_id_alias_map = {}

            # перебираємо кожен вибраний рядок в SQL таблиці
            for row in rows_database:

                # Клонуємо рядок
                new_row = row.copy()

                # Змінюємо context (по стандарту - web) на поточне значення мови
                new_row['context_key'] = lang

                # ID - Визначаємо новий id та записуємо в словник, Змінюємо id збільшуючи на +1
                if start_id == 0:
                    start_id = max_id + 1
                else:
                    start_id += 1

                new_row['id'] = start_id
                struktura_id_map[row['id']] = new_row['id']

                # BABEL baza _ADD в словник звязоних між собою ID
                babel_baza_dict.setdefault(row['id'], {row['context_key']: row['id']})
                babel_baza_dict[row['id']].setdefault(new_row['context_key'], new_row['id'])

                # PARENT - Визначаємо структуру
                if new_row['parent'] != 0:
                    new_row['parent'] = struktura_id_map[new_row['parent']]
                    # print(str(row['parent']) + " - " + str(new_row['parent'])  + " : " + str(row['menutitle']))

                # AMP -ID - Content налаштування
                if new_row['template'] == amp_templates:
                    for key, value in struktura_id_map.items():
                        if str(key) == row['content']:
                            new_row['content'] = value
                            # print(str(row['id']) + " - " + str(new_row['id'])  + " : " + str(new_row['content']))

                # Стандартні налаштування published-editedby-editedon-publishedon-publishedby
                for key, value in standart_nalashtuvannya.items():
                    new_row[key] = value
                    # {**new_row, **{key: value for key, value in standart_nalashtuvannya.items()}}

                # pub_date - Дата публікації
                # randon секунди дати UNIX ( 6 годин - це 21000)
                random_time = random.choice([22850, 35700, 40200, 42320])
                random_pub_date = random.choice([1350, 2450])

                new_create_date['createdon'] = new_create_date['createdon'] + random_time
                new_row['createdon'] = new_create_date['createdon']
                new_create_date['pub_date'] = new_create_date['pub_date'] + random_time + random_pub_date
                new_row['pub_date'] = new_create_date['pub_date']
                print(str(lang) + ' - ' + str(new_row['id']) + ': ' + str(datetime.datetime.fromtimestamp(new_row['pub_date'])))

                # # TRANSLATE - Перекладаємо поля використовуючи DEEPL
                # for name in translate_name:
                #     if len(new_row[name]) > 0:
                #         # Замінюємо входження зі списку dont_translate на тег <keep>
                #         for word in dont_translate:
                #             #new_row[name] = new_row[name].replace(word, f"<keep>{word}</keep>")
                #             # без врахування регістру
                #             new_row[name] = re.sub(f'(?i){re.escape(word)}', f"<keep>{word}</keep>", new_row[name])
                #         translate = translator.translate_text(new_row[name], tag_handling='xml', ignore_tags='keep', target_lang=lang)
                #         new_row[name] = translate.text
                #         new_row[name] = new_row[name].replace("<keep>", "").replace("</keep>", "")
                #         # видаляэмо - \n, \t, "
                #         new_row[name] = my_clean_ekran_string(new_row[name])

                # ALIAS - транслітерація
                if len(new_row['menutitle']) > 0:
                    new_row['alias'] = unidecode(new_row['menutitle'].lower())
                else:
                    new_row['alias'] = unidecode(new_row['pagetitle'].lower())
                new_row['alias'] = re.sub(r'[^a-zA-Z0-9]+-*$' , '', re.sub(r'[^a-zA-Z0-9]+', '-', new_row['alias']))
                new_row['uri'] = str(new_row['alias'] + '/')
                if new_row['template'] == amp_templates:
                    new_row['alias'] = 'amp-' + str(new_row['alias'])
                    new_row['uri'] = 'amp/amp-' + str(new_row['uri'])
                if row['id'] == amp_catalog:
                    new_row['alias'] = 'amp'
                    new_row['uri'] = 'amp/'

                # Структура id:alias для внутрішньої перелінковки
                struktura_id_alias_map[row['id']] = my_site + row['uri']
                struktura_id_alias_map[new_row['id']] = my_site + lang + '/'+ new_row['uri']

                # SQL INSERT запись modx_site_content
                baza_key_new_row = ", ".join([f"`{key}`" for key in new_row.keys()])
                baza_value_new_row = tuple(new_row.values())
                baza_sql_dublikat = ", ".join([f"`{key}`=VALUES(`{key}`)" for key in new_row.keys()])
                # with connect_database.cursor() as cursor:
                #     # Create a new record
                #     sql_resurs = f"INSERT INTO `modx_site_content` ({baza_key_new_row})\
                #                     VALUES {baza_value_new_row} \
                #                     ON DUPLICATE KEY UPDATE {baza_sql_dublikat}"
                #     cursor.execute(sql_resurs)
                # connect_database.commit()

                # CSV
                if new_row['id'] == struktura_id_map[1]:  # URI
                    css_uri = str(lang) + '/'
                else:
                    css_uri = str(lang) + '/' + new_row['uri']
                if len(new_row['menutitle']) > 4:  # Menutitle or Pagetitle
                    css_name = new_row['menutitle']
                else:
                    css_name = new_row['pagetitle']

                csv_writer.writerow({'csv_id': csv_id,
                                    'lang': lang,
                                    'id': new_row['id'],
                                    'menutitle': css_name,
                                    'pubdate': new_row['pub_date'],
                                    'pubdatetime': str(datetime.datetime.fromtimestamp(new_row['pub_date'])),
                                    'url': my_site + css_uri,
                                    })
                csv_id += 1


            ################################################################################################
            # TODO: modx_games_co
            ################################################################################################

            # for key_row, key_new_row in struktura_id_map.items():  # перебираем структуру ресурсов row and new_row

            #     # Выбор всех строк таблицы modx_games_co
            #     my_cursor.execute(f"SELECT * FROM modx_games_co WHERE `resource_id` = '{key_row}'")
            #     row_database_game = my_cursor.fetchone()

            #     if row_database_game is not None:
            #         # resource_id
            #         row_database_game['resource_id'] = key_new_row
            #         # id такий як і в ресурса
            #         row_database_game['id'] = key_new_row

            #         # res_context_key - Контекст або мова
            #         row_database_game['res_context_key'] = lang

                    # # TRANSLATE - Перекладаємо поля без HTML використовуючи DEEPL
                    # translate_title_games_co = ['res_pagetitle','res_longtitle','b1_comments_h2','b1_video_json_h2',
                    #                             'b0_res_content','image_galer_h2','faq_block_h2','casino_geo']
                    # for name in translate_title_games_co:
                    #     if len(row_database_game[name]) > 1:
                    #         for word in dont_translate:
                    #             # row_database_game[name] = row_database_game[name].replace(word, f"<keep>{word}</keep>")
                    #             row_database_game[name] = re.sub(f'(?i){re.escape(word)}', f"<keep>{word}</keep>", row_database_game[name])
                    #         translate_title = translator.translate_text(row_database_game[name], tag_handling='xml', ignore_tags='keep', target_lang=lang)
                    #         row_database_game[name] = translate_title.text
                    #         row_database_game[name] = row_database_game[name].replace("<keep>", "").replace("</keep>", "")

                    # TRANSLATE - Розбираємо та перекладаємо JSON поля DEEPL
                    # translate_baza_keys = {'b1_content_json': {'h2_title':'','description':'','alt_img':''},
                    #                     'b1_demo_iframe': {'demo_h2':'','alt_img':''},
                    #                     'b1_content_table_json': {'td_1':'','td_2':''},
                    #                     'b1_comments_json': {'h3_name_comment':'','p_review_comment':'','person_name':''},
                    #                     'b1_video_json': {'video_name':'','video_description':''},
                    #                     'image_galer_json': {'description':''},
                    #                     'faq_block_json': {'question_text':'','answer_text':''}
                    #                     }
                    # for key, value in translate_baza_keys.items():
                    #     if row_database_game[key] is not None and len(row_database_game[key]) > 0:  # перевіряємо чи не пусте JSON поле
                    #         sql_json = json.loads(row_database_game[key])  # розпакуємо JSON
                    #         for row_json in sql_json:
                    #             for key_baza in value.keys():
                    #                 # Translate JSON if not NONE
                    #                 if len(row_json[key_baza]) > 0:
                    #                     # Замінюємо входження зі списку dont_translate на тег <keep>
                    #                     for word in dont_translate:
                    #                         # row_json[key_baza] = row_json[key_baza].replace(word, f"<keep>{word}</keep>")
                    #                         row_json[key_baza] = re.sub(f'(?i){re.escape(word)}', f"<keep>{word}</keep>", row_json[key_baza])
                    #                     # # DEEPL переклад
                    #                     # translate_json = translator.translate_text(row_json[key_baza], tag_handling='xml', ignore_tags='keep', target_lang=lang)
                    #                     # row_json[key_baza] = translate_json.text
                    #                     # row_json[key_baza] = row_json[key_baza].replace("<keep>", "").replace("</keep>", "")
                    #                     # видаляэмо - \n, \t, "
                    #                     row_json[key_baza] = my_clean_ekran_string(row_json[key_baza])
                    #                     if key == 'b1_comments_json' or key == 'faq_block_json':
                    #                         row_json[key_baza] = row_json[key_baza].replace('"', '')

                    #                     # Визначаємо регулярний вираз для пошуку посилань (перелінковка кожного контексту)
                    #                     pattern = r'<a\s+href="(.*?)".*?>.*?</a>'
                    #                     #re.search шукає перше входження відповідності регулярному виразу у заданому рядку, повертає об'єкт "Match"
                    #                     if re.search(pattern, row_json[key_baza]):
                    #                         # re.findall знаходить всі невкладені відповідності регулярному виразу та повертає список
                    #                         for match in re.findall(pattern, row_json[key_baza]):
                    #                             # Перебираємо всі ключі та значення зі структури аліасів
                    #                             for key_alias_map, value_alias_map in struktura_id_alias_map.items():
                    #                                 # Якщо знайдено відповідне значення аліасу, то замінюємо посилання
                    #                                 if match == value_alias_map:
                    #                                     print(row_json[key_baza])
                    #                                     map_key = struktura_id_map[key_alias_map]
                    #                                     # Отримуємо нове посилання за допомогою ключа зі структури
                    #                                     new_href = struktura_id_alias_map.get(map_key, match)
                    #                                     # Замінюємо оригінальне посилання на нове
                    #                                     row_json[key_baza] = row_json[key_baza].replace(match, new_href)
                    #                                     print(row_json[key_baza])
                    #                                     break

                    #             row_database_game[key] = json.dumps(sql_json)
                    #             #######################
                    #     elif row_database_game[key] is None:
                    #         row_database_game[key] = 'NULL'

                    # # SQL INSERT запись modx_games_co
                    # baza_key_games_co = ", ".join([f"`{key}`" for key in row_database_game.keys()])
                    # baza_value_games_co = tuple(row_database_game.values())
                    # baza_sql_dublikat_games_co = ", ".join([f"`{key}`=VALUES(`{key}`)" for key in row_database_game.keys()])

                    # with connect_database.cursor() as cursor:
                    #     # Create a new record
                    #     sql_resurs = f"INSERT INTO `modx_games_co` ({baza_key_games_co})\
                    #                     VALUES {baza_value_games_co} \
                    #                     ON DUPLICATE KEY UPDATE {baza_sql_dublikat_games_co}"
                    #     cursor.execute(sql_resurs)
                    # connect_database.commit()



            # ################################################################################################
            # # TODO: CONTEXT настройка контекста - modx_context_setting
            # ################################################################################################

            keys_context_setting = {'base_url': f'/{lang}/',
                                    'cazino_catalog_id': struktura_id_map[6],
                                    'chan_locale': locale_alternate[lang],
                                    'cultureKey': lang,
                                    'error_page': struktura_id_map[2],
                                    'locale': locale_alternate[lang].replace("[[$", "").replace("]]", ""),
                                    'site_name': site_name,
                                    'site_start': struktura_id_map[1],
                                    'site_url': f'{my_site}{lang}/'
                                    }
            # TRANSLATE - контекст параметри через DEEPL
            # ???????????????????????????????????????????????????????????????????????????????
            translate_context_param = [footer_allrights]
            for name in translate_context_param:
                if len(row_database_game[name]) > 1:
                    for word in dont_translate:
                        # row_database_game[name] = row_database_game[name].replace(word, f"<keep>{word}</keep>")
                        row_database_game[name] = re.sub(f'(?i){re.escape(word)}', f"<keep>{word}</keep>", row_database_game[name])
                    translate_title = translator.translate_text(row_database_game[name], tag_handling='xml', ignore_tags='keep', target_lang=lang)
                    row_database_game[name] = translate_title.text
                    row_database_game[name] = row_database_game[name].replace("<keep>", "").replace("</keep>", "")

            for key, value in keys_context_setting.items():
                # SQL INSERT запись modx_context_setting
                with connect_database.cursor() as cursor_set:
                    sql_babel = "INSERT INTO `modx_context_setting` (`context_key`, `key`, `value`, `xtype`, `namespace`, `area`) \
                                VALUES (%s, %s, %s, %s, %s, %s) \
                                ON DUPLICATE KEY UPDATE value=VALUES(value), xtype=VALUES(xtype), namespace=VALUES(namespace), area=VALUES(area)"
                    val = (lang, key, value, 'textfield', 'core', 'language')
                    cursor_set.execute(sql_babel, val)
                connect_database.commit()


    ################################################################################################
    # TODO: Babel - INSERT SQL - modx_site_tmplvar_contentvalues
    ################################################################################################

    # Додамо вручну РУ - якщо існує
    # ru_versiya = {1: {'ru': 104}, 3: {'ru': 107}, 4: {'ru': 109}, 5: {'ru': 121}, 6: {'ru': 111}, 30: {'ru': 113},
    #               21: {'ru': 112}, 124: {'ru': 128}}

    # ru_versiya_keys = ru_versiya.keys()

    # for key in ru_versiya_keys:
    #     if key in babel_baza_dict:
    #         babel_baza_dict[key].update(ru_versiya[key])
    #     else:
    #         babel_baza_dict[key] = ru_versiya[key]
    ##################################################################################################

    for babel_row in babel_baza_dict.values():
        # перебираэмо словник контекстів та звязаних id
        result_value_str = ";".join([f"{key}:{value}" for key, value in babel_row.items()])
        for contentid in babel_row.values():
            # print(str(contentid) + " - " + result_str)
            with connect_database.cursor() as cursor_bab:
                sql_babel = "INSERT INTO `modx_site_tmplvar_contentvalues` (tmplvarid, contentid, value) VALUES (%s, %s, %s) \
                             ON DUPLICATE KEY UPDATE value = VALUES (value)"
                val = (1, contentid, result_value_str)
                cursor_bab.execute(sql_babel, val)
            connect_database.commit()

# except Exception as ex:
#     print("Connection refused...")
#     print(ex)
# finally:
#     connect_database.close()
#     print("ALL GOOD - Connection CLOSE")
print("ALL GOOD - Connection CLOSE")
connect_database.close()
