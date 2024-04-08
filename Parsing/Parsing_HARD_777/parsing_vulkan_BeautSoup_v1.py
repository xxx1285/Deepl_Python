import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Функция для сохранения файлов
def save_file(url, base_folder, headers):
    # Извлекаем путь из URL и очищаем его от параметров запроса
    url_path = urlparse(url).path
    url_path = url_path.split('?')[0]
    if not url_path or os.path.basename(url_path) == '':
        # Если в URL нет имени файла, пропускаем его
        return None
    # Создаем полный путь к файлу, сохраняя структуру папок
    filepath = os.path.join(base_folder, url_path.lstrip('/'))
    # Создаем все подпапки в пути, если они еще не существуют
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    # Сохраняем файл
    with open(filepath, 'wb') as f:
        response = requests.get(url, headers=headers)
        f.write(response.content)
    return filepath

# Функция для загрузки ресурсов
def download_assets(url, user_agent, base_folder):
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Создаем папку для сохранения файлов, если она не существует
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)

    # Сохраняем ресурсы
    for tag in soup.find_all(['link', 'script', 'img', 'source']):
        resource_url = tag.get('href') or tag.get('src') or tag.get('srcset')
        if resource_url:
            # Игнорируем внешние URL
            if resource_url.startswith('http') and not resource_url.startswith(url):
                continue
            saved_path = save_file(urljoin(url, resource_url), base_folder, headers)
            if saved_path:  # Проверяем, что файл был сохранен
                # Обновляем атрибуты тегов, чтобы указывать на локальные файлы
                # new_path = os.path.relpath(saved_path, base_folder).replace('\\', '/')
                new_path = os.path.abspath(saved_path).replace('\\', '/')
                if tag.name == 'link':
                    tag['href'] = new_path
                elif tag.name == 'script':
                    tag['src'] = new_path
                elif tag.name == 'img':
                    tag['src'] = new_path
                elif tag.name == 'source':
                    tag['srcset'] = new_path

    # Сохраняем обновленный HTML-файл с измененными путями к ресурсам
    with open(os.path.join(base_folder, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == "__main__":
    url = "https://casino-vulkan24.top/"
    user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15Z (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1 (Applebot/0.1)"
    base_folder = r"Parsing\Parsing_site_Vulkan\klon_vulkan"  # Исправлено здесь
    download_assets(url, user_agent, base_folder)
