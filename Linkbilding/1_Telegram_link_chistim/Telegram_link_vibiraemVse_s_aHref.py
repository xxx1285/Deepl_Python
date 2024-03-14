import re

def extract_urls(text):
    # Regular expression to find URLs within href attributes of anchor tags
    url_pattern = re.compile(r'<a href="(http[^\s"]+)"')

    # Find all URLs in the text
    urls = url_pattern.findall(text)

    urls = [url for url in urls if len(url) > 35]

    return urls

def save_to_txt(urls, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for url in urls:
            file.write(url + '\n')

def read_from_txt(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

if __name__ == "__main__":
    input_filename = r'Linkbilding\1_Telegram_link_chistim\input\text_and_telegramText.txt'  
    output_filename = r'Linkbilding\1_Telegram_link_chistim\output\redici-2.txt'  

    text = read_from_txt(input_filename)

    urls = extract_urls(text)
    save_to_txt(urls, output_filename)
