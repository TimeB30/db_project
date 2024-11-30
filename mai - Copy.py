from PyQt5 import QtCore, QtGui, QtWidgets
class PlaceholderLineEdit(QtWidgets.QLineEdit):
    def __init__(self, placeholder_text, parent=None):
        super().__init__(parent)
        self.placeholder_text = placeholder_text
        self.setText(self.placeholder_text)
        self.user_typed = False

    def focusInEvent(self, event):
        if not self.user_typed and (self.text() == self.placeholder_text or self.text() == "Введите логин" or self.text() == "Введите пароль"):
            self.setText("")  # Очищаем поле
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        if not self.text().strip():  # Если поле пустое
            self.setText(self.placeholder_text)
            self.user_typed = False
        else:
            self.user_typed = True
        super().focusOutEvent(event)

class FirstWidget(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("works")
        self.setStyleSheet("background: transparent;")
        gridLayout = QtWidgets.QGridLayout(self)
        push_button = QtWidgets.QPushButton(self)
        gridLayout.addWidget(push_button, 43, 55)
class MainWindow(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()

        # Создание двух экранов (виджетов)
        self.first_widget = FirstWidget()
        # self.second_widget = SecondWidget()

        # Добавление виджетов в StackedWidget
        self.addWidget(self.first_widget)
        # self.addWidget(self.second_widget)

        # Устанавливаем начальный экран
        self.setCurrentWidget(self.first_widget)

        self.setWindowTitle("Переключение экранов")
        self.resize(1195, 775)
        self.setStyleSheet("background-image: url(\'C:/Users/TimeB/Desktop/db_project/clouds.jpg\');\n"
                           "background-repeat: no-repeat;\n"
                           "background-position: center;\n"
                           "background-size: cover;")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
