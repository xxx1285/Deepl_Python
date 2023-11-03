
# v.0.0.8
# 03.07.2023, 31.10.2023
# gatesofolympus
import os
import time
import random
import re
import json
import pymysql
from unidecode import unidecode
import datetime
import deepl
import csv
import os


# функція що видаляє екранування та символи - JSON
def my_clean_ekran_string(string):
    string = string.replace('\n', '')
    string = string.replace('\t', '')
    string = string.replace('&nbsp;', '')
    return string

# BABEL Функция для добавления данных в существующий JSON-файл
def add_to_json(babel_file_path, new_data):
    try:
        with open(babel_file_path, 'r', encoding='utf-8') as file:
            current_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):  # Если файл не существует или пуст
        current_data = {}

    for key, value in new_data.items():
        if key in current_data:
            current_data[key].update(value)  # Объединяем словари на втором уровне
        else:
            current_data[key] = value
    with open(babel_file_path, 'w', encoding='utf-8') as file:
        json.dump(current_data, file, ensure_ascii=False, indent=4)


def translate_deepl_keep_and_clean(translator, row, name, lang, dont_translate):
    if isinstance(row[name], str):
        for word in dont_translate:
            # без врахування регістру
            # re.sub(pattern, repl, string) - функция, которая ищет шаблон pattern в строке string и заменяет его на repl.
            # f'(?i){re.escape(word)}' - (?i) означает, что поиск будет игнорировать регистр (будет искать word 
            # независимо от того, написано ли оно заглавными или строчными буквами). 
            # Функция re.escape(word) используется для экранирования всех специальных символов в word.
            row[name] = re.sub(f'(?i){re.escape(word)}', f"<keep>{word}</keep>", row[name])

        translated = translator.translate_text(row[name], tag_handling='xml', ignore_tags='keep', target_lang=lang)
        cleaned_text = translated.text
        cleaned_text = cleaned_text.replace("<keep>", "").replace("</keep>", "")
        cleaned_text = my_clean_ekran_string(cleaned_text)
        return cleaned_text


# Translate + Dont-translate words
def translate_with_exceptions(name, dont_translate, translator, lang):
   # Проверка, что текст не пустой и не состоит только из пробелов
    if not name or name.strip() == '':
        return name
    
    # Замена слов, которые не должны переводиться, на версии с тегами <keep>
    for word in dont_translate:
        name = re.sub(f'(?i){re.escape(word)}', f"<keep>{word}</keep>", name)
    # Перевод строки с учетом исключений
    translate_title = translator.translate_text(name, tag_handling='xml', ignore_tags='keep', target_lang=lang)
    name = translate_title.text
    name = name.replace("<keep>", "").replace("</keep>", "")
    return name

# Функція для заміни посилань в тексті
def replace_link(link_obgect):
    # Витягуємо значення href (group(1) - перша група у регулярному виразі, в нашому випадку значення href)
    full_match = link_obgect.group(0)
    url = link_obgect.group(1)
    if url in inv_struktura_id_alias_map:
        id_ = inv_struktura_id_alias_map[url]
        if id_ in struktura_id_map:
            new_id = struktura_id_map[id_]
            new_url = struktura_id_alias_map[new_id]
            return full_match.replace(url, new_url)
    # Якщо заміна не відбулась, повертаємо вихідний тег без змін
    return full_match

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


current_folder = os.path.basename(os.path.dirname(__file__))

# BABEL JSON path
babel_file_path = f'Clon_MultiLang_SQL_Games\\{current_folder}\\Babel_svyazi_all_lang\\babel_baza_dict.json'
# SQL Config path
sql_config = f'Clon_MultiLang_SQL_Games\\{current_folder}\\configs\\config_sql.json'
# DEEPL Config path
# TODO: при смене версий меняй IP
deepl_config = f'Clon_MultiLang_SQL_Games\\{current_folder}\\configs\\config_Deepl_1_zvdt18.json'
# deepl_config = f'Clon_MultiLang_SQL_Games\\{current_folder}\\configs\\config_Deepl_2_00018ds.json'

