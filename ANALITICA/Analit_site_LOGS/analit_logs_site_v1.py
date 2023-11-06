import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import re

# Функция для парсинга строки лога
def parse_log_line(line):
    match = re.match(r'(\S+) - - \[(.*?)\] "(\S+) (\S+).*" (\d{3}) (\d+) ".*" "(.*)"', line)
    if match:
        return {
            'ip': match.group(1),
            'date': datetime.strptime(match.group(2), '%d/%b/%Y'),
            'method': match.group(3),
            'path': match.group(4),
            'status': int(match.group(5)),
            'size': int(match.group(6)),
            'user_agent': match.group(7)
        }

# Чтение и парсинг файла
with open('logs.txt', 'r') as file:
    logs = [parse_log_line(line) for line in file if parse_log_line(line)]

# Преобразование в DataFrame
df_logs = pd.DataFrame(logs)

# Агрегация и визуализация данных
plt.figure(figsize=(10,5))
sns.countplot(data=df_logs, x='status')
plt.title('HTTP Status Codes Frequency')
plt.show()
