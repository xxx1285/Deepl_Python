import os
import gzip
import re
import pandas as pd

# Регулярное выражение для парсинга строк лога
# log_pattern = re.compile(
#     r'(?P<ip>\d+\.\d+\.\d+\.\d+)\s+-\s+-\s+'
#     r'\[(?P<date>.+?)\]\s+'
#     r'"(?P<request_method>[A-Z]+)\s+(?P<request_path>[^"]*?)\s+HTTP/\d\.\d"\s+'
#     r'(?P<status>\d{3})\s+'
#     r'(?P<bytes_sent>\d+)\s+'
#     r'"(?P<referer>[^"]*?)"\s+'
#     r'"(?P<user_agent>[^"]*?)"'
# )
log_pattern = re.compile(
    r'(?P<ip>\S+) ' # IP адрес
    r'\S+ \S+ ' # Идентификатор и ID пользователя (не используем, поэтому \S+)
    r'\[(?P<date>.+)\] ' # Дата и время
    r'"(?P<request_method>\S+) ' # Метод запроса
    r'(?P<request_path>[^\"]+) ' # Путь запроса
    r'(?P<http_version>\S+)" ' # Версия HTTP
    r'(?P<response_code>\S+) ' # Код ответа
    r'(?P<response_size>\S+) ' # Размер ответа
    r'"(?P<referrer>[^\"]*)" ' # Referrer
    r'"(?P<user_agent>[^\"]*)"' # User agent
)

def parse_log_line(line):
    match = log_pattern.match(line)
    if match:
        return match.groupdict()
    else:
        return None

def preprocess_log_files(logs_directory, output_csv):
    # Список для хранения данных из всех файлов логов
    logs_data = []
    
    # Считываем первые 1000 файлов .gz из директории
    gz_files = [f for f in os.listdir(logs_directory) if f.endswith('.gz')]
    for gz_file in gz_files[:1000]:
        gz_file_path = os.path.join(logs_directory, gz_file)
        
        # Открываем и читаем содержимое архива
        with gzip.open(gz_file_path, 'rt') as f:
            # Для каждой строки в файле
            for line in f:
                parsed_line = parse_log_line(line)
                if parsed_line:
                    logs_data.append(parsed_line)
    
    # Создаем DataFrame из собранных данных
    logs_df = pd.DataFrame(logs_data)
    
    # Преобразуем и сохраняем DataFrame в CSV файл для дальнейшего использования
    logs_df.to_csv(output_csv, index=False, header=True)

# Путь к директории с логами
logs_directory = r'ANALITICA\Analit_site_LOGS\input\gatesofolympus_club'
# Путь к выходному CSV файлу
output_csv = r'ANALITICA\Analit_site_LOGS\output\logs2.csv'

# Вызов функции
preprocess_log_files(logs_directory, output_csv)
