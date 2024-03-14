import pyshorteners
from urllib.parse import quote

# Путь к входному файлу с URL
input_file_path = r'Rediki\4-s_uls_create_A_Link_Zamena301Ankora\output\redici-URL-esperancacooesperanca_org.txt'
# Путь к выходному файлу с результатами
output_file_path = r'Linkbilding\SHORT_URL\output\output-redik-esperancacooesperanca_org.txt'

# s = pyshorteners.Shortener()
def read_urls(file_path):
    """Читает список URL-адресов из файла."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def shorten_url(url, service, services):
    """Сокращает URL с использованием указанного сервиса."""
    s = pyshorteners.Shortener()
    try:
        # Кодируем URL для обработки специальных символов
        # encoded_url = quote(url, safe='/:')
        encoded_url = url

        if service == 'bitly':
            s = pyshorteners.Shortener(api_key='0e5bedd2d4a717cb74f61962357c0255a5a9cf3f')
            return s.bitly.short(encoded_url)
        elif service == 'cuttly':
            s = pyshorteners.Shortener(api_key='40d3eb8eda5c622c0b4024479295f4ec06848')
            return s.cuttly.short(encoded_url)
        elif service == 'tinycc':
            s = pyshorteners.Shortener(api_key='bb16f950-8f04-4134-8342-d9a8af5596c1', login='Alex18')
            return s.tinycc.short(encoded_url)
        elif service == 'shortcm':
            s = pyshorteners.Shortener(api_key='sk_0zZi1dy5wWHMljH0')
            return s.shortcm.short(encoded_url)
        elif service == 'nullpointer':
            s = pyshorteners.Shortener()
            resultshorturl = s.nullpointer.short(encoded_url)
            print(f"{service}: {resultshorturl}")
            return resultshorturl
        elif service.lower() in services:
            # Для Bit.ly требуется ваш API ключ
            # s = pyshorteners.Shortener(api_key='ВАШ_API_КЛЮЧ')
            shortener = getattr(s, service.lower())
            resultshorturl = shortener.short(encoded_url)
            print(f"{service}: {resultshorturl}")
            return resultshorturl
        # Добавьте дополнительные условия для других сервисов
        else:
            print(f"Сервис {service} не поддерживается.")
            return None
    except Exception as e:
        print(f"Ошибка при сокращении URL {url} через {service}: {e}")
        return None

def write_urls_to_file(urls, file_path):
    """Записывает список URL-адресов в файл."""
    with open(file_path, 'w') as file:
        for url in urls:
            if url:
                file.write(url + '\n')

def main():
    urls = read_urls(input_file_path)
    shortened_urls = []
    for url in urls:
        services = ['isgd'] # , 'dagd'
        # , 'owly', 'qpsru', 'chilpit', 'clckru', 'nullpointer', 'qpsru', 'shortcm, 'osdb'',---- 'tinyurl', 'tinycc', 'cuttly', 'bitly'
        for service in services:  # Добавьте сюда другие сервисы
            short_url = shorten_url(url, service, services)
            if short_url:
                shortened_urls.append(short_url)
    write_urls_to_file(shortened_urls, output_file_path)

if __name__ == '__main__':
    main()


