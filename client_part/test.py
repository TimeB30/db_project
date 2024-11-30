from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class PopupWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
        self.setStyleSheet("""
            background-color: #f0f0f0;
            border-radius: 15px;
            border: 1px solid #ccc;
        """)
        layout = QVBoxLayout()
        button1 = QPushButton("Option 1", self)
        button2 = QPushButton("Option 2", self)
        layout.addWidget(button1)
        layout.addWidget(button2)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    popup = PopupWindow()
    popup.resize(200, 100)
    popup.show()
    app.exec_()
