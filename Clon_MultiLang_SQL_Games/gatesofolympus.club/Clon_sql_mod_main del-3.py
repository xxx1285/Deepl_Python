
# v.0.0.5
# 30.06.2023
# gatesofolympus
import os
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

# Translate + Clean
def translate_deepl_and_clean(translator, row, name, lang):
    translated = translator.translate_text(row[name], tag_handling='xml', ignore_tags='keep', target_lang=lang)
    cleaned_text = translated.text.replace("<keep>", "").replace("</keep>", "")
    cleaned_text = my_clean_ekran_string(cleaned_text).replace('"', '')
    return cleaned_text

# Translate + Dont-translate words
def translate_with_exceptions(name, dont_translate, translator, lang):
    # Замена слов, которые не должны переводиться, на версии с тегами <keep>
    for word in dont_translate:
        name = re.sub(f'(?i){re.escape(word)}', f"<keep>{word}</keep>", name)
    # Перевод строки с учетом исключений
    translate_title = translator.translate_text(name, tag_handling='xml', ignore_tags='keep', target_lang=lang)
    name = translate_title.text
    name = name.replace("<keep>", "").replace("</keep>", "")
    return name

# Функція для заміни посилань в тексті
# def replace_link(link_obgect):
#     # Витягуємо значення href (group(1) - перша група у регулярному виразі, в нашому випадку значення href)
#     full_match = link_obgect.group(0)
#     url = link_obgect.group(1)
#     if url in inv_struktura_id_alias_map:
#         id_ = inv_struktura_id_alias_map[url]
#         if id_ in struktura_id_map:
#             new_id = struktura_id_map[id_]
#             new_url = struktura_id_alias_map[new_id]
#             return full_match.replace(url, new_url)
#     # Якщо заміна не відбулась, повертаємо вихідний тег без змін
#     return full_match

# Функция для замены ссылок в тексте
def replace_link(link_object):
    # Извлекаем значение href (group(1) - первая группа в регулярном выражении, в нашем случае значение href)
    full_match = link_object.group(0)
    url = link_object.group(1)
    
    # Удаляем "-keep-" и "-keep" из URL
    url = url.replace("-keep-", "").replace("-keep", "")
    
    if url in inv_struktura_id_alias_map:
        id_ = inv_struktura_id_alias_map[url]
        if id_ in struktura_id_map:
            new_id = struktura_id_map[id_]
            new_url = struktura_id_alias_map[new_id]
            # Также необходимо убрать "-keep-" и "-keep" из new_url
            new_url = new_url.replace("-keep-", "").replace("-keep", "")
            return full_match.replace(url, new_url)
    # Если замена не произошла, возвращаем исходный тег без изменений, но уже с удалёнными "-keep-" и "-keep"
    return full_match.replace(link_object.group(1), url)


# Функція вибору випадкового слова (ключове слово регіону) з язиковими версіями GEO, та заміни в тексті
def replace_keys_with_random_values(text, lang, keys_in_geo):
    if lang in keys_in_geo:
        for key in keys_in_geo[lang]:
            text = re.sub(key, lambda _: random.choice(keys_in_geo[lang][key]), text, flags=re.IGNORECASE)
    return text

# перевірити, чи є об'єкт рядком, а потім використати len()
def get_length(obj):
    if isinstance(obj, str):
        return len(obj)
    elif isinstance(obj, int):
        return len(str(obj))
    else:
        return "Can't get length of this object type"


# SQL Зчитуємо параметри з конфігураційного файлу
current_folder = os.path.basename(os.path.dirname(__file__))
with open(f'Clon_MultiLang_SQL_Games\\{current_folder}\\configs\\config_sql_Deepl.json') as f:
    config = json.load(f)

# CSV файл куди зберігаємо результат
csv_url_file = f'Clon_MultiLang_SQL_Games\\{current_folder}\\csv\\zvit.csv'  # !!!!!! СТВОРИ ВРУЧНУ ФАЙЛ


# TODO:сайт для якого обробляємо - з слешем вкінці
my_site = "https://gatesofolympus.club/"
site_name = "Gates of Olympus slot"
author_name = "Garry Dranik"

# Контекст по замовчуванням (web == en) та з якого копіюємо
context_web = 'web'

