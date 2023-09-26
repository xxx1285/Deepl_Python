import json

# def process_url(url):
#     parts = url.split('/', 3)
#     domain = parts[2]
#     path = '/' + parts[3] if len(parts) > 3 else '/'
#     return domain, path
def process_url(url):
    # Розбиваємо URL на частини, враховуючи протокол
    parts = url.split('/', 3)
    domain = parts[2]
    path = '/' + parts[3] if len(parts) > 3 else '/'
    return f"{parts[0]}//{domain}", path

def generate_map_dict(filename):
    map_dict = {}
    
    with open(filename, 'r') as file:
        for line in file:
            url = line.strip()
            domain, path = process_url(url)
            
            if domain not in map_dict:
                map_dict[domain] = {
                    "urls": [],
                    "selenium_actions": []
                }
            
            map_dict[domain]["urls"].append(path)
    
    return map_dict

input_filename = r'Linkbilding\edit_spam_url_in_Selenium_format\input_urls.txt'  # Ім'я вхідного файлу
output_filename = r'Linkbilding\edit_spam_url_in_Selenium_format\output_map_dict.txt'  # Ім'я вихідного файлу

map_dict = generate_map_dict(input_filename)

# Збереження словника у файл
with open(output_filename, 'w') as outfile:
    outfile.write(json.dumps(map_dict, indent=4, ensure_ascii=False))

print(f"Map dict збережено у файлі {output_filename}")
