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


# функція що додає екранування - JSON
def my_add_ekran_string(string):
    string = string.replace('/', '\\/')
    string = string.replace('"', '\\"')
    string = string.replace("'", "\\'")
    return string

# функція що видаляє екранування та символи - JSON
def my_clean_ekran_string(string):
    string = string.replace('\\', '')
    string = string.replace('&nbsp;', '')
    return string


# # функція що очищає або добавляє екранування - JSON
# def my_clean_string(string, escape=True):
#     if escape:
#         # Замінюємо спеціальні символи на їх екрановані еквіваленти
#         string = string.replace('/', '\/')
#     else:
#         # Видаляємо екранування спеціальних символів
#         string = string.replace('\\', '')
#         # string = string.replace('\n', '')
#         # string = string.replace('\t', '')
#         string = string.replace('&nbsp;', '')
#     return string


# SQL Зчитуємо параметри з конфігураційного файлу
with open(r'SQL_clon_modx_resourse\configs\config_sql_Deepl.json') as f:
    config = json.load(f)


# TODO:сайт для якого обробляємо - з слешем вкінці
my_site = "https://gatesofolympus.club/"
site_name = "Gates of Olympus"

"""
#############################################
    >>>>    modx_site_content
##############################################
"""
# Контекст по замовчуванням (web == en) та з якого копіюємо
context_web = 'web'
# TODO: Максимальний id в таблиці
start_id = 200
# Контексти та мови для перекладу
context_and_lang = ["ru","es","pl","pt-br","fr","id","el","de","tr","hu","uk","it","ro","bg","fi","et",
                    "lt","lv","nl","cs","da","ja","nb","sk","sl","sv"]
# web,ru,es,pl,pt-br,fr,id,el,de,tr,hu,uk,it,ro,bg,fi,et,lt,lv,nl,cs,da,ja,nb,sk,sl,sv,az,kz,ar,uz


# Словник звязаних між собою EN Контекста та інших Ресурсів
dict_id_clon_resouses = {}

# Поля що потрібно перекласти
translate_name = ['pagetitle','menutitle']
# translate_name = ['pagetitle','longtitle','description','menutitle']

