from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget, QVBoxLayout, QCheckBox, QLabel, QPushButton, QLineEdit

from src.assignments.sign.account_store import AccountStore
from src.assignments.sign.signup_state import SignupState


class SignupTermsPage(QWidget):
    """
    약관. 다른 파일로 분리하면 더 좋을 수 있겠지만 귀찮으니 냅두도록 한다.
    """

    previous_clicked = Signal()

    next_clicked = Signal()

    def __init__(self):
        super().__init__()

        # terms
        term_label = QLabel("약관 동의")
        self.service_term = QCheckBox("[필수] 서비스 이용약관에 동의합니다.")
        self.service_term.stateChanged.connect(self.update_next_btn_state)
        self.privacy_term = QCheckBox("[필수] 개인정보가 유출되어도 고소하지 않겠습니다.")
        self.privacy_term.stateChanged.connect(self.update_next_btn_state)

        # buttons
        self.previous_btn = QPushButton("이전")
        self.previous_btn.clicked.connect(self.uncheck_terms)
        self.previous_btn.clicked.connect(self.previous_clicked.emit)

        self.next_btn = QPushButton("다음")
        self.next_btn.setEnabled(False)
        self.next_btn.clicked.connect(self.next_clicked.emit)

        # set_layout
        layout = QVBoxLayout(self)
        # add widgets
        layout.addWidget(term_label)
        layout.addWidget(self.service_term)
        layout.addWidget(self.privacy_term)
        layout.addWidget(self.previous_btn)
        layout.addWidget(self.next_btn)

    @Slot()
    def uncheck_terms(self):
        self.service_term.setChecked(False)
        self.privacy_term.setChecked(False)

    @Slot()
    def update_next_btn_state(self):
        state = self.service_term.isChecked() and self.privacy_term.isChecked()
        self.next_btn.setEnabled(state)


class SignupAccountPage(QWidget):
    next_clicked = Signal()

    previous_clicked = Signal()

    def __init__(self, state: SignupState, store: AccountStore):
        super().__init__()
        self.state = state
        self.store = store
        layout = QVBoxLayout(self)

        # form
        label = QLabel("ID/ Password / Email 입력")
        self.id_edit = QLineEdit()
        self.id_edit.setPlaceholderText("ID")

        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)

        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText("sample@sample.com")

        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red;")

        # connect
        self.id_edit.textChanged.connect(self.on_text_changed)
        self.password_edit.textChanged.connect(self.on_text_changed)
        self.email_edit.textChanged.connect(self.on_text_changed)

        # buttons
        self.previous_btn = QPushButton("이전")
        self.next_btn = QPushButton("다음")
        self.next_btn.setEnabled(False)
        # connect
        self.previous_btn.clicked.connect(self.previous_clicked.emit)
        self.next_btn.clicked.connect(self.signup)

        # set_layout, add_widgets
        layout.addWidget(label)
        layout.addWidget(self.id_edit)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.email_edit)
        layout.addWidget(self.error_label)
        layout.addWidget(self.previous_btn)
        layout.addWidget(self.next_btn)

    @Slot()
    def on_text_changed(self):
        self.state.user_id = self.id_edit.text()
        self.state.password = self.password_edit.text()
        self.state.email = self.email_edit.text()

        errors = self.state.validate()

        if errors:
            message = next(iter(errors.values()))
            self.error_label.setText(message)
            self.next_btn.setEnabled(False)
        else:
            self.error_label.setText("")
            self.next_btn.setEnabled(True)

    @Slot()
    def signup(self):
        self.store.add_account(self.state)
        self.next_clicked.emit()
