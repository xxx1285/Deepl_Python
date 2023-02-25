
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
#         with open('baza1.sql', 'r') as f:
#             sql = f.read()
#             cursor.execute(sql)


# except Exception as ex:
#     print("Connection refused...")
#     print(ex)
# finally:
#     connect_import_2.close()
#     print("Connection import CLOSE")