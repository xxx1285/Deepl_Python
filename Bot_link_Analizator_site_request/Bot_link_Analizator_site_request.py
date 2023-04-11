"""
    Перебираємо всі аналізатори та WHOIS and перевіряємо свої сайти
"""

import requests
import csv
import json
import re
import os
from bs4 import BeautifulSoup

###############################################################################
###############################################################################

my_site_analiz = 'the-dog-house.org'
del_site = 'fijisportclub.ru'

###############################################################################
###############################################################################

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36\
           (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
          }

num = 1
link_json_data = []
# link_json_data = {}
with open(r'Bot_link_Analizator_site_request\csv\Redic-Analizatori.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=';', quotechar=' ')
    # збереження даних у CSV файл
    with open(r'Bot_link_Analizator_site_request\csv\new_Redic-Analizatori_3.csv', 'w', newline='', encoding='utf-8') as new_csv:
        field_names = ['csv_id', 'url', 'kod', 'error_key']
        csv_writer = csv.DictWriter(new_csv, fieldnames=field_names)
        csv_writer.writeheader()
        for row in data:
            # зчитування значення другого стовбця
            value = row[1]
            if re.search(del_site, value):
                # заміна значень
                new_value = value.replace(del_site, my_site_analiz)

                # додавання JSON
                # link_json_data.append({'num': num, 'new_value': new_value})
                link_json_data.append(new_value)
                # print(str(num) + ':' + new_value)

                # индексируем ссылку
                try:
                    response = requests.get(f'{new_value}', headers=headers, timeout=10)
                    response.raise_for_status()
                    # error_key = 'OK'
                    kod = 200
                    response_title = requests.get(f'{new_value}', headers=headers, timeout=3).text
                    soup = BeautifulSoup(response_title, 'lxml')
                    error_key = soup.find('title').text[:25]
                    print(error_key)
                except requests.exceptions.Timeout:
                    error_key = 'Запит не відповів за встановлений таймаут'
                    kod = 408
                except requests.exceptions.ConnectionError:
                    error_key = 'Не вдалось підключитися до сервера'
                    kod = 503
                except requests.exceptions.HTTPError as http_err:
                    error_key = f'HTTP помилка: {http_err}'
                    kod = response.status_code
                except Exception as err:
                    error_key = f'Інша помилка: {err}'
                    kod = 500

                print(kod)
                # print(error_key)

                csv_writer.writerow({'csv_id': num,
                                    'url': new_value,
                                    'kod': kod,
                                    'error_key': error_key
                                    })
                num += 1


# збереження даних у JSON файл
with open(r'Bot_link_Analizator_site_request\json\Redic-Analizatori.json', 'w') as jsonfile:
    json.dump(link_json_data, jsonfile)

print('OLL GOOD')

# response = requests.post(url, params=params, data=data)

