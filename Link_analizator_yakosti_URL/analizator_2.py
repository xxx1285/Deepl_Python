import asyncio
import httpx
from bs4 import BeautifulSoup
import re
import os
import urllib.parse
from langdetect import detect

# Задайте пределы для анализа сайта
MAX_OUTBOUND_LINKS = 50
MIN_TEXT_LENGTH = 200
CONCURRENT_LIMIT = 10  

# Визначаємо назву поточної директорії
current_folder = os.path.basename(os.path.dirname(__file__))

# Определение групп языков
language_group = {
    'en': ['en', 'am', 'sw', 'af', 'zu'],  # Англійська, Амхарська, Суахілі, Африкаанс, Зулуська
    'ru': ['ru', 'sr', 'uk', 'be', 'kk', 'uz', 'ky', 'tg'],  # Російська, Сербська, Українська, Білоруська, Казахська, Узбецька, Киргизька, Таджицька
    'es': ['es', 'gl', 'qu', 'an', 'ast', 'eu', 'ca', 'gn', 'ay', 'lad', 'pap'],  # Іспанська, Галісійська, Кечуа, Арагонська, Астурська, Баскська, Каталонська, Гуарані, Аймара, Ладіно, Пап’яменто
    'pl': ['pl', 'cs', 'sk', 'hsb', 'dsb', 'wen'],  # Польська, Чеська, Словацька, Верхньолужицька, Нижньолужицька, Серболужицька
    'pt': ['pt', 'mwl'],  # Португальська, Мірандська
    'fr': ['fr', 'wa', 'co', 'br', 'oc', 'ht', 'lb', 'gsw'],  # Французька, Валлонська, Корсиканська, Бретонська, Окситанська, Гаїтянська, Люксембурзька, Альзаська
    'id': ['id', 'jv', 'su', 'ms', 'min', 'bug', 'ace', 'ban', 'bjn'],  # Індонезійська, Яванська, Суданська, Малайська, Мінангкабау, Бугійська, Ачехська, Балійська, Банджарська
    'el': ['el', 'grc'],  # Грецька, Давньогрецька
    'de': ['de', 'nds', 'fy', 'stq'],  # Німецька, Нижньосаксонська, Фрізька, Сатерландська фрізька
    'tr': ['tr', 'az', 'crh', 'kaa', 'ug', 'tk'],  # Турецька, Азербайджанська, Кримська татарська, Каракалпацька, Уйгурська, Туркменська
    'hu': ['hu'],  # Угорська
    'it': ['it', 'mt', 'scn', 'co', 'eml', 'lld', 'lij', 'fur', 'pms', 'lmo'],  # Італійська, Мальтійська, Сицилійська, Корсиканська, Емільянська-Романьйольська, Ладінська, Лігурська, Фріульська, П'ємонтська, Ломбардійська
    'ro': ['ro', 'rup', 'mo'],  # Румунська, Аромунська, Молдавська
    'bg': ['bg', 'mk'],  # Болгарська, Македонська
    'fi': ['fi', 'sv', 'se', 'smn', 'sms', 'sma', 'krl', 'fit', 'fkv', 'olo', 'rmf', 'liv', 'vep', 'izh'],  # Фінська, Шведська, Північна саамська, Інаріська саамська, Скольська саамська, Південна саамська, Карельська, Торнедальська фінська, Квенська, Вепська, Романі, Лівонська, Вепська, Іжорська
    'et': ['et', 'vro'],  # Естонська, Вирська
    'lt': ['lt', 'sgs'],  # Литовська, Самогітська
    'lv': ['lv', 'ltg'],  # Латвійська, Латгальська
    'nl': ['nl', 'fy', 'li', 'zea', 'vls', 'af'],  # Голландська, Фрізька, Лімбурзька, Зеландська, Західнофламандська, Африкаанс
    'cs': ['cs', 'sk', 'pl'],  # Чеська, Словацька, Польська
    'da': ['da', 'fo', 'kl'],  # Данська, Фарерська, Гренландська
    'ja': ['ja', 'zh', 'ko', 'vi'],  # Японська, Китайська, Корейська, В'єтнамська
    'nb': ['nb', 'nn', 'no', 'se', 'sma', 'smj', 'smn', 'sms'],  # Норвезька (букмол), Норвезька (нюнорск), Норвезька, Північна саамська, Південна саамська, Лулська саамська, Інаріська саамська, Скольська саамська
    'sk': ['sk', 'cs'],  # Словацька, Чеська
    'sl': ['sl', 'hr', 'bs', 'sh'],  # Словенська, Хорватська, Боснійська, Сербохорватська
    'sv': ['sv', 'da', 'no', 'nb', 'nn'],  # Шведська, Данська, Норвезька, Норвезька (букмол), Норвезька (нюнорск)
    'az': ['az', 'tr', 'tk', 'uz', 'kaa'],  # Азербайджанська, Турецька, Туркменська, Узбецька, Каракалпацька
    'kk': ['kk', 'ky', 'ug', 'uz'],  # Казахська, Киргизька, Уйгурська, Узбецька
    'ar': ['ar', 'shu', 'ary', 'arq', 'aeb', 'arz', 'acm', 'ayh', 'afb', 'acx', 'ayl'],  # Арабська, Чадська арабська, Марокканська арабська, Алжирська арабська, Туніська арабська, Єгипетська арабська, Месопотамська арабська, Північноєгипетська арабська, Гебелейська арабська, Сусська арабська, Лівійська арабська
    'uz': ['uz', 'az', 'kaa', 'ug', 'tk']  # Узбецька, Азербайджанська, Каракалпацька, Уйгурська, Туркменська
}


