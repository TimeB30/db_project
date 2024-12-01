import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QWidget, QPushButton
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QIcon
from services import *
import re
def is_password_secure(password):
    if len(password) < 8:
        return False, "Пароль должен быть\nне короче 8 символов."

    if not re.search(r"\d", password):
        return False, "Пароль должен\nсодержать хотя бы одну цифру."

    if not re.search(r"[A-Z]", password):
        return False, "Пароль должен\nсодержать хотя бы одну заглавную букву."

    if not re.search(r"[a-z]", password):
        return False, "Пароль должен\nсодержать хотя бы одну строчную букву."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Пароль должен\nсодержать хотя бы один специальный символ."
    return True, "Пароль безопасен."
def go_to(widgets,widget_name):
    next_widget = widgets.findChild(QWidget, widget_name)
    widgets.setCurrentWidget(next_widget)
def handle_focus_in(event, line_edit):
    """Обработка события focusIn (при получении фокуса)."""
    if not hasattr(line_edit, "user_typed"):
        line_edit.user_typed = False
    if not line_edit.user_typed and (line_edit.text() == line_edit.placeholder_text or line_edit.text() in ["Введите логин", "Введите пароль"]):
        line_edit.setText("")
    QLineEdit.focusInEvent(line_edit, event)


def handle_focus_out(event, line_edit):
    """Обработка события focusOut (при потере фокуса)."""
    if not hasattr(line_edit, "user_typed"):
        line_edit.user_typed = False
    if not line_edit.text().strip():
        line_edit.setText(line_edit.placeholder_text)
        line_edit.user_typed = False
    else:
        line_edit.user_typed = True
    QLineEdit.focusOutEvent(line_edit, event)
def rows(users,path):
    layout = QVBoxLayout()
    for i in users.users_info:
        row = loadUi(path)
        row.task.setText(f"{i.user_name}: {i.user_role}")
        row.setMinimumSize(0, 60)
        layout.addWidget(row)
    layout.setObjectName("main_layout")
    return layout
def admin_rows(users,path,func,admin_id):
    layout = QVBoxLayout()
    for i in users.users_info:
        row = loadUi(path)
        row.task.setText(f"{i.user_name}: {i.user_role}")
        row.setMinimumSize(0, 60)
        if (i.user_id == admin_id):
            row.button.deleteLater()
            layout.addWidget(row)
            continue
        row.button.setProperty("user_info",i)
        row.button.setText(":")
        row.button.clicked.connect(func)
        layout.addWidget(row)
    layout.setObjectName("main_layout")
    return layout
class EntryWindow(QMainWindow):
    def __init__(self,UserService):
        self.UserService = UserService
        super(EntryWindow,self).__init__()
        loadUi("ui/entry.ui",self)
        self.sign_up_button.clicked.connect(self.sign_up)
        self.sign_in_button.clicked.connect(self.sign_in)
        line_edits = self.findChildren(QLineEdit)
        for i in line_edits:
            i.placeholder_text = i.text()
            i.user_typed = False
            i.focusInEvent = lambda event, line_edit=i: handle_focus_in(event, line_edit)
            i.focusOutEvent = lambda event, line_edit=i: handle_focus_out(event, line_edit)
    def sign_up(self):
        self.setCentralWidget(RegistrationWindow(self.UserService))
    def sign_in(self):
        if (self.login_line.text() == self.login_line.placeholder_text or self.password_line.text() == self.password_line.placeholder_text):
            self.appointment.setText("Введите логин и пароль")
            return
        user_info = self.UserService.GetUser(self.login_line.text(),self.password_line.text())
        if (user_info.user_id):
            self.login_line.setText("")
            self.password_line.setText("")
            self.appointment.setText("")
            if (user_info.block_id == 0):
                request = self.UserService.GetRequest(user_info.user_id)
                if (request.request_id == 0):
                    next_widget = NoBlockWindow(self.UserService,user_info)
                    self.setCentralWidget(next_widget)
                else:
                    self.setCentralWidget( RequestSentWindow(self.UserService,user_info,request))

                return
            self.setCentralWidget(MainWindow(self.UserService, user_info))
            return
        self.appointment.setText("Неверный логин или пароль")
