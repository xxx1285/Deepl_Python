

# import os
import re
import json
import pymysql


# куди зберігаємо SQL файл
output_file = r'Game_SQL_Import_export\baza\test_4.sql'

# SQL Зчитуємо параметри з конфігураційного файлу
with open(r"Game_SQL_Import_export\configs\config_sql_import_export.json") as f:
    config = json.load(f)

# Експорт таблиць
my_tables = ['modx_categories', 'modx_context', 'modx_context_setting',
             'modx_media_sources_elements', 'modx_migx_configs',
             'modx_migx_formtabs', 'modx_migx_formtab_fields',
             'modx_site_content', 'modx_site_htmlsnippets', 'modx_site_templates',
             'modx_site_tmplvars', 'modx_site_tmplvar_contentvalues',
             'modx_site_tmplvar_templates', 'modx_system_settings']

# my_tables_str = ", ".join(my_tables)

# Функция для удаления экранирования лапок
def remove_quotes(s):
    if s[0] == "'" and s[-1] == "'":
        return s[1:-1].replace("\\'", "'")
    return s


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
    with open(output_file, 'w', encoding='utf8') as f:
        with connect_export_1.cursor() as cursor:
            # Проходимося по всім таблицям і отримуємо їх структуру та дані

            # Додаємо коментар до файлу
            f.write(f"-- Dump of tables {my_tables} \n\n")

            # ЗНАЧЕННЯ - ДАНІ КОЖНОГО РЯДКА
            for table in my_tables:

                # Додаємо коментар до таблиці
                f.write(f"-- Dump of table {table} \n\n")

                # WRITE СТРУКТУРА ТАБЛИЦІ
                cursor.execute(f"SHOW CREATE TABLE {table}")
                create_table_query = cursor.fetchone()['Create Table']
                f.write(f"{create_table_query};\n\n")

                # Вибираємо всі рядки з таблиці
                cursor.execute(f"SELECT * FROM {table}")
                rows = cursor.fetchall()

                # Загальний список значень для таблиці
                all_values = []

                for row in rows:
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
                            # value = value.replace("'", "\\'").replace('"', '\\"')
                            value = value.replace("'", "\\'")
                            values.append(f"'{value}'")
                        # Якщо значення є числом, додати до списку без лапок
                        elif isinstance(value, (int, float)):
                            values.append(f"{value}")
                        else:
                            values.append(f"'{value}'")
                        # добавляем значение в список значений

                    # объединяем список значений в строку, разделяя их запятыми
                    values = ', '.join(values)

                    # отримуэмо та об'єднуємо список полів до таблиці
                    fields = ', '.join([f"`{key}`" for key in row.keys()])

                    # Добавляємо значення кожного рядка в Загальний список
                    all_values.append(f"({values})")


                # об'єднуємо загальний список в STR розділяючи комами та з нової
                all_values = ', '.join(all_values)

                # Записуємо всі значення
                insert_query = f"INSERT INTO `{table}` ({fields}) VALUES\n{all_values};\n"
                # додаємо вираз вставки даних до файлу
                f.write(f"{insert_query}\n\n")


            # Проходимося по всім таблицям і отримуємо їх структуру та дані
            for table in my_tables:

                # Отримуємо всі індекси таблиці
                cursor.execute(f"SHOW INDEXES FROM `{table}`")
                indexes = cursor.fetchall()
                # Додаємо коментар до файлу
                f.write(f"-- INDEXES table {table} \n\n")

                # Додаємо всі індекси таблиці до файлу
                if len(indexes) > 0:
                    f.write(f"ALTER TABLE `{table}`\n")

                    index_list = []
                    for index in indexes:
                        if index['Key_name'] == 'PRIMARY':
                            index_list.append(f"ADD PRIMARY KEY (`{index['Column_name']}`)")
                            # f.write(f"ADD PRIMARY KEY (`{index['Column_name']}`),\n")
                        elif index['Non_unique'] == 0:
                            index_list.append(f"ADD UNIQUE KEY `{index['Key_name']}` (`{ index['Column_name']}`)")
                        else:
                            index_list.append(f"ADD KEY `{index['Key_name']}` (`{index['Column_name']}`)")

                    index_list = ', \n'.join(index_list)

                    f.write(f"{index_list};\n\n")

                # Получаем название поля с AUTO_INCREMENT
                # cursor.execute(f"SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` \
                #                 WHERE `TABLE_SCHEMA`='{config['export_1']['database']}' AND \
                #                 `TABLE_NAME`='{table}' AND `EXTRA`='auto_increment'")
                # auto_increment_column = cursor.fetchone()

                # cursor.execute(f"SELECT AUTO_INCREMENT FROM information_schema.TABLES \
                #                 WHERE TABLE_SCHEMA = '{config['export_1']['database']}' AND TABLE_NAME = '{table}'")





                cursor.execute(f"SELECT TABLE_NAME, AUTO_INCREMENT \
                                FROM information_schema.TABLES \
                                WHERE TABLE_SCHEMA = '{config['export_1']['database']}' \
                                AND TABLE_NAME = '{table}'")
                cursor_auto = cursor.fetchall()

                # записываем результаты запроса в дамп файл
                for (table, auto_increment) in cursor_auto:
                    f.write(f"ALTER TABLE `{table}` AUTO_INCREMENT = {auto_increment};\n")










                # # Добавляем AUTO_INCREMENT, если он есть
                # if auto_increment_column:
                #     f.write(f"ALTER TABLE {table} MODIFY {auto_increment_column[0]} INT AUTO_INCREMENT;\n")

                # Добавляем COMMIT
                f.write("COMMIT;\n")



