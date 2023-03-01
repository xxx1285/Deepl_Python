                # Записуємо всі значення
                insert_query = f"INSERT INTO `{table}` ({fields}) VALUES\n{all_values};\n"
                # додаємо вираз вставки даних до файлу
                f.write(insert_query)
                # додаємо символ переведення рядка до файлу, щоб розділити таблиці
                f.write('\n')