class RegistrationWindow(QMainWindow):
    def __init__(self,UserService):
        super(RegistrationWindow,self).__init__()
        loadUi("ui/registration.ui",self)
        self.back_button.clicked.connect(self.back)
        self.UserService = UserService
        self.registry_button.clicked.connect(self.registry_button_func)
        line_edits = self.findChildren(QLineEdit)
        for i in line_edits:
            i.placeholder_text = i.text()
            i.user_typed = False
            i.focusInEvent = lambda event, line_edit = i: handle_focus_in(event, line_edit)
            i.focusOutEvent = lambda event, line_edit = i: handle_focus_out(event, line_edit)
    def back(self):
        self.setCentralWidget(EntryWindow(self.UserService))
    def registry_button_func(self):
        line_edits = self.findChildren(QLineEdit)
        for i in line_edits:
            if (i.text() == i.placeholder_text):
                if (i.objectName() == "middle_name_line"):
                    i.setText("")
                    continue
                self.appointment.setText("! Заполните все поля")
                return
        user_login = self.login_line.text()
        user_password = self.password_line.text()
        if (len(user_login) < 4):
            self.appointment.setText("! Логин должен состоять\n минимум из 4 символов")
            return
        is_secure, message = is_password_secure(user_password)
        if not (is_secure):
            self.appointment.setText(message)
            return
        is_user = self.UserService.CheckLogin(user_login).is_busy
        if not (is_user):
            user_name = self.name_line.text()
            user_surname = self.surname_line.text()
            user_middle_name = self.middle_name_line.text()
            user_id = self.UserService.Register(user_name=user_name, user_surname=user_surname, user_middle_name=user_middle_name,
                                      user_login=user_login, user_password=user_password).user_id
            if (user_id == 0):
                self.appointment.setText("!Ошибка, попробуйте снова")
                return
            user_info = services_pb2.GetUserResponse(user_id=user_id,user_name=user_name,user_role="user",block_id=0,dorm_id=0)
            self.setCentralWidget(NoBlockWindow(self.UserService, user_info))
        self.appointment.setText("!Логин уже занят")
class MainWindow(QMainWindow):
    def __init__(self,UserService,user_info):
        self.user_info = user_info
        self.UserService = UserService
        super(MainWindow,self).__init__()
        loadUi("ui/main.ui",self)
        layout = QVBoxLayout()
        self.scroll_area.setMinimumSize(0, 200)
        self.history_button.clicked.connect(self.history_button_func)
        self.leave_button.clicked.connect(self.leave_button_func)
        self.exit_button.clicked.connect(self.exit_button_func)
        self.users_button.clicked.connect(self.users_button_func)
        self.tasks_button.clicked.connect(self.tasks_button_func)
        self.tasks_info = self.UserService.GetUserTasks(user_info.user_id)
        if (self.user_info.user_role == "admin"):
            requests_info = self.UserService.GetRequests(self.user_info.block_id)
            for i in requests_info.requests:
                if i.status != "declined":
                    row = loadUi("ui/row.ui")
                    button = loadUi("ui/decline_button.ui",row)
                    decline_button = button.decline_button
                    decline_button.clicked.connect(self.decline_user)
                    decline_button.setProperty("request",i)
                    decline_button.setObjectName("decline_button")
                    row.task.setText(f"Заявка от {i.user_surname} {i.user_name}")
                    row.button.setText("Принять")
                    row.horizontalLayout.addWidget(decline_button)
                    row.button.setProperty("request",i)
                    row.button.clicked.connect(self.accept_user)
                    layout.addWidget(row)
        for i in self.tasks_info.tasks:
            row = loadUi("ui/row.ui")
            row.task.setText(f"{i.task_name}")
            row.button.clicked.connect(self.task_done_button)
            row.button.setProperty("task", i)
            layout.addWidget(row)
        layout.setObjectName("main_layout")
        self.scroll_widget.setLayout(layout)
    def accept_user(self):
        button = self.sender()
        button.deleteLater()
        parent_widget = button.parentWidget()
        parent_widget.decline_button.deleteLater()
        task = parent_widget.findChild(QLabel, "task")
        task.setText("Пользователь добавлен")
        request_info = button.property("request")
        request_id = request_info.request_id
        user_id = request_info.user_id
        block_id = self.user_info.block_id
        self.UserService.AddUser(user_id,"user",block_id)
        self.UserService.CancelRequest(request_id)
        self.UserService.AddHistory(self.user_info, f"{self.user_info.user_name} добавил пользователя {request_info.user_name}")
    def decline_user(self):
        button = self.sender()
        button.deleteLater()
        parent_widget = button.parentWidget()
        parent_widget.button.deleteLater()
        task = parent_widget.findChild(QLabel, "task")
        task.setText("Пользователь отклонен")
        request_info = button.property("request")
        request_id = request_info.request_id
        user_id = request_info.user_id
        block_id = self.user_info.block_id
        self.UserService.SetRequestStatus(request_id,"declined")
        self.UserService.AddHistory(self.user_info,
                                    f"{self.user_info.user_name} отклонил заявку пользователя {request_info.user_name}")
    def users_button_func(self):
        self.setCentralWidget(UsersWindow(self.UserService,self.user_info))
    def tasks_button_func(self):
        self.setCentralWidget(TaskWindow(self.UserService,self.user_info))
    def exit_button_func(self):
        self.setCentralWidget(EntryWindow(self.UserService))
    def leave_button_func(self):
        self.setCentralWidget(AskWindow(self.UserService,self.user_info))
    def task_done_button(self):
        button = self.sender()
        task_info = button.property("task")
        task_id = task_info.task_id
        parent_widget = button.parentWidget()
        task = parent_widget.findChild(QLabel, "task")
        parent_layout = button.parentWidget().layout()
        parent_layout.removeWidget(button)
        button.deleteLater()
        task.setText(f"Задание выполено")
        user_name = self.user_info.user_name
        self.UserService.AddHistory(self.user_info,f"{user_name} выполнил задание {task_info.task_name}")
        self.UserService.TaskDone(self.user_info.user_id, task_id)

    def history_button_func(self):
        self.setCentralWidget(HistoryWindow(self.UserService,self.user_info))
