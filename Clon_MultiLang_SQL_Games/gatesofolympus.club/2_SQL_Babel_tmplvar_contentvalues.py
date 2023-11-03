
# v.2.0.0

import json
import pymysql
import os


# SQL Зчитуємо параметри з конфігураційного файлу
current_folder = os.path.basename(os.path.dirname(__file__))

# BABEL JSON path
babel_file_path = f'Clon_MultiLang_SQL_Games\\{current_folder}\\Babel_svyazi_all_lang\\babel_baza_dict.json'
# SQL Config path
sql_config = f'Clon_MultiLang_SQL_Games\\{current_folder}\\configs\\config_sql.json'


# SQL Config REED
with open(sql_config, 'r') as f:
    configSQL = json.load(f)

# BABEL JSON reed
with open(babel_file_path, 'r', encoding='utf-8') as file:
        babel_baza_dict_json = json.load(file)



try:
     
    # Приєднуємось до бази для Export SQL
    connect_database = pymysql.connect(**configSQL['config_database'],
                                        port=3306,
                                        cursorclass=pymysql.cursors.DictCursor
                                        )




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

    with connect_database.cursor() as my_cursor:
        for babel_row in babel_baza_dict_json.values():
            # перебираэмо словник контекстів та звязаних id
            result_value_str = ";".join([f"{key}:{value}" for key, value in babel_row.items()])
            for contentid in babel_row.values():
                with connect_database.cursor() as cursor_bab:
                    sql_babel = "INSERT INTO `modx_site_tmplvar_contentvalues` (tmplvarid, contentid, value) VALUES (%s, %s, %s) \
                                ON DUPLICATE KEY UPDATE value = VALUES (value)"
                    val = (1, contentid, result_value_str)
                    cursor_bab.execute(sql_babel, val)
                connect_database.commit()

except Exception as ex:
    print("Connection refused...")
    print(ex)
finally:
    connect_database.close()
    print("ALL GOOD - Connection CLOSE")

#####################################################################
# print("ALL GOOD - Connection CLOSE")
# connect_database.close()