# SQL Config REED
with open(sql_config, 'r') as f:
    configSQL = json.load(f)

# DEEPL Config REED
with open(deepl_config, 'r') as f:
    configDEEPL = json.load(f)

# CSV файл куди зберігаємо результат
csv_url_file = f'Clon_MultiLang_SQL_Games\\{current_folder}\\csv\\zvit.csv'  # !!!!!! СТВОРИ ВРУЧНУ ФАЙЛ


# SETTINGS - з слешем вкінці
MY_SITE = "https://gatesofolympus.club/"
site_name = "Gates of Olympus"
author_name = "Garry Dranik"
author_role = "author - chief editor"
# Контекст по замовчуванням (web == en) та з якого копіюємо
CONTEXT_WEB = 'web'
# Налаштування розділів WEB версії 
about_us = 488              # id ABOUT_US каталога
author_url_id = 487         # id автора
cazino_catalog_id = 6       # id розділу казіно
error_page = 2              # id 404 сторінки
site_start = 1              # id тартової першої-головної сторінки


# Контексти та мови для перекладу
# context_and_lang = ["uk"]
context_and_lang = ["de","fr","it","pt-br","ro","lt","lv","ru"]
# context_and_lang = ["es","ru","tr","ro","pl","pt-br","fr","el","de","uk","it","bg","fi","et",
#                     "lt","lv","da","nb","sv"]
# context_and_lang = ["ru","es","pl","pt-br","fr","id","el","de","tr","hu","uk","it","ro","bg","fi","et",
#                     "lt","lv","nl","cs","da","ja","nb","sk","sl","sv"]

# перебираємо префікси мов, щоб аліас не починався з 'ru', 'es', 'pl'....
all_prefix_for_alias = ["en","ru","es","pl","pt-br","pt","fr","id","el","de","tr","hu","uk","it","ro","bg","fi","et",
                        "lt","lv","nl","cs","da","ja","nb","sk","sl","sv","az","kk","ar","uz"]
# web,ru,es,pl,pt-br,fr,id,el,de,tr,hu,uk,it,ro,bg,fi,et,lt,lv,nl,cs,da,ja,nb,sk,sl,sv,az,kk,ar,uz

#  Слова які не потрібно перекладати 'Aviator', 'The dog house', 'Gates of Olympus'
dont_translate = ['Gates of Olympus', 'Megaways', '1win', 'Pin-up', 'Pin up', 'Pragmatic Play', '1xbet', 'Vavada', '1xSlots',
                  'Dunder', 'Casumo', 'Bwin', 'Eurobet', 'FairSpin', 'Vulkan Vegas', 'FastPay', 'Betano', 'Betplay',
                  '4rabet', 'AllRight', 'Betway', 'LeoVegas', 'Mansion', 'Mostbet', 'Mr Green', 'Red Dog']

#  Використовуй ключові слова з язиковими версіями GEO
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
connect_database = pymysql.connect(**configSQL['config_database'],
                                    port=3306,
                                    cursorclass=pymysql.cursors.DictCursor
                                    )
print("\n*************************************\
        \n--> Succesfully connect - " + configSQL['config_database']['database'])

# Ініціалізуємо Deepl API key
translator = deepl.Translator(configDEEPL['config_deepl']['deepl_api_key'])
print("--> Deepl API - OK \n*************************************")


