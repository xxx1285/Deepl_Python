import os
import re
import requests

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36\
           (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
          }

folder_path = r"Links_Baza_all_Domains\EDU_poisk_posts_for_coments\edu_domeins"

possible_subdirectories = ["category/blogs/", "blog/", "blogs/", "blogpost/", "forum/", "forums/", "category/articles/", "articles/", 
                           "subforum/", "topic/", "topics/", "discussion/", "post/", "posts/", 
                           "thread/", "threads/", "comment/", "comments/", "messageboards/", "bulletinboard/", "bulletinboards/"
                        ]

files = os.listdir(folder_path)

# Перевіряємо "https://" чи "http://" протокол
def is_valid_page(file_lang, response):
    translation_dict = {
    'ar': 'تعليق', # арабский
    'au': 'comment', # английский (Австралия)
    'bd': 'মন্তব্য', # бенгальский
    'br': 'comentário', # португальский (Бразилия)
    'cn': '评论', # китайский (Китай)
    'co': 'comentario', # испанский (Колумбия)
    'ec': 'comentario', # испанский (Эквадор)
    'ee': 'kommentaar', # эстонский
    'gr': 'σχόλιο', # греческий
    'hk': '評論', # китайский (Гонконг)
    'in': 'कमेंट', # хинди (Индия)
    'it': 'commento', # итальянский
    'kz': 'пікір', # казахский
    'mx': 'comentario', # испанский (Мексика)
    'my': 'komen', # малайский
    'ng': 'comment', # английский (Нигерия)
    'np': 'प्रतिक्रिया', # непальский
    'pe': 'comentario', # испанский (Перу)
    'ph': 'komento', # филиппинский
    'pk': 'تبصرہ', # урду (Пакистан)
    'pl': 'komentarz', # польский
    'rs': 'коментар', # сербский
    'sg': 'comment', # английский (Сингапур)
    'uy': 'comentario', # испанский (Уругвай)
    'vn': 'bình luận', # вьетнамский
    'jp': 'コメント' # японский
    }
    translation_my_lang = [translation_dict['au']]

    if file_lang in translation_dict:
        translation_my_lang.append(translation_dict[file_lang])
        # return translation_dict[file_lang] in response.text
    
    for word in translation_my_lang:
        if word in response.text:
            return True
    return False

# Перевіряємо "https://" чи "http://" протокол
def get_protocol(domain_name):
    try:
        response = requests.get('https://' + domain_name, headers=headers, timeout=3)
        if response.status_code == 200:
            return 'https://'
    except requests.exceptions.RequestException:
        pass
    try:
        response = requests.get('http://' + domain_name, headers=headers, timeout=3)
        if response.status_code == 200:
            return 'http://'
    except requests.exceptions.RequestException:
        pass
    return None


for file in files:

    # выбираем расширение между "_" и "." а именно "br" с 'edu_br.txt'
    match = re.search(r'_(.*?)\.', file)
    if match:
        file_lang = match.group(1)
    else:
        file_lang = 'au'
    
    if file.endswith(".txt"):
        with open(os.path.join(folder_path, file), "r") as f:
            domain_names = f.readlines()

            output_file_name = os.path.join(folder_path, f"200_{os.path.splitext(file)[0]}.txt")
        
            with open(output_file_name, "w") as output_file:
                for domain_name in domain_names:
                    domain_name = domain_name.strip()
                    protocol_http = get_protocol(domain_name)
                    if protocol_http is not None:
                        domain_name = protocol_http + domain_name
                        # domain_name = 'https://' + domain_name
                        response = requests.get(domain_name, headers=headers, timeout=3)
                        if response.status_code == 200:
                            for subdir in possible_subdirectories:
                                url = domain_name.strip() + '/' +subdir
                                try:
                                    response = requests.get(url, headers=headers, timeout=10)
                                    if response.status_code == 200:
                                        if is_valid_page(file_lang, response):
                                            output_file.write(url + '\n')
                                            print(f"{url} - OK")
                                        else:
                                            print(f"{url} - Ignored")
                                except requests.exceptions.RequestException:
                                    print(f"An error occurred with URL: {url}")