
# 01.03.2024
# 1winlucky-jet - CLON-CONTEXT

import os
import json
import pymysql
import os

############################################
# CЛОВНИК КЛОНУВАНЬ КОНТЕКСТІВ - РЕСУРСІВ та MIGX ['CONTEXT_NEW','DOMAIN_SITE']
############################################
# dict_clon_contexts = {
#     'anlcreativetest.site': {'d2anlcreativetest': 'tr'},
#     'booi-casinosclub.online': {'d2booicasinosclub': 'ru'},
#     'igry-na-dengi.online': {'d2igrynadengi': 'ru'},
#     'netgames777.top': {'d2netgames777': 'ru'},
#     'slotsboss.top': {'d2slotsboss': 'ru'}
# }
dict_clon_contexts = {
    'fittor.top': {'d2fittor': 'pl'}
}
############################################



current_folder = os.path.basename(os.path.dirname(__file__))

############################################
# SQL
############################################
sql_config = f'Clon_MultiLang_SQL_Games\\{current_folder}\\configs\\config_sql.json'
# SQL Config REED
with open(sql_config, 'r') as f:
    configSQL = json.load(f)
# Приєднуємось до бази для Export SQL
connect_database = pymysql.connect(**configSQL['config_database'],
                                    port=3306,
                                    cursorclass=pymysql.cursors.DictCursor
                                    )
print("\n*************************************\
        \n--> Succesfully connect - " + configSQL['config_database']['database'] + "\
        \n*************************************")
############################################


# Контексти та мови для перекладу
# context_and_lang = ["ru","es","pl","pt-br","fr","id","el","de","tr","hu","uk","it","ro","bg","fi","et",
#                     "lt","lv","nl","cs","da","ja","nb","sk","sl","sv"]
# перебираємо префікси мов, щоб аліас не починався з 'ru', 'es', 'pl'....
# all_prefix_for_alias = ["en","ru","es","pl","pt-br","pt","fr","id","el","de","tr","hu","uk","it","ro","bg","fi","et",
#                         "lt","lv","nl","cs","da","ja","nb","sk","sl","sv","az","kk","ar","uz"]
# web,ru,es,pl,pt-br,fr,id,el,de,tr,hu,uk,it,ro,bg,fi,et,lt,lv,nl,cs,da,ja,nb,sk,sl,sv,az,kk,ar,uz