class TaskWindow(QMainWindow):
    def __init__(self,UserService, user_info):
        self.UserService = UserService
        self.user_info = user_info
        super(TaskWindow, self).__init__()
        loadUi("ui/task.ui", self)
        self.make_task_button.clicked.connect(self.make_task_button_func)
        self.back_button.clicked.connect(self.back_button_func)
        self.all_tasks_button.clicked.connect(self.all_tasks_button_func)
    def make_task_button_func(self):
        self.setCentralWidget(MakeTaskWindow(self.UserService, self.user_info))
    def back_button_func(self):
        self.setCentralWidget(MainWindow(self.UserService,self.user_info))
    def all_tasks_button_func(self):
        self.setCentralWidget(AllTasksWindow(self.UserService, self.user_info))
class MakeTaskWindow(QMainWindow):
    def __init__(self,UserService,user_info):
        self.UserService = UserService
        self.user_info = user_info
        super(MakeTaskWindow,self).__init__()
        loadUi("ui/make_task.ui", self)
        self.back_button.clicked.connect(self.back_button_func)
        self.task_type.addItem("Задание всем", "for_all")
        self.task_type.addItem("Поочерёдное", "cycled")
        self.task_info.placeholder_text = self.task_info.text()
        self.task_info.user_typed = False
        self.task_info.focusInEvent = lambda event, line_edit=self.task_info: handle_focus_in(event, line_edit)
        self.task_info.focusOutEvent = lambda event, line_edit=self.task_info: handle_focus_out(event, line_edit)
        users = self.UserService.GetUsers(self.user_info.block_id)
        for i in users.users_info:
            self.task_type.addItem(i.user_name, str(i.user_id))
        self.task_info.placeholder_text = self.task_info.text()
        self.task_info.user_typed = False
        self.task_info.focusOutEvent = lambda event, line_edit=self.task_info: handle_focus_out(event, line_edit)
        self.task_info.focusInEvent = lambda event, line_edit=self.task_info: handle_focus_in(event, line_edit)
        self.make_task_button.clicked.connect(self.make_task_button_func)
    def make_task_button_func(self):
        if (self.task_info.text() == self.task_info.placeholder_text):
            self.appointment2.setText("Заполните наименование задания")
            return
        task_type = self.task_type.currentData()
        task_name = self.task_info.text()
        if (self.UserService.MakeTask(task_type, task_name, self.user_info)):
            self.UserService.AddHistory(self.user_info, f"Создал задание {task_name}")
            self.appointment2.setText("Задание создано!")
        else:
            self.appointment2.setText("Ошибка!")
    def back_button_func(self):
        self.setCentralWidget(TaskWindow(self.UserService,self.user_info))