# TODO:  Налаштування розділів WEB версії 
amp_templates = 7           # id шаблона AMP
amp_catalog = 14            # id каталога AMP
about_us = 488              # id about_us каталога
author_url_id = 487         # id автора
cazino_catalog_id = 6       # id розділу казіно
error_page = 2              # id 404 сторінки
site_start = 1              # id тартової першої-головної сторінки


# TODO: Контексти та мови для перекладу
# context_and_lang = ["uk"]
# context_and_lang = ["es","ru"]
context_and_lang = ["es","ru","tr","ro","pl","pt-br","fr","el","de","uk"]
# context_and_lang = ["es","ru","tr","ro","pl","pt-br","fr","el","de","uk","it","bg","fi","et",
#                     "lt","lv","da","nb","sv"]
# context_and_lang = ["ru","es","pl","pt-br","fr","id","el","de","tr","hu","uk","it","ro","bg","fi","et",
#                     "lt","lv","nl","cs","da","ja","nb","sk","sl","sv"]

# перебираємо префікси мов, щоб аліас не починався з 'ru', 'es', 'pl'....
all_prefix_for_alias = ["en","ru","es","pl","pt-br","pt","fr","id","el","de","tr","hu","uk","it","ro","bg","fi","et",
                        "lt","lv","nl","cs","da","ja","nb","sk","sl","sv","az","kk","ar","uz"]
# web,ru,es,pl,pt-br,fr,id,el,de,tr,hu,uk,it,ro,bg,fi,et,lt,lv,nl,cs,da,ja,nb,sk,sl,sv,az,kk,ar,uz

# TODO: Слова які не потрібно перекладати 'Aviator', 'The dog house', 'Gates of Olympus'
dont_translate = ['Gates of Olympus', 'Megaways', '1win', 'Pin-up', 'Pragmatic Play', '1xbet']

# TODO: Використовуй ключові слова з язиковими версіями GEO
keys_in_geo = {
    'ru':   {'Gates of Olympus':['Gates of Olympus','Олимпус']},
    'uk':   {'Gates of Olympus':['Gates of Olympus','Олимпус']},
    'pt-br':{'Gates of Olympus':['Gates of Olympus','Olympus gates']},
    'es':{'Gates of Olympus':['Gates of Olympus','Olympus gates']}    
}

# Словник звязаних між собою EN Контекста та інших Ресурсів
dict_id_clon_resouses = {}
# Словник контекстів та звязаних id  >>>> BABEL - modx_site_tmplvar_contentvalues
babel_baza_dict = {}

# Не змінювати - базове налаштування - стартовий ID
start_id = 0
# Context   >>>> modx_context_setting
cazino_catalog_id = 6

# Поля що потрібно перекласти
translate_name = ['pagetitle','longtitle','description','menutitle','introtext','content']
# Стандартні налаштувавання бази
standart_nalashtuvannya = {'published': 0,'editedby': 0,'editedon': 0,'publishedon': 0,'publishedby': 0}
# дата UNIX на даний час для 'createdon': int(time.time()),'pub_date': int(time.time())
# Або визначити самостійно - наприклад через місяць після запуску сайта
new_create_date = {'createdon': int(time.time()),'pub_date': int(time.time())}

"""
############################################
    >>>>    modx_context_setting
#############################################
"""

