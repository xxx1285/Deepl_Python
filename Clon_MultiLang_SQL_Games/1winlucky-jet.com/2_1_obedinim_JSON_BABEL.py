
# Если мы дозаписываем то нужно обьединить со старым JSON файлом
import json

# Пути к файлам JSON
file1_path = r'Clon_MultiLang_SQL_Games\1winlucky-jet.com\Babel_svyazi_all_lang\babel_baza_dict.json'
file2_path = r'Clon_MultiLang_SQL_Games\1winlucky-jet.com\Babel_svyazi_all_lang\babel_baza_dict_PL.json'
output_file_path = r'Clon_MultiLang_SQL_Games\1winlucky-jet.com\Babel_svyazi_all_lang\babel_baza_dict_RES.json'

def read_json_file(file_path):
    """Функция для чтения содержимого файла JSON."""
    with open(file_path, 'r') as file:
        return json.load(file)

def merge_json_objects(obj1, obj2):
    """Функция для объединения двух JSON объектов."""
    for key in obj2:
        if key in obj1:
            if isinstance(obj1[key], dict) and isinstance(obj2[key], dict):
                merge_json_objects(obj1[key], obj2[key])
            elif obj1[key] != obj2[key]:
                obj1[key] = [obj1[key], obj2[key]] if obj1[key] != obj2[key] else obj1[key]
        else:
            obj1[key] = obj2[key]
    return obj1

def merge_json_data(data1, data2):
    """Функция для объединения двух словарей JSON."""
    final_result = {}

    for key in data1:
        final_result[key] = data1[key]

    for key in data2:
        if key in final_result:
            final_result[key] = merge_json_objects(final_result[key], data2[key])
        else:
            final_result[key] = data2[key]

    return final_result

def duplicate_for_each_language(data):
    """Функция для дублирования каждой записи для каждого языка, включая 'web'."""
    duplicated_data = {}
    for key, values in data.items():
        web_value = values.get('web')  # Получаем значение 'web' для текущей записи
        duplicated_data[web_value] = values  # Дублируем запись для 'web'
        for lang_key, lang_value in values.items():
            if lang_key != 'web':  # Для всех ключей, кроме 'web'
                duplicated_data[lang_value] = values.copy()  # Создаем дубликат с ключом, равным значению языка
    return duplicated_data

def write_json_file(file_path, data):
    """Функция для записи данных в файл JSON."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Чтение содержимого JSON-файлов
data1 = read_json_file(file1_path)
data2 = read_json_file(file2_path)

# Объединение данных
merged_data = merge_json_data(data1, data2)

# Дублирование для каждого языка, включая 'web'
final_result = duplicate_for_each_language(merged_data)

# Запись итогового JSON в файл
write_json_file(output_file_path, final_result)

print(f'Объединенный и дублированный JSON-файл был успешно сохранен как {output_file_path}.')