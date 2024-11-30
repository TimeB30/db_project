import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit
from PyQt5.uic import loadUi
from common_func import *
class EntryWindow(QMainWindow):
    def __init__(self,UserService):
        super(EntryWindow,self).__init__()
        loadUi("ui/entry.ui",self)
        self.sign_up_button.clicked.connect(self.sign_up)
        self.sign_in_button.clicked.connect(self.sign_in)
        line_edits = self.findChildren(QLineEdit)
        self.UserService = UserService
        for i in line_edits:
            i.placeholder_text = i.text()
            i.user_typed = False
            i.focusInEvent = lambda event, line_edit=i: handle_focus_in(event, line_edit)
            i.focusOutEvent = lambda event, line_edit=i: handle_focus_out(event, line_edit)
    def sign_up(self):
        print("yes yes yes")
        widgets.setCurrentIndex(1)
    def sign_in(self):
        if (self.login_line.text() == self.login_line.placeholder_text or self.password_line.text() == self.password_line.placeholder_text):
            self.appointment.setText("Введите логин и пароль")
            return
        user_info = self.UserService.GetUser(self.login_line.text(),self.password_line.text())
        if (user_info.user_id):
            next_widget = MainWindow(self.UserService, user_info)
            widgets.addWidget(next_widget)
            widgets.setCurrentWidget(next_widget)
        self.appointment.setText("Неверный логин или пароль")