import os
from multiprocessing import Pool

# Глобальные переменные
INPUT_DIRECTORY = 'GSA/Clean_dublicate_URL/input'
OUTPUT_DIRECTORY = 'GSA/Clean_dublicate_URL/output'
CHUNK_SIZE = 500000  # Количество строк для обработки за один раз
PROCESSES = 4  # Количество процессов

def clean_line(line):
    colon_pos = line.find(": ")
    if colon_pos != -1:
        return line[:colon_pos] + '\n'
    else:
        return line

def process_file(file_info):
    input_file_path, output_file_path = file_info

    output_buffer = []

    with open(input_file_path, 'r', encoding='utf-8', errors='ignore') as input_file:
        for line in input_file:
            cleaned_line = clean_line(line)
            output_buffer.append(cleaned_line)

            # При достижении CHUNK_SIZE, записываем данные из буфера
            if len(output_buffer) >= CHUNK_SIZE:
                with open(output_file_path, 'a', encoding='utf-8') as output_file:
                    output_file.writelines(output_buffer)
                    output_buffer.clear()

        # Записываем оставшиеся данные из буфера после завершения чтения файла
        if output_buffer:
            with open(output_file_path, 'a', encoding='utf-8') as output_file:
                output_file.writelines(output_buffer)

def process_files():
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.makedirs(OUTPUT_DIRECTORY)

    files_to_process = []
    for filename in os.listdir(INPUT_DIRECTORY):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(INPUT_DIRECTORY, filename)
            output_filename = f"cleaned_{filename}"
            output_file_path = os.path.join(OUTPUT_DIRECTORY, output_filename)
            files_to_process.append((input_file_path, output_file_path))

    with Pool(PROCESSES) as pool:
        pool.map(process_file, files_to_process)

if __name__ == "__main__":
    process_files()
