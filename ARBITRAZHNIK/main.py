import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile, QTextStream
from ui.main_window import MainWindow


def loadStyles(stylesheetFile):
    """
    Загружает стили из внешнего файла.

    :param stylesheetFile: Путь к файлу со стилями.
    :return: Строка со стилями.
    """
    file = QFile(stylesheetFile)
    if not file.open(QFile.ReadOnly | QFile.Text):
        print(f"Не удалось открыть файл стилей: {stylesheetFile}")
        return ""
    stream = QTextStream(file)
    styles = stream.readAll()
    file.close()
    return styles


def main():
    # Создаем экземпляр QApplication
    app = QApplication(sys.argv)

    # Загрузка и применение стилей ко всему приложению
    styles = loadStyles("ARBITRAZHNIK/resources/styles/style.css")
    app.setStyleSheet(styles)

    # Создаем и показываем главное окно приложения
    main_window = MainWindow()
    main_window.show()
    # Запускаем основной цикл приложения
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