# Слова які не потрібно перекладати
dont_translate = ['Aviator', 'The dog house', 'Gates of Olympus']

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
                    'ar': '[[$ar_EG]]', 'az': '[[$az_AZ]]', 'kz': '[[$kz_KZ]]', 'uz': '[[$uz_UZ]]'
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

    # перебираємо контексти (язики) - lang
    for lang in context_and_lang:

        # Структура id з new id щоб зробити (вложения) вкладення в структуру - та для AMP
        struktura_id_map = {}

        # перебираємо кожен вибраний рядок в SQL таблиці
        for row in rows_database:

            # Клонуємо рядок
            new_row = row.copy()

            # Змінюємо context на поточне значення мови
            new_row['context_key'] = lang

            # TODO: ID - Визначаємо новий id та записуємо в словник, Змінюємо id збільшуючи на +1
            new_row['id'] = start_id
            struktura_id_map[row['id']] = new_row['id']
            start_id += 1

            # TODO: BABEL baza _ADD в словник звязоних між собою ID
            babel_baza_dict.setdefault(row['id'], {row['context_key']: row['id']})
            babel_baza_dict[row['id']].setdefault(new_row['context_key'], new_row['id'])

            # TODO: PARENT - Визначаємо структуру
            if new_row['parent'] != 0:
                new_row['parent'] = struktura_id_map[new_row['parent']]
                # print(str(row['parent']) + " - " + str(new_row['parent'])  + " : " + str(row['menutitle']))

            # TODO: AMP -ID - Content налаштування
            if new_row['template'] == 7:
                for key, value in struktura_id_map.items():
                    if str(key) == row['content']:
                        new_row['content'] = value
                        # print(str(row['id']) + " - " + str(new_row['id'])  + " : " + str(new_row['content']))

            # TODO: Стандартні налаштування published-editedby-editedon-publishedon-publishedby
            for key, value in standart_nalashtuvannya.items():
                new_row[key] = value
                # {**new_row, **{key: value for key, value in standart_nalashtuvannya.items()}}

            # TODO: Дата публікації
            # randon секунди дати UNIX
            random_time = random.choice([15150, 18500, 21500, 23700, 36200, 40320, 43800, 65300, 99300, 145300])
            random_pub_date = random.choice([1550, 2100, 2450, 3620, 4020, 5800])

            new_create_date['createdon'] = new_create_date['createdon'] + random_time
            new_row['createdon'] = new_create_date['createdon']
            new_create_date['pub_date'] = new_create_date['pub_date'] + random_time + random_pub_date
            new_row['pub_date'] = new_create_date['pub_date']
            print(str(lang) + ' - ' + str(new_row['id']) + ': ' + str(datetime.datetime.fromtimestamp(new_row['pub_date'])))

            # TODO: TRANSLATE - Перекладаємо поля використовуючи DEEPL
            for name in translate_name:
                if len(new_row[name]) > 0:
                    # Замінюємо входження зі списку dont_translate на тег <keep>
                    for word in dont_translate:
                        new_row[name] = new_row[name].replace(word, f"<keep>{word}</keep>")
                    translate = translator.translate_text(new_row[name], tag_handling='xml', ignore_tags='keep', target_lang=lang)
                    new_row[name] = translate.text
                    new_row[name] = new_row[name].replace("<keep>", "").replace("</keep>", "")

            # TODO: ALIAS - транслітерація
            if len(new_row['menutitle']) > 0:
                new_row['alias'] = unidecode(new_row['menutitle'].lower())
            else:
                new_row['alias'] = unidecode(new_row['pagetitle'].lower())
            new_row['alias'] = re.sub(r'[^a-zA-Z0-9]+-*$' , '', re.sub(r'[^a-zA-Z0-9]+', '-', new_row['alias']))
            new_row['uri'] = str(new_row['alias'] + '/')
            if new_row['template'] == 7:
                new_row['alias'] = str(new_row['alias'] + '-amp')
                new_row['uri'] = str(new_row['alias'] + '-amp/')

            # TODO: SQL INSERT запись modx_site_content
            baza_key_new_row = ", ".join([f"`{key}`" for key in new_row.keys()])
            baza_value_new_row = tuple(new_row.values())
            baza_sql_dublikat = ", ".join([f"`{key}`=VALUES(`{key}`)" for key in new_row.keys()])

            with connect_database.cursor() as cursor:
                # Create a new record
                sql_resurs = f"INSERT INTO `modx_site_content` ({baza_key_new_row})\
                                VALUES {baza_value_new_row} \
                                ON DUPLICATE KEY UPDATE {baza_sql_dublikat}"
                cursor.execute(sql_resurs)
            connect_database.commit()



            # ################################################################################################
            # # TODO: modx_games_co
            # ################################################################################################
            # # Выбор всех строк таблицы modx_site_content, где context = 'web' id = 75
            # my_cursor.execute(f"SELECT * FROM modx_games_co WHERE `resource_id` = '{row['id']}'")
            # row_database_game = my_cursor.fetchone()

            # if row_database_game is not None:
            #     # resource_id
            #     row_database_game['resource_id'] = new_row['id']
            #     # id такий як і в ресурса
            #     row_database_game['id'] = new_row['id']

            #     # res_context_key - Контекст або мова
            #     row_database_game['res_context_key'] = lang

            #     # TRANSLATE - Перекладаємо поля без HTML використовуючи DEEPL
            #     translate_title_games_co = ['res_pagetitle','res_longtitle','b1_comments_h2','b1_video_json_h2',
            #                                 'b0_res_content','image_galer_h2','faq_block_h2','casino_geo']
            #     for name in translate_title_games_co:
            #         if len(row_database_game[name]) > 1:
            #             for word in dont_translate:
            #                 row_database_game[name] = row_database_game[name].replace(word, f"<keep>{word}</keep>")
            #             translate_title = translator.translate_text(row_database_game[name], tag_handling='xml', ignore_tags='keep', target_lang=lang)
            #             row_database_game[name] = translate_title.text
            #             row_database_game[name] = row_database_game[name].replace("<keep>", "").replace("</keep>", "")

            #     # TRANSLATE - Розбираємо та перекладаємо JSON поля DEEPL
            #     translate_baza_keys = {'b1_content_json': {'h2_title':'','description':'','alt_img':''},
            #                         'b1_demo_iframe': {'demo_h2':'','alt_img':''},
            #                         'b1_content_table_json': {'td_1':'','td_2':''},
            #                         'b1_comments_json': {'h3_name_comment':'','p_review_comment':'','person_name':''},
            #                         'b1_video_json': {'video_name':'','video_description':''},
            #                         'image_galer_json': {'description':''},
            #                         'faq_block_json': {'question_text':'','answer_text':''}
            #                         }
            #     for key, value in translate_baza_keys.items():
            #         if len(row_database_game[key]) > 0:  # перевіряємо чи не пусте JSON поле
            #             sql_json = json.loads(row_database_game[key])  # розпакуємо JSON
            #             for row_json in sql_json:
            #                 for key_baza in value.keys():
            #                     # Translate JSON if not NONE
            #                     if len(row_json[key_baza]) > 0:
            #                         # Замінюємо входження зі списку dont_translate на тег <keep>
            #                         for word in dont_translate:
            #                             row_json[key_baza] = row_json[key_baza].replace(word, f"<keep>{word}</keep>")
            #                         # DEEPL переклад
            #                         translate_json = translator.translate_text(row_json[key_baza], tag_handling='xml', ignore_tags='keep', target_lang=lang)
            #                         row_json[key_baza] = translate_json.text
            #                         row_json[key_baza] = row_json[key_baza].replace("<keep>", "").replace("</keep>", "")
            #                         # row_json[key_baza] = my_add_ekran_string(row_json[key_baza])

            #                 row_database_game[key] = json.dumps(sql_json)
            #                 #######################

            #     # SQL INSERT запись modx_games_co
            #     baza_key_games_co = ", ".join([f"`{key}`" for key in row_database_game.keys()])
            #     baza_value_games_co = tuple(row_database_game.values())
            #     baza_sql_dublikat_games_co = ", ".join([f"`{key}`=VALUES(`{key}`)" for key in row_database_game.keys()])

            #     with connect_database.cursor() as cursor:
            #         # Create a new record
            #         sql_resurs = f"INSERT INTO `modx_games_co` ({baza_key_games_co})\
            #                         VALUES {baza_value_games_co} \
            #                         ON DUPLICATE KEY UPDATE {baza_sql_dublikat_games_co}"
            #         cursor.execute(sql_resurs)
            #     connect_database.commit()



        ################################################################################################
        # TODO: CONTEXT настройка контекста - modx_context_setting
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
connect_database.close()
