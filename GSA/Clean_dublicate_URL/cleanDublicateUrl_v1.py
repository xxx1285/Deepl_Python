import os

def extract_domain(url):
    start = url.find("://") + 3
    end = url.find("/", start)
    if end == -1:
        return url[start:]
    else:
        return url[start:end]

def process_file_chunk(input_file, seen_domains, output_file):
    for line in input_file:
        url = line.strip()
        domain = extract_domain(url)
        
        if domain not in seen_domains:
            seen_domains.add(domain)
            output_file.write(url + '\n')

def process_files(input_dir, output_dir, chunk_size=500000):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as input_file:
                output_filename = f"processed2_{filename}"
                with open(os.path.join(output_dir, output_filename), 'w', encoding='utf-8') as output_file:
                    seen_domains = set()
                    lines_processed = 0
                    
                    while True:
                        # Читаем часть файла
                        lines = [next(input_file) for _ in range(chunk_size)]
                        if not lines:
                            break  # Прекращаем обработку, если достигнут конец файла
                        
                        process_file_chunk(lines, seen_domains, output_file)
                        lines_processed += len(lines)
                        print(f"Processed {lines_processed} lines from {filename}")

                        if len(lines) < chunk_size:
                            break  # Конец файла

# Укажите путь к директории с исходными файлами и путь к директории для сохранения результатов
process_files(r'GSA\Clean_dublicate_URL\input', r'GSA\Clean_dublicate_URL\output')
