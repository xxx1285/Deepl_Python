import os
import logging
from datetime import datetime

def create_logger(name):
    """
    Создает и возвращает логгер с заданным именем.

    :param name: Имя логгера.
    :return: Объект логгера.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Создание обработчика, который записывает логи в файл
    filename = f'logs/{name}_{datetime.now().strftime("%Y-%m-%d")}.log'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    file_handler = logging.FileHandler(filename)

    # Создание форматтера и добавление его в обработчик
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Добавление обработчика к логгеру
    logger.addHandler(file_handler)

    return logger

def read_file(file_path):
    """
    Читает содержимое файла и возвращает его.

    :param file_path: Путь к файлу.
    :return: Содержимое файла.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except IOError:
        print(f"Ошибка при чтении файла: {file_path}")
        return None

# Здесь можно добавить другие вспомогательные функции по мере необходимости
