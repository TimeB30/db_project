from PyQt5 import QtCore, QtGui, QtWidgets

class FirstWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Первый экран")
        self.setGeometry(100, 100, 400, 300)

        self.button = QtWidgets.QPushButton("Перейти ко второму экрану", self)
        self.button.clicked.connect(self.go_to_second_screen)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)

    def go_to_second_screen(self):
        self.parent().setCurrentIndex(1)  # Переход к следующему экрану


class SecondWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Второй экран")
        self.setGeometry(100, 100, 400, 300)

        self.button = QtWidgets.QPushButton("Вернуться на первый экран", self)
        self.button.clicked.connect(self.go_to_first_screen)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)

    def go_to_first_screen(self):
        self.parent().setCurrentIndex(0)  # Переход обратно к первому экрану


class MainWindow(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()

        # Создание двух экранов (виджетов)
        self.first_widget = FirstWidget()
        self.second_widget = SecondWidget()

        # Добавление виджетов в StackedWidget
        self.addWidget(self.first_widget)
        self.addWidget(self.second_widget)

        # Устанавливаем начальный экран
        self.setCurrentIndex(0)

        self.setWindowTitle("Переключение экранов")
        self.setGeometry(100, 100, 400, 300)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
