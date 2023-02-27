                insert_query = f"INSERT INTO `{table}` ({fields}) VALUES ({values});\n"


                # додаємо вираз вставки даних до файлу
                f.write(insert_query)