class AllTasksWindow(QMainWindow):
    def __init__(self,UserService,user_info):
        self.UserService = UserService
        self.user_info = user_info
        super(AllTasksWindow,self).__init__()
        loadUi("ui/all_tasks.ui", self)
        users = self.UserService.GetUsers(self.user_info.block_id)
        block_tasks = self.UserService.GetBlockTasks(self.user_info.block_id)
        self.back_button.clicked.connect(self.back_button_func)
        layout = QVBoxLayout()
        is_admin = self.user_info.user_role == "admin"
        row_path = "ui/row_empty.ui"
        if (is_admin):
            row_path = "ui/row.ui"
        for i in block_tasks.users_task:
            row = loadUi(row_path)
            row.task.setText(f"{i.user_name} {i.user_surname}: {i.task_name}")
            if (is_admin):
                row.button.setText("Удалить")
                row.button.clicked.connect(self.delete_task_button_func)
                row.button.setProperty("task", i)
            layout.addWidget(row)
        layout.setObjectName("main_layout")
        self.scroll_widget.setLayout(layout)
    def back_button_func(self):
        self.setCentralWidget(TaskWindow(self.UserService,self.user_info))
    def delete_task_button_func(self):
        button = self.sender()
        task_info = button.property("task")
        user_id = task_info.user_id
        task_id = task_info.task_id
        parent_widget = button.parentWidget()
        task = parent_widget.findChild(QLabel, "task")
        parent_layout = button.parentWidget().layout()
        parent_layout.removeWidget(button)
        button.deleteLater()
        task.setText(f"Задание удалено")
        self.UserService.DeleteTask(task_id,user_id)
class HistoryWindow(QMainWindow):
    def __init__(self,UserService, user_info):
        self.UserService = UserService
        self.user_info = user_info
        super(HistoryWindow,self).__init__()
        loadUi("ui/history.ui", self)
        self.back_button.clicked.connect(self.back_button_func)
        layout = QVBoxLayout()
        self.scroll_area.setMinimumSize(0, 200)
        users_history = self.UserService.GetBlockHistory(self.user_info.block_id)
        for i in users_history.history:
            row = loadUi("ui/row_empty.ui")
            row.task.setText(f"{i.user_name} {i.user_surname} {i.action}")
            layout.addWidget(row)
        layout.setObjectName("main_layout")
        self.scroll_widget.setLayout(layout)
    def back_button_func(self):
        self.setCentralWidget(MainWindow(self.UserService,self.user_info))
class RequestWindow(QMainWindow):
    def __init__(self,UserService, user_info):
        self.UserService = UserService
        self.user_info = user_info
        super(RequestWindow,self).__init__()
        loadUi("ui/request.ui", self)
        self.back_button.clicked.connect(self.back_button_func)
        self.request_button.clicked.connect(self.request_button_func)
        self.dorm_info.addItem("Выберите общежитие",0)
        self.block_info.addItem("Для начала выберите общежитие", 0)
        self.dorms = self.UserService.GetDormsBlocks(free=0)
        for i in self.dorms.DormsBlocks:
            self.dorm_info.addItem(f"{i.dorm_name}",i.dorm_id)
        self.dorm_info.currentIndexChanged.connect(self.update_block_info)
    def update_block_info(self):
        self.request_button.setText("Подать зявку")
        self.block_info.clear()
        self.block_info.addItem("Для начала выберите общежитие", 0)
        dorm_id = self.dorm_info.currentData()
        if dorm_id == 0:
            self.block_info.setCurrentIndex(0)
        else:
            for i in self.dorms.DormsBlocks:
                if (i.dorm_id == dorm_id):
                    for t in i.blocks:
                        self.block_info.addItem(f"{t.block_number}", t.block_id)
            self.block_info.setItemText(0, "Выберите блок")
    def request_button_func(self):
        if (self.dorm_info.currentData() == 0 or self.block_info.currentData() == 0):
            self.request_button.setText("Выберите общежитие")
            return
        dorm_id = self.dorm_info.currentData()
        block_id = self.block_info.currentData()
        user_id = self.user_info.user_id
        request_id = self.UserService.AddRequest(dorm_id,block_id,user_id).is_added
        self.user_info.dorm_id = self.dorm_info.currentData()
        self.user_info.block_id = self.block_info.currentData()
        next_widget = RequestSentWindow(self.UserService,self.user_info,services_pb2.GetRequestResponse(request_id=request_id,
                                                                                                        dorm_id=dorm_id,
                                                                                                        dorm_name=self.dorm_info.currentText(),
                                                                                                        block_id=block_id,
                                                                                                        block_number=int(self.block_info.currentText()),
                                                                                                        status="created" ))
        self.setCentralWidget(next_widget)
    def back_button_func(self):
        self.setCentralWidget(NoBlockWindow(self.UserService,self.user_info))
