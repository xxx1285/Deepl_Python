import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import csv


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36\
           (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
          }

# Загружает содержимое веб-страницы по номеру
def get_page_content(page_number):
    # TODO: Указать сайт
    url = f"http://www.zhygg.com/domain-list-{page_number}"
    response = requests.get(f'{url}', headers=headers)
    return response.text

# Возвращает код состояния HTTP для заданного URL
def get_status_code(url):
    try:
        response = requests.head(url, headers=headers, timeout=5)
        return response.status_code
    except RequestException as e:
        return e
    # except requests.exceptions.RequestException:
    #     return "Error"

# Проверяет наличие CMS в содержимом заданного URL
def check_cms(url):
    cms_list = ["Modx", "Joomla"]
    try:
        response = requests.get(url, timeout=5)
        for cms in cms_list:
            if cms.lower() in response.text.lower():
                return cms
        return ""
    except requests.exceptions.RequestException:
        return ""

# Парсит содержимое страницы и извлекает данные о сайтах
def parse_page(content):
    soup = BeautifulSoup(content, "html.parser")
    tbody = soup.find("tbody")
    rows = tbody.find_all("tr")

    data = []
    for row in rows:
        if row.find("td") and row.td.text.startswith("#"):
            rank = row.td.text[1:]
            website_url = row.td.find_next("td").a["href"]
            kod_200 = get_status_code(website_url)
            cms = check_cms(website_url)
            data.append((rank, website_url, kod_200, cms))

    return data

# Сохраняет данные в файл CSV
def save_to_csv(data, filename):
    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Rank", "Website URL", "Kod 200", "CMS"])
        for row in data:
            writer.writerow(row)

# Основная функция, которая выполняет всю работу
def main():
    page_number = 1
    all_data = []

    while True:
        print(f"Processing page {page_number}...")
        content = get_page_content(page_number)
        data = parse_page(content)
        all_data.extend(data)

        # Проверяет наличие ссылки на следующую страницу
        soup = BeautifulSoup(content, "html.parser")
        tbody = soup.find("tbody")
        next_link = tbody.find("a", href=f"/domain-list-{page_number + 1}")

        if not next_link:
            break

        page_number += 1

    save_to_csv(all_data, "output.csv")
    print("Done!")

if __name__ == "__main__":
    main()
