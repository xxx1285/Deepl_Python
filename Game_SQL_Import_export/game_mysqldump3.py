

# import os
import json
import pymysql


# куди зберігаємо SQL файл
output_file = r'Game_SQL_Import_export\baza\dump_game0003312.sql'

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

    # Відкриваємо файл для запису SQL-дампу
    with open(output_file, 'w', encoding="utf8") as f:
        # Проходимося по всім таблицям і отримуємо їх структуру та дані
        for table in my_tables:
            # all_value = []
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
                # Отримуємо структуру таблиці
                cursor.execute(f"SHOW CREATE TABLE {table}")
                create_table_query = cursor.fetchone()['Create Table']
                f.write(f"{create_table_query};\n")

                # Експортуємо таблиці у SQL форматі
                sql_export = f"SELECT * FROM {table}"
                cursor.execute(sql_export)
                rows = cursor.fetchall()

                # Загальний список значень для таблиці
                all_values = []

                # перебираємо кожен рядок таблиці
                for row in rows:
                    # values = ', '.join([f"'{value.hex()}'" if isinstance(value, bytes) else f"'{value}'" for value in row.values()])
                    # формируємо список значень для кожного рядка
                    values = []
                    for value in row.values():
                        # Якщо значення є NULL, додати до списку значення 'NULL'
                        if value is None:
                            values.append('NULL')
                        elif isinstance(value, bytes):
                            value = value.hex()
                            values.append(f"'{value}'")
                        # Якщо значення є рядком, додати до списку лапки з екрануванням лапок всередині рядка
                        elif isinstance(value, str):
                            # values.append("'" + value.replace("'", "\\'") + "'")
                            value = value.replace("'", "\\'").replace('"', '\\"')
                            values.append(f"'{value}'")
                        # Якщо значення є числом, додати до списку без лапок
                        elif isinstance(value, (int, float)):
                            values.append(f"{value}")
                        else:
                            values.append(f"'{value}'")
                        # добавляем значение в список значений

                    # объединяем список значений в строку, разделяя их запятыми
                    values = ', '.join(values)

                    # об'єднуємо список полів до таблиці
                    fields = ', '.join([f"`{key}`" for key in row.keys()])

                    # Добаляємо значення в Загальний список значень для таблиці
                    all_values.append(f"({values})")

                # об'єднуємо загальий список значень таблиці розділяючи комами та з нової
                all_values = ', \n'.join(all_values)

                # fields = ', '.join([f"`{key}`" for key in row.keys()])
                #     # insert_query = f"INSERT INTO `{table}` ({fields}) VALUES ({values});\n"
            insert_query = f"INSERT INTO `{table}` ({fields}) VALUES\n{all_values};\n"

            # додаємо вираз вставки даних до файлу
            f.write(insert_query)

            # додаємо символ переведення рядка до файлу, щоб розділити таблиці
            f.write('\n')

except Exception as ex:
    print("Connection refused...")
    print(ex)
finally:
    connect_export_1.close()
    print("Connection Export CLOSE")

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
#         # with open(output_file, 'r', encoding='utf-8') as f:
#         #     sql = f.read()
#         #     cursor.execute(sql)

#         # Відкриття файлу для читання
#         with open(output_file, 'r') as f:
#             # Читання SQL-запитів з файлу
#             sql_commands = f.read()

#             # Виконання кожного SQL-запиту
#             for command in sql_commands:
#                 cursor.execute(command)


# except Exception as ex:
#     print("Connection refused...")
#     print(ex)
# finally:
#     connect_import_2.close()
#     print("Connection import CLOSE")
