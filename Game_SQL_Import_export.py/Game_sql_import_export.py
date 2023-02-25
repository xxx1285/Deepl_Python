

import os
import json
import pymysql


# SQL Зчитуємо параметри з конфігураційного файлу
with open(r"C:\Gembling\Deepl_Python\Deepl_Python\Game_SQL_Import_export.py\configs\config_sql_import_export.json") as f:
    config = json.load(f)

# Експорт таблиць
tables = ['11111', 'wwwww', 'eeeeee', 'rrrrrrr']

try:
    # Приєднуємось до бази для export SQL
    connect_export_1 = pymysql.connect(host=config['export_1']['host'],
                                       port=3306,
                                       user=config['export_1']['user'],
                                       password=config['export_1']['password'],
                                       database=config['export_1']['database'],
                                       cursorclass=pymysql.cursors.DictCursor
                                       )
    print("succesfully connect Export base..")

    # Приєднуємось до бази для export SQL
    connect_import_2 = pymysql.connect(host=config['import_2']['host'],
                                       port=3306,
                                       user=config['import_2']['user'],
                                       password=config['import_2']['password'],
                                       database=config['import_2']['database'],
                                       cursorclass=pymysql.cursors.DictCursor
                                       )
    print("succesfully connect Import base..")

    try:
        with connection.cursor() as cursor:
            # вибираємо з таблиці за параметром,
            # або використати cursor.execute("SELECT * FROM modx_site WHERE context='web'")
            select_all_rows = f"SELECT * FROM {config['database_sql']['resources_table']} WHERE id IN(39)"
            cursor.execute(select_all_rows)
            rows_site_content = cursor.fetchall()
            for row in rows_site_content:
                # обробляємо json параметри рядків
                # json_2s = json.loads(row["b1_content"])
                # for row1 in json_2s:
                #     row_descript = row1["description"]
                #     transl_result = translator.translate_text(row_descript, target_lang="FR")
                #     print(transl_result.text)

                # Вибираємо Psrent де context=web стовбець в строці SQL
                parent = row['parent']
                if parent != 0:
                    select_query = f"SELECT id FROM {config['database_sql']['resources_table']} WHERE context='web' AND pagetitle=%s AND parent=%s AND template=%s AND menuindex=%s AND content=%s"

                print(parent)

    finally:
        connection.close()
except Exception as ex:
    print("Connection refused...")
    print(ex)
