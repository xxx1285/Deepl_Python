def wrap_urls_in_a_tags(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
        for line in infile:
            url = line.strip()  # Видаляємо зайві пробіли та символи переносу рядка
            if url:  # Переконуємося, що рядок не є пустим
                # Створюємо HTML-тег <a>
                short_name = url[:30]
                # Замінюємо "777.com" на "888.com" у URL
                modified_url = url.replace("777.com", "esperancacooesperanca.org")
                # modified_url = modified_url.replace("://1", "%3A%2F%2F1")
                # modified_url = modified_url.replace("store/", "store%2F")
                # a_tag = f'<a href="{modified_url}">1win-officialsite.store</a>\n'
                a_tag = f"{modified_url}\n"
                outfile.write(a_tag)  # Записуємо тег <a> у вихідний файл

if __name__ == "__main__":
    input_filename = r'Rediki\3-FiltrRediki_naKod200\output\redici-3-res-Good.txt'
    output_filename = r'Rediki\4-s_uls_create_A_Link_Zamena301Ankora\output\redici-URL-esperancacooesperanca_org.txt'

    wrap_urls_in_a_tags(input_filename, output_filename)
