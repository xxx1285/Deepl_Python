import re

struktura_id_alias_map = {
    127:'https://the-dog-house.org/es/',
    1:'https://the-dog-house.org/',
    129:'https://the-dog-house.org/es/bonuses-and-strategies.html',
    3:'https://the-dog-house.org/bonuses-and-strategies-the-dog-house.html',
    130:'https://the-dog-house.org/es/win_demo-game.html',
    4:'https://the-dog-house.org/the-dog-house-slot-demo.html',
    131:'https://the-dog-house.org/es/reviews.html',
    5:'https://the-dog-house.org/the-dog-house-reviews-megaways-free-game.html'
}

struktura_id_map = {1:127, 2:128, 3:129, 4:130, 5:131, 6:132}


row_database_game = {
    'name_title': '<p>Immerse <a href="https://the-dog-house.org/bonuses-and-strategies-the-dog-house.html" title="2222">2222</a> yourself in the barking world of <a href="https://the-dog-house.org/" title="Pragmatic Plays Dog House slot">Pragmatic Plays Dog House slot</a>, a sure-fire way to entertain and reward.</p><p>What sets this game apart are its innovative features,  of landing a <a href="https://the-dog-house.org/the-dog-house-reviews-megaways-free-game.html" title="winning combination (reed reviews)">winning combination (reed reviews)</a>.</p>'
}

# Створюємо інвертований словник для знаходження id за url
inv_struktura_id_alias_map = {v: k for k, v in struktura_id_alias_map.items()}

# Функція для заміни посилань в тексті
def replace_link(link_obgect):
    # Витягуємо значення href (group(1) - перша група у регулярному виразі, в нашому випадку значення href)
    url = link_obgect.group(1)
    if url in inv_struktura_id_alias_map:
        id_ = inv_struktura_id_alias_map[url]
        if id_ in struktura_id_map:
            new_id = struktura_id_map[id_]
            new_url = struktura_id_alias_map[new_id]
            return f'<a href="{new_url}"'
    # Якщо заміна не відбулась, повертаємо вихідний тег без змін (group(0) - цілий знайдений текст, що відповідає регулярному виразу)
    return link_obgect.group(0)

# Змінюємо посилання в тексті використовуючи функцію replace_link та регулярний вираз
row_database_game['name_title'] = re.sub(r'<a href="(.*?)"', replace_link, row_database_game['name_title'])

print(row_database_game['name_title'])

language_dict = {"en": "English", "ru": "Русский", "es": "Español", "pl": "Polski", "pt-br": "Português (Brasil)", 
                    "pt": "Português", "fr": "Français", "id": "Bahasa Indonesia", "el": "Ελληνικά", "de": "Deutsch", 
                    "tr": "Türkçe", "hu": "Magyar", "uk": "Українська", "it": "Italiano", "ro": "Română", "bg": "Български", 
                    "fi": "Suomi", "et": "Eesti", "lt": "Lietuvių", "lv": "Latviešu", "nl": "Nederlands", "cs": "Čeština", 
                    "da": "Dansk", "ja": "日本語", "nb": "Norsk Bokmål", "sk": "Slovenčina", "sl": "Slovenščina", "sv": "Svenska", 
                    "az": "Azərbaycan", "kk": "Қазақ", "ar": "العربية", "uz": "O'zbek"
                    }
lang = 'hu'

print(language_dict[lang])