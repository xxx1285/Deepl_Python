import openai
import json
import io
from datetime import datetime
import pprint


# Загружаем параметры из конфигурационного файла
with open(r'AI_content_Chat_GPT\config\config_OpenAi_Key.json') as f:
    config = json.load(f)
openai.api_key = config['config_openai']['api_openai_key']

######################################################################################
######################################################################################
# Запрос к OpenAI

######################################################################################
######################################################################################


spisok = {}

top_country = ["English","Russian","Spanish","Polish","Portuguese","French","Indonesian","Greek","German","Turkish","Hungarian","Ukrainian","Italian","Romanian","Bulgarian","Finnish","Estonian","Lithuanian","Latvian","Dutch","Czech","Danish","Japanese","Norwegian","Slovak","Slovenian","Swedish","Azerbaijani","Kazakh","Arabic","Uzbek","Korean","Chinese"]

language_tld_mapping = {
    "English": ["en", "us"],
    "Russian": ["ru"],
    "Spanish": ["es"],
    "Polish": ["pl"],
    "Portuguese": ["pt"],
    "French": ["fr"],
    "Indonesian": ["id"],
    "Greek": ["el"],
    "German": ["de"],
    "Turkish": ["tr"],
    "Hungarian": ["hu"],
    "Ukrainian": ["uk"],
    "Italian": ["it"],
    "Romanian": ["ro"],
    "Bulgarian": ["bg"],
    "Finnish": ["fi"],
    "Estonian": ["et"],
    "Lithuanian": ["lt"],
    "Latvian": ["lv"],
    "Dutch": ["nl"],
    "Czech": ["cs"],
    "Danish": ["da"],
    "Japanese": ["ja"],
    "Norwegian": ["nb"],
    "Slovak": ["sk"],
    "Slovenian": ["sl"],
    "Swedish": ["sv"],
    "Azerbaijani": ["az"],
    "Kazakh": ["kk"],
    "Arabic": ["ar"],
    "Uzbek": ["uz"],
    "Korean": ["ko"],
    "Chinese": ["zh"],
    "Other": ["club"]
}


# Відкриваємо файл з доменними зонами
with open(r'AI_content_Chat_GPT\domen_zona\all_domen_zona.txt', 'r') as file:
    # Зчитуємо весь вміст файлу
    content = file.read()
    # Розділяємо доменні зони за комами
    domains = content.split(', ')
    # Перебираємо доменні зони
    for domain in domains:

        # AI Promt Chat GPT
        prompt = f"we have a domain zone '{domain}', select from the list '{top_country}' the language that best matches the regionality of the domain zone '{domain}'. If the domain is not regional, then indicate the area to which it belongs. Answer in one word."
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=10,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # Получаем ответ и убираем лишние символы
        ai_response = response.choices[0].text.strip()

        if ai_response in top_country:
            language_tld_mapping[ai_response].append(domain)
        else:
            spisok[ai_response] = domain  # Додаємо новий ключ і значення




# Збереження зміненого словника в новому файлі
with open(r'AI_content_Chat_GPT\domen_zona\dict_domen_lang.py', 'w') as file:
    file.write("language_tld_mapping = ")
    pprint.pprint(language_tld_mapping, stream=file)
    file.write("\n")
    file.write("spisok = ")
    pprint.pprint(spisok, stream=file)

print('Oll OK')