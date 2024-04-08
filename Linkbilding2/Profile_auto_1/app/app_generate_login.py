import random
import string

# Список известных мировых имен
known_names = [
    "john", "jane", "michael", "emma", "oliva",
    "alex", "sophi", "willi", "emil", "dani",
    "charl", "matt", "ameli", "abiga", "jacob",
    "han", "samuel", "grace", "benj", "ava",
    "eliz", "andre", "mia", "david", "madis",
    "luke", "sofi", "christ", "evel", "james"
]

def generate_unique_login():
    base_login = random.choice(known_names)  # Выбираем случайное имя из списка
    suffix_digits = random.randint(1000, 9999)  # Генерируем случайное трехзначное число
    suffix_letter = random.choice(string.ascii_lowercase)  # Генерируем случайную букву

    # Генерация уникального логина
    login = f"{base_login}{suffix_digits}{suffix_letter}"
    return login