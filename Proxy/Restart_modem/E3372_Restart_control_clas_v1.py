import requests
import xmltodict
import re
import time

class ModemController:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_token_and_cookie(self):
        with requests.Session() as session:
            response = session.get(self.base_url + '/api/webserver/SesTokInfo')
            if response.status_code == 200:
                ses_info = re.search(r"<SesInfo>(.*?)</SesInfo>", response.text)
                tok_info = re.search(r"<TokInfo>(.*?)</TokInfo>", response.text)
                if ses_info and tok_info:
                    return tok_info.group(1), ses_info.group(1)
        return None, None

    def set_network_mode(self, mode):
        token, cookie = self.get_token_and_cookie()
        if token and cookie:
            headers = {'__RequestVerificationToken': token, 'Content-Type': 'application/xml', 'Cookie': cookie}
            data = f"<?xml version='1.0' encoding='UTF-8'?><request><NetworkMode>{mode}</NetworkMode><NetworkBand>3FFFFFFF</NetworkBand><LTEBand>7FFFFFFFFFFFFFFF</LTEBand></request>"
            with requests.Session() as session:
                response = session.post(self.base_url + '/api/net/net-mode', data=data, headers=headers)
                return response.status_code == 200
        return False

    def change_network_mode(self, mode):
        if self.set_network_mode(mode):
            mode_name = 'LTE' if mode == '03' else 'GSM'
            print(f"Сетевой режим успешно изменен на {mode_name}.")
        else:
            print(f"Ошибка при изменении сетевого режима на {mode}.")

    def get_device_information(self):
        token, cookie = self.get_token_and_cookie()
        if token and cookie:
            headers = {'__RequestVerificationToken': token, 'Cookie': cookie}
            with requests.Session() as session:
                response = session.get(self.base_url + '/api/device/information', headers=headers)
            if response.status_code == 200:
                try:
                    return xmltodict.parse(response.text).get('response', None)
                except Exception as e:
                    print(f"Ошибка при разборе XML: {e}")
        return None

    def wait_for_connection(self, timeout=60):
        start_time = time.time()
        while time.time() - start_time < timeout:
            token, cookie = self.get_token_and_cookie()
            if token and cookie:
                headers = {'__RequestVerificationToken': token, 'Cookie': cookie}
                with requests.Session() as session:
                    response = session.get(self.base_url + '/api/monitoring/status', headers=headers)
                if response.status_code == 200:
                    try:
                        status_info = xmltodict.parse(response.text).get('response', None)
                        if status_info and status_info.get('ConnectionStatus') == '901':
                            return True
                    except Exception as e:
                        print(f"Ошибка при разборе XML: {e}")
            time.sleep(2)
        return False

    def main_restart(self):
        old_ip = self.get_device_information().get('WanIPAddress')
        self.change_network_mode('01')  # GSM
        self.wait_for_connection()

        self.change_network_mode('03')  # LTE
        self.wait_for_connection()

        new_ip = self.get_device_information().get('WanIPAddress')
        print(f"RESULT: IP4({old_ip}) --> IP4({new_ip})")
