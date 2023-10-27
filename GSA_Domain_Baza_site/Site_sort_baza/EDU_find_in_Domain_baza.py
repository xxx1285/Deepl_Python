def process_file(input_path, output_path):
    buffer = []  # буфер для хранения строк
    buffer_size = 10000  # увеличим размер буфера

    with open(input_path, 'r') as f:
        for line in f:
            if ".hr" in line:
                buffer.append(line)
                if len(buffer) >= buffer_size:
                    with open(output_path, 'a') as out:
                        out.writelines(buffer)
                    print(line + " +10000")
                    buffer.clear()
    # Записываем оставшиеся строки в буфере
    if buffer:
        with open(output_path, 'a') as out:
            out.writelines(buffer)

def main():
    process_file(r'GSA_Domain_Baza_site\Site_sort_baza\csv_baza\domains.txt', r'GSA_Domain_Baza_site\Site_sort_baza\output\output_hr_Horvatiya.txt')

if __name__ == "__main__":
    main()
