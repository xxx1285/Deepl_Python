import os
import re
# import asyncio
import aiofiles

exclusions = ['w3.org', 'w2.org']

# Функция для замены ссылок в JavaScript файлах
async def replace_links_in_js(js_file, my_domain):
    async with aiofiles.open(js_file, 'r', encoding='utf-8') as f:
        js_content = await f.read()
        # Находим все ссылки в кавычках
        matches = re.findall(r'(["\'])(https?:\/\/.*?)\1', js_content)
        for match in matches:
            # Проверяем, содержится ли ссылка в списке исключений
            if not any(exclusion in match[1] for exclusion in exclusions):
                # Производим замену
                js_content = js_content.replace(match[1], f"https://{my_domain}")
        # Записываем обновленное содержимое обратно в файл
    async with aiofiles.open(js_file, 'w', encoding='utf-8') as f:
        await f.write(js_content)

# Функция для перебора всех JavaScript файлов и замены ссылок
async def app_edit__js_files(base_folder, my_domain):
    if os.path.isdir(base_folder):
        for root, dirs, files in os.walk(base_folder):
            for file in files:
                if file.endswith('.js'):
                    js_file = os.path.join(root, file)
                    await replace_links_in_js(js_file, my_domain)
    else:
        print(f"Error: {base_folder} is not a directory.")