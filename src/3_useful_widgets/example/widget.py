from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QScrollArea,
    QLabel, QPushButton, QListWidget, QTextEdit, QTabWidget
)
from PySide6.QtCore import Qt, Slot


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab Example 2")

        # tab widget
        self.tab_widget = QTabWidget(self)

        # scroll area
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout()
        scroll_widget.setLayout(scroll_layout)

        self.scroll_add_btn = QPushButton("Add")
        self.scroll_add_btn.clicked.connect(self.add_scroll_item)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.scroll_content_widget = QWidget()
        self.scroll_content_layout = QVBoxLayout(self.scroll_content_widget)
        self.scroll_content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.scroll_area.setWidget(self.scroll_content_widget)

        self.scroll_item_count = 0
        for i in range(5):
            self.add_scroll_label(f"init {i + 1}")
        self.scroll_item_count = 5

        scroll_layout.addWidget(self.scroll_add_btn)
        scroll_layout.addWidget(self.scroll_area)

        # list
        list_area = QWidget()
        list_layout = QVBoxLayout()
        list_area.setLayout(list_layout)

        # button
        self.list_add_button = QPushButton("Add")
        self.list_add_button.clicked.connect(self.add_list_item)

        # list_widget
        self.list_widget = QListWidget()

        self.list_item_count = 0
        for i in range(10):
            self.list_widget.addItem(f"init {i + 1}")
        self.list_item_count = 10

        list_layout.addWidget(self.list_add_button)
        list_layout.addWidget(self.list_widget)

        # log
        log_widget = QWidget()
        log_layout = QVBoxLayout()
        log_widget.setLayout(log_layout)

        self.log_count = 0
        self.log_edit = QTextEdit()
        self.log_edit.setReadOnly(True)

        self.log_button = QPushButton("Add Log")
        self.log_button.clicked.connect(self.add_log)

        log_layout.addWidget(self.log_edit)
        log_layout.addWidget(self.log_button)

        # add to tab_widget
        self.tab_widget.addTab(scroll_widget, "스크롤")
        self.tab_widget.addTab(list_area, "리스트")
        self.tab_widget.addTab(log_widget, "로그")

        # root_layout
        root_layout = QVBoxLayout()
        root_layout.addWidget(self.tab_widget)
        self.setLayout(root_layout)

    def add_scroll_label(self, text: str):
        label = QLabel(text)
        self.scroll_content_layout.addWidget(label)

    @Slot()
    def add_scroll_item(self):
        self.scroll_item_count += 1
        new_text = f"추가된 항목: {self.scroll_item_count}"
        self.add_scroll_label(new_text)
        print(new_text)

    @Slot()
    def add_list_item(self):
        self.list_item_count += 1
        new_text = f"추가된 항목: {self.list_item_count}"
        self.list_widget.addItem(new_text)
        print(new_text)
        self.list_widget.scrollToBottom()

    def add_log(self):
        self.log_count += 1
        message = f"[Log] {self.log_count}번째 메시지."
        self.log_edit.append(message)
        print(message)

        # cursor
        cursor = self.log_edit.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.log_edit.setTextCursor(cursor)
        self.log_edit.ensureCursorVisible()