locale_alternate = {'bg': '[[$bg_BG]]', 'cs': '[[$cs_CZ]]', 'da': '[[$da_DK]]', 'de': '[[$de_DE]]', 'el': '[[$el_GR]]',
                    'en': '[[$en_US]]', 'es': '[[$es_ES]]', 'et': '[[$et_EE]]', 'fi': '[[$fi_FI]]', 'fr': '[[$fr_FR]]',
                    'hu': '[[$hu_HU]]', 'id': '[[$id_ID]]', 'it': '[[$it_IT]]', 'ja': '[[$ja_JP]]', 'lt': '[[$lt_LT]]',
                    'lv': '[[$lv_LV]]', 'nb': '[[$nb_NO]]', 'nl': '[[$nl_NL]]', 'pl': '[[$pl_PL]]', 'pt-br': '[[$pt_BR]]',
                    'ro': '[[$ro_RO]]', 'ru': '[[$ru_RU]]', 'sk': '[[$sk_SK]]', 'sl': '[[$sl_SL]]', 'sv': '[[$sv_SE]]',
                    'tr': '[[$tr_TR]]', 'uk': '[[$uk_UA]]',
                    'ar': '[[$ar_EG]]', 'az': '[[$az_AZ]]', 'kk': '[[$kk_KZ]]', 'uz': '[[$uz_UZ]]'
               }


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
    # TODO: для теста використовуй  WHERE `id` IN (1,2)     АБО     WHERE `context_key` = '{context_web}'
    my_cursor.execute(f"SELECT * FROM modx_site_content WHERE `context_key` = '{context_web}' \
                        AND (`id` = 75 OR `template` IN (6,7,24,26,27))")
    rows_database = my_cursor.fetchall()

    # Мах id в таблиці для правильного визначення наступного значення в SQL таблиці
    # my_cursor.execute("SELECT MAX(`id`) as max_id FROM modx_site_content")
    # result = my_cursor.fetchone()
    # max_id = result['max_id']
    max_id = 491


    # CSV створюємо файл для запису
    csv_id = 0
    with open(csv_url_file, 'w', newline='', encoding='utf-8') as file:
        field_names = ['csv_id', 'id', 'lang', 'menutitle', 'pubdate', 'pubdatetime', 'url']
        csv_writer = csv.DictWriter(file, fieldnames=field_names)
        csv_writer.writeheader()

        # перебираємо контексти (язики) - lang
        # try:
        for lang in context_and_lang:

            # ################################################################################################
            # ################################################################################################
            # # TODO: modx_site_content
            # ################################################################################################
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

                new_row['id'] = start_id    # новий id елемента
                struktura_id_map[row['id']] = new_row['id']  # структура вкладень 

                # BABEL baza _ADD в словник звязоних між собою ID (web:5;ru:120)
                babel_baza_dict.setdefault(row['id'], {row['context_key']: row['id']})          # базовые значения для row
                babel_baza_dict[row['id']].setdefault(new_row['context_key'], new_row['id'])    # добавляем по ключю new_row

                # PARENT - Визначаємо структуру
                if new_row['parent'] != 0:  # 0 - это нет вложености по SQL таблице
                    new_row['parent'] = struktura_id_map[new_row['parent']] # берем значение parant з структури по new_row['id']
                    # print(str(row['parent']) + " - " + str(new_row['parent'])  + " : " + str(row['menutitle']))

                # AMP -ID - Content налаштування
                if new_row['template'] == amp_templates:
                    for key, value in struktura_id_map.items():
                        if str(key) == row['content']:
                            new_row['content'] = value


                # Стандартні налаштування published-editedby-editedon-publishedon-publishedby
                for key, value in standart_nalashtuvannya.items():
                    new_row[key] = value
                    # {**new_row, **{key: value for key, value in standart_nalashtuvannya.items()}}
                

                # TODO: pub_date - Дата публікації
                # randon секунди дати UNIX ( 6 годин - це 21000)
                random_time = random.choice([29850, 33370, 46370, 55700, 38200, 68320])
                random_pub_date = random.choice([1350, 2450])

                new_create_date['createdon'] = new_create_date['createdon'] + random_time
                new_row['createdon'] = new_create_date['createdon']
                new_create_date['pub_date'] = new_create_date['pub_date'] + random_time + random_pub_date
                new_row['pub_date'] = new_create_date['pub_date']
                print(str(lang) + ' - ' + str(new_row['id']) + ': ' + str(datetime.datetime.fromtimestamp(new_row['pub_date'])))

                # TRANSLATE - Перекладаємо поля використовуючи DEEPL
                for name in translate_name:
                    if get_length(new_row[name]) > 0:
                        # Замінюємо входження зі списку dont_translate на тег <keep>
                        for word in dont_translate:
                            # без врахування регістру
                            # re.sub(pattern, repl, string) - функция, которая ищет шаблон pattern в строке string и заменяет его на repl.
                            # f'(?i){re.escape(word)}' - (?i) означает, что поиск будет игнорировать регистр (будет искать word 
                            # независимо от того, написано ли оно заглавными или строчными буквами). 
                            # Функция re.escape(word) используется для экранирования всех специальных символов в word.
                            if isinstance(new_row[name], str):
                                new_row[name] = re.sub(f'(?i){re.escape(word)}', f"<keep>{word}</keep>", new_row[name])

                        
                        ##########################################################################################################
                        #   TRANSLATE and CLEAN
                        ##########################################################################################################
                        # if isinstance(new_row[name], str):  # Переконайтесь, що new_row[name] є рядком перед перекладом
                        #     new_row[name] = translate_deepl_and_clean(translator, new_row, name, lang)

                ###################################################################################################################
                # ALIAS - транслітерація
                # для новых убрать .html
                if get_length(new_row['menutitle']) > 0:
                    new_row['alias'] = unidecode(new_row['menutitle'].lower())
                else:
                    new_row['alias'] = unidecode(new_row['pagetitle'].lower())
                new_row['alias'] = re.sub(r'[^a-zA-Z0-9]+-*$' , '', re.sub(r'[^a-zA-Z0-9]+', '-', new_row['alias']))
                # перебираємо префікси мов, щоб аліас не починався з 'ru', 'es', 'pl'....
                if any(new_row['alias'].startswith(prefix) for prefix in all_prefix_for_alias):
                    new_row['alias'] = 'win_' + new_row['alias']
                # ******************************************************************
                # TODO: для новых сайтов убираем - оставляем только + '/'
                new_row['uri'] = str(new_row['alias'] + '/')
                # if new_row['isfolder'] == 1:
                #     new_row['uri'] = str(new_row['alias'] + '/')
                # else:
                #     new_row['uri'] = str(new_row['alias'] + '.html')
                # *****************************************************************
                if new_row['template'] == amp_templates:
                    new_row['alias'] = 'amp-' + str(new_row['alias'])
                    new_row['uri'] = 'amp/amp-' + str(new_row['uri'])
                if row['id'] == amp_catalog:
                    new_row['alias'] = 'amp'
                    new_row['uri'] = 'amp/'

                ############################################################################
                #  Структура id:alias для внутрішньої перелінковки
                #  находим минимальный ключ в словаре
                min_key = min(struktura_id_map.keys())
                if row['id'] == min_key:
                    struktura_id_alias_map[new_row['id']] = my_site + lang + '/'
                    #  Записываем значение только если такого ключа еще нет
                    if row['id'] not in struktura_id_alias_map:
                        struktura_id_alias_map[row['id']] = my_site
                else:
                    struktura_id_alias_map[new_row['id']] = my_site + lang + '/'+ new_row['uri']
                    #  Записываем значение только если такого ключа еще нет
                    if row['id'] not in struktura_id_alias_map:
                        struktura_id_alias_map[row['id']] = my_site + row['uri']

                ##############################################################################
                # SQL INSERT запись modx_site_content
                # baza_key_new_row = ", ".join([f"`{key}`" for key in new_row.keys()])
                # baza_value_new_row = tuple(new_row.values())
                # baza_sql_dublikat = ", ".join([f"`{key}`=VALUES(`{key}`)" for key in new_row.keys()])
                # with connect_database.cursor() as cursor:
                #     # Create a new record
                #     sql_resurs = f"INSERT INTO `modx_site_content` ({baza_key_new_row})\
                #                     VALUES ({', '.join(['%s'] * len(baza_value_new_row))}) \
                #                     ON DUPLICATE KEY UPDATE {baza_sql_dublikat}"
                #     cursor.execute(sql_resurs, baza_value_new_row)
                # connect_database.commit()

                # # CSV
                # if new_row['id'] == struktura_id_map[1]:  # URI
                #     css_uri = str(lang) + '/'
                # else:
                #     css_uri = str(lang) + '/' + new_row['uri']
                # if get_length(new_row['menutitle']) > 4:  # Menutitle or Pagetitle
                #     css_name = new_row['menutitle']
                # else:
                #     css_name = new_row['pagetitle']

                # csv_writer.writerow({'csv_id': csv_id,
                #                     'lang': lang,
                #                     'id': new_row['id'],
                #                     'menutitle': css_name,
                #                     'pubdate': new_row['pub_date'],
                #                     'pubdatetime': str(datetime.datetime.fromtimestamp(new_row['pub_date'])),
                #                     'url': my_site + css_uri,
                #                     })
                # csv_id += 1


            ################################################################################################
            ################################################################################################
            # TODO: modx_games_co
            ################################################################################################
            ################################################################################################

            # Створюємо інвертований словник для знаходження id за url (внутрішня перелінковка)
            inv_struktura_id_alias_map = {v: k for k, v in struktura_id_alias_map.items()}

            for key_row, key_new_row in struktura_id_map.items():  # перебираем структуру ресурсов row and new_row

                # Выбор всех строк таблицы modx_games_co
                my_cursor.execute(f"SELECT * FROM modx_games_co WHERE `resource_id` = '{key_new_row}'")
                row_database_game = my_cursor.fetchone()

                if row_database_game is not None:

                    # ##############################################################################################
                    # TRANSLATE - Перекладаємо поля без HTML використовуючи DEEPL
                    translate_title_games_co = ['res_pagetitle','res_longtitle','b1_comments_h2','b1_video_json_h2',
                                                'b0_res_content','image_galer_h2','faq_block_h2','b2_instruction_how_to_h2']
                    for name_title in translate_title_games_co:
                        # if get_length(row_database_game[name_title]) > 1:
                        #     for word in dont_translate:
                        #         # row_database_game[name_title] = row_database_game[name_title].replace(word, f"<keep>{word}</keep>")
                        #         row_database_game[name_title] = re.sub(f'(?i){re.escape(word)}', f"<keep>{word}</keep>", row_database_game[name_title])
                            ##########################################################################################################
                            #   TRANSLATE and CLEAN
                            ##########################################################################################################
                            # row_database_game[name_title] = translate_deepl_and_clean(translator, row_database_game, name_title, lang)
                            # #   СЕО замена ключевого слова если есть популярное в GEO
                            # row_database_game[name_title] = replace_keys_with_random_values(row_database_game[name_title], lang, keys_in_geo)

                        # ############################################################################################
                        # Перелінковка - Пошук посилань - (перелінковка кожної сторінки контексту)
                        if name_title == 'b0_res_content':
                            # Змінюємо посилання в тексті використовуючи функцію replace_link та регулярний вираз
                            row_database_game[name_title] = re.sub(r'href="?([^"\s]+)"?', replace_link, row_database_game[name_title])
                            # Теперь удалим все атрибуты кроме href, target и title
                            row_database_game[name_title] = re.sub(r'<a\s+([^>]+)>', lambda match: "<a " + " ".join([f for f in match.group(1).split() if f.startswith(("href=", "target=", "title=", "id="))]) + ">", row_database_game[name_title])

                    # TRANSLATE - Розбираємо та перекладаємо JSON поля DEEPL
                    translate_baza_keys = {'b1_content_json': {'h2_title':'','description':'','alt_img':''},
                                        'b1_demo_iframe': {'demo_h2':'','alt_img':''},
                                        'b1_content_table_json': {'td_1':'','td_2':''},
                                        'b1_comments_json': {'h3_name_comment':'','p_review_comment':''},
                                        'b1_video_json': {'video_name':'','video_description':''},
                                        'image_galer_json': {'description':''},
                                        'faq_block_json': {'question_text':'','answer_text':''},
                                        'b2_instruction_how_to_json': {'h3_insruction':'','text':''}
                                        }

                    for key, value in translate_baza_keys.items():
                        if row_database_game[key] is not None and len(row_database_game[key]) > 0:  # перевіряємо чи не пусте JSON поле
                            sql_json = json.loads(row_database_game[key])  # розпакуємо JSON
                            for row_json in sql_json:
                                for key_baza in value.keys():
                                    # Translate JSON if not NONE
                                    if get_length(row_json[key_baza]) > 0:
                                        # Замінюємо входження зі списку dont_translate на тег <keep>
                                        # for word in dont_translate:
                                        #     row_json[key_baza] = re.sub(f'(?i){re.escape(word)}', f"<keep>{word}</keep>", row_json[key_baza])
                                        ##########################################################################################################
                                        #   TRANSLATE and CLEAN
                                        ##########################################################################################################
                                        # row_json[key_baza] = translate_deepl_and_clean(translator, row_json, key_baza, lang)
                                        # #   СЕО замена ключевого слова если есть популярное в GEO
                                        # row_json[key_baza] = replace_keys_with_random_values(row_json[key_baza], lang, keys_in_geo)

                                        
                                        # ###############################################################################################
                                        # Перелінковка Змінюємо посилання в тексті використовуючи функцію replace_link та регулярний вираз
                                        row_json[key_baza] = re.sub(r'href="?([^"\s]+)"?', replace_link, row_json[key_baza])
                                        # Теперь удалим все атрибуты кроме href, target и title
                                        row_json[key_baza] = re.sub(r'<a\s+([^>]+)>', lambda match: "<a " + " ".join([f for f in match.group(1).split() if f.startswith(("href=", "target=", "title=", "id="))]) + ">", row_json[key_baza])


                                row_database_game[key] = json.dumps(sql_json)
                                #######################
                        # elif row_database_game[key] is None:
                        #     row_database_game[key] = 'NULL'

                        # # !!! TODO: 29-06-2023 Проверь - текстовый NULL не подходит
                        # if  len(row_database_game['b1_demo_iframe']) > 5:
                        #     row_database_game['b1_demo_iframe'] = ''

                    # SQL INSERT запись modx_games_co
                    def create_update_expression(keys, values):
                        return ", ".join([f"`{key}`=IFNULL(VALUES(`{key}`), '')" if value is None else f"`{key}`=VALUES(`{key}`)" for key, value in zip(keys, values)])

                    baza_key_games_co = [f"`{key}`" for key in row_database_game.keys()]
                    baza_value_games_co = tuple(row_database_game.values())
                    baza_sql_dublikat_games_co = create_update_expression(row_database_game.keys(), baza_value_games_co)

                    with connect_database.cursor() as cursor:
                        # Create a new record
                        sql_resurs = f"INSERT INTO `modx_games_co` ({', '.join(baza_key_games_co)})\
                                        VALUES ({', '.join(['%s'] * len(baza_value_games_co))}) \
                                        ON DUPLICATE KEY UPDATE {baza_sql_dublikat_games_co}"
                        cursor.execute(sql_resurs, baza_value_games_co)
                    connect_database.commit()

                    print("modx_games_co - " + str(row_database_game['res_context_key']) + ": " + str(row_database_game['resource_id']))

    #         # ################################################################################################
    #         # # TODO: CONTEXT настройка контекста - modx_context_setting
    #         # ################################################################################################

    #         language_dict = {"en": "English", "ru": "Русский", "es": "Español", "pl": "Polski", "pt-br": "Português (Brasil)", 
    #                         "pt": "Português", "fr": "Français", "id": "Bahasa Indonesia", "el": "Ελληνικά", "de": "Deutsch", 
    #                         "tr": "Türkçe", "hu": "Magyar", "uk": "Українська", "it": "Italiano", "ro": "Română", "bg": "Български", 
    #                         "fi": "Suomi", "et": "Eesti", "lt": "Lietuvių", "lv": "Latviešu", "nl": "Nederlands", "cs": "Čeština", 
    #                         "da": "Dansk", "ja": "日本語", "nb": "Norsk Bokmål", "sk": "Slovenčina", "sl": "Slovenščina", "sv": "Svenska", 
    #                         "az": "Azərbaycan", "kk": "Қазақ", "ar": "العربية", "uz": "O'zbek"
    #                         }

    #         # достаємо з бази modx_context_setting (контекст web) настройку 'amp_fullvers' для перекладу
    #         my_cursor.execute(f"SELECT * FROM modx_context_setting WHERE `context_key` = '{context_web}' AND `key` = 'amp_fullvers'")
    #         rows_context_amp_fullvers = my_cursor.fetchone()
    #         amp_fullvers = rows_context_amp_fullvers['value']
    #         # переклад amp_fullvers
    #         amp_fullvers = translate_with_exceptions(amp_fullvers, dont_translate, translator, lang)

    #         # достаємо з бази modx_context_setting (контекст web) настройку 'footer_allrights' для перекладу
    #         my_cursor.execute(f"SELECT * FROM modx_context_setting WHERE `context_key` = '{context_web}' AND `key` = 'footer_allrights'")
    #         rows_context_footer_allrights = my_cursor.fetchone()
    #         footer_allrights = rows_context_footer_allrights['value']
    #         # переклад footer_allrights
    #         footer_allrights = translate_with_exceptions(footer_allrights, dont_translate, translator, lang)

    #         # достаємо з бази cookies (контекст web) настройку 'cookies' для перекладу
    #         my_cursor.execute(f"SELECT * FROM modx_context_setting WHERE `context_key` = '{context_web}' AND `key` = 'cookies'")
    #         rows_context_cookies = my_cursor.fetchone()
    #         cookies = rows_context_cookies['value']
    #         # переклад cookies
    #         cookies = translate_with_exceptions(cookies, dont_translate, translator, lang)

    #         # CONTEXT настройка
    #         keys_context_setting = {'about_us':             struktura_id_map[about_us],
    #                                 'amp_fullvers':         amp_fullvers,
    #                                 'amp_parent':           struktura_id_map[amp_catalog],
    #                                 'author_name':          author_name,
    #                                 'author_url_id':        struktura_id_map[author_url_id],
    #                                 'base_url':             f'/{lang}/',
    #                                 'cazino_catalog_id':    struktura_id_map[cazino_catalog_id],
    #                                 'chan_locale':          locale_alternate[lang],
    #                                 'cookies':              cookies,
    #                                 'cultureKey':           lang,
    #                                 'error_page':           struktura_id_map[error_page],
    #                                 'footer_allrights':     footer_allrights,
    #                                 'lang_name':            language_dict[lang],
    #                                 'locale':               locale_alternate[lang].replace("[[$", "").replace("]]", ""),
    #                                 'site_name':            site_name,
    #                                 'site_start':           struktura_id_map[site_start],
    #                                 'site_url':             f'{my_site}{lang}/'
    #                                 }

    #         for key, value in keys_context_setting.items():
    #             # SQL INSERT запись modx_context_setting
    #             with connect_database.cursor() as cursor_set:
    #                 sql_babel = "INSERT INTO `modx_context_setting` (`context_key`, `key`, `value`, `xtype`, `namespace`, `area`) \
    #                             VALUES (%s, %s, %s, %s, %s, %s) \
    #                             ON DUPLICATE KEY UPDATE value=VALUES(value), xtype=VALUES(xtype), namespace=VALUES(namespace), area=VALUES(area)"
    #                 val = (lang, key, value, 'textfield', 'core', 'language')
    #                 cursor_set.execute(sql_babel, val)
    #             connect_database.commit()

    #     # except Exception as ex:
    #     #     print("Connection refused...")
    #     #     print(ex)
            

    # # ################################################################################################
    # # # TODO: Babel - INSERT SQL - modx_site_tmplvar_contentvalues
    # # ################################################################################################

    # # # Додамо вручну РУ - якщо існує
    # # ru_versiya = {1: {'ru': 104}, 3: {'ru': 107}, 4: {'ru': 109}, 5: {'ru': 120}, 6: {'ru': 111}, 30: {'ru': 113},
    # #               21: {'ru': 112}, 14: {'ru': 106}, 14: {'ru': 106}, 53: {'ru': 108}, 14: {'ru': 106}, 83: {'ru': 121}, 70: {'ru': 110}}

    # # ru_versiya_keys = ru_versiya.keys()

    # # for key in ru_versiya_keys:
    # #     if key in babel_baza_dict:
    # #         babel_baza_dict[key].update(ru_versiya[key])
    # #     else:
    # #         babel_baza_dict[key] = ru_versiya[key]
    # # ##################################################################################################

    # for babel_row in babel_baza_dict.values():
    #     # перебираэмо словник контекстів та звязаних id
    #     result_value_str = ";".join([f"{key}:{value}" for key, value in babel_row.items()])
    #     for contentid in babel_row.values():
    #         # print(str(contentid) + " - " + result_str)
    #         with connect_database.cursor() as cursor_bab:
    #             sql_babel = "INSERT INTO `modx_site_tmplvar_contentvalues` (tmplvarid, contentid, value) VALUES (%s, %s, %s) \
    #                          ON DUPLICATE KEY UPDATE value = VALUES (value)"
    #             val = (1, contentid, result_value_str)
    #             cursor_bab.execute(sql_babel, val)
    #         connect_database.commit()

# except Exception as ex:
#     print("Connection refused...")
#     print(ex)
# finally:
#     connect_database.close()
#     print("ALL GOOD - Connection CLOSE")

#####################################################################
print("ALL GOOD - Connection CLOSE")
connect_database.close()
