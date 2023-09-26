import ssl
import httpx
from httpx import ReadTimeout, RequestError, InvalidURL

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.110 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
}


def parse_robots_txt_content(content):
    blocks = []  # Список для хранения всех блоков правил
    current_block = []  # Список для хранения текущего блока правил
    target_blocks = []  # Список для хранения целевых блоков правил (с интересующими нас User-agent)

    lines = content.split("\n")  # Разбиваем содержимое файла на строки по символу переноса строки

    # Разделение на блоки
    for line in lines:
        stripped_line = line.strip()  # Удаляем пробельные символы с обеих сторон строки
        if stripped_line:  # Если строка не пустая
            current_block.append(stripped_line)  # Добавляем строку в текущий блок
        else:
            if current_block:  # Если текущий блок не пуст
                blocks.append(current_block)  # Добавляем текущий блок в список всех блоков
                current_block = []  # Очищаем текущий блок для следующего набора правил

    # Добавляем последний блок, если он не пуст
    if current_block:
        blocks.append(current_block)

    # Поиск интересующих блоков
    for block in blocks:
        first_line = block[0]  # Получаем первую строку текущего блока
        if first_line.startswith("User-agent:"):  # Проверяем, начинается ли строка с "User-agent:"
            agent = first_line.split("User-agent:")[1].strip()  # Извлекаем имя User-agent
            if agent == "*" or agent == "Googlebot":  # Если имя User-agent интересует нас
                # Добавляем блок в список целевых блоков
                target_blocks.append([line for line in block if not (line.startswith("Disallow:") and line.split("Disallow:")[1].strip() == '')])


    return target_blocks  # Возвращаем список целевых блоков


async def is_url_indexed(domain: str, url_to_check: str, timeout=30) -> str:
    robots_url = f"{domain}robots.txt"

    try:
        async with httpx.AsyncClient(verify=False, timeout=timeout) as client:
            response = await client.get(robots_url, headers=headers)

        if response.status_code == 200:
            robots_txt_content = response.text

            if "User-agent" not in robots_txt_content:
                return "No User-agent found"

            target_blocks = parse_robots_txt_content(robots_txt_content)

            disallow_rules = []
            for block in target_blocks:
                for line in block:
                    if line.startswith("Disallow:"):
                        rule = line.split("Disallow:")[1].strip()
                        disallow_rules.append(rule)

            for rule in disallow_rules:
                if rule == '':
                    continue  # Пропускаем пустые правила
                if rule in url_to_check:
                    return "Not Indexed"

            return "Indexed"

        else:
            return f"Error, status code: {response.status_code}"

    except (ReadTimeout, RequestError, ssl.SSLError, InvalidURL) as e:
        if isinstance(e, InvalidURL):
            return "Invalid URL"
        return "Request timed out or failed SSL"
