import os
from multiprocessing import Pool, Manager

# Глобальные переменные
INPUT_DIRECTORY = 'GSA/Clean_dublicate_URL/input'
OUTPUT_DIRECTORY = 'GSA/Clean_dublicate_URL/output'
CHUNK_SIZE = 500000  # Количество строк для обработки за один раз
PROCESSES = 4  # Количество процессов

def extract_domain(url):
    start = url.find("://") + 3
    end = url.find("/", start)
    if end == -1:
        return url[start:]
    else:
        return url[start:end]

def process_file(file_info, counters):
    input_file_path, output_file_path, duplicates_file_path = file_info
    seen_domains = set()

    output_buffer = []
    duplicates_buffer = []

    with open(input_file_path, 'r', encoding='utf-8', errors='ignore') as input_file:
        for line in input_file:
            url = line.strip()
            domain = extract_domain(url)
            
            if domain not in seen_domains:
                seen_domains.add(domain)
                output_buffer.append(url + '\n')
                # Считаем уникальные домены
                counters['unique_domains'] += 1
            else:
                duplicates_buffer.append(url + '\n')
                # Считаем дубликаты только если это первый дубликат данного домена
                if domain not in counters['duplicate_domains']:
                    counters['duplicate_domains'].add(domain)

            # При достижении CHUNK_SIZE, записываем данные из буфера
            if len(output_buffer) >= CHUNK_SIZE:
                with open(output_file_path, 'a', encoding='utf-8') as output_file:
                    output_file.writelines(output_buffer)
                    output_buffer.clear()

            if len(duplicates_buffer) >= CHUNK_SIZE:
                with open(duplicates_file_path, 'a', encoding='utf-8') as duplicates_file:
                    duplicates_file.writelines(duplicates_buffer)
                    duplicates_buffer.clear()

        # Записываем оставшиеся данные из буфера после завершения чтения файла
        if output_buffer:
            with open(output_file_path, 'a', encoding='utf-8') as output_file:
                output_file.writelines(output_buffer)
        
        if duplicates_buffer:
            with open(duplicates_file_path, 'a', encoding='utf-8') as duplicates_file:
                duplicates_file.writelines(duplicates_buffer)

def process_files():
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.makedirs(OUTPUT_DIRECTORY)

    files_to_process = []
    for filename in os.listdir(INPUT_DIRECTORY):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(INPUT_DIRECTORY, filename)
            output_filename = f"{filename}"
            duplicates_filename = f"duplicates21_{filename}"
            output_file_path = os.path.join(OUTPUT_DIRECTORY, output_filename)
            duplicates_file_path = os.path.join(OUTPUT_DIRECTORY, duplicates_filename)
            files_to_process.append((input_file_path, output_file_path, duplicates_file_path))

    with Manager() as manager:
        counters = manager.dict({'unique_domains': 0, 'duplicate_domains': manager.list()})
        with Pool(PROCESSES) as pool:
            pool.starmap(process_file, [(file_info, counters) for file_info in files_to_process])

        # Выводим итоговые счетчики
        print(f"Всего уникальных доменов: {counters['unique_domains']}")
        print(f"Всего доменов-дубликатов: {len(counters['duplicate_domains'])}")

if __name__ == "__main__":
    process_files()