# Функция для парсинга контента страницы
async def analyze_site(semaphore, client, url):
    async with semaphore:  
        try:
            r = await client.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')

            # Извлечение домена из URL
            netloc = urllib.parse.urlparse(url).netloc

            # Проверка на спам:
            # 1. Количество внешних ссылок (может быть признаком спама)
            outbound_links = [a['href'] for a in soup.find_all('a', href=True) 
                            if urllib.parse.urlparse(a['href']).netloc != netloc]
            # 2. Количество слов в тексте страницы (слишком мало может быть признаком недостаточного содержания)
            text_content = re.findall(r'\b\w+\b', soup.get_text())

            # Если сайт кажется хорошим для обратной ссылки, определяем язык первых 100 символов
            if len(outbound_links) < MAX_OUTBOUND_LINKS and len(text_content) > MIN_TEXT_LENGTH:
                language = detect(soup.get_text()[:100])  # Используем langdetect на первых 100 символах
                print(f"{language}_{url}")
                # Записываем URL в файл в зависимости от определенного языка
                for key in language_group:
                    if language in language_group[key]:
                        os.makedirs(f'{current_folder}\\result\\{key}', exist_ok=True)
                        with open(f'{current_folder}\\result\\{key}\\{language}_urls.txt', 'a') as f:
                            f.write(url + '\n')
                        break

        except Exception as e:
            print(f"Error {url}: {str(e)}")


def chunked(iterable, n):
    """Разбивает iterable на части размером n"""
    return [iterable[i:i + n] for i in range(0, len(iterable), n)]


# Основная функция
async def main():
    semaphore = asyncio.Semaphore(CONCURRENT_LIMIT)  # Создаем семафор
    async with httpx.AsyncClient(timeout=30.0) as client:

        # Получение списка файлов в директории
        files = os.listdir(f"{current_folder}\\proverit")

        for file in files:
            # Проверяем, что это текстовый файл
            if file.endswith('.txt'):
                # Получение списка URL из файла
                with open(f"{current_folder}\\proverit\\{file}", "r") as file:
                    urls = [line.strip() for line in file]

                # Разделение списка URL на части по 50
                url_chunks = chunked(urls, 50)

                for url_chunk in url_chunks:
                    tasks = (analyze_site(semaphore, client, url) for url in url_chunk)
                    await asyncio.gather(*tasks)


# Запуск асинхронного цикла событий
asyncio.run(main())
