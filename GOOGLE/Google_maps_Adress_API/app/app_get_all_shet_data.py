from typing import List, Dict

def get_sheet_data(client, spreadsheet_key: str) -> List[List[str]]:
    """
    Получение данных из Google таблицы.

    :param client: Авторизованный клиент gspread.
    :param spreadsheet_key: Ключ Google таблицы. "1nZxr6X9uhfBwmf*******fs7ZpWI8da-NrXvk"
    :return: Данные из таблицы.
    """
    sheet = client.open_by_key(spreadsheet_key).sheet1
    return sheet.get_all_values()