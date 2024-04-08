import os
import re
# import asyncio
import aiofiles

# Функция для замены ссылок в CSS файлах
# Функция для удаления содержимого блоков с классом содержащим "captionFadeout" и свойством "animation"
async def remove_blocks_with_animation(css_file):
    async with aiofiles.open(css_file, 'r', encoding='utf-8') as f:
        css_content = await f.read()
        # Ищем блоки с классом содержащим "captionFadeout"
        for match in re.finditer(r'\.(?:caption|character)Fadeout[^{]*{([^}]*)}', css_content):
            # Проверяем наличие свойства "animation" в блоке
            if re.search(r'\banimation:[^;]+?linear', match.group(1)):
                # Удаляем содержимое внутри фигурных скобок для найденного блока
                css_content = css_content.replace(match.group(0), f'.captionFadeout {{}}')
    async with aiofiles.open(css_file, 'w', encoding='utf-8') as f:
        await f.write(css_content)

# Функция для перебора всех JavaScript файлов и замены ссылок
async def app_edit__css_vulkan_casino(base_folder):
    if os.path.isdir(base_folder):
        for root, dirs, files in os.walk(base_folder):
            for file in files:
                if file.endswith('.css'):
                    css_file = os.path.join(root, file)
                    await remove_blocks_with_animation(css_file)
    else:
        print(f"Error: {base_folder} is not a directory.")