except Exception as ex:
    print("Connection refused...")
    print(ex)
finally:
    connect_export_1.close()
    print("Connection Export CLOSE")

# Import SQL
# try:
#     # Приєднуємось до бази для Import SQL
#     connect_import_2 = pymysql.connect(**config['import_2'],
#                                         port=3306,
#                                         cursorclass=pymysql.cursors.DictCursor
#                                         )
#     # sql_mode='NONE',  # режим совместимости SQL
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
#         # with open(output_file, 'r', encoding='utf8') as f:
#         #     # Читання SQL-запитів з файлу
#         #     sql_import = f.read()

#         #     # Видаляємо екранування лапок
#         #     sql_import = re.sub(r"\\'", "'", sql_import)

#         #     # Розділяємо SQL-запити за допомогою ";"
#         #     queries = sql_import.split(';')

#         #     # Разделение файла на отдельные SQL-запросы
#         #     # queries = re.findall(r';\n.*?(?=--|$)', sql_import, re.DOTALL)

#         #     for query in queries:
#         #         # Якщо запит не є порожнім рядком
#         #         if query.strip():
#         #             try:
#         #                 # Удаление экранирования лапок
#         #                 query = re.sub(r"'(.*?)'", lambda x: remove_quotes(x.group()), query)
#         #                 cursor.execute(query)
#         #                 connect_import_2.commit()
#         #             except pymysql.Error as e:
#         #                 # Якщо виникає помилка "Таблиця вже існує"
#         #                 if e.args[0] == 1050:
#         #                     print(f"Таблиця {query.split()[2]} вже існує. Доповнюємо таблицю.")
#         #                     # Доповнюємо таблицю
#         #                     cursor.execute(re.sub(r"CREATE TABLE", "INSERT INTO", query))
#         #                     connect_import_2.commit()
#         #                 else:
#         #                     print(f"Помилка: {e}")
#         #                     connect_import_2.rollback()

#             # # Виконання кожного SQL-запиту
#             # for command in sql_import:
#             #     cursor.execute(command)


# except Exception as ex:
#     print("Connection refused...")
#     print(ex)
# finally:
#     connect_import_2.close()
#     print("Connection import CLOSE")
