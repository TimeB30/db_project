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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1195, 775)
        MainWindow.setStyleSheet("background-image: url(\'C:/Users/TimeB/Desktop/db_project/clouds.jpg\');\n"
                                 "background-repeat: no-repeat;\n"
                                 "background-position: center;\n"
                                 "background-size: cover;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background: transparent; ")
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)

        self.lineEdit_4 = PlaceholderLineEdit("Пароль", self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background: white;\n"
                                      "border: none;                \n"
                                      "    border-radius: 10px;        \n"
                                      "    padding: 10px 20px;          ")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        # Используем кастомные PlaceholderLineEdit
        self.lineEdit_3 = PlaceholderLineEdit("Логин", self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background: white;\n"
                                      "border: none;                \n"
                                      "    border-radius: 10px;        \n"
                                      "    padding: 10px 20px;          ")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "    background: rgb(0, 148, 216);\n"
                                        "    color: white;\n"
                                        "    border: none;\n"
                                        "    border-radius: 10px;\n"
                                        "    padding: 10px 20px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background: rgb(0, 120, 190); /* Цвет при наведении */\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background: rgb(0, 100, 160); /* Цвет при нажатии */\n"
                                        "}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 5, 1, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 2, 1, 1)



        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
                                        "    background: rgb(0, 148, 216);\n"
                                        "    color: white;\n"
                                        "    border: none;\n"
                                        "    border-radius: 10px;\n"
                                        "    padding: 10px 20px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background: rgb(0, 120, 190); /* Цвет при наведении */\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background: rgb(0, 100, 160); /* Цвет при нажатии */\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 1, 1, 1)
        self.pushButton_3.clicked.connect(self.pushButton_3_action)

        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.setText("Tasker")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1195, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_4.setFocus()
    def pushButton_3_action(self):
        if self.lineEdit_3.text() == "Логин":
            self.lineEdit_3.setText("Введите логин")
        if self.lineEdit_4.text() == "Пароль":
            self.lineEdit_4.setText("Введите пароль")
    def pushButton_4_action(self):
        self.pushButton_4.setText("have work to do")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Войти"))
        self.pushButton_4.setText(_translate("MainWindow", "Зарегистрироваться"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
