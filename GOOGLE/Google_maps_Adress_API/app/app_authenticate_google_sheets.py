import gspread
from oauth2client.service_account import ServiceAccountCredentials

def authenticate_google_sheets(service_key_google_sheets: str):
    """
    Аутентификация и создание клиента для Google Sheets.

    :param service_key_google_sheets: Путь к файлу учетных данных.
    :return: Авторизованный клиент gspread.
    """
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(service_key_google_sheets, scope)
    return gspread.authorize(creds)



# Шаги для создания файла учетных данных:
# Создайте проект в Google Cloud Console:

# Перейдите на Google Cloud Console.
# Если у вас еще нет аккаунта Google Cloud, вам нужно его создать.
# Затем создайте новый проект.
# Включите Google Sheets API для вашего проекта:

# Внутри вашего проекта перейдите в раздел "API и сервисы" > "Библиотека".
# Найдите "Google Sheets API" и включите его для вашего проекта.
# Создайте учетные данные:

# После активации API перейдите в раздел "Учетные данные".
# Нажмите "Создать учетные данные" и выберите "Сервисный аккаунт".
# Следуйте инструкциям для создания сервисного аккаунта. В процессе вы зададите имя аккаунта и определите его роль. В качестве роли можно выбрать "Редактор" или любую другую, которая подходит под ваши нужды.
# После создания сервисного аккаунта, вам нужно создать ключ. Нажмите на созданный сервисный аккаунт, выберите вкладку "Ключи" и создайте новый ключ. Выберите тип ключа JSON и скачайте его.
# Файл, который вы скачаете, и есть creds_file:

# Этот JSON-файл содержит необходимые учетные данные для аутентификации вашего приложения.
# В вашем Python скрипте вы должны указать путь к этому файлу (например, creds_file = 'path/to/your/credentials.json').