class RequestSentWindow(QMainWindow):
    def __init__(self,UserService,user_info,request):

        self.request_id = request.request_id
        self.UserService = UserService
        self.user_info = user_info
        super(RequestSentWindow, self).__init__()
        loadUi("ui/request_sent.ui", self)
        verdict = "отпарвлена"
        if request.status == "declined":
            verdict = "отклонена"
            self.cancel_button.setText("ОК")
            self.exit_button.deleteLater()
        self.appointment.setText(f"Ваша заявка на вступления в блок {request.block_number} "
                                 f"общежития {request.dorm_name} {verdict}")
        self.exit_button.clicked.connect(self.exit_button_func)
        self.cancel_button.clicked.connect(self.cancel_button_func)
    def exit_button_func(self):
        next_widget = EntryWindow(self.UserService)
        self.setCentralWidget(next_widget)
    def cancel_button_func(self):
        next_widget = NoBlockWindow(self.UserService,self.user_info)
        self.setCentralWidget(next_widget)
        self.UserService.CancelRequest(self.request_id)
class NoBlockWindow(QMainWindow):
    def __init__(self,UserService,user_info):
        self.UserService = UserService
        self.user_info = user_info
        super(NoBlockWindow,self).__init__()
        loadUi("ui/no_block.ui", self)
        self.exit_button.clicked.connect(self.exit_button_func)
        self.request_button.clicked.connect(self.request_button_func)
        self.create_block_button.clicked.connect(self.create_block_button_func)
    def exit_button_func(self):
        next_widget = EntryWindow(self.UserService)
        self.setCentralWidget(next_widget)
    def request_button_func(self):
        self.setCentralWidget(RequestWindow(self.UserService, self.user_info))
    def create_block_button_func(self):
        self.setCentralWidget(CreateBlockWindow(self.UserService,self.user_info))
class CreateBlockWindow(QMainWindow):
    def __init__(self,UserService,user_info):
        self.UserService = UserService
        self.user_info = user_info
        super(CreateBlockWindow,self).__init__()
        loadUi("ui/create_block.ui", self)
        self.create_block_button.clicked.connect(self.create_block_button_func)
        self.back_button.clicked.connect(self.back_button_func)
        self.dorm_info.addItem("Выберите общежитие", 0)
        self.block_info.addItem("Для начала выберите общежитие", 0)
        self.dorms = self.UserService.GetDormsBlocks()
        for i in self.dorms.DormsBlocks:
            self.dorm_info.addItem(f"{i.dorm_name}",i.dorm_id)
        self.dorm_info.currentIndexChanged.connect(self.update_block_info)
    def update_block_info(self):
        self.create_block_button.setText("Создать блок")
        self.block_info.clear()
        self.block_info.addItem("Для начала выберите общежитие", 0)
        dorm_id = self.dorm_info.currentData()
        if dorm_id == 0:
            self.block_info.setCurrentIndex(0)
        else:
            for i in self.dorms.DormsBlocks:
                if (i.dorm_id == dorm_id):
                    for t in i.blocks:
                        self.block_info.addItem(f"{t.block_number}",t.block_id)
            self.block_info.setItemText(0, "Выберите блок")
    def create_block_button_func(self):
        if (self.dorm_info.currentData() == 0 or self.block_info.currentData() == 0):
            self.create_block_button.setText("Выберите общежитие и блок")
            return
        self.user_info.dorm_id = self.dorm_info.currentData()
        self.user_info.block_id = self.block_info.currentData()
        self.user_info.user_role = "admin"
        res = self.UserService.AddUser(self.user_info.user_id, self.user_info.user_role, self.user_info.block_id).is_added
        next_widget = MainWindow(self.UserService,self.user_info)
        self.setCentralWidget(next_widget)
    def back_button_func(self):
        self.setCentralWidget(NoBlockWindow(self.UserService,self.user_info))
class AskWindow(QMainWindow):
    def __init__(self,UserService,user_info):
        self.UserService = UserService
        self.user_info = user_info
        super(AskWindow,self).__init__()
        loadUi("ui/ask.ui",self)
        self.no_button.clicked.connect(self.no_button_func)
        self.yes_button.clicked.connect(self.yes_button_func)
    def no_button_func(self):
        self.setCentralWidget(MainWindow(self.UserService,self.user_info))
    def yes_button_func(self):
        self.setCentralWidget(NoBlockWindow(self.UserService,self.user_info))
        users = self.UserService.GetUsers(self.user_info.block_id).users_info
        if (len(users) == 1):
            self.UserService.DeleteRequests(self.user_info.block_id)
        else:
            if (self.user_info.user_role == "admin"):
                next_user_index = 0
                for i in range(len(users)):
                    if (users[i].user_id == self.user_info.user_id):
                        next_user_index = i + 1
                        continue
                    if (users[i].user_role == "admin"):
                        self.UserService.KickUser(self.user_info.user_id, self.user_info.block_id)
                        break
                if (next_user_index == len(users)):
                    next_user_index = 0
                self.UserService.ChangeRole(users[next_user_index].user_id, "admin")
        self.UserService.KickUser(self.user_info.user_id,self.user_info.block_id)
class UsersWindow(QMainWindow):
    def __init__(self,UserService,user_info):
        self.user_info = user_info
        self.UserService = UserService
        super(UsersWindow,self).__init__()
        loadUi("ui/users.ui", self)
        self.back_button.clicked.connect(self.back_button_func)
        self.pop_up = PopUpWidget(self)
        self.last_row = None
        self.pop_up.delete_button.clicked.connect(self.delete_button_func)
        self.pop_up.make_admin_button.clicked.connect(self.make_admin_button_func)
        self.pop_up.take_admin_button.clicked.connect(self.take_admin_button_func)
        self.scroll_area.setMinimumSize(0, 200)
        layout = QVBoxLayout()
        users = self.UserService.GetUsers(self.user_info.block_id)
        if self.user_info.user_role == "admin":
            layout = admin_rows(users,"ui/row.ui",self.pop_up_button,self.user_info.user_id)
        else:
            layout = rows(users,"ui/row_empty.ui")
        self.scroll_widget.setLayout(layout)
    def pop_up_button(self):
        button = self.sender()
        user_info = button.property("user_info")
        button_pos = button.mapToGlobal(QPoint(button.width()-300, button.height()))
        self.pop_up.move(button_pos)
        self.pop_up.show()
        self.pop_up.delete_button.setProperty("user_info",user_info)
        self.pop_up.make_admin_button.setProperty("user_info",user_info)
        self.pop_up.take_admin_button.setProperty("user_info",user_info)
        self.last_row = button.parentWidget()
    def delete_button_func(self):
        self.pop_up.hide()
        label = self.last_row.findChild(QLabel,"task")
        label.setText("Пользователь удален")
        button = self.last_row.findChild(QPushButton,"button")
        button.deleteLater()
        user_id = button.property("user_info").user_id
        self.UserService.KickUser(user_id, self.user_info.block_id)
    def make_admin_button_func(self):
        self.pop_up.hide()
        button = self.sender()
        user_info = button.property("user_info")
        if (user_info.user_role == "admin"):
            return
        user_name = user_info.user_name
        user_id = user_info.user_id
        label = self.last_row.findChild(QLabel,"task")
        label.setText(f"{user_name}: admin")
        self.UserService.ChangeRole(user_id,"admin")
        self.UserService.AddHistory(self.user_info,f"{self.user_info.user_name} сделал администратором {user_name}")
    def take_admin_button_func(self):
        self.pop_up.hide()
        button = self.sender()
        user_info = button.property("user_info")
        if (user_info.user_role == "user"):
            return
        user_name = user_info.user_name
        user_id = user_info.user_id
        label = self.last_row.findChild(QLabel, "task")
        label.setText(f"{user_name}: user")
        self.UserService.ChangeRole(user_id, "user")
        self.UserService.AddHistory(self.user_info, f"{self.user_info.user_name} отобрал права администратора {user_name}")
    def back_button_func(self):
        self.setCentralWidget(MainWindow(self.UserService,self.user_info))
class PopUpWidget(QWidget):
    def __init__(self,parent):
        super(PopUpWidget, self).__init__(parent)
        self.setWindowFlags(Qt.Popup)
        loadUi("ui/pop_up.ui", self)

app = QApplication(sys.argv)
window = EntryWindow(UserService())
window.setWindowIcon(QIcon("png/Default_eng.png"))
window.setWindowTitle("МАИ Tasks")
window.resize(1195, 775)
window.show()


sys.exit(app.exec_())