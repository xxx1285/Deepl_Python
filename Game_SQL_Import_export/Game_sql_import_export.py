

import os
import json
import pymysql


# куди зберігаємо SQL файл
output_file = 'export.sql'

# SQL Зчитуємо параметри з конфігураційного файлу
with open(r"C:\Gembling\Deepl_Python\Deepl_Python\Game_SQL_Import_export.py\configs\config_sql_import_export.json") as f:
    config = json.load(f)

# Експорт таблиць
my_tables = ['modx_categories', 'modx_context', 'modx_context_setting',
             'modx_media_sources_elements', 'modx_migx_configs',
             'modx_migx_formtabs', 'modx_migx_formtab_fields',
             'modx_site_content', 'modx_site_htmlsnippets', 'modx_site_templates',
             'modx_site_tmplvars', 'modx_site_tmplvar_contentvalues',
             'modx_site_tmplvar_templates', 'modx_system_settings']

my_tables = ", ".join(my_tables)

try:
    # Приєднуємось до бази для Export SQL
    connect_export_1 = pymysql.connect(host=config['export_1']['host'],
                                       port=3306,
                                       user=config['export_1']['user'],
                                       password=config['export_1']['password'],
                                       database=config['export_1']['database'],
                                       cursorclass=pymysql.cursors.DictCursor
                                       )
    print("succesfully connect Export base..")

    # # Приєднуємось до бази для Import SQL
    # connect_import_2 = pymysql.connect(**config['import_2'],
    #                                    port=3306,
    #                                    cursorclass=pymysql.cursors.DictCursor
    #                                    )
    # print("succesfully connect Import base..")

    try:
        """
        Використання with забезпечує правильне закриття з'єднання з базою даних, навіть у випадку,
        якщо сталася помилка в середині блоку with. Це дає можливість уникнути потенційних
        проблем з пам'яттю та забезпечити коректну роботу з базою даних.
        Використовуючи with конструкцію, ми можемо гарантувати, що після завершення
        виконання програми об'єкти, які були відкриті, будуть автоматично закриті.
        Це дуже зручно, оскільки нам не потрібно додатково вказувати закриття курсора
        та з'єднання з базою даних.
        Курсор cursor() викор... для виконання SQL запитів та отримання резу.
        """
        with connect_export_1.cursor() as cursor:
            # Експортуємо таблиці у SQL форматі
            query = f"SELECT * INTO OUTFILE 'C:/Gembling/Deepl_Python/Deepl_Python/Game_SQL_Import_export/baza/export.sql' FROM {my_tables}"
            cursor.execute(query)
            print("Tables exported to file")



            for table_name in my_tables:
                cursor.execute(f"SELECT * INTO OUTFILE '{table_name}.sql' FROM {table_name}")
                print(f"Exported {table_name} table to SQL file")

                # Додаємо до експортного SQL файлу SQL запит на створення таблиці
                with open(f"Root/{table_name}.sql") as f:
                    table_sql = f.read()
                export_sql += table_sql
            for table_name in limon:
                # Перейменовуємо базу даних в запиті на експорт
                query = f"SELECT * INTO OUTFILE 'Root/{table_name}.sql' FROM baza1.{table_name}"
                cursor.execute(query.replace('baza1', 'baza2'))



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
        connect_export_1.close()
        # connect_import_2.close()
except Exception as ex:
    print("Connection refused...")
    print(ex)
