

import os
import json
import pymysql


# куди зберігаємо SQL файл
output_file = 'export.sql'

# SQL Зчитуємо параметри з конфігураційного файлу
with open(r"C:\Gembling\Deepl_Python\Deepl_Python\Game_SQL_Import_export\configs\config_sql_import_export.json") as f:
    config = json.load(f)

# Експорт таблиць
my_tables = ['modx_categories', 'modx_context', 'modx_context_setting',
             'modx_media_sources_elements', 'modx_migx_configs',
             'modx_migx_formtabs', 'modx_migx_formtab_fields',
             'modx_site_content', 'modx_site_htmlsnippets', 'modx_site_templates',
             'modx_site_tmplvars', 'modx_site_tmplvar_contentvalues',
             'modx_site_tmplvar_templates', 'modx_system_settings']

# my_tables_str = ", ".join(my_tables)
data = []

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

    for table in my_tables:
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
            sql_export = f"SELECT * FROM {table}"
            cursor.execute(sql_export)
            result = cursor.fetchall()
            data.append(result)
            print("Tables" + table + " exported to file")

    # збереження результату у файлі
    with open('baza2.sql', 'w', encoding="utf-8") as f:
        for table, result in zip(my_tables, data):
            f.write(f"INSERT INTO {table} VALUES\n")
            for row in result:
                f.write(f"{row}\n")

except Exception as ex:
    print("Connection refused...")
    print(ex)
finally:
    connect_export_1.close()
    print("Connection import CLOSE")




# try:
#     # Приєднуємось до бази для Import SQL
#     connect_import_2 = pymysql.connect(**config['import_2'],
#                                        port=3306,
#                                        cursorclass=pymysql.cursors.DictCursor
#                                        )
#     print("succesfully connect Import base..")

#     # Використання with забезпечує правильне закриття з'єднання з базою даних
#     with connect_export_1.cursor() as cursor:
#         # Експортуємо таблиці у SQL форматі
#         query = f'SELECT * INTO OUTFILE "C:/Gembling/Deepl_Python/Deepl_Python/Game_SQL_Import_export/baza/export.sql" FROM {my_tables}'
#         print(query)
#         cursor.execute(query)
#         print("Tables exported to file")

# except Exception as ex:
#     print("Connection refused...")
#     print(ex)
# finally:
#     connect_import_2.close()
#     print("Connection import CLOSE")
