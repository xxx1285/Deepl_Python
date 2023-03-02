
import json


# функція що очищає або добавляє екранування
def my_clean_string(string, escape=True):
    if escape:
        # Замінюємо спеціальні символи на їх екрановані еквіваленти
        string = string.replace('/', '\/')
        string = string.replace('\n', '\\n')
        string = string.replace('\t', '\\t')
    else:
        # Видаляємо екранування спеціальних символів
        string = string.replace('\\', '')
        string = string.replace('\n', '')
        string = string.replace('\t', '')
    return string

def escape_and_unescape_string(s):
    """
    Функція приймає рядок s і екранує всі небезпечні символи у рядку s.
    Потім вона повертає екранований рядок.
    """
    escaped_string = s.encode('unicode_escape').decode()
    return escaped_string

def remove_escape_characters(s):
    """
    Функція приймає рядок s і видаляє всі екранування символів у рядку s.
    Потім вона повертає виправлений рядок.
    """
    unescaped_string = bytes(s, "utf-8").decode("unicode_escape")
    return unescaped_string

# !!!!!!!!!!!! Екрануємо рядок JSON:
def escape_json_string(s):
    """
    Функція приймає рядок s, екранує всі спеціальні символи, які можуть викликати помилки при
    спробі десеріалізації в формат JSON, і повертає екранований рядок.
    """
    return json.dumps(s).replace('/', r'\/')

def unescape_json_string(s):
    """
    Функція приймає екранований рядок s, знімає екранування всіх спеціальних символів,
    і повертає рядок у вигляді неекранованого рядка JSON.
    """
    return json.loads(s.replace(r'\/', '/'))
