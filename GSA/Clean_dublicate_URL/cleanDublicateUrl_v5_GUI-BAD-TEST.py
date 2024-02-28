import tkinter as tk
from tkinter import filedialog, messagebox
import os
from concurrent.futures import ProcessPoolExecutor, as_completed
import itertools

CHUNK_SIZE = 500000  # Количество строк для обработки за один раз
PROCESSES = 4  # Количество процессов

def extract_domain(url):
    start = url.find("://") + 3
    end = url.find("/", start)
    return url[start:end] if end != -1 else url[start:]

def process_chunk(chunk_data):
    chunk, output_file_path, duplicates_file_path = chunk_data
    seen_domains = set()
    output_buffer = []
    duplicates_buffer = []
    for url in chunk:
        domain = extract_domain(url.strip())
        if domain:
            if domain not in seen_domains:
                seen_domains.add(domain)
                output_buffer.append(url)
            else:
                duplicates_buffer.append(url)
    with open(output_file_path, 'a', encoding='utf-8') as output_file:
        output_file.writelines(output_buffer)
    with open(duplicates_file_path, 'a', encoding='utf-8') as duplicates_file:
        duplicates_file.writelines(duplicates_buffer)
    return f"Processed chunk with {len(chunk)} lines"

def process_file(file_info):
    input_file_path, output_file_path, duplicates_file_path = file_info

    # Очистка выходных файлов
    open(output_file_path, 'w').close()
    open(duplicates_file_path, 'w').close()

    chunks = []
    with open(input_file_path, 'r', encoding='utf-8', errors='ignore') as input_file:
        while True:
            lines = list(itertools.islice(input_file, CHUNK_SIZE))
            if not lines:
                break
            chunks.append((lines, output_file_path, duplicates_file_path))
    return chunks

def select_input_directory():
    directory = filedialog.askdirectory()
    if directory:
        input_dir.set(directory)

def select_output_directory():
    directory = filedialog.askdirectory()
    if directory:
        output_dir.set(directory)

def start_processing():
    input_directory = input_dir.get()
    output_directory = output_dir.get()

    if not input_directory or not output_directory:
        messagebox.showwarning("Warning", "Please select both input and output directories.")
        return

    start_button['state'] = 'disabled'

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    files_to_process = [
        (
            os.path.join(input_directory, filename),
            os.path.join(output_directory, f"processed_{filename}"),
            os.path.join(output_directory, f"duplicates_{filename}")
        )
        for filename in os.listdir(input_directory) if filename.endswith(".txt")
    ]

    chunks_to_process = []
    for file_info in files_to_process:
        chunks_to_process.extend(process_file(file_info))

    with ProcessPoolExecutor(max_workers=PROCESSES) as executor:
        future_to_chunk = {executor.submit(process_chunk, chunk): chunk for chunk in chunks_to_process}
        for future in as_completed(future_to_chunk):
            chunk = future_to_chunk[future]
            try:
                result = future.result()
                print(result)  # Вывод статуса выполнения в консоль
            except Exception as exc:
                print(f"Chunk generated an exception: {exc}")

    messagebox.showinfo("Info", "Processing completed successfully!")
    start_button['state'] = 'normal'

# GUI Initialization
root = tk.Tk()
root.title("File Processor")
root.geometry("400x200")

input_dir = tk.StringVar()
output_dir = tk.StringVar()

tk.Label(root, text="Input Directory:").pack()
tk.Entry(root, textvariable=input_dir).pack()
tk.Button(root, text="Select", command=select_input_directory).pack()

tk.Label(root, text="Output Directory:").pack()
tk.Entry(root, textvariable=output_dir).pack()
tk.Button(root, text="Select", command=select_output_directory).pack()

start_button = tk.Button(root, text="Start Processing", command=start_processing)
start_button.pack(pady=10)

root.mainloop()
