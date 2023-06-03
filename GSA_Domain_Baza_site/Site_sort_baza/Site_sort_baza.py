"""
    1 - Розбити файл 250 млн доменів по файлам з язиками
    2 - Видалити файли де менше 5 записів
"""
import os
# import csv
from collections import defaultdict
from pathlib import Path

# Функція-генератор для зчитування рядків з файлу покроково
def read_large_file(file_object):
    while True:
        line = file_object.readline()
        if not line:
            break
        yield line.strip()

# Вкажіть шлях до папки з CSV-файлами
folder_path = 'Site_sort_baza/csv_finish_sort'

# Створюємо словник для зберігання доменів, розділених за зонами
domain_files = defaultdict(list)

# set унікальних доменних зон
unique_data = set()

# Відкриваємо файл baza.txt для зчитування доменів
with open(r'Site_sort_baza\csv_baza\domains.txt', 'r') as txtfile:
    # Проходимося по кожному рядку у файлі, використовуючи генератор
    for domain in read_large_file(txtfile):
        # Витягуємо TLD (домен верхнього рівня) з доменного ім'я
        tld = domain.split('.', 1)[-1]
        unique_data.add(tld)
        # Замінюємо символ "." на "_" в TLD
        tld = tld.replace('.', '_')
        # Додаємо домен до відповідного списку в словнику зон доменів
        domain_files[tld].append(domain)

        # Записуємо розділених доменів у відповідні файли після кожних 1000 записів
        if len(domain_files[tld]) >= 1000:
            with open(f'Site_sort_baza/csv_finish_sort/{tld}.txt', 'a', newline='', encoding='utf-8') as outfile:
                # csvwriter = csv.writer(outfile)   CSV
                for domain in domain_files[tld]:
                    # csvwriter.writerow([domain])  CSV
                    outfile.write(domain + '\n')
            # Очищуємо список записів для поточної зони
            domain_files[tld].clear()

# Записуємо розділених доменів у відповідні файли
for tld, domains in domain_files.items():
    # Відкриваємо файл для запису доменів з певною зоною
    with open(f'Site_sort_baza/csv_finish_sort/{tld}.txt', 'a', newline='', encoding='utf-8') as outfile:
        # csvwriter = csv.writer(outfile)   CSV
        # Записуємо кожен домен у файл
        for domain in domains:
            # csvwriter.writerow([domain])  CSV
            outfile.write(domain + '\n')
            print(domain + ' > 1000')

# Виводимо повідомлення про успішне розділення доменів
print('Домени успішно розділені та додані в файли.')

################################################################################################################
    # Видаляємо всі файли де менше 5 записів - фільтруємо сміття
################################################################################################################

# # Перебираємо всі файли CSV в папці
# for file_name in os.listdir(folder_path):
#     # Перевіряємо, чи файл має розширення .csv
#     if file_name.endswith('.csv'):
#         # Створюємо повний шлях до файлу
#         file_path = os.path.join(folder_path, file_name)
#         # Відкриваємо файл та рахуємо кількість рядків
#         with open(file_path, 'r', encoding='utf-8', newline='') as csvfile:
#             row_count = 0
#             for row in csv.reader(csvfile):
#                 row_count += 1
#                 if row_count > 505:
#                     break
#         # Якщо кількість рядків менше 5, видаляємо файл
#         if row_count < 501:
#             os.remove(file_path)
#             print(f'Файл {file_name} видалено, бо містить менше 25 рядків.')


min_file_size = 6500  # Мінімальний розмір файла в байтах (1500 = 1.5 KB)

# Перебираємо всі файли в папці
for file_name in os.listdir(folder_path):
    # Перевіряємо, чи файл має розширення .txt
    if file_name.endswith('.txt'):
        # Створюємо повний шлях до файлу
        file_path = os.path.join(folder_path, file_name)
        # Отримуємо розмір файла в байтах
        file_size = os.path.getsize(file_path)
        # Перевіряємо, чи розмір файла менше за заданий мінімальний розмір
        if file_size < min_file_size:
            # Видаляємо файл
            os.remove(file_path)



print('Файли з рядками менше 100 - ВИДАЛЕНІ.')

################################################################################################################
    # Перебираємо файли та зберігаємо в файл для запису унікальних доменних зон
################################################################################################################

unique_names = set()

# Перебір файлів у каталозі 'large'
for file_name in os.listdir(folder_path):
    # Отримання імені файлу без розширення
    base_name = Path(file_name).stem

    # Заміна символу "_" на "."
    modified_name = base_name.replace('_', '.')

    # Додавання зміненого імені до множини unique_names
    unique_names.add(modified_name)

# Запис унікальних імен файлів у файл
with open('Site_sort_baza/all_domen_zona.txt', 'w', encoding='utf-8', newline='') as output_file:
    for name in unique_names:
        output_file.write(f'{name}, ')

print('Створено файл всіх доменних зон що оброблено')