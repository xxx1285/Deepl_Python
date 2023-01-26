

import pymysql
from config import host, user, password, db_name, table_game


try:
    connection = pymysql.connect(host=host,
                                 port=3306,
                                 user=user,
                                 password=password,
                                 database=db_name,
                                 cursorclass=pymysql.cursors.DictCursor
                                 )
    print("succesfully...")
    try:
        with connection.cursor() as cursor:
            select_all_rows = f"SELECT * FROM {table_game}"
            cursor.execute(select_all_rows)
            rows_table_game = cursor.fetchall()
            for row in rows_table_game:
                print(row)
    finally:
        connection.close()
except Exception as ex:
    print("Connection refused...")
    print(ex)
