from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout, QMessageBox

from signup_state import SignupState
from login_page import LoginPage
from signup_page import SignupAccountPage, SignupTermsPage
from src.assignments.sign.account_store import AccountStore


class RootWidget(QWidget):

    def __init__(self):
        super().__init__()
        # set title, size
        self.setWindowTitle("Sing-up Example")
        self.setMinimumWidth(500)
        self.setMinimumHeight(600)

        self.state = SignupState()
        self.store = AccountStore()

        # stacked
        self.stacked = QStackedWidget()

        # pages
        self.login_page = LoginPage(self.store)
        self.signup_terms_page = SignupTermsPage()
        self.signup_account_page = SignupAccountPage(self.state, self.store)

        # add to stack (index 0 ~ 2)
        self.stacked.addWidget(self.login_page)
        self.stacked.addWidget(self.signup_terms_page)
        self.stacked.addWidget(self.signup_account_page)

        # previous/next button interaction
        # login page
        self.login_page.signup_clicked.connect(self.to_term_page)
        self.login_page.login_success.connect(self.handle_login)

        # term
        self.signup_terms_page.previous_clicked.connect(self.to_login_page)
        self.signup_terms_page.next_clicked.connect(self.to_account_page)

        # account
        self.signup_account_page.previous_clicked.connect(self.to_term_page)
        self.signup_account_page.next_clicked.connect(self.to_login_page)

        # set_layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.stacked)
        self.setLayout(self.layout)

    @Slot()
    def to_login_page(self):
        self.change_current_stack(self.login_page)

    @Slot()
    def to_term_page(self):
        self.change_current_stack(self.signup_terms_page)

    @Slot()
    def to_account_page(self):
        self.change_current_stack(self.signup_account_page)

    @Slot(str)
    def handle_login(self, user_id: str):
        QMessageBox.information(self, "Login", f"Welcome, {user_id}")

    def change_current_stack(self, widget: QWidget) -> None:
        self.stacked.setCurrentWidget(widget)
