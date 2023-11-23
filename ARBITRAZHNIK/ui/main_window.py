from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton
from ui.profile_manager import ProfileManager  # Предполагается, что этот класс будет определен в profile_manager.py
from ui.settings_window import SettingsWindow  # Аналогично, для settings_window.py

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Profile Manager")  # Заголовок окна
        self.setGeometry(100, 100, 800, 600)    # Размеры и позиция окна

        self.central_widget = QWidget()         # Центральный виджет
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()             # Вертикальное расположение виджетов
        self.central_widget.setLayout(self.layout)

        self.profile_manager = ProfileManager() # Экземпляр менеджера профилей
        self.settings_window = SettingsWindow() # Экземпляр окна настроек

        self.initUI()

    def initUI(self):
        # Создаем кнопки
        open_profile_manager_button = QPushButton("Open Profile Manager", self)
        open_profile_manager_button.clicked.connect(self.openProfileManager)

        open_settings_button = QPushButton("Open Settings", self)
        open_settings_button.clicked.connect(self.openSettings)

        self.layout.addWidget(open_profile_manager_button)
        self.layout.addWidget(open_settings_button)

    def openProfileManager(self):
        # Открываем окно менеджера профилей
        self.profile_manager.show()

    def openSettings(self):
        # Открываем окно настроек
        self.settings_window.show()
