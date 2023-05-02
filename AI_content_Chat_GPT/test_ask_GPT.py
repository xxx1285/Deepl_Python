
import os
import openai
import json
import csv
import requests
from requests.exceptions import RequestException

# Загружаем параметры из конфигурационного файла
with open(r'AI_content_Chat_GPT\config\config_OpenAi_Key.json') as f:
    config = json.load(f)
openai.api_key = config['config_openai']['api_openai_key']

# Для запроса и получения кода ответа
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36\
           (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
          }

# Локалі
locales = ["en", "ru"]
# locales = ["en", "ru", "es", "pl", "pt-br", "fr", "id", "el", "de", "tr", "hu", "uk", "it", "ro", 
#            "bg", "fi", "et", "lt", "lv", "nl", "cs", "da", "ja", "nb", "sk", "sl", "sv", "kk", "ar"
#            ]

# Категорії сайтів
categories = [
    "социальные сети", "поиск работы", "Q&A сайты", "видеохостинги", "подкасты", "фриланс сайты с портфолио",
    "обмен документацией/презентациями", "PDF директории", "форумы", "агрегаторы сайтов/блогов", "гостевые посты с размещением игр"
]

# Funktion - AI ZAPROS
def response_ai(promt_ai):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=promt_ai,
        temperature=0.5,
        max_tokens=200,
        top_p=1.0,
        frequency_penalty=0.8,
        presence_penalty=0.0
        )
    return response['choices'][0]['text']

# Clean TEXT
def my_clean_string(string):
    string = string.replace('\n', '')
    string = string.replace(' ', '')
    return string

# Перебор локалей
for loc in locales:
    csv_id = 0

    # Куди зберігати для кожної локалі
    output_file_url = f'AI_content_Chat_GPT/csv/{loc}_links.csv'
    with open(output_file_url, 'w', newline='', encoding='utf-8') as file:
        field_names = ['csv_id', 'local', 'country', 'type_site', 'url', 'kod_200', 'seo_poleznost_ai']
        csv_writer = csv.DictWriter(file, fieldnames=field_names)
        csv_writer.writeheader()

        country = response_ai(f"Основные страны локали {loc}, укажи до 3 стран")

        for categor in categories:
            categor_ai = response_ai(f'найди до 15 популярных и до 5 новых сайтов за типом сайтов "{categor}" в странах локали "{loc}", Напиши только url адреса сайтов разделив запятыми без перечисления, поддоменов и другой информации.')
            
            # Очищаем результат и преобразуем его в список URL
            cleaned_result = my_clean_string(categor_ai)
            urls = cleaned_result.split(', ')

            # Перебираем полученные URL
            for url in urls:
                # Полезность для SEO
                seo_poleznost_ai = response_ai(f"Укажи полезность сайта {url} для SEO, поставив от 1 до 5")
                # код ответа сайта
                try:
                    kod_vidpovidi = requests.get(f'{url}', headers=headers, timeout=10)
                    kod_200 = kod_vidpovidi.status_code
                except RequestException as e:
                    kod_200 = e
                # Добавляем запись в CSV-файл
                csv_id += 1
                csv_writer.writerow({'csv_id': csv_id, 'local': loc, 'country': country, 'type_site': categor, 'url': url, \
                                     'kod_200': kod_200, 'seo_poleznost_ai': seo_poleznost_ai})
