import json
import os

# Указываем папку с JSON файлами
json_folder = r'Parsing\Wikipedia\New_Drops\res'
# Запись уникальных доменов в текстовый файл
output_file = r'Parsing\Wikipedia\New_Drops\res\unique_free_domains.txt'


# Список всех JSON файлов в указанной папке
json_files = [f for f in os.listdir(json_folder) if f.endswith('.json')]

# Множество для хранения уникальных доменов
unique_domains = set()

# Перебор всех файлов и сбор уникальных доменов
for json_file in json_files:
    full_path = os.path.join(json_folder, json_file)
    with open(full_path, 'r') as file:
        data = json.load(file)
        for item in data:
            if item['whois_domain_status'] == 'FREE':
                unique_domains.add(item['domain'])


with open(output_file, 'w') as file:
    for domain in unique_domains:
        file.write(domain + '\n')

print(f"Домены записаны в файл '{output_file}'")
