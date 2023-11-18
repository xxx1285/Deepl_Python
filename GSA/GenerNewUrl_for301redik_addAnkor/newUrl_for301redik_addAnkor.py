
# https://gatesofolympus.club/el/#{Gates of Olympus| υποδοχή Pragmatic| Βυθιστείτε στον μαγευτικό}

import random
import string

# Функция для генерации случайной строки из букв и цифр
def generate_random_string(length=4):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

# Количество строк, которые вы хотите записать
num_lines = 50

with open(r'GSA\GenerNewUrl_for301redik_addAnkor\output\output.txt', 'w') as file:
    for _ in range(num_lines):
        no_index = 'dd'
        random_part_start = generate_random_string()
        random_part_end = generate_random_string()
        # line = f"https://gatesofolympus.club/el/{no_index}{random_part_start}red4el-1{random_part_end}/\n"
        # line = f"https://aviator--game.com/tr/{no_index}{random_part_start}red4tr-1{random_part_end}/\n"
        line = f"https://the-dog-house.org/ru/{no_index}{random_part_start}red4ru-1{random_part_end}/\n"

        file.write(line)
