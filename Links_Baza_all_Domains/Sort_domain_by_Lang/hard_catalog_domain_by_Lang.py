# Імпортуються потрібні бібліотеки:
import os  # для взаємодії з операційною системою
import asyncio  # для асинхронного програмування
import httpx  # для асинхронних HTTP запитів
from bs4 import BeautifulSoup  # для парсингу HTML
from langdetect import detect  # для виявлення мови тексту
import langid
import aiofiles  # для асинхронної роботи з файлами


# Створюємо семафор, що обмежує асинхронність до 5
semaphore = asyncio.Semaphore(5)

# Асинхронна функція, яка отримує URL, робить HTTP запит до цього URL, а потім аналізує відповідь на предмет мови
async def fetch_and_detect_language(url):
    async with semaphore:
        try:
            # Створюємо асинхронного клієнта для HTTP запитів
            async with httpx.AsyncClient(timeout=10.0) as client:
                r = await client.get(url)  # Виконуємо GET запит до URL
                # Парсимо HTML відповідь за допомогою BeautifulSoup
                soup = BeautifulSoup(r.text, 'lxml')
                # Знаходимо `title` та витягуємо перші 150 символів тексту сторінки.
                title = soup.find('title').text if soup.find('title') else ""
                text = soup.text[:150] if soup.text else ""
                combined_text = " ".join([title, text])

                # Визначаємо мову за допомогою langdetect.
                lang, _ = langid.classify(combined_text)
                print(lang)

                # lang = detect(title_text)
                return url, lang  # повертаємо URL та виявлену мову
        except Exception:  # Якщо щось пішло не так, повертаємо URL і "error" як мову
            return url, "error"

# Асинхронна функція для обробки файлу з URL
async def process_file(filepath, output_dir):
    # Відкриваємо файл для читання
    with open(filepath, 'r') as file:
        urls = file.read().splitlines()  # читаємо URL з файлу

    tasks = []  # список для зберігання майбутніх завдань
    for url in urls:
        tasks.append(fetch_and_detect_language(url))  # Додаємо завдання для кожного URL
    # Виконуємо всі завдання асинхронно та збираємо результати
    responses = await asyncio.gather(*tasks, return_exceptions=True)

    for response in responses:  # обробляємо кожну відповідь
        url, lang = response
        # Створюємо шлях до вихідного файлу для кожної мови
        output_file = os.path.join(output_dir, f"{lang}.txt")
        async with aiofiles.open(output_file, 'a') as f:  # відкриваємо файл для запису (або додавання, якщо файл уже існує)
            await f.write(url + '\n')  # записуємо URL у файл

# Асинхронна функція для обробки каталогу з текстовими файлами
async def process_directory(input_dir, output_dir):
    tasks = []  # список для зберігання майбутніх завдань
    for filename in os.listdir(input_dir):  # перебираємо всі файли в каталозі
        if filename.endswith('.txt'):  # якщо це текстовий файл
            # додаємо завдання на обробку цього файлу
            tasks.append(process_file(os.path.join(input_dir, filename), output_dir))
    await asyncio.gather(*tasks)  # виконуємо всі завдання асинхронно

# Виконуємо головну асинхронну функцію, що обробляє каталог з файлами
asyncio.run(process_directory('Links_Baza_all_Domains/Sort_domain_by_Lang/katalog_domain/input', 'Links_Baza_all_Domains/Sort_domain_by_Lang/katalog_domain/output'))
