import requests
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

API_ENDPOINT = "https://www.1secmail.com/api/v1/"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, r"json_all_email\mailboxes.json")


class EmailApp:
    def __init__(self, root):
        self.root = root
        self.root.title("1SecMail Client")
        self.root.minsize(700, 0)  # Установка минимальной ширины

        self.mailboxes = []
        self.load_mailboxes()

        # Left Frame
        left_frame = ttk.Frame(root)
        left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.generate_btn = ttk.Button(left_frame, text="Generate New Email", command=self.generate_email)
        self.generate_btn.grid(row=0, column=0, pady=20, sticky="ew")

        # Добавим стиль для красных кнопок
        style = ttk.Style()
        style.configure("Red.TButton", foreground="red")

        self.mailbox_listbox_scroll = ttk.Scrollbar(left_frame)
        self.mailbox_listbox_scroll.grid(row=1, column=1, sticky="ns")

        self.mailbox_listbox = tk.Listbox(left_frame, width=30, height=15, yscrollcommand=self.mailbox_listbox_scroll.set)
        self.mailbox_listbox.grid(row=1, column=0, pady=20, sticky="ew")
        self.mailbox_listbox.bind('<Button-3>', self.copy_to_clipboard)

        self.mailbox_listbox_scroll.config(command=self.mailbox_listbox.yview)
        self.load_listbox()

        self.delete_all_mailboxes_btn = ttk.Button(left_frame, text="Delete All Emails", command=self.delete_all_mailboxes, style="Red.TButton")
        self.delete_all_mailboxes_btn.grid(row=2, column=0, pady=10, sticky="ew")

        # Right Frame
        right_frame = ttk.Frame(root)
        right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.check_btn = ttk.Button(right_frame, text="Check Selected Mailbox", command=self.check_mailbox)
        self.check_btn.grid(row=0, column=0, pady=20, sticky="ew")

        self.messages_listbox_scroll = ttk.Scrollbar(right_frame)
        self.messages_listbox_scroll.grid(row=1, column=1, sticky="ns")

        self.messages_listbox = tk.Listbox(right_frame, width=100, height=10, yscrollcommand=self.messages_listbox_scroll.set)
        self.messages_listbox.grid(row=1, column=0, pady=20, sticky="ew")
        self.messages_listbox_scroll.config(command=self.messages_listbox.yview)
        
        # Добавьте обработчик событий для messages_listbox
        self.messages_listbox.bind('<<ListboxSelect>>', self.auto_load_message_content)

        self.view_btn = ttk.Button(right_frame, text="View Message", command=self.view_message)
        self.view_btn.grid(row=2, column=0, pady=20, sticky="ew")

        message_content_frame = ttk.Frame(right_frame)
        message_content_frame.grid(row=3, column=0, columnspan=2, pady=20, sticky="nsew")

        self.message_content = tk.Text(message_content_frame, wrap=tk.WORD, height=10, width=75)
        self.message_content.grid(row=0, column=0, sticky="nsew")

        self.message_content_scroll = ttk.Scrollbar(message_content_frame, command=self.message_content.yview)
        self.message_content_scroll.grid(row=0, column=1, sticky="ns")
        self.message_content.config(yscrollcommand=self.message_content_scroll.set)


    def load_mailboxes(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                self.mailboxes = json.load(file)

    def auto_load_message_content(self, event):
        # Этот метод автоматически загружает содержимое сообщения при выборе письма
        self.view_message()

    # Функция для удаления всех почтовых ящиков
    def delete_all_mailboxes(self):
        self.mailboxes.clear()
        self.save_mailboxes()
        self.load_listbox()

    def save_mailboxes(self):
        with open(DATA_FILE, 'w') as file:
            json.dump(self.mailboxes, file)

    def load_listbox(self):
        self.mailbox_listbox.delete(0, tk.END)
        for index, mailbox in enumerate(self.mailboxes, 1):  # начинаем с 1
            self.mailbox_listbox.insert(tk.END, f"{index}. {mailbox}")


    def generate_email(self):
        params = {
            "action": "genRandomMailbox",
            "count": 1
        }
        response = requests.get(API_ENDPOINT, params=params)
        self.email_address = response.json()[0]
        self.mailboxes.append(self.email_address)
        self.save_mailboxes()
        self.load_listbox()

    def check_mailbox(self):
        selected_index = self.mailbox_listbox.curselection()
        if not selected_index:
            return
        # Получаем адрес без номера порядка
        selected_mailbox_with_number = self.mailboxes[selected_index[0]]
        self.email_address = selected_mailbox_with_number.split(". ", 1)[-1]

        login, domain = self.email_address.split("@")
        params = {
            "action": "getMessages",
            "login": login,
            "domain": domain
        }
        response = requests.get(API_ENDPOINT, params=params)
        self.messages = response.json()

        self.messages_listbox.delete(0, tk.END)
        for message in self.messages:
            date_time = message['date']  # предполагается, что у сообщения есть поле 'date'
            self.messages_listbox.insert(tk.END, f"{date_time} - {message['from']} - {message['subject']}")


    def view_message(self):
        selected_index = self.messages_listbox.curselection()
        if not selected_index:
            return
        message = self.messages[selected_index[0]]

        login, domain = self.email_address.split("@")
        params = {
            "action": "readMessage",
            "login": login,
            "domain": domain,
            "id": message['id']
        }
        response = requests.get(API_ENDPOINT, params=params)
        message_content = response.json()

        self.message_content.delete(1.0, tk.END)
        self.message_content.insert(tk.END, message_content['textBody'])

    def copy_to_clipboard(self, event):
        selected_index = self.mailbox_listbox.curselection()
        if not selected_index:
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(self.mailboxes[selected_index[0]])
        messagebox.showinfo("Info", "Mailbox copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmailApp(root)
    root.mainloop()