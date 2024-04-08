import re
import time

def remove_ld_json_keys(soup):
    # Чистим LD-JSON
    for script in soup.find_all("script", type="application/ld+json"):
        script_content = script.string
        if script_content:
            # Удаляем "founders" и "sameAs" из JSON-содержимого
            script_content = re.sub(r'"founders"\s*:\s*{[^}]+},?', '', script_content)
            script_content = re.sub(r'"sameAs"\s*:\s*\[[^\]]+\],?', '', script_content)
            # Удаляем запятую, если она есть, перед последней фигурной скобкой
            script_content = re.sub(r',\s*}', '}', script_content)
            # Обновляем содержимое элемента
            script.string = script_content.strip()
    return soup

def app_remove_external_scripts(soup, my_domain):
    start_time = time.time()
    stop_words = ["google", "gtag", "yandex", "clarity", "datpix", "track", "pixel", ".webmanifest", "widget"]
    # Исключения
    exclude_domains = ['w3.org', 'github', 'docs']
    tracking_patterns = [
        r"google",
        r"analytics",
        r"ga\('create'",
        r"ga\('send'"
    ]
    # tracking_patterns = [
    #     r"google",
    #     r"analytics",
    #     r"new Image\(\d+,\d+\)"  # Создание изображения для отслеживания
    #     r"\.gif",
    #     r"ga\('create'",
    #     r"ga\('send'",
    #     r"track", 
    #     r"cookie", 
    #     r"pixel", 
    #     r"beacon"
    # ]
    tracking_regex = re.compile('|'.join(tracking_patterns), re.IGNORECASE)

    #####################################################################################
    #####################################################################################
    # Удаляем все скрипты !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for script in soup.find_all("script"):
            script.decompose()
    # Находим и удаляем все ссылки на скрипты с расширением ".js"
    for script in soup.find_all("link", href=True):
        if script["href"].endswith(".js"):
            script.decompose()
    #####################################################################################
    #Удаляем скрипты по стоп словам
    for script in soup.find_all("script"):
        # Проверяем на наличие стоп-слов
        if any(word in script.get_text().lower() for word in stop_words):
            script.decompose()
        else:
            # Перебираем все атрибуты элемента
            for attr_name, attr_value in script.attrs.items():
                # Проверяем содержимое атрибута на наличие стоп-слов
                if isinstance(attr_value, str):  # Проверяем, что значение атрибута строка
                    for word in stop_words:
                        if word in attr_value.lower():
                            script.decompose()
                            break
    #####################################################################################
    #####################################################################################
    # Удаление iframe блоков
    for iframe in soup.find_all("iframe"):
        iframe.decompose()
    # Чистим картинки от мусора
    for source in soup.find_all('source'):
        srcset = source.get('srcset')
        if srcset:
            # Удаляем все после символов '@', '?', '#'
            srcset_cleaned = re.sub(r'[@?#].*', '', srcset)
            # Удаляем подстроки из списка ['/rsimages']
            for substring in ['/rsimages']:
                srcset_cleaned = srcset_cleaned.replace(substring, '')
            source['srcset'] = srcset_cleaned
            
    # Перебор всех тегов <script> и анализ их содержимого на Куки и уязвимости
    for script in soup.find_all("script"):
        script_content = script.string or ""
        script_src = script.get("src", "").lower()
        if tracking_regex.search(script_content) or tracking_regex.search(script_src):
            script.decompose()
    
    # Перебор всех тегов <img> и удаление изображений, используемых для отслеживания
    for img in soup.find_all("img"):
        src = img.get("src", "")
        if "1x1" in src or tracking_regex.search(src):
            img.decompose()

    
    soup = remove_ld_json_keys(soup)

    # Поиск строк, содержащих "http" или "https" внутри скриптов и их замена
    # for script in soup.find_all("script"):
    #     script_content = script.string
    #     if script_content:
    #         updated_content = re.sub(r'(https?:[^"\']+)["\']', lambda match: f"https://{my_domain}" if match.group(1).split('/')[2] not in exclude_domains else match.group(0), script_content)
    #         script.string = updated_content

    end_time = time.time()
    print(f"{app_remove_external_scripts.__name__} took {end_time - start_time} seconds to complete.")
    return soup