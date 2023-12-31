import requests
import xmltodict
import re
import time

# XML_APIS = [
# '/api/device/information',
# '/api/device/signal',
# '/api/monitoring/status',
# '/api/monitoring/traffic-statistics',
# '/api/dialup/connection',
# '/api/global/module-switch',
# '/api/net/current-plmn',
# '/api/net/net-mode',
# ]

def get_token_and_cookie(base_url):
    """
    Получает токен и куки для аутентификации запросов.
    tuple: Возвращает токен и куки (если запрос успешен), иначе (None, None).
    """
    with requests.Session() as session:
        response = session.get(base_url + '/api/webserver/SesTokInfo')
        if response.status_code == 200:
            ses_info = re.search(r"<SesInfo>(.*?)</SesInfo>", response.text)
            tok_info = re.search(r"<TokInfo>(.*?)</TokInfo>", response.text)
            if ses_info and tok_info:
                return tok_info.group(1), ses_info.group(1)
    return None, None

def set_network_mode(base_url, mode):
    """
    Устанавливает сетевой режим модема.
    Режим сети ('01' для GSM, '03' для LTE).
    Returns:
    bool: True, если запрос успешен, иначе False.
    """
    token, cookie = get_token_and_cookie(base_url)
    if token and cookie:
        headers = {'__RequestVerificationToken': token, 'Content-Type': 'application/xml', 'Cookie': cookie}
        data = f"<?xml version='1.0' encoding='UTF-8'?><request><NetworkMode>{mode}</NetworkMode><NetworkBand>3FFFFFFF</NetworkBand><LTEBand>7FFFFFFFFFFFFFFF</LTEBand></request>"
        with requests.Session() as session:
            response = session.post(base_url + '/api/net/net-mode', data=data, headers=headers)
            return response.status_code == 200
    return False


def change_network_mode(base_url, mode):
    """
    Переключает сетевой режим модема и выводит результат.
    host (str): IP-адрес модема.
    mode (str): Режим сети ('01' для GSM, '03' для LTE).
    """
    if set_network_mode(base_url, mode):
        print(f"Сетевой режим успешно изменен на {'LTE' if mode == '03' else 'GSM'}.")
    else:
        print(f"Ошибка при изменении сетевого режима на {'LTE' if mode == '03' else 'GSM'}.")
    
def get_device_information(base_url):
    """
    Получает информацию об устройстве.
    Args:
    session (requests.Session): Активная сессия requests.
    base_url (str): Базовый URL модема.
    token (str): Токен для аутентификации.
    cookie (str): Куки для аутентификации.
    Returns:
    dict: Информация об устройстве, если запрос успешен.
    """
    token, cookie = get_token_and_cookie(base_url)
    headers = {'__RequestVerificationToken': token, 'Cookie': cookie}
    with requests.Session() as session:
        response = session.get(base_url + '/api/device/information', headers=headers)
    if response.status_code == 200:
        try:
            return xmltodict.parse(response.text).get('response', None)
        except Exception as e:
            print(f"Ошибка при разборе XML: {e}")
    return None

# def device_info_parametres(base_url):
#     device_info= get_device_information(base_url).get('WanIPAddress')
#     if device_info:
#         device_name = f"Имя устройства: {device_info.get('DeviceName')}"
#         telephone = f"Номер телефона: {device_info.get('Msisdn')}"
#         ip4 = f"IP-адрес WAN: {device_info.get('WanIPAddress')}"
#         ipv6 = f"IPv6-адрес WAN: {device_info.get('WanIPv6Address')}"
#         return 
#     else:
#         print("Не удалось получить информацию об устройстве.")


def wait_for_connection(base_url, timeout=60):
    """
    Ожидает установления соединения, проверяя статус каждые 2 секунды.

    Args:
    base_url (str): Базовый URL модема.
    timeout (int): Максимальное время ожидания в секундах.

    Returns:
    bool: True, если соединение установлено, иначе False.
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        token, cookie = get_token_and_cookie(base_url)
        if token and cookie:
            headers = {'__RequestVerificationToken': token, 'Cookie': cookie}
            with requests.Session() as session:
                response = session.get(base_url + '/api/monitoring/status', headers=headers)
            if response.status_code == 200:
                try:
                    status_info = xmltodict.parse(response.text).get('response', None)
                    if status_info and status_info.get('ConnectionStatus') == '901':
                        # elapsed_time = time.time() - start_time
                        # print(f"Соединение установлено за {elapsed_time:.2f} секунд.")
                        return True
                except Exception as e:
                    print(f"Ошибка при разборе XML: {e}")
        time.sleep(2)
    return False



def main_E3372_Restart(host):
    base_url = f"http://{host}"
    # Текущий IP
    print(get_device_information(base_url).get('WanIPAddress'))

    old_ip = get_device_information(base_url).get('WanIPAddress')
    change_network_mode(base_url, '01')  # GSM
    # Очікуємо
    wait_for_connection(base_url)

    change_network_mode(base_url, '03')  # LTE
    # Очікуємо
    wait_for_connection(base_url)


    smena_ip = f"RESULT for {get_device_information(base_url).get('DeviceName')}, {get_device_information(base_url).get('Msisdn')}: \
        IP4({old_ip}) -->  IP4({get_device_information(base_url).get('WanIPAddress')})"
    print(smena_ip) 


# Пример использования
# host = "192.168.8.1"  # Замените на реальный адрес вашего модема
# main_E3372_Restart(host)