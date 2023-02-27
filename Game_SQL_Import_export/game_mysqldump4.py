import json
import pymysql
import datetime

# куди зберігаємо SQL файл
output_file = r'Game_SQL_Import_export\baza\dump_game0003321.sql'

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

    # Відкриття файлу для запису
    with open(output_file, 'w', encoding='utf-8') as f:

        # Створення курсору
        with connect_export_1.cursor() as cursor:
            # Виконання запиту для вибірки даних з таблиць
            select_query = f"SELECT * FROM {' ,'.join(my_tables)};"
            cursor.execute(select_query)
            results = cursor.fetchall()

            # Запис команди для створення бази даних
            f.write("CREATE DATABASE IF NOT EXISTS " + config['database'] + ";\n\n")
            f.write("USE " + config['database'] + ";\n\n")

            # Запис команд для створення таблиць
            for table in my_tables:
                cursor.execute("SHOW CREATE TABLE " + table)
                create_table = cursor.fetchone()['Create Table']
                f.write(create_table + ";\n\n")

            # Запис даних у таблиці
            for row in results:
                values = []
                for value in row.values():
                    # Якщо значення є NULL, додати до списку значення 'NULL'
                    if value is None:
                        values.append('NULL')
                    # Якщо значення є рядком, додати до списку лапки з екрануванням лапок всередині рядка
                    elif isinstance(value, str):
                        values.append("'" + value.replace("'", "''") + "'")
                    # Якщо значення є числом, додати до списку без лапок
                    elif isinstance(value, (int, float)):
                        values.append(str(value))
                    # Якщо значення є датою, додати до списку лапки зі значенням дати в форматі "%Y-%m-%d %H:%M:%S"
                    elif isinstance(value, datetime.datetime):
                        values.append("'" + value.strftime('%Y-%m-%d %H:%M:%S') + "'")
                # Створення запиту для вставки даних у таблицю
                query = "INSERT INTO " + tables[i] + " VALUES (" + ", ".join(values) + ")"
                # Запис запиту до файлу
                f.write(query + ";\n")

except Exception as ex:
    print("Connection refused...")
    print(ex)
finally:
    connect_export_1.close()
    print("Connection import CLOSE")
