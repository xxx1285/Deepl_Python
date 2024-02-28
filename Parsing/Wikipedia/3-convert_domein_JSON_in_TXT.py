import json

# Предположим, что ваш JSON файл называется 'data.json'
json_file = r'Parsing\Wikipedia\Result_Status_domain_JSON\wiki_Backstage_South_African_TV_series_DROP_RES_14-01-2024_v1.json'

# Считывание данных из файла
with open(json_file, 'r') as file:
    data = json.load(file)

# Фильтрация доменов со статусом "FREE"
# free_domains = [item['domain'] for item in data if item['whois_domain_status'] == 'FREE']
free_domains = set(item['domain'] for item in data if item['whois_domain_status'] == 'FREE')


# Запись доменов в текстовый файл
with open(r'Parsing\Wikipedia\Result_Status_domain_TXT\wiki_Backstage_South_African_TV_series_DROP_RES_14-01-2024_v1.txt', 'w') as file:
    for domain in free_domains:
        file.write(domain + '\n')

print("Домены записаны в файл 'free_domains.txt'")
