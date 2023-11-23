from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout

class EditProfileDialog(QDialog):
    def __init__(self, profile, parent=None):
        super(EditProfileDialog, self).__init__(parent)
        self.profile = profile
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Edit Profile")
        self.setGeometry(200, 200, 300, 200)

        self.layout = QVBoxLayout()
        self.formLayout = QFormLayout()

        # Поля для редактирования
        self.nameEdit = QLineEdit(self.profile.name)
        self.userAgentEdit = QLineEdit(self.profile.user_agent)
        self.startUrlEdit = QLineEdit(self.profile.start_url)

        self.formLayout.addRow("Name:", self.nameEdit)
        self.formLayout.addRow("User-Agent:", self.userAgentEdit)
        self.formLayout.addRow("Start URL:", self.startUrlEdit)

        # Кнопки
        self.buttonsLayout = QHBoxLayout()
        self.saveButton = QPushButton("Save")
        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.setStyleSheet("QPushButton { color: red; }")

        self.buttonsLayout.addWidget(self.saveButton)
        self.buttonsLayout.addWidget(self.cancelButton)

        self.layout.addLayout(self.formLayout)
        self.layout.addLayout(self.buttonsLayout)
        self.setLayout(self.layout)

        # Подключение событий
        self.saveButton.clicked.connect(self.saveProfile)
        self.cancelButton.clicked.connect(self.reject)

    def saveProfile(self):
        self.profile.name = self.nameEdit.text()
        self.profile.user_agent = self.userAgentEdit.text()
        self.profile.start_url = self.startUrlEdit.text()
        self.accept()
