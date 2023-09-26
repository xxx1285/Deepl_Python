import ssl
import httpx
from httpx import ReadTimeout, RequestError


headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.110 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
}

async def is_url_indexed(domain: str, url_to_check: str, timeout=30) -> str:
    """
    Проверяет, индексируется ли URL на основе правил из файла robots.txt.
    Возвращает 'Indexed', 'Not Indexed', 'Error fetching robots.txt' или 'No User-agent found'.
    """
    robots_url = f"{domain}robots.txt"

    try:
        async with httpx.AsyncClient(verify=False, timeout=timeout) as client:
            response = await client.get(robots_url, headers=headers)

        if response.status_code == 200:
            robots_txt_content = response.text
            
            # Проверяем наличие "User-agent" в тексте
            if "User-agent" not in robots_txt_content:
                return "No User-agent found"

            lines = robots_txt_content.split("\n")
            disallow_rules = []

            for line in lines:
                stripped_line = line.strip()
                if stripped_line.startswith("Disallow:"):
                    rule = stripped_line.split("Disallow:")[1].strip()
                    disallow_rules.append(rule)

            for rule in disallow_rules:
                if rule in url_to_check:
                    return "Not Indexed"

            return "Indexed"

        else:
            return f"Error, status code: {response.status_code}"

    except (ReadTimeout, RequestError, ssl.SSLError):
        return "Request timed out or failed SSL"
