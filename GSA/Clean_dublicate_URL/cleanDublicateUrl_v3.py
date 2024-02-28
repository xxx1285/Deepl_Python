import os

# Глобальные переменные
INPUT_DIRECTORY = r'GSA\Clean_dublicate_URL\input'
OUTPUT_DIRECTORY = r'GSA\Clean_dublicate_URL\output'
CHUNK_SIZE = 500000  # Количество строк для обработки за один раз

def extract_domain(url):
    start = url.find("://") + 3
    end = url.find("/", start)
    if end == -1:
        return url[start:]
    else:
        return url[start:end]

def process_file(input_file_path, output_file_path, duplicates_file_path):
    seen_domains = set()

    with open(input_file_path, 'r', encoding='utf-8', errors='ignore') as input_file:
        with open(output_file_path, 'w', encoding='utf-8') as output_file, \
             open(duplicates_file_path, 'w', encoding='utf-8') as duplicates_file:
            while True:
                lines = [input_file.readline() for _ in range(CHUNK_SIZE)]
                lines = [line for line in lines if line]  # Remove empty strings
                if not lines:
                    break

                for line in lines:
                    url = line.strip()
                    domain = extract_domain(url)
                    
                    if domain not in seen_domains:
                        seen_domains.add(domain)
                        output_file.write(url + '\n')
                    else:
                        duplicates_file.write(url + '\n')

def process_files():
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.makedirs(OUTPUT_DIRECTORY)

    for filename in os.listdir(INPUT_DIRECTORY):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(INPUT_DIRECTORY, filename)
            output_filename = f"processed5_{filename}"
            duplicates_filename = f"duplicates1_{filename}"
            output_file_path = os.path.join(OUTPUT_DIRECTORY, output_filename)
            duplicates_file_path = os.path.join(OUTPUT_DIRECTORY, duplicates_filename)
            process_file(input_file_path, output_file_path, duplicates_file_path)

if __name__ == "__main__":
    process_files()

# 12-35