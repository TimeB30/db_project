def handle_focus_in(event, line_edit):
    """Обработка события focusIn (при получении фокуса)."""
    if not hasattr(line_edit, "user_typed"):
        line_edit.user_typed = False  # Инициализируем атрибут, если он отсутствует
    if not line_edit.user_typed and (line_edit.text() == line_edit.placeholder_text or line_edit.text() in ["Введите логин", "Введите пароль"]):
        line_edit.setText("")  # Очищаем поле
    QLineEdit.focusInEvent(line_edit, event)  # Вызов стандартного обработчика


def handle_focus_out(event, line_edit):
    """Обработка события focusOut (при потере фокуса)."""
    if not hasattr(line_edit, "user_typed"):
        line_edit.user_typed = False  # Инициализируем атрибут, если он отсутствует
    if not line_edit.text().strip():  # Если поле пустое
        line_edit.setText(line_edit.placeholder_text)
        line_edit.user_typed = False
    else:
        line_edit.user_typed = True
    QLineEdit.focusOutEvent(line_edit, event)  # Вызов стандартного обработчика
def rows(users,path):
    layout = QVBoxLayout()
    for i in users.users_info:
        row = loadUi(path)
        if (i.user_role == "admin"):
            role = "admin"
        row.task.setText(f"{i.user_name}: {i.user_role}") # подумать стоит ли светить user_login
        row.setMinimumSize(0, 60)
        layout.addWidget(row)
    layout.setObjectName("main_layout")
    return layout
def admin_rows(users,path):
    layout = QVBoxLayout()
    for i in users.users_info:
        row = loadUi(path)
        if (i.user_role == "admin"):
            role = "admin"
        row.task.setText(f"{i.user_name}: {i.user_role}") # подумать стоит ли светить user_login
        row.setMinimumSize(0, 60)
        row.button.setProperty("user_id", i.user_id)
        row.button.setText(":")
        layout.addWidget(row)
    layout.setObjectName("main_layout")
    return layout