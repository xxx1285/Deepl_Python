import re

def extract_urls_from_file(input_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Разделяем текст на потенциальные URL
    potential_urls = re.split(r'\s+', text)

    # Отфильтровываем потенциальные URL, оставляя только валидные
    valid_urls = [url for url in potential_urls if re.match(r'https?://\S+', url)]

    return valid_urls

def save_to_file(urls, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        for url in urls:
            file.write(url + "\n")

if __name__ == "__main__":
    input_path = r"Linkbilding\Google_tables_URL_chistim\input\source.txt"
    output_path = r"Linkbilding\Google_tables_URL_chistim\output\urls.txt"

    urls = extract_urls_from_file(input_path)
    save_to_file(urls, output_path)
