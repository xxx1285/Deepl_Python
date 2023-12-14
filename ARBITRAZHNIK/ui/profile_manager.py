import json
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                             QTableWidget, QTableWidgetItem, QMessageBox, QInputDialog,
                             QCheckBox)
from ui.edit_profile import EditProfileDialog
from app.profile import Profile
from app.browser_launcher import BrowserLauncher


class ProfileManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.profiles = []
        self.loadProfiles()
        self.updateProfileList()

    def initUI(self):
        self.setWindowTitle("Profile Manager")
        self.setGeometry(200, 200, 600, 300)  # Увеличено для лучшего отображения таблицы

        self.layout = QVBoxLayout(self)

        self.profile_table = QTableWidget(0, 8)  # 8 столбцов
        self.profile_table.setHorizontalHeaderLabels(['№', 'Select', 'Name', 'Country', 'User-Agent', 'Start URL', 'Edit', 'Launch'])
        self.layout.addWidget(self.profile_table)

        self.buttons_layout = QHBoxLayout()
        self.add_profile_button = QPushButton("Add Profile")
        self.add_profile_button.clicked.connect(self.addProfile)
        self.buttons_layout.addWidget(self.add_profile_button)

        self.remove_profile_button = QPushButton("Remove Selected Profiles")
        self.remove_profile_button.clicked.connect(self.removeSelectedProfiles)
        self.buttons_layout.addWidget(self.remove_profile_button)

        self.layout.addLayout(self.buttons_layout)

        self.profiles = []
        self.loadProfiles()
        self.updateProfileList()

    def updateProfileList(self):
        self.profile_table.setRowCount(0)
        for idx, profile in enumerate(self.profiles):
            row = self.profile_table.rowCount()
            self.profile_table.insertRow(row)

            # Добавление данных профиля
            self.profile_table.setItem(row, 0, QTableWidgetItem(str(idx + 1)))
            self.profile_table.setItem(row, 2, QTableWidgetItem(profile.name))
            self.profile_table.setItem(row, 3, QTableWidgetItem(profile.country))
            self.profile_table.setItem(row, 4, QTableWidgetItem(profile.user_agent))
            self.profile_table.setItem(row, 5, QTableWidgetItem(profile.start_url or "http://example.com"))

            # Checkboxes for selection
            checkbox = QCheckBox()
            self.profile_table.setCellWidget(row, 1, checkbox)

            # Кнопки запуска и редактирования
            launch_button = QPushButton("Launch")
            launch_button.setFixedSize(80, 30)
            launch_button.clicked.connect(lambda checked, p=profile: self.launchBrowserWithProfile(p))
            edit_button = QPushButton("Edit")
            edit_button.setFixedSize(80, 30)
            edit_button.clicked.connect(lambda checked, p=profile: self.editProfile(p))

            button_layout = QHBoxLayout()
            button_layout.addWidget(launch_button)
            button_layout.addWidget(edit_button)
            button_widget = QWidget()
            button_widget.setLayout(button_layout)
            self.profile_table.setCellWidget(row, 6, button_widget)

    def addProfile(self):
        name, ok = QInputDialog.getText(self, 'Add Profile', 'Enter profile name:')
        if ok and name:
            user_agent, ok = QInputDialog.getText(self, 'Add Profile', 'Enter user agent:')
            if ok and user_agent:
                start_url, ok = QInputDialog.getText(self, 'Add Profile', 'Enter start URL:')
                new_profile = Profile(name, user_agent, start_url=start_url)
                self.profiles.append(new_profile)
                self.updateProfileList()
                self.saveProfiles()


    def editProfile(self, profile):
        dialog = EditProfileDialog(profile, self)
        if dialog.exec_():
            self.updateProfileList()
            self.saveProfiles()

    def removeProfile(self):
        selected_rows = set()
        for item in self.profile_table.selectedItems():
            selected_rows.add(item.row())
        for row in sorted(selected_rows, reverse=True):
            del self.profiles[row]
        self.updateProfileList()
        self.saveProfiles()

    def removeSelectedProfiles(self):
        selected_rows = set()
        for idx in range(self.profile_table.rowCount()):
            checkbox = self.profile_table.cellWidget(idx, 1)
            if checkbox and checkbox.isChecked():
                selected_rows.add(idx)
        for row in sorted(selected_rows, reverse=True):
            del self.profiles[row]
        self.updateProfileList()
        self.saveProfiles()

    def saveProfiles(self):
        with open('ARBITRAZHNIK\profiles\profiles.json', 'w') as file:
            json.dump([p.__dict__ for p in self.profiles], file)

    def loadProfiles(self):
        try:
            with open('ARBITRAZHNIK\profiles\profiles.json', 'r') as file:
                profiles_data = json.load(file)
                self.profiles = [Profile(**data) for data in profiles_data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.profiles = []

    def launchBrowserWithProfile(self, profile):
        launcher = BrowserLauncher()
        launcher.launch_browser(profile)
