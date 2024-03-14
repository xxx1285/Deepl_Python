import os

# Пути к папкам с исходными и обработанными файлами
input_dir = r'GSA\Clean_txt_urls_ot_hvostov\input'
output_dir = r'GSA\Clean_txt_urls_ot_hvostov\output'

# Получение списка всех файлов в исходной папке
files = os.listdir(input_dir)

for file in files:
    input_file_path = os.path.join(input_dir, file)
    output_file_path = os.path.join(output_dir, file)

    # Открытие каждого файла для чтения и записи
    with open(input_file_path, 'r', encoding='utf-8', errors='ignore') as source_file, open(output_file_path, 'w', encoding='utf-8') as result_file:
        for line in source_file:
            # Поиск первого пробела в строке
            space_index = line.find(' ')
            # Если пробел найден, удаление всего после пробела
            if space_index != -1:
                line = line[:space_index] + '\n'
            # Запись обработанной строки в новый файл
            result_file.write(line)
