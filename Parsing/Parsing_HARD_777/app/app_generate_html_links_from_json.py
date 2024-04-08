import json

def generate_html_links_from_json(json_file):
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