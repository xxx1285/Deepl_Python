import json
from unidecode import unidecode
import re
from pprint import pformat


data = {
    "bg": {
        "bg-bg": ["България", "София", "пл. „Независимост“ 1", "1000", "бул. Витоша 20"]
    },
    "cs": {
        "cs-cz": ["Česká republika", "Praha", "Hradčanské náměstí 1", "118 00", "Václavské náměstí 20"]
    },
    "da": {
        "da-dk": ["Danmark", "København", "Christiansborg Slotsplads 1", "1218", "Strøget 20"],
        "da-fo": ["Færøerne", "Tórshavn", "Vaglið 1", "100", "Niels Finsens gøta 20"],
        "da-gl": ["Grønland", "Nuuk", "Aqqusinersuaq 1", "3900", "Imaneq 20"]
    },
    "de": {
        "de-at": ["Österreich", "Wien", "Ballhausplatz 1", "1010", "Kärntner Straße 20"],
        "de-ch": ["Schweiz", "Bern", "Bundesplatz 1", "3005", "Bahnhofstrasse 20"],
        "de-de": ["Deutschland", "Berlin", "Platz der Republik 1", "11011", "Kurfürstendamm 20"],
        "de-li": ["Liechtenstein", "Vaduz", "Fürst-Franz-Josef-Straße 1", "9490", "Äulestrasse 20"]
    },
    "el": {
        "el-cy": ["Κύπρος", "Λευκωσία", "Πρεζιδεντικό Μέγαρο 1", "1066", "Λήδρας 20"],
        "el-gr": ["Ελλάδα", "Αθήνα", "Σύνταγμα 1", "105 57", "Ερμού 20"]
    },
    "en": {
        "en-ad": ["Andorra", "Andorra la Vella", "Meritxell Avenue 20", "AD500", "Business Center Street 1"],
        "en-ae": ["United Arab Emirates", "Abu Dhabi", "Corniche Road 50", "0000", "Sheikh Zayed Road 20"],
        "en-af": ["Afghanistan", "Kabul", "Central Street 5", "1001", "Business Avenue 3"],
        "en-ag": ["Antigua and Barbuda", "St. John's", "High Street 11", "0000", "Corporate Blvd 2"],
        "en-al": ["Albania", "Tirana", "Skanderbeg Square 12", "1000", "Main Business St 7"],
        "en-as": ["American Samoa", "Pago Pago", "Central Avenue 6", "96799", "Island Business Way 5"],
        "en-au": ["Australia", "Canberra", "Commonwealth Ave 15", "2600", "Sydney Business Park 18"],
        "en-ba": ["Bosnia and Herzegovina", "Sarajevo", "Marsala Tita 20", "71000", "Business Plaza 3"],
        "en-bd": ["Bangladesh", "Dhaka", "Mirpur Road 80", "1205", "Commercial Street 16"],
        "en-bh": ["Bahrain", "Manama", "King Faisal Highway 10", "317", "Financial Harbour 20"],
        "en-bn": ["Brunei", "Bandar Seri Begawan", "Sultan Omar Ali Saifuddien Rd 7", "BS8711", "Business Park 5"],
        "en-bs": ["Bahamas", "Nassau", "Bay Street 20", "N-7148", "Corporate Drive 3"],
        "en-bt": ["Bhutan", "Thimphu", "Norzin Lam 12", "11001", "Commercial Road 2"],
        "en-bw": ["Botswana", "Gaborone", "Queens Road 15", "10100", "High-Tech Park 11"],
        "en-bz": ["Belize", "Belmopan", "Ring Road 2", "0000", "Business Circle 6"],
        "en-ca": ["Canada", "Ottawa", "Wellington Street 45", "K1A 0A6", "Bay Street 100"],
        "en-cc": ["Cocos Islands", "West Island", "Pulu Keeling Drive 3", "6799", "Business Island Way 1"],
        "en-cx": ["Christmas Island", "Flying Fish Cove", "Gaze Road 11", "6798", "Corporate Avenue 4"],
        "en-dm": ["Dominica", "Roseau", "Great George Street 8", "00152", "Financial Center 4"],
        "en-eg": ["Egypt", "Cairo", "Tahrir Square 1", "11511", "Smart Village 12"],
        "en-er": ["Eritrea", "Asmara", "Independence Avenue 10", "1234", "Business Park 3"],
        "en-et": ["Ethiopia", "Addis Ababa", "Churchill Road 20", "1000", "Kazanchis 5"],
        "en-fj": ["Fiji", "Suva", "Victoria Parade 15", "0001", "Fiji Business Park 2"],
        "en-fm": ["Micronesia", "Palikir", "Nanpohnmal 4", "96941", "Corporate Avenue 5"],
        "en-gb": ["United Kingdom", "London", "Whitehall 50", "SW1A 2AS", "Canary Wharf 15"],
        "en-gg": ["Guernsey", "Saint Peter Port", "High Street 12", "GY1 2HP", "Business Lane 6"],
        "en-gh": ["Ghana", "Accra", "Oxford Street 25", "GA-010-5374", "Airport City 10"],
        "en-gm": ["Gambia", "Banjul", "Independence Drive 3", "12345", "Kairaba Avenue 15"],
        "en-gy": ["Guyana", "Georgetown", "Regent Street 7", "41237", "Main Business Plaza 15"],
        "en-hr": ["Croatia", "Zagreb", "Ilica Street 50", "10000", "Business Tower 20"],
        "en-ie": ["Ireland", "Dublin", "O'Connell Street 20", "D01 F5P2", "Docklands Ave 12"],
        "en-in": ["India", "New Delhi", "Rajpath 11", "110001", "Cyber City 55"],
        "en-jm": ["Jamaica", "Kingston", "Knutsford Boulevard 5", "876", "New Kingston 3"],
        "en-jo": ["Jordan", "Amman", "Rainbow Street 21", "11118", "Abdali Boulevard 14"],
        "en-ke": ["Kenya", "Nairobi", "Kenyatta Avenue 45", "00100", "Westlands Road 11"],
        "en-kh": ["Cambodia", "Phnom Penh", "Preah Sihanouk Blvd 12", "12207", "Mao Tse Tung Blvd 32"],
        "en-ki": ["Kiribati", "South Tarawa", "Main Road 6", "G8101", "Bairiki Square 3"],
        "en-kw": ["Kuwait", "Kuwait City", "Gulf Road 9", "13001", "Financial Street 19"],
        "en-la": ["Laos", "Vientiane", "Lane Xang Avenue 16", "01000", "Kumkha Road 10"],
        "en-lb": ["Lebanon", "Beirut", "Hamra Street 25", "1103", "Verdun Street 8"],
        "en-lc": ["Saint Lucia", "Castries", "Jeremie Street 19", "LC04 101", "Bridge Street 5"],
        "en-lk": ["Sri Lanka", "Colombo", "Galle Road 34", "00100", "World Trade Center 23"],
        "en-lr": ["Liberia", "Monrovia", "Broad Street 18", "1000", "Mamba Point 5"],
        "en-ls": ["Lesotho", "Maseru", "Kingsway Road 20", "100", "Pioneer Road 12"],
        "en-ly": ["Libya", "Tripoli", "Sharia Fatah 44", "82612", "Martyrs' Square 7"],
        "en-me": ["Montenegro", "Podgorica", "Bulevar Džordža Vašingtona 55", "81000", "Stanka Dragojevića 7"],
        "en-mh": ["Marshall Islands", "Majuro", "Laura Beach Road 9", "96960", "Long Island Boulevard 6"],
        "en-mk": ["North Macedonia", "Skopje", "Pella Square 15", "1000", "Business Avenue 20"],
        "en-mm": ["Myanmar (Burma)", "Yangon", "Sule Pagoda Road 35", "11181", "Pyay Road 47"],
        "en-mp": ["Northern Mariana Islands", "Saipan", "Beach Road 11", "96950", "Micro Beach 2"],
        "en-mt": ["Malta", "Valletta", "Republic Street 29", "VLT 1116", "Merchant Street 8"],
        "en-mu": ["Mauritius", "Port Louis", "Royal Street 65", "11328", "Caudan Waterfront 22"],
        "en-mv": ["Maldives", "Malé", "Majeedhee Magu 10", "20026", "Orchid Magu 17"],
        "en-mw": ["Malawi", "Lilongwe", "Presidential Way 47", "442", "Chilambula Road 14"],
        "en-my": ["Malaysia", "Kuala Lumpur", "Jalan Sultan Hishamuddin 35", "50000", "Bukit Bintang Street 20"],
        "en-na": ["Namibia", "Windhoek", "Independence Avenue 52", "10001", "Robert Mugabe Avenue 28"],
        "en-ng": ["Nigeria", "Abuja", "Yakubu Gowon Crescent 70", "900001", "Adetokunbo Ademola Crescent 15"],
        "en-np": ["Nepal", "Kathmandu", "Durbar Marg 9", "44600", "Thamel Street 25"],
        "en-nu": ["Niue", "Alofi", "Main Road 12", "4033", "Commercial Centre 7"],
        "en-nz": ["New Zealand", "Wellington", "Lambton Quay 42", "6011", "Courtenay Place 28"],
        "en-om": ["Oman", "Muscat", "Sultan Qaboos Street 70", "100", "Al Khuwair Street 15"],
        "en-pg": ["Papua New Guinea", "Port Moresby", "Waigani Drive 33", "131", "Boroko Drive 18"],
        "en-ph": ["Philippines", "Manila", "Roxas Boulevard 55", "1000", "Ayala Avenue 25"],
        "en-pk": ["Pakistan", "Islamabad", "Jinnah Avenue 28", "44000", "Constitution Avenue 19"],
        "en-ps": ["Palestine", "Ramallah", "Rukab Street 11", "969", "Al-Ersal Street 16"],
        "en-pw": ["Palau", "Ngerulmud", "Capitol Complex 5", "96940", "Koror Road 22"],
        "en-qa": ["Qatar", "Doha", "Corniche Street 9", "12345", "Wadi Msheireb Street 18"],
        "en-rs": ["Serbia", "Belgrade", "Knez Mihailova 33", "11000", "Terazije 15"],
        "en-rw": ["Rwanda", "Kigali", "Nyarugenge Street 24", "1100", "KN 3 Road 9"],
        "en-sa": ["Saudi Arabia", "Riyadh", "Olaya Street 55", "11547", "King Fahd Road 108"],
        "en-sb": ["Solomon Islands", "Honiara", "Mendana Avenue 12", "131", "Kukum Highway 17"],
        "en-sd": ["Sudan", "Khartoum", "Nile Street 64", "11111", "Airport Road 40"],
        "en-sg": ["Singapore", "Singapore", "Orchard Road 999", "238883", "Marina Bay Street 18"],
        "en-sj": ["Svalbard and Jan Mayen", "Longyearbyen", "Vei 222-2", "9170", "Vei 508-10"],
        "en-sl": ["Sierra Leone", "Freetown", "Siaka Stevens Street 51", "1000", "Lumley Beach Road 7"],
        "en-sm": ["San Marino", "San Marino", "Via del Voltone 13", "47890", "Contrada Omagnano 8"],
        "en-so": ["Somalia", "Mogadishu", "Maka Al Mukarama Road 78", "2525", "Zobe Junction 3"],
        "en-sr": ["Suriname", "Paramaribo", "Kwattaweg 45", "1000", "Domineestraat 12"],
        "en-ss": ["South Sudan", "Juba", "Tongping Road 10", "00211", "Ministries Road 7"],
        "en-st": ["São Tomé and Príncipe", "São Tomé", "Independencia Avenue 42", "00209", "Amilcar Cabral Street 3"],
        "en-sx": ["Sint Maarten", "Philipsburg", "Frontstreet 28", "0001", "Back Street 12"],
        "en-sy": ["Syria", "Damascus", "Umayyad Square 6", "1001", "Mezzeh Highway 17"],
        "en-sz": ["Eswatini", "Mbabane", "Gwamile Street 7", "H100", "Mhlambanyatsi Road 23"],
        "en-tc": ["Turks and Caicos Islands", "Cockburn Town", "Duke Street 11", "TKCA 1ZZ", "Leeward Highway 20"],
        "en-th": ["Thailand", "Bangkok", "Sukhumvit Road 777", "10110", "Silom Road 32"],
        "en-tl": ["Timor-Leste", "Dili", "Avenida de Portugal 19", "0001", "Rua Martires da Patria 22"],
        "en-tt": ["Trinidad and Tobago", "Port of Spain", "Frederick Street 56", "00000", "Ariapita Avenue 22"],
        "en-tz": ["Tanzania", "Dodoma", "Chama Avenue 47", "40100", "Gaddafi Road 33"],
        "en-ug": ["Uganda", "Kampala", "Kampala Road 11", "256", "Acacia Avenue 32"],
        "en-um": ["U.S. Minor Outlying Islands", "Baker Island", "Main Street 1", "96898", "Harbor Road 7"],
        "en-us": ["United States", "Washington, D.C.", "Pennsylvania Avenue 1600", "20500", "Wall Street 15"],
        "en-va": ["Vatican City", "Vatican City", "Vatican Square 1", "00120", "St. Peter's Square 7"],
        "en-vg": ["British Virgin Islands", "Road Town", "Main Street 22", "VG1110", "Waterfront Drive 8"],
        "en-vn": ["Vietnam", "Hanoi", "Ba Dinh Square 1", "10000", "Tran Hung Dao Street 23"],
        "en-ws": ["Samoa", "Apia", "Beach Road 15", "WS0979", "Cross Island Road 11"],
        "en-xk": ["Kosovo", "Pristina", "Mother Teresa Street 21", "10000", "Agim Ramadani Street 13"],
        "en-ye": ["Yemen", "Sana'a", "60 Meter Road 32", "00967", "Hadda Street 11"],
        "en-za": ["South Africa", "Pretoria", "Church Street 101", "0002", "Rivonia Road 90"],
        "en-zm": ["Zambia", "Lusaka", "Cairo Road 27", "10101", "Thabo Mbeki Road 12"],
        "en-zw": ["Zimbabwe", "Harare", "Samora Machel Avenue 65", "00263", "Rotten Row 22"]
    },
    "es": {
        "es-ar": ["Argentina", "Buenos Aires", "Avenida 9 de Julio 123", "1000", "Calle Florida 456"],
        "es-aw": ["Aruba", "Oranjestad", "Caya G. F. Betico Croes 10", "0001", "Calle Comercial 20"],
        "es-bo": ["Bolivia", "Sucre", "Avenida 16 de Julio 50", "0900", "Calle Mercado 25"],
        "es-cl": ["Chile", "Santiago", "Avenida Libertador Bernardo O'Higgins 70", "8320000", "Calle Providencia 80"],
        "es-co": ["Colombia", "Bogotá", "Carrera 7 #26", "111711", "Calle 80 #10"],
        "es-cr": ["Costa Rica", "San José", "Avenida Central 5", "1000", "Calle Paseo Colón 40"],
        "es-cu": ["Cuba", "La Habana", "Paseo del Prado 10", "10100", "Calle 23 #15"],
        "es-do": ["República Dominicana", "Santo Domingo", "Avenida George Washington 60", "10101", "Calle El Conde 45"],
        "es-ec": ["Ecuador", "Quito", "Avenida Amazonas 20", "170143", "Calle García Moreno 30"],
        "es-eh": ["Sahara Occidental", "Laayoune", "Avenida Smara 15", "70000", "Calle Hassan II 25"],
        "es-es": ["España", "Madrid", "Gran Vía 30", "28013", "Calle Serrano 40"],
        "es-gq": ["Guinea Ecuatorial", "Malabo", "Avenida Hassan II 25", "00209", "Calle Américo Vespucio 10"],
        "es-gt": ["Guatemala", "Ciudad de Guatemala", "6A Avenida 5", "01001", "7A Avenida 10"],
        "es-hn": ["Honduras", "Tegucigalpa", "Bulevar Suyapa 10", "11101", "Calle Los Alamos 35"],
        "es-mx": ["México", "Ciudad de México", "Paseo de la Reforma 50", "06500", "Avenida Insurgentes Sur 300"],
        "es-ni": ["Nicaragua", "Managua", "Avenida Bolívar 10", "11001", "Calle Bello Horizonte 30"],
        "es-pa": ["Panamá", "Ciudad de Panamá", "Avenida Balboa 45", "0819-05760", "Calle 50 #22"],
        "es-pe": ["Perú", "Lima", "Avenida Abancay 50", "15001", "Calle Larco 40"],
        "es-pr": ["Puerto Rico", "San Juan", "Avenida Ponce de León 123", "00901", "Calle Fortaleza 55"],
        "es-py": ["Paraguay", "Asunción", "Avenida Mariscal López 100", "1119", "Calle Palma 50"],
        "es-sv": ["El Salvador", "San Salvador", "Alameda Roosevelt 25", "1101", "Bulevar de Los Héroes 20"],
        "es-uy": ["Uruguay", "Montevideo", "Avenida 18 de Julio 130", "11000", "Calle Rambla 40"],
        "es-ve": ["Venezuela", "Caracas", "Avenida Bolívar 140", "1010", "Calle Andrés Bello 60"]
    },
    "fr": {
        "fr-bf": ["Burkina Faso", "Ouagadougou", "Avenue de l'Indépendance 10", "01", "Rue de la Paix 20"],
        "fr-bi": ["Burundi", "Bujumbura", "Boulevard de l'Uprona 50", "1100", "Avenue de la Liberté 35"],
        "fr-bj": ["Bénin", "Cotonou", "Avenue Clozel 15", "3000", "Rue de l'Entente 25"],
        "fr-bl": ["Saint-Barthélemy", "Gustavia", "Rue du Bord de Mer 1", "97133", "Rue de la République 5"],
        "fr-ca": ["Canada", "Montréal", "Rue Sainte-Catherine 100", "H2W 1N1", "Boulevard René-Lévesque 75"],
        "fr-cd": ["République Démocratique du Congo", "Kinshasa", "Avenue des Huileries 5", "1000", "Boulevard du 30 Juin 20"],
        "fr-cf": ["République Centrafricaine", "Bangui", "Avenue des Martyrs 8", "1010", "Rue de France 12"],
        "fr-cg": ["République du Congo", "Brazzaville", "Avenue du Général de Gaulle 15", "2000", "Rue Makabandilou 10"],
        "fr-ci": ["Côte d'Ivoire", "Abidjan", "Boulevard de la République 35", "5000", "Avenue Houphouët-Boigny 30"],
        "fr-cm": ["Cameroun", "Yaoundé", "Avenue Ahmadou Ahidjo 25", "3000", "Boulevard de la Liberté 40"],
        "fr-dj": ["Djibouti", "Djibouti", "Place Lagarde 2", "1000", "Avenue Georges Clemenceau 10"],
        "fr-dz": ["Algérie", "Alger", "Boulevard Zighout Youcef 100", "16000", "Avenue de la Liberté 50"],
        "fr-fr": ["France", "Paris", "Champs-Élysées 10", "75008", "Rue de Rivoli 30"],
        "fr-ga": ["Gabon", "Libreville", "Boulevard Triomphal 20", "6000", "Rue de la Paix 45"],
        "fr-gn": ["Guinée", "Conakry", "Avenue de la République 15", "2000", "Rue de France 25"],
        "fr-gp": ["Guadeloupe", "Pointe-à-Pitre", "Rue Frébault 5", "97110", "Rue Schoelcher 8"],
        "fr-ht": ["Haïti", "Port-au-Prince", "Rue Capois 10", "6110", "Avenue Jean-Jacques Dessalines 20"],
        "fr-km": ["Comores", "Moroni", "Avenue de l'Indépendance 5", "2000", "Rue du Commerce 30"],
        "fr-lu": ["Luxembourg", "Luxembourg", "Avenue de la Liberté 50", "L-1930", "Rue Royale 10"],
        "fr-ma": ["Maroc", "Rabat", "Avenue Mohammed V 40", "10000", "Boulevard de la Résistance 25"],
        "fr-mc": ["Monaco", "Monaco", "Avenue d'Ostende 15", "98000", "Boulevard des Moulins 10"],
        "fr-mf": ["Saint-Martin", "Marigot", "Rue de la Liberté 2", "97150", "Rue de Hollande 5"],
        "fr-mg": ["Madagascar", "Antananarivo", "Avenue de l'Indépendance 10", "101", "Rue Ratsimilaho 20"],
        "fr-ml": ["Mali", "Bamako", "Avenue de la Nation 15", "1000", "Rue de la Paix 30"],
        "fr-mq": ["Martinique", "Fort-de-France", "Rue Victor Hugo 1", "97200", "Rue de la Liberté 10"],
        "fr-mr": ["Mauritanie", "Nouakchott", "Avenue Gamal Abdel Nasser 5", "0001", "Rue de la République 20"],
        "fr-nc": ["Nouvelle-Calédonie", "Nouméa", "Avenue de la Victoire 30", "98800", "Rue du Général Mangin 15"],
        "fr-ne": ["Niger", "Niamey", "Avenue du Général de Gaulle 10", "9000", "Rue de la République 25"],
        "fr-pf": ["Polynésie Française", "Papeete", "Boulevard Pomare 20", "98713", "Avenue du Prince Hinoi 10"],
        "fr-pm": ["Saint-Pierre-et-Miquelon", "Saint-Pierre", "Rue Albert Briand 5", "97500", "Rue du 11 Novembre 10"],
        "fr-re": ["La Réunion", "Saint-Denis", "Rue de Paris 15", "97400", "Rue du Général de Gaulle 20"],
        "fr-sc": ["Seychelles", "Victoria", "Rue de la République 5", "0000", "Avenue de l'Indépendance 10"],
        "fr-sn": ["Sénégal", "Dakar", "Avenue Cheikh Anta Diop 20", "5000", "Rue de Thann 35"],
        "fr-td": ["Tchad", "N'Djamena", "Avenue Charles de Gaulle 15", "1000", "Rue de la Liberté 30"],
        "fr-tf": ["Terres Australes Françaises", "Port-aux-Français", "Rue Principale 1", "98400", "Rue des Manchots 2"],
        "fr-tg": ["Togo", "Lomé", "Boulevard du 13 Janvier 10", "1000", "Rue des Flamboyants 25"],
        "fr-tn": ["Tunisie", "Tunis", "Avenue Habib Bourguiba 50", "1000", "Rue de Marseille 40"],
        "fr-wf": ["Wallis-et-Futuna", "Mata-Utu", "Rue Kafika 1", "98600", "Rue Sagato Soane 5"],
        "fr-yt": ["Mayotte", "Mamoudzou", "Rue du Commerce 10", "97600", "Avenue du Général de Gaulle 15"]
    },
    "pt": {
        "pt-ao": ["Angola", "Luanda", "Avenida 4 de Fevereiro 100", "1000", "Rua Amílcar Cabral 20"],
        "pt-br": ["Brasil", "São Paulo", "Avenida Paulista 1578", "01310-200", "Rua Augusta 501"],
        "pt-cv": ["Cabo Verde", "Praia", "Avenida Cidade de Lisboa 30", "7600", "Rua Serpa Pinto 10"],
        "pt-gw": ["Guiné-Bissau", "Bissau", "Avenida Amílcar Cabral 50", "1001", "Rua José Carlos Schwarz 15"],
        "pt-mz": ["Moçambique", "Maputo", "Avenida Julius Nyerere 1111", "1010", "Rua Eduardo Mondlane 25"],
        "pt-pt": ["Portugal", "Lisboa", "Avenida da Liberdade 120", "1250-145", "Rua Augusta 50"],
        "pt-st": ["São Tomé e Príncipe", "São Tomé", "Avenida Marginal 12 de Julho 5", "1000", "Rua da Independência 10"],
        "pt-tl": ["Timor-Leste", "Díli", "Avenida de Portugal 20", "1000", "Rua 28 de Novembro 15"]
    },
    "ru": {
        "ru-am": ["Армения", "Ереван", "Проспект Маршала Баграмяна 1", "375019", "Улица Абовяна 5"],
        "ru-az": ["Азербайджан", "Баку", "Проспект Нефтяников 10", "1010", "Улица Гадрутская 20"],
        "ru-by": ["Беларусь", "Минск", "Проспект Независимости 100", "220050", "Улица Коммунистическая 25"],
        "ru-ge": ["Грузия", "Тбилиси", "Проспект Руставели 40", "0108", "Улица Чавчавадзе 15"],
        "ru-kg": ["Киргизия", "Бишкек", "Проспект Чуй 100", "720001", "Улица Боконбаева 20"],
        "ru-kz": ["Казахстан", "Астана", "Проспект Мангилик Ел 55", "010000", "Улица Кенесары 10"],
        "ru-mn": ["Монголия", "Улан-Батор", "Проспект Сухэ-Батора 5", "210646", "Улица Сансар 20"],
        "ru-ru": ["Россия", "Москва", "Тверская улица 7", "125009", "Арбат 15"],
        "ru-tj": ["Таджикистан", "Душанбе", "Проспект Рудаки 50", "734025", "Улица И. Сомони 30"],
        "ru-tm": ["Туркменистан", "Ашхабад", "Проспект Мактумкули 70", "744000", "Улица Героя Туркменистана Атаева 5"],
        "ru-ua": ["Украина", "Киев", "Хрещатик 50", "01001", "Улица Владимирская 20"],
        "ru-uz": ["Узбекистан", "Ташкент", "Проспект Мустакиллик 30", "100000", "Улица Амира Темура 15"]
    },
    "sk": {
        "sk-sk": ["Slovensko", "Bratislava", "Námestie SNP 1", "81101", "Obchodná ulica 20"]
    },
    "sl": {
        "sl-si": ["Slovenija", "Ljubljana", "Prešernov trg 1", "1000", "Slovenska cesta 20"]
    },
    "sv": {
        "sv-ax": ["Åland", "Mariehamn", "Torggatan 10", "22100", "Nybovägen 20"],
        "sv-se": ["Sverige", "Stockholm", "Kungsgatan 10", "11143", "Sveavägen 20"]
    },
    "tr": {
        "tr-az": ["Azerbaycan", "Bakü", "Neftçilar Prospekti 10", "1010", "Qədrut Küçəsi 20"],
        "tr-tm": ["Türkmenistan", "Aşkabat", "Mahtumkuli prospekti 70", "744000", "Garaşsyzlyk şayoli 5"],
        "tr-tr": ["Türkiye", "Ankara", "Atatürk Bulvarı 10", "06050", "Tunalı Hilmi Caddesi 20"]
    },
    "uk": {
        "uk-ua": ["Україна", "Київ", "Хрещатик 50", "01001", "Вулиця Володимирська 20"]
    },
    "zh": {
        "zh-cn": ["中国", "北京", "长安街1号", "100000", "王府井大街20号"],
        "zh-hk": ["香港", "中環", "皇后大道中1號", "999077", "彌敦道20號"],
        "zh-mo": ["澳門", "澳門半島", "南灣大馬路1號", "999078", "巴素打路20號"],
        "zh-tw": ["台灣", "台北", "中正路1號", "10048", "忠孝東路20號"]
    },
    "et": {
        "et-ee": ["Eesti", "Tallinn", "Vabaduse väljak 10", "10146", "Viru tänav 20"]
    },
    "fi": {
        "fi-fi": ["Suomi", "Helsinki", "Senatsplatsen 1", "00170", "Aleksanterinkatu 20"]
    },
    "hu": {
        "hu-hu": ["Magyarország", "Budapest", "Kossuth tér 1-3.", "1055", "Váci utca 20"]
    },
    "id": {
        "id-id": ["Indonesia", "Jakarta", "Jalan Medan Merdeka Selatan No.1", "10110", "Jalan Thamrin No. 20"]
    },
    "it": {
        "it-it": ["Italia", "Roma", "Piazza Venezia 1", "00187", "Via del Corso 20"],
        "it-sm": ["San Marino", "Città di San Marino", "Piazza della Libertà 1", "47890", "Via del Teatro 20"]
    },
    "ja": {
        "ja-jp": ["日本", "東京", "千代田区丸の内1-1", "100-0005", "渋谷区道玄坂20"]
    },
    "ko": {
        "ko-kp": ["조선민주주의인민공화국", "평양", "김일성광장 1", "100-000", "독립대로 20"],
        "ko-kr": ["대한민국", "서울", "태평로 1", "04544", "강남대로 20"]
    },
    "lt": {
        "lt-lt": ["Lietuva", "Vilnius", "Gedimino pr. 1", "01103", "Pilies g. 20"]
    },
    "lv": {
        "lv-lv": ["Latvija", "Rīga", "Brīvības bulvāris 1", "LV-1050", "Elizabetes iela 20"]
    },
    "nb": {
        "nb-no": ["Norge", "Oslo", "Stortingsgata 1", "0161", "Karl Johans gate 20"]
    },
    "nl": {
        "nl-be": ["België", "Brussel", "Wetstraat 1", "1000", "Nieuwstraat 20"],
        "nl-bq": ["Bonaire", "Kralendijk", "Plasa Wilhelmina 1", "Caribbean Netherlands", "Kaya Grandi 20"],
        "nl-cw": ["Curaçao", "Willemstad", "Handelskade 1", "Curaçao", "Breedestraat 20"],
        "nl-nl": ["Nederland", "Amsterdam", "Dam 1", "1012 NP", "Kalverstraat 20"]
    },
    "pl": {
        "pl-pl": ["Polska", "Warszawa", "Plac Zamkowy 1", "00-277", "Nowy Świat 20"]
    },
    "ro": {
        "ro-md": ["Republica Moldova", "Chișinău", "Bulevardul Ștefan cel Mare și Sfânt 1", "2001", "Strada București 20"],
        "ro-ro": ["România", "București", "Piața Revoluției 1", "010375", "Bulevardul Magheru 20"]
    }
}


spisok_dublikatov = ["en-ca","fr-ca","ru-ua","uk-ua","ru-tm","tr-tm","en-sm","it-sm","ru-az","tr-az","pt-tl","en-tl"]

country_variants = []
translit_names = []
switch_context_lines = []

# Добавление ключа с последними двумя символами в верхнем регистре и транслитерация
for language in data.keys():
    for country_variant in data[language]:
        upper_country_variant = f"{country_variant[:-2]}{country_variant[-2:].upper()}"
        data[language][country_variant].insert(0, upper_country_variant)

        country_name = data[language][country_variant][1]  # Изначальное название страны (после добавления ключа стало вторым элементом)
        translit_name = unidecode(country_name)
        translit_name = translit_name.lower()
        translit_name = re.sub(r'[^a-zA-Z0-9]+-*$' , '', re.sub(r'[^a-zA-Z0-9]+', '-', translit_name))

        # Проверка на совпадение с spisok_dublikatov и модификация translit_name при совпадении
        if country_variant in spisok_dublikatov:
            translit_name = f"{translit_name}-{language}"
        

        data[language][country_variant].append(translit_name)  # Добавляем транслитерацию в конец списка

        # Добавление в списки
        country_variants.append(country_variant)
        translit_names.append(translit_name)
        switch_context_lines.append(f"case '{translit_name}': $modx->switchContext('{translit_name}');\n    break;")


# Конвертация в JSON строку
json_str = json.dumps(data, ensure_ascii=False, indent=4)

# Запись JSON строки в файл
with open(r'SETTINGS\BigData\result_BigData_Lang_Country.json', 'w', encoding='utf-8') as f:
    f.write(json_str)


# Сохранение python словаря с обновлениями
with open(r'SETTINGS\BigData\result_BigData_Lang_Country.py', 'w', encoding='utf-8') as f:
    f.write(f"data = {pformat(data)}")


# Создание и открытие .txt файла для записи
with open(r'SETTINGS\BigData\result_modx_all_context.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.write("|".join(country_variants) + "\n")
    txt_file.write("|".join(translit_names) + "\n")
    txt_file.write(",".join(translit_names) + "\n")
    for line in switch_context_lines:
        txt_file.write(line + "\n")