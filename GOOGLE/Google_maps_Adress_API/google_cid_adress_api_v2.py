import requests
import json
import urllib.parse
from typing import List, Dict

from app.app_authenticate_google_sheets import authenticate_google_sheets
from app.app_get_all_shet_data import get_sheet_data

# INSTADIVAAN = 8207621176809025478
# FRAYAMEBEL = 13280552074301093291
# clothes repair Dubai = 13683745809905570146
CID_MY_COMPANY = 13280552074301093291
CID_PLACE_TARGET = ['18050907804186843608']
# Dubai 13683745809905570146   Борисполь  18050907804186843608

spreadsheet_key = "1nZor6X9uhfBwmffUMnYar2sxmLvfs5ZpWI8da-NrXvk"    # ключ Google таблици
service_key_google_sheets = r"GOOGLE\Google_maps_Adress_API\config\serv-account-Google-Sheets-API-KEY.json"
save_urls_CIT_result = r"GOOGLE\Google_maps_Adress_API\output\CID_URLs_Borispol_Freyamebel_16-01-2024.txt"


def fun_cid_combi_url(keyword, cid_target_place, CID_MY_COMPANY):
    encoded_str_keyword = urllib.parse.quote(keyword.encode('utf-8'))
    combi_url = f"https://www.google.com/search?q={encoded_str_keyword}&oq={encoded_str_keyword}&rldimm={cid_target_place}&rlst=f#rlfi=hd:;si:{CID_MY_COMPANY}" 
    return combi_url

def process_headers(headers: List[str]):
    """
    :param headers: Список заголовков.
    """
    print("Headers:", headers)

def main():
    try:
        client = authenticate_google_sheets(service_key_google_sheets)
        data = get_sheet_data(client, spreadsheet_key)

        if data:
            headers = data[0]  # Первая строка содержит заголовки
            process_headers(headers)

            with open(save_urls_CIT_result, 'w', encoding='utf-8') as file:
                for row in data[1:]:  # Обработка данных, начиная со второй строки
                    row_data = dict(zip(headers, row))
                    if row_data['CID_target_num'] in CID_PLACE_TARGET and row_data['CID_my_company'] == str(CID_MY_COMPANY):
                        keywords = row_data['keyword'].split(', ')
                        cid_target_place = row_data['CID_target_num']
                        for keyword in keywords:
                            line = fun_cid_combi_url(keyword, cid_target_place, CID_MY_COMPANY)
                            file.write(line + '\n')
        else:
            print("Таблица пуста.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == '__main__':
    main()
