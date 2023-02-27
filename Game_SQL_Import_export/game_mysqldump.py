

# import os
import json
import pymysql
import subprocess


# куди зберігаємо SQL файл
output_file = r'Game_SQL_Import_export\baza\dump_game3.sql'

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

HOST = config['export_1']['host']
USER = config['export_1']['user']
PASSWORD = config['export_1']['password']
DATABASE = config['export_1']['database']

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

    # Відкриваємо файл для запису SQL-дампу
    with open(output_file, 'w', encoding="utf8") as f:

        # Записуємо початок транзакції
        f.write('START TRANSACTION;\n\n')

        # Проходимося по всім таблицям і отримуємо їх структуру та дані
        for table in my_tables:
            # Формуємо команду для експорту таблиці
            command = f"mysqldump --host={HOST} --user={USER} --password={PASSWORD} {DATABASE} `{table}`"

            # Додаємо параметри експорту
            command += " --skip-triggers"  # відключаємо експорт тригерів
            command += " --skip-add-drop-table"  # відключаємо видалення та створення таблиці
            command += " --skip-lock-tables"  # відключаємо блокування таблиць
            command += " --no-create-info"  # відключаємо експорт структури таблиці

            # Додаємо додаткові параметри
            command += " --hex-blob"  # збереження бінарних полів в шістнадцятковому форматі
            command += " --tz-utc"  # збереження TIMESTAMP у форматі UTC
            command += f" --result-file={output_file}"  # файл для збереження dump
            command += " --skip-comments"  # відключаємо коментарі

except Exception as ex:
    print("Connection refused...")
    print(ex)
finally:
    connect_export_1.close()
    print("Connection import CLOSE")

# # Import SQL
# try:
#     # Приєднуємось до бази для Import SQL
#     connect_import_2 = pymysql.connect(**config['import_2'],
#                                        port=3306,
#                                        cursorclass=pymysql.cursors.DictCursor
#                                        )
#     print("succesfully connect Import base..")

#     # Використання with забезпечує правильне закриття з'єднання з базою даних
#     with connect_import_2.cursor() as cursor:
#         # Перебираємо та видаляємо таблиці з Бази данних
#         for table in my_tables:
#             cursor.execute(f"DROP TABLE IF EXISTS {table};")

#         # імпортуємо SQL Dump файл до бази даних
#         with open(output_file, 'r', encoding='utf-8') as f:
#             sql = f.read()
#             cursor.execute(sql)


# except Exception as ex:
#     print("Connection refused...")
#     print(ex)
# finally:
#     connect_import_2.close()
#     print("Connection import CLOSE")