for domain, details in dict_clon_contexts.items():
    for new_context, clon_context_name in details.items():

        # Словник звязаних між собою Ресурсів
        struktura_id_map = {}

        ############################################
        # СТВОРЮЄМО НОВІ КОНТЕКСТИ
        ############################################
        with connect_database.cursor() as cursor:
            name_new_context = f'Drop {clon_context_name.upper()} - {domain}'
            sql_babel = "INSERT INTO `modx_context` (`key`, `name`, `description`, `rank`) \
                        VALUES (%s, %s, %s, %s) \
                        ON DUPLICATE KEY UPDATE name=VALUES(name)"
            val = (new_context, name_new_context, '', 5)
            cursor.execute(sql_babel, val)
        connect_database.commit()
        ############################################

        ############################################
        # КЛОНУЄМО РЕСУРСИ
        ############################################

        with connect_database.cursor() as cursor:
            # Максимальне значення ID в таблиці для правильного визначення наступного значення в SQL таблиці
            cursor.execute("SELECT MAX(`id`) as max_id FROM `modx_site_content`")
            result = cursor.fetchone()
            max_id = result['max_id']
            start_id = max_id + 1
            ############################################
            sql_select = "SELECT * FROM `modx_site_content` WHERE `context_key` = %s"
            cursor.execute(sql_select, (clon_context_name,))
            rows = cursor.fetchall()


            for row in rows:
                # Клонуємо рядок
                new_row = row.copy()
                # новий id елемента
                new_row['id'] = start_id    
                start_id += 1
                # структура вкладень
                struktura_id_map[row['id']] = new_row['id']  # структура вкладень
                # PARENT - Визначаємо структуру
                if new_row['parent'] != 0:  # 0 - это нет вложености по SQL таблице
                    new_row['parent'] = struktura_id_map[new_row['parent']]

                ##############################################################################
                new_row['context_key'] = new_context
                ##############################################################################
                # SQL INSERT запись modx_site_content
                ##############################################################################
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

                print(f"modx_site_content ==> {new_context} -- {new_row['id']}") 


        ############################################
        # КЛОНУЄМО MIGX modx_games_co
        ############################################
        with connect_database.cursor() as cursor:    
            for key_row, key_new_row in struktura_id_map.items():

                # Максимальне значення ID в таблиці для правильного визначення наступного значення в SQL таблиці
                cursor.execute("SELECT MAX(`id`) as max_id FROM `modx_games_co`")
                result = cursor.fetchone()
                max_id = result['max_id']
                start_id = max_id + 1

                # Выбор всех строк таблицы modx_games_co
                cursor.execute(f"SELECT * FROM `modx_games_co` WHERE `resource_id` = '{key_row}'")
                row_modx_games = cursor.fetchone()

                if row_modx_games is not None:

                    # новий id елемента
                    row_modx_games['id'] = start_id    
                    start_id += 1
                    # resource_id
                    row_modx_games['resource_id'] = key_new_row
                    # id такий як і в ресурса
                    row_modx_games['res_context_key'] = new_context


                    ############################################
                    # SQL INSERT запись modx_games_co
                    ############################################
                    baza_key_games_co = ", ".join([f"`{key}`" for key in row_modx_games.keys()])
                    baza_value_games_co = tuple(row_modx_games.values())
                    baza_sql_dublikat_games_co = ", ".join([f"`{key}`=VALUES(`{key}`)" for key in row_modx_games.keys()])

                    sql_resurs = f"INSERT INTO `modx_games_co` ({baza_key_games_co})\
                                    VALUES ({', '.join(['%s'] * len(baza_value_games_co))}) \
                                    ON DUPLICATE KEY UPDATE {baza_sql_dublikat_games_co}"
                    cursor.execute(sql_resurs, baza_value_games_co)
                    connect_database.commit()

                    print(f"modx_games_co ==> {new_context} -- {row_modx_games['id']}")  

        ############################################
        # НАЛАШТУВАННЯ ДЛЯ КОНТЕКСТІВ
        ############################################

        # Выборка и изменение данных из другой таблицы
        with connect_database.cursor() as cursor:
            sql_select = "SELECT * FROM `modx_context_setting` WHERE `context_key` = %s"
            cursor.execute(sql_select, (clon_context_name,))
            rows = cursor.fetchall()

            for row in rows:
                # Изменение данных в row по вашим требованиям
                row['context_key'] = new_context
                
                if row['key'] == 'site_url':
                    row['value'] = f'https://{domain}/'
                if row['key'] in ['site_start', 'error_page', 'cazino_catalog_id', 'catalog_app', 'author_url_id', 
                                  'apk_page', 'about_us']:
                    value_as_int = int(row['value'])
                    row['value'] = str(struktura_id_map[value_as_int])
                if row['key'] == 'base_url':
                    row['value'] = '/'

                
                ############################################
                # SQL INSERT запись modx_context_setting
                ############################################
                baza_key_context_setting = ", ".join([f"`{key}`" for key in row.keys()])
                baza_value_context_setting = tuple(row.values())
                baza_sql_dublikat_context_setting = ", ".join([f"`{key}`=VALUES(`{key}`)" for key in row.keys()])

                sql_resurs = f"INSERT INTO `modx_context_setting` ({baza_key_context_setting})\
                                VALUES ({', '.join(['%s'] * len(baza_value_context_setting))}) \
                                ON DUPLICATE KEY UPDATE {baza_sql_dublikat_context_setting}"
                cursor.execute(sql_resurs, baza_value_context_setting)
                connect_database.commit()
                print(f"modx_context_setting => {new_context}")


            sql_resurs = "INSERT INTO `modx_context_setting` (`context_key`, `key`, `value`, `xtype`, `namespace`, `area`, `editedon`)\
                VALUES (%s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP) ON DUPLICATE KEY UPDATE `context_key`=VALUES(`context_key`), `key`=VALUES(`key`), `value`=VALUES(`value`), `xtype`=VALUES(`xtype`), `namespace`=VALUES(`namespace`), `area`=VALUES(`area`)"
            cursor.execute(sql_resurs, (new_context, 'http_host', domain, 'textfield', 'core', 'language'))
            connect_database.commit()


        #####################################################################
        print("ОК")
        # connect_database.close()
