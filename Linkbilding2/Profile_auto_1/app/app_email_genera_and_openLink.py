import requests
import re
import time

API_ENDPOINT = "https://www.1secmail.com/api/v1/"
MAX_RETRIES = 3
WAIT_TIME = 15


def generate_email():
    params = {
        "action": "genRandomMailbox",
        "count": 1
    }
    response = requests.get(API_ENDPOINT, params=params)
    return response.json()[0]


def check_mailbox(email_address):
    login, domain = email_address.split("@")

    for retry in range(MAX_RETRIES):
        params = {
            "action": "getMessages",
            "login": login,
            "domain": domain
        }
        response = requests.get(API_ENDPOINT, params=params)
        messages = response.json()

        if not messages:
            print(f"No messages found. Retrying in {WAIT_TIME} seconds...")
            time.sleep(WAIT_TIME)
        else:
            break

    if not messages:
        print("No messages found after retries. Exiting...")
        return
    
    for message in messages:
        message_id = message['id']
        fetch_message_params = {
            "action": "readMessage",
            "login": login,
            "domain": domain,
            "id": message_id
        }
        fetch_message_response = requests.get(API_ENDPOINT, params=fetch_message_params)
        message_data = fetch_message_response.json()

        if 'textBody' in message_data:
            text_body = message_data['textBody']
            match = re.search(r'\[LINK: (http[^]]+)\]', text_body)
            links = re.findall(r'\[LINK: (http[^]]+)\]', text_body)

            # Поиск первой ссылки, содержащей подстроку "confirm"
            confirm_link = None
            for link in links:
                if "confirm" in link:
                    confirm_link = link
                    break
            if confirm_link:
                print(f"Найдена ссылка: {confirm_link}")
                return confirm_link