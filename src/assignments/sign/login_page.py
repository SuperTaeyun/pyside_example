from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

from src.assignments.sign.account_store import AccountStore


class LoginPage(QWidget):
    signup_clicked = Signal()
    login_success = Signal(str)

    def __init__(self, store: AccountStore):
        super().__init__()
        self.store = store

        title = QLabel("Login")

        # login form
        self.id_edit = QLineEdit()
        self.id_edit.setPlaceholderText("ID")

        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_edit.setPlaceholderText("Password")

        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red;")

        # buttons
        self.login_button = QPushButton("login")
        self.signup_button = QPushButton("sign-up")
        # connect
        self.login_button.clicked.connect(self.login)
        self.signup_button.clicked.connect(self.signup_clicked.emit)

        # set_layout, add_widgets
        layout = QVBoxLayout(self)
        layout.addWidget(title)
        layout.addWidget(self.id_edit)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.error_label)
        layout.addWidget(self.error_label)
        layout.addWidget(self.login_button)
        layout.addWidget(self.signup_button)

    @Slot()
    def login(self):
        user_id = self.id_edit.text().strip()
        password = self.password_edit.text().strip()

        if not user_id or not password:
            self.error_label.setText("ID와 Password를 입력해주십쇼.")
            return

        if self.store.is_exists(user_id, password):
            self.error_label.setText("")
            self.login_success.emit(user_id)
        else:
            self.error_label.setText("ID 또는 Password 불일치.")
