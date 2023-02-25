

import json
import pymysql
import deepl

# SQL Зчитуємо параметри з конфігураційного файлу
with open(r"C:\Gembling\Deepl_Python\Deepl_Python\My_unik_text\configs\config_sql_deepl.json") as f:
    config = json.load(f)

# доп налаштування
context_baza = "web"
lang_baza = "en"
lang_pereklad = ["es", "pl"]

try:
    # Приєднуємось до бази SQL
    connection = pymysql.connect(host=config['database_sql']['host'],
                                 port=3306,
                                 user=config['database_sql']['user'],
                                 password=config['database_sql']['password'],
                                 database=config['database_sql']['database'],
                                 cursorclass=pymysql.cursors.DictCursor
                                 )
    print("succesfully...")
    # translator = deepl.Translator(deepl_api_key)

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
