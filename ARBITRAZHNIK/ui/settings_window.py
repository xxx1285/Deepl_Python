from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class SettingsWindow(QWidget):
    def __init__(self):
        super(SettingsWindow, self).__init__()

        self.setWindowTitle("Settings")
        self.setGeometry(300, 300, 300, 200)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Пример настройки: путь к браузеру
        self.layout.addWidget(QLabel("Path to Browser:"))
        self.browser_path_edit = QLineEdit(self)
        self.layout.addWidget(self.browser_path_edit)

        # Кнопка для сохранения настроек
        self.save_settings_button = QPushButton("Save Settings", self)
        self.save_settings_button.clicked.connect(self.saveSettings)
        self.layout.addWidget(self.save_settings_button)

    def saveSettings(self):
        # Здесь должна быть логика для сохранения настроек
        browser_path = self.browser_path_edit.text()
        print("Settings Saved:", browser_path)  # Пример вывода, заменить на реальное сохранение настроек
