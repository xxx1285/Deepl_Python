import os
import re
import httpx
import ssl
import asyncio

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36\
           (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
          }

folder_path = r"Links_Baza_all_Domains\EDU_poisk_posts_for_coments\edu_domeins"

possible_subdirectories = ["cate7456/", "cate7456/", "category/blogs/", "blog/", "blogs/", "blogpost/", "forum/", "forums/", 
                           "category/articles/", "articles/", "subforum/", "topic/", "topics/", "discussion/", "post/", "posts/", 
                           "thread/", "threads/", "comment/", "comments/", "messageboards/", "bulletinboard/", "bulletinboards/"
                        ]
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

# Встановіть максимальну кількість одночасних асинхронних завдань
semaphore = asyncio.Semaphore(40)

class AsyncClientManager:
    #  клас AsyncClientManager, який використовується як асинхронний менеджер контексту
    #  не функцію, тому що нам потрібно створити об'єкт, який можна використовувати у контексті менеджера контексту Python
    def __init__(self):
        self.client = None

    async def __aenter__(self):
        # Коли ви входите в контекст (всередині блоку with) викликається метод __aenter__ (асинхронний)
        self.client = httpx.AsyncClient(timeout=7.0, verify=False)
        return self.client

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # Коли ви виходите з контексту (всередині блоку with) викликається метод __aexit__ (асинхронний)
        # exc_type, exc_val, exc_tb - це стандартні аргументи, які передаються в метод __aexit__
        await self.client.aclose()


async_client_manager = AsyncClientManager()

# Функція перевірки ключевих слів в тексті
def is_valid_page(file_lang, text):
    translation_my_lang = [translation_dict['au'], 'message']
    if file_lang in translation_dict:
        translation_my_lang.append(translation_dict[file_lang])
    for word in translation_my_lang:
        if word in text:
            return True
    return False


# Асинхронна функція визначення 'https://' або 'http://'
async def get_protocol(domain_name):
    async with semaphore, async_client_manager as client: # створюємо асинхронного клієнта
        try:
            # await використовується для "очікування" результату асинхронної операції
            response = await client.get('https://' + domain_name) # використовуємо асинхронний запит
            # last_modified = response.headers.get('last-modified')
            if response.status_code == 200:
                return 'https://'
        except (httpx.RequestError, ssl.SSLError):
            pass
        except UnicodeEncodeError:  # коли ваш код обробляє небуквені символи або небуквені мови
            print(f"Unicode error with domain: {domain_name}")
            pass
        try:
            # await використовується для "очікування" результату асинхронної операції
            response = await client.get('http://' + domain_name) # використовуємо асинхронний запит
            if response.status_code == 200:
                return 'http://'
        except (httpx.RequestError, ssl.SSLError):
            pass
        except UnicodeEncodeError:  # коли ваш код обробляє небуквені символи або небуквені мови
            print(f"Unicode error with domain: {domain_name}")
            pass
    return None


if __name__ == "__main__":
    files = os.listdir(folder_path)
    # Перебираємо файли каталога
    for file in files:

        # выбираем расширение между "_" и "." а именно "br" с 'edu_br.txt'
        match = re.search(r'_(.*?)\.', file)  # match - це обьєкт що тримуємо
        if match:
            file_lang = match.group(1)  # якщо match is True тоді розпаковуємо
        else:
            file_lang = 'au'

        if file.endswith(".txt"):
            with open(os.path.join(folder_path, file), "r") as f:
                domain_names = f.readlines()

                output_file_name = os.path.join(folder_path, f"200_{os.path.splitext(file)[0]}.txt")
            
                with open(output_file_name, "w") as output_file:

                    # Створюємо асинхронну функцію
                    async def process_domain(domain_name):
                        domain_name = domain_name.strip()               # чистимо від пробілів та символів пробілів \n
                        protocol_http = await get_protocol(domain_name) # вик функцію по перебору "https"/"http" на код 200
                        print(str(protocol_http) + " - " + domain_name)

                        if protocol_http is not None:
                            domain_name = protocol_http + domain_name
                            async with semaphore, async_client_manager as client: # використовуємо асинхронного клієнта
                                try:
                                    response = await client.get(domain_name, headers=headers) # використовуємо асинхронний запит
                                    if response.status_code == 200:
                                        success_counter = 1
                                        for subdir in possible_subdirectories:
                                            if success_counter >= 2: 
                                                break
                                            url = domain_name.strip() + '/' + subdir
                                            try:
                                                response = await client.get(url, headers=headers, timeout=10.0) # використовуємо асинхронний запит
                                                if response.status_code == 200:
                                                    success_counter += 1
                                                    if is_valid_page(file_lang, response.text):
                                                        output_file.write(url + '\n')
                                                        print(f"{url} - OK")
                                                    else:
                                                        print(f"{url} - Ignored")
                                            except (httpx.RequestError, ssl.SSLError):
                                                print(f"An error occurred with URL: {url}")
                                            except UnicodeEncodeError:  # коли ваш код обробляє небуквені символи або небуквені мови
                                                print(f"Unicode error url: {url}")
                                except (httpx.RequestError, ssl.SSLError):
                                    print(f"An error occurred with URL: {domain_name}")
                                except UnicodeEncodeError:  # коли ваш код обробляє небуквені символи або небуквені мови
                                    print(f"Unicode error domain_name in process_domain: {domain_name}")
                    
                    # Запускаємо всі задачі паралельно
                    # Замість прямого запуску asyncio.gather, викликайте його в асинхронній функції main()
                    # це генератор, який створює асинхронне завдання для кожного доменного імені в списку domain_names
                    # * (або оператор розпакування) розпаковує цей генератор у список завдань, які потім передаються в asyncio.gather
                    async def main():
                        await asyncio.gather(*(process_domain(domain_name) for domain_name in domain_names))

                    #  Запускаємо всі задачі паралельно
                    #  цей рядок отримує поточний цикл подій. Цикл подій - це ядро кожної асинхронної програми і керує виконанням різних завдань
                    loop = asyncio.get_event_loop()
                    #  ця перевірка перевіряє, чи закритий поточний цикл подій
                    if loop.is_closed():  # Додано перевірку, чи цикл подій вже закритий
                        loop = asyncio.new_event_loop()
                        asyncio.set_event_loop(loop)
                    loop.run_until_complete(main())