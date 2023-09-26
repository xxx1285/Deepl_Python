import ssl
import httpx
import random
from httpx import ReadTimeout, RequestError, InvalidURL

configurations = [
    # {
    #     "headers": {
    #         "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.110 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    #         "Accept-Encoding": "gzip, deflate",
    #         "Connection": "keep-alive"
    #     }
    # },
    {
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            # "Referer": "https://m.facebook.com/watch/",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive"
        }
    },
    # {
    #     "headers": {
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    #         "From": "https://m.facebook.com/watch/",
    #         "Accept-Encoding": "gzip, deflate",
    #         "Connection": "keep-alive"
    #     }
    # }
]


def parse_robots_txt_content(content):
    blocks = []
    current_block = []
    target_blocks = []

    lines = content.split("\n")
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            # Игнорируем пустые директивы Disallow и Allow
            if not (stripped_line.startswith("Disallow:") and stripped_line.split("Disallow:")[1].strip() == ''):
                if not (stripped_line.startswith("Allow:") and stripped_line.split("Allow:")[1].strip() == ''):
                    current_block.append(stripped_line)
        else:
            if current_block:
                blocks.append(current_block)
                current_block = []

    if current_block:
        blocks.append(current_block)

    for block in blocks:
        first_line = block[0]
        if first_line.startswith("User-agent:"):
            agent = first_line.split("User-agent:")[1].strip()
            if agent in ["*", "Googlebot"]:
                target_blocks.append(block)

    return target_blocks


async def is_url_indexed(domain: str, url_to_check: str, timeout=30) -> str:
    robots_url = f"{domain}robots.txt"
    headers = random.choice(configurations)["headers"]

    try:
        async with httpx.AsyncClient(verify=False, timeout=timeout) as client:
            response = await client.get(robots_url, headers=headers)

        if response.status_code == 200:
            robots_txt_content = response.text

            if "User-agent" not in robots_txt_content:
                return "No User-agent found"

            target_blocks = parse_robots_txt_content(robots_txt_content)

            googlebot_allows_all = False
            disallow_rules = []
            allow_rules = []

            for block in target_blocks:
                is_googlebot_block = block[0].split("User-agent:")[1].strip() == "Googlebot"
                for line in block[1:]:
                    if line.startswith("Allow:") and is_googlebot_block:
                        rule = line.split("Allow:")[1].strip()
                        if rule == "/":
                            googlebot_allows_all = True
                            break
                        if rule:  # only non-empty rules
                            allow_rules.append(rule)
                    elif line.startswith("Disallow:"):
                        rule = line.split("Disallow:")[1].strip()
                        if rule:  # only non-empty rules
                            disallow_rules.append(rule)

                if googlebot_allows_all:
                    break

            if googlebot_allows_all:
                return "Indexed"

            # Implement a more precise rule matching here.
            for rule in disallow_rules:
                if url_to_check.startswith(rule):
                    return "Not Indexed"

            for rule in allow_rules:
                if url_to_check.startswith(rule):
                    return "Indexed"

            return "Indexed"

        else:
            return f"Error, status code: {response.status_code}"

    except (ReadTimeout, RequestError, ssl.SSLError, InvalidURL) as e:
        if isinstance(e, InvalidURL):
            return "Invalid URL"
        return "Request timed out or failed SSL"