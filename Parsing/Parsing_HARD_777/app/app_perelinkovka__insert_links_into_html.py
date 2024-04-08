from bs4 import BeautifulSoup
import json

def generate_html_links_from_json(json_file):
    # Генерируем HTML блок ссылок - перелинковка между сайтами
    html_links = ""
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for url, title in data.items():
                # Если URL начинается с "http", вырезаем до трех слешей
                if url.startswith("http"):
                    url = url.split("/", 3)[-1]
                html_links += f'<a class="my-link" href="{url}" title="{title}">{title}</a>\n'
    except Exception as e:
        print(f"Error generating HTML links from JSON file: {e}")
    return html_links

def perelinkovka__insert_links_into_html(soup, json_file):
    try:
        # Находим последний блок <p> с текстом
        last_paragraphs = soup.find_all('p')
        if last_paragraphs:
            last_paragraph = last_paragraphs[-1]
            # Создаем новый блок <p> с содержимым ссылок
            new_paragraph = soup.new_tag('p')

            new_paragraph.append(BeautifulSoup(generate_html_links_from_json(json_file), 'html.parser'))
            # Вставляем новый блок <p> после последнего блока <p>
            last_paragraph.insert_after(new_paragraph)
        else:
            # Если блоков <p> нет, вставляем новый блок перед закрывающим </body>
            last_paragraph = soup.body

            # Создаем новый блок <p> для вставки ссылок
            new_paragraph = soup.new_tag('p')
            # Вставляем HTML с ссылками в новый блок <p>
            new_paragraph.append(BeautifulSoup(generate_html_links_from_json(json_file), 'html.parser'))
            # Добавляем новый блок <p> перед закрывающим </body>
            last_paragraph.insert_before(new_paragraph)
    except Exception as e:
        print(f"Error inserting links into HTML content: {e}")

    # Возвращаем модифицированный объект soup
    return soup