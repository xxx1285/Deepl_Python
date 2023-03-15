from unidecode import unidecode
import re

# def transliterate_to_en(text, lang):
#     if lang in ["ru","es","pl","pt","fr","id","el","de","tr","hu","uk","it","ro","bg","fi","et","lv","nl"]:
#         text = unidecode(text) # перетворення у транслітерований варіант
#         # заміна всіх символів, крім літер та цифр, на дефіси
#         text = re.sub(r'[^a-zA-Z0-9]+', '-', text)
#     return text

text = {"ru": "Це російський текст з діакритичними знаками, який потрібно транслітерувати. Мама - мила раму та з'їла рибу вчора",
        "en": "This is a Russian text with diacritics that needs to be transliterated. Mom - washed her face and ate fish yesterday",
        "bg": "Това е руски текст с диакритични знаци, който трябва да бъде транслитериран. Мама - вчера си изми лицето и яде риба",
        "hu": "Ez egy diakritikus orosz szöveg, amelyet át kell írni. Anya - tegnap megmosta az arcát és halat evett.",
        "el": "Πρόκειται για ένα ρωσικό κείμενο με διακριτικά που πρέπει να μεταγραφεί. Η μαμά - έπλυνε το πρόσωπό της και έφαγε ψάρι χθες",
        "da": "Dette er en russisk tekst med diakritiske tegn, som skal translittereres. Mor - vaskede sit ansigt og spiste fisk i går",
        "id": "Ini adalah teks bahasa Rusia dengan diakritik yang perlu ditransliterasi. Ibu - mencuci muka dan makan ikan kemarin",
        "es": "Este es un texto en ruso con diacríticos que necesita ser transliterado. Mamá - se lavó la cara y comió pescado ayer",
        "it": "Questo è un testo russo con diacritici che deve essere traslitterato. Mamma - si è lavata la faccia e ha mangiato pesce ieri",
        "zh": "这是一篇带有变音符的俄语文章，需要进行音译。妈妈--昨天洗了脸，吃了鱼",
        "ko": "이것은 음역해야하는 분음 부호가있는 러시아어 텍스트입니다. 엄마-어제 세수하고 생선을 먹었습니다.",
        "lv": "Šis ir teksts krievu valodā ar diakritikas zīmēm, kas jātranliterē. Mamma - vakar mazgāja seju un ēda zivis",
        "lt": "Tai rusiškas tekstas su diakritiniais ženklais, kurį reikia transliteruoti. Mama - vakar nusiprausė veidą ir valgė žuvį",
        "de": "Dies ist ein russischer Text mit diakritischen Zeichen, der transkribiert werden muss. Mama - hat sich gestern das Gesicht gewaschen und Fisch gegessen",
        "nl": "Dit is een Russische tekst met diakritische tekens die vertaald moet worden. Mam - heeft gisteren haar gezicht gewassen en vis gegeten",
        "nb": "Dette er en russisk tekst med diakritiske tegn som må translittereres. Mamma - vasket ansiktet sitt og spiste fisk i går",
        "pl": "To jest tekst rosyjski z diakrytykami, który wymaga transliteracji. Mama - umyła twarz i zjadła wczoraj rybę",
        "pt": "Este é um texto russo com diacríticos que precisa de ser transliterado. Mãe - lavou a cara e comeu peixe ontem",
        "pt": "Este é um texto russo com diacríticos que precisa ser transliterado. Mãe - lavou seu rosto e comeu peixe ontem",
        "ro": "Acesta este un text în limba rusă cu diacritice care trebuie transliterat. Mama - s-a spălat pe față și a mâncat pește ieri",
        "sk": "Ide o ruský text s diakritikou, ktorý je potrebné preložiť. Mama - včera si umyla tvár a jedla rybu",
        "sl": "To je rusko besedilo z diakritičnimi znaki, ki ga je treba prevesti. Mama - včeraj si je umila obraz in jedla ribo",
        "tr": "Bu, harf çevirisi yapılması gereken aksan işaretli Rusça bir metindir. Annem - dün yüzünü yıkadı ve balık yedi",
        "fi": "Tämä on venäjänkielinen teksti, jossa on diakriittisiä merkkejä ja joka on translitteroitava. Äiti - pesi kasvonsa ja söi kalaa eilen.",
        "fr": "Il s'agit d'un texte russe avec des signes diacritiques qui doit être translittéré. Maman - s'est lavée le visage et a mangé du poisson hier",
        "cs": "Jedná se o ruský text s diakritikou, který je třeba přeložit. Maminka - včera si umyla obličej a snědla rybu",
        "sv": "Detta är en rysk text med diakritiska tecken som måste translittereras. Mamma - tvättade sitt ansikte och åt fisk igår",
        "et": "See on diakriitiliste tähtedega vene tekst, mis tuleb translitereerida. Ema - pesi eile nägu ja sõi kala",
        "ja": "この文章はロシア語で発音記号があるため、音訳が必要です。お母さん - 昨日、顔を洗って、魚を食べました"
        }
alik = []

for lang, txt in text.items():
    translit_text = unidecode(txt.lower())[:60]
    translit_text = re.sub(r'[^a-zA-Z0-9]+', '-', translit_text)
    alik.append(translit_text)
    print(translit_text)

print(alik)



# def transliterate_to_en(text, lang):
#     if lang in ["ru","es","pl","pt","fr","id","el","de","tr","hu","uk","it","ro","bg","fi","et","lv","nl"]:
#         text = unidecode(text) # перетворення у транслітерований варіант
#         # заміна всіх символів, крім літер та цифр, на дефіси
#         text = re.sub(r'[^a-zA-Z0-9]+', '-', text)
#     return text




# lang = "es"
# transliterated_text = transliterate(text, lang)
# print(transliterated_text) # Виведе "ce-rossijskij-tekst-z-diakritichnymi-znakami-jakyj-potribno-transliteruvati"

# for i in text:
#     transliterated_text = transliterate_to_en(i, lang)
#     print(transliterated_text)