with connect_database.cursor() as my_cursor:
    # Выбор всех строк таблицы modx_site_content, где context = 'web' id = 75
    # TODO: для теста використовуй  WHERE `id` IN (1,2)     АБО     WHERE `context_key` = '{CONTEXT_WEB}'
    my_cursor.execute(f"SELECT * FROM modx_site_content WHERE `context_key` = '{CONTEXT_WEB}' \
                      AND `class_key` = 'modDocument' \
                      AND (`id` = 75 OR `template` IN (6,24,26,27))")
    rows_database = my_cursor.fetchall()

    # Максимальне значення ID в таблиці для правильного визначення наступного значення в SQL таблиці
    my_cursor.execute("SELECT MAX(`id`) as max_id FROM modx_site_content")
    result = my_cursor.fetchone()
    max_id = result['max_id']


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

            # перебираємо кожен вибраний рядок в SQL таблиці - Кожен РЕСУРС
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

                # BABEL baza _ADD в словник звязоних між собою ID (web:5;ru:120) - І в Окремий файл
                babel_baza_dict.setdefault(row['id'], {row['context_key']: row['id']})          # базовые значения для row
                babel_baza_dict[row['id']].setdefault(new_row['context_key'], new_row['id'])    # добавляем по ключю new_row
                # Используйте функцию для сохранения данных в файл
                add_to_json(babel_file_path, babel_baza_dict)

                # PARENT - Визначаємо структуру
                if new_row['parent'] != 0:  # 0 - это нет вложености по SQL таблице
                    try:
                        # берем значение parant з структури по new_row['id']
                        new_row['parent'] = struktura_id_map[new_row['parent']]
                    except KeyError:
                        pass  # или обработать ошибку каким-либо другим способом


                # Стандартні налаштування published-editedby-editedon-publishedon-publishedby
                for key, value in standart_nalashtuvannya.items():
                    new_row[key] = value
                    # {**new_row, **{key: value for key, value in standart_nalashtuvannya.items()}}
                

                # TODO: pub_date - Дата публікації
                # randon секунди дати UNIX ( 6 годин - це 21000)
                random_time = random.choice([9000, 15300, 29850, 33370, 46370, 55700, 38200, 68320])
                random_pub_date = random.choice([1350, 2450])

                new_create_date['createdon'] = new_create_date['createdon'] + random_time
                new_row['createdon'] = new_create_date['createdon']
                new_create_date['pub_date'] = new_create_date['pub_date'] + random_time + random_pub_date
                new_row['pub_date'] = new_create_date['pub_date']
                print(str(lang) + ' - ' + str(new_row['id']) + ': ' + str(datetime.datetime.fromtimestamp(new_row['pub_date'])))

                # TRANSLATE - Перекладаємо поля використовуючи DEEPL
                for name in translate_name:
                    if get_length(new_row[name]) > 0:
                        if isinstance(new_row[name], str):  # Переконайтесь, що new_row[name] є рядком перед перекладом
                            new_row[name] = translate_deepl_keep_and_clean(translator, new_row, name, lang, dont_translate)


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

                ############################################################################
                #  Структура id:alias для внутрішньої перелінковки
                #  находим минимальный ключ в словаре
                min_key = min(struktura_id_map.keys())
                if row['id'] == min_key:
                    struktura_id_alias_map[new_row['id']] = MY_SITE + lang + '/'
                    #  Записываем значение только если такого ключа еще нет
                    if row['id'] not in struktura_id_alias_map:
                        struktura_id_alias_map[row['id']] = MY_SITE
                else:
                    struktura_id_alias_map[new_row['id']] = MY_SITE + lang + '/'+ new_row['uri']
                    #  Записываем значение только если такого ключа еще нет
                    if row['id'] not in struktura_id_alias_map:
                        struktura_id_alias_map[row['id']] = MY_SITE + row['uri']


                ##############################################################################
                # SQL INSERT запись modx_site_content
                baza_key_new_row = ", ".join([f"`{key}`" for key in new_row.keys()])
                baza_value_new_row = tuple(new_row.values())
                baza_sql_dublikat = ", ".join([f"`{key}`=VALUES(`{key}`)" for key in new_row.keys()])
                with connect_database.cursor() as cursor:
                    # Create a new record
                    sql_resurs = f"INSERT INTO `modx_site_content` ({baza_key_new_row})\
                                    VALUES ({', '.join(['%s'] * len(baza_value_new_row))}) \
                                    ON DUPLICATE KEY UPDATE {baza_sql_dublikat}"
                    cursor.execute(sql_resurs, baza_value_new_row)
                connect_database.commit()

                # CSV
                if new_row['id'] == struktura_id_map[1]:  # URI
                    css_uri = str(lang) + '/'
                else:
                    css_uri = str(lang) + '/' + new_row['uri']
                if get_length(new_row['menutitle']) > 4:  # Menutitle or Pagetitle
                    css_name = new_row['menutitle']
                else:
                    css_name = new_row['pagetitle']

                csv_writer.writerow({'csv_id': csv_id,
                                    'lang': lang,
                                    'id': new_row['id'],
                                    'menutitle': css_name,
                                    'pubdate': new_row['pub_date'],
                                    'pubdatetime': str(datetime.datetime.fromtimestamp(new_row['pub_date'])),
                                    'url': MY_SITE + css_uri,
                                    })
                csv_id += 1


            ################################################################################################
            ################################################################################################
            # modx_games_co
            ################################################################################################
            ################################################################################################

            # Створюємо інвертований словник для знаходження id за url (внутрішня перелінковка)
            inv_struktura_id_alias_map = {v: k for k, v in struktura_id_alias_map.items()}

            for key_row, key_new_row in struktura_id_map.items():  # перебираем структуру ресурсов row and new_row

                # Выбор всех строк таблицы modx_games_co
                my_cursor.execute(f"SELECT * FROM modx_games_co WHERE `resource_id` = '{key_row}'")
                row_database_game = my_cursor.fetchone()

                if row_database_game is not None:
                    # resource_id
                    row_database_game['resource_id'] = key_new_row
                    # id такий як і в ресурса
                    row_database_game['id'] = key_new_row

                    # res_context_key - Контекст або мова
                    row_database_game['res_context_key'] = lang

                    # ##############################################################################################
                    # TRANSLATE - Перекладаємо поля без HTML використовуючи DEEPL
                    translate_title_games_co = ['res_pagetitle','res_longtitle','b1_comments_h2','b1_video_json_h2',
                                                'b0_res_content','image_galer_h2','faq_block_h2','b2_instruction_how_to_h2']
                    for name_title in translate_title_games_co:
                        if get_length(row_database_game[name_title]) > 1:
                            if isinstance(row_database_game[name_title], str):  # Переконайтесь, що row_database_game[name_title] є рядком перед перекладом
                                row_database_game[name_title] = translate_deepl_keep_and_clean(translator, row_database_game, name_title, lang, dont_translate)
                                #   СЕО замена ключевого слова если есть популярное в GEO
                                row_database_game[name_title] = replace_keys_with_random_values(row_database_game[name_title], lang, keys_in_geo)

                        # ############################################################################################
                        # Перелінковка - Пошук посилань - (перелінковка кожної сторінки контексту)
                        if name_title == 'b0_res_content':
                            # Змінюємо посилання в тексті використовуючи функцію replace_link та регулярний вираз
                            # row_database_game[name_title] = re.sub(r'<a href="(.*?)"', replace_link, row_database_game[name_title])
                            row_database_game[name_title] = re.sub(r'href="?([^"\s]+)"?', replace_link, row_database_game[name_title])

                    # TRANSLATE - Розбираємо та перекладаємо JSON поля DEEPL
                    translate_baza_keys = {'b1_content_json': {'h2_title':'','description':'','alt_img':''},
                                        'b1_demo_iframe': {'demo_h2':'','alt_img':''},
                                        'b1_content_table_json': {'td_1':'','td_2':''},
                                        'b1_comments_json': {'h3_name_comment':'','p_review_comment':''},
                                        'b1_video_json': {'video_name':'','video_description':''},
                                        'image_galer_json': {'description':''},
                                        'faq_block_json': {'question_text':'','answer_text':''},
                                        'b2_instruction_how_to_json': {'h3_insruction':'','text':''},
                                        'new_block_p_json': {'h2':'','p_text':''},  #pub_date
                                        }

                    for key, value in translate_baza_keys.items():
                        if row_database_game[key] is not None and len(row_database_game[key]) > 0:  # перевіряємо чи не пусте JSON поле
                            sql_json = json.loads(row_database_game[key])  # розпакуємо JSON
                            for row_json in sql_json:
                                for key_baza in value.keys():
                                    # Translate JSON if not NONE
                                    if get_length(row_json[key_baza]) > 0:
                                        # Замінюємо входження зі списку dont_translate на тег <keep>
                                        if isinstance(row_json[key_baza], str):  # Переконайтесь, що row_database_game[key_baza] є рядком перед перекладом
                                            #   TRANSLATE
                                            row_json[key_baza] = translate_deepl_keep_and_clean(translator, row_json, key_baza, lang, dont_translate)
                                            #   СЕО замена ключевого слова если есть популярное в GEO
                                            row_json[key_baza] = replace_keys_with_random_values(row_json[key_baza], lang, keys_in_geo)
                                            #   Перелінковка Змінюємо посилання в тексті використовуючи функцію replace_link та регулярний вираз
                                            row_json[key_baza] = re.sub(r'href="?([^"\s]+)"?', replace_link, row_json[key_baza])
                                            #   чистим от двойных кавычек
                                            if key_baza == 'b1_comments_json' or key_baza == 'faq_block_json' or key_baza == 'image_galer_json':
                                                row_json[key_baza] = row_json[key_baza].replace('"', '')

                                row_database_game[key] = json.dumps(sql_json)

                    # SQL INSERT запись modx_games_co
                    baza_key_games_co = ", ".join([f"`{key}`" for key in row_database_game.keys()])
                    baza_value_games_co = tuple(row_database_game.values())
                    baza_sql_dublikat_games_co = ", ".join([f"`{key}`=VALUES(`{key}`)" for key in row_database_game.keys()])

                    with connect_database.cursor() as cursor:
                        # Create a new record
                        sql_resurs = f"INSERT INTO `modx_games_co` ({baza_key_games_co})\
                                        VALUES ({', '.join(['%s'] * len(baza_value_games_co))}) \
                                        ON DUPLICATE KEY UPDATE {baza_sql_dublikat_games_co}"
                        cursor.execute(sql_resurs, baza_value_games_co)
                    connect_database.commit()

                    print("modx_games_co - " + str(row_database_game['res_context_key']) + ": " + str(row_database_game['resource_id']))

            # ################################################################################################
            # # CONTEXT настройка контекста - modx_context_setting
            # ################################################################################################

            language_dict = {"en": "English", "ru": "Русский", "es": "Español", "pl": "Polski", "pt-br": "Português (Brasil)", 
                            "pt": "Português", "fr": "Français", "id": "Bahasa Indonesia", "el": "Ελληνικά", "de": "Deutsch", 
                            "tr": "Türkçe", "hu": "Magyar", "uk": "Українська", "it": "Italiano", "ro": "Română", "bg": "Български", 
                            "fi": "Suomi", "et": "Eesti", "lt": "Lietuvių", "lv": "Latviešu", "nl": "Nederlands", "cs": "Čeština", 
                            "da": "Dansk", "ja": "日本語", "nb": "Norsk Bokmål", "sk": "Slovenčina", "sl": "Slovenščina", "sv": "Svenska", 
                            "az": "Azərbaycan", "kk": "Қазақ", "ar": "العربية", "uz": "O'zbek"
                            }

            # Список ключей настроек, которые необходимо получить
            settings_keys = ['amp_fullvers', 'footer_allrights', 'cookies', 'author_url_sots_set', 'casino_message_new_player',
                             'header_btn_green_big', 'header_btn_green_small', 'header_btn_red_big', 'header_btn_red_small',
                             'text_redirect_best_casino']

            # Формируем строку с перечислением ключей для SQL запроса
            keys_str = "', '".join(settings_keys)

            # my_cursor.execute(f"SELECT * FROM modx_context_setting WHERE `context_key` = '{CONTEXT_WEB}' AND `key` = 'footer_allrights'")
            # Получаем все нужные настройки одним запросом
            my_cursor.execute(f"SELECT * FROM modx_context_setting WHERE `context_key` = '{CONTEXT_WEB}' AND `key` IN ('{keys_str}')")

            # Создаем словарь для хранения настроек
            settings = {key: None for key in settings_keys}

            # Заполняем словарь значениями из базы данных
            for row in my_cursor.fetchall():
                key = row['key']
                if key in settings:
                    settings[key] = row['value']

            # Теперь переводим каждую настройку
            for key in settings_keys:
                if settings[key] is not None:
                    settings[key] = translate_with_exceptions(settings[key], dont_translate, translator, lang)

            # Доступ к настройкам через словарь settings
            amp_fullvers =              settings['amp_fullvers']
            footer_allrights =          settings['footer_allrights']
            cookies =                   settings['cookies']
            author_url_sots_set =       settings['author_url_sots_set']
            casino_message_new_player = settings['casino_message_new_player']
            header_btn_green_big =      settings['header_btn_green_big']
            header_btn_green_small =    settings['header_btn_green_small']
            header_btn_red_big =        settings['header_btn_red_big']
            header_btn_red_small =      settings['header_btn_red_small']
            text_redirect_best_casino = settings['text_redirect_best_casino']

            # CONTEXT настройка
            keys_context_setting = {'about_us':             struktura_id_map[about_us],
                                    'amp_fullvers':         amp_fullvers,
                                    'author_name':          author_name,
                                    'author_role':          author_role,
                                    'author_url_id':        struktura_id_map[author_url_id],
                                    'author_url_sots_set':  author_url_sots_set,
                                    'base_url':             f'/{lang}/',
                                    'casino_message_new_player':  casino_message_new_player,
                                    'cazino_catalog_id':    struktura_id_map[cazino_catalog_id],
                                    'chan_locale':          locale_alternate[lang],
                                    'cookies':              cookies,
                                    'cultureKey':           lang,
                                    'error_page':           struktura_id_map[error_page],
                                    'footer_allrights':     footer_allrights,
                                    'header_btn_green_big': header_btn_green_big,
                                    'header_btn_green_small': header_btn_green_small,
                                    'header_btn_red_big':   header_btn_red_big,
                                    'header_btn_red_small': header_btn_red_small,
                                    'lang_name':            language_dict[lang],
                                    'locale':               locale_alternate[lang].replace("[[$", "").replace("]]", ""),
                                    'site_name':            site_name,
                                    'site_start':           struktura_id_map[site_start],
                                    'site_url':             f'{MY_SITE}{lang}/',
                                    'text_redirect_best_casino': text_redirect_best_casino
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

        # except Exception as ex:
        #     print("Connection refused...")
        #     print(ex)
            

    # ################################################################################################
    # # TODO: Babel - INSERT SQL - modx_site_tmplvar_contentvalues
    # ################################################################################################

    ############### Видалити всі контексти Бебел
    ############### DELETE FROM `modx_site_tmplvar_contentvalues` WHERE `tmplvarid` = 1;

    # # Додамо вручну РУ - якщо існує
    # ru_versiya = {1: {'ru': 104}, 3: {'ru': 107}, 4: {'ru': 109}, 5: {'ru': 120}, 6: {'ru': 111}, 30: {'ru': 113},
    #               21: {'ru': 112}, 14: {'ru': 106}, 14: {'ru': 106}, 53: {'ru': 108}, 14: {'ru': 106}, 83: {'ru': 121}, 70: {'ru': 110}}

    # ru_versiya_keys = ru_versiya.keys()

    # for key in ru_versiya_keys:
    #     if key in babel_baza_dict:
    #         babel_baza_dict[key].update(ru_versiya[key])
    #     else:
    #         babel_baza_dict[key] = ru_versiya[key]
    # ##################################################################################################

    # with open(r'Clon_MultiLang_SQL_Games\gatesofolympus.club\Babel_SQL_svyazi_all_lang\babel_baza_dict.json', 'r', encoding='utf-8') as file:
    #     babel_baza_dict_json = json.load(file)

    # for babel_row in babel_baza_dict_json.values():
    #     # перебираэмо словник контекстів та звязаних id
    #     result_value_str = ";".join([f"{key}:{value}" for key, value in babel_row.items()])
    #     for contentid in babel_row.values():
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
