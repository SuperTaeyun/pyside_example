from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QScrollArea,
    QLabel, QPushButton, QListWidget, QTextEdit
)
from PySide6.QtCore import Qt, Slot


class Widget(QWidget):
    def __init__(self):
        super().__init__()


class ScrollAreaTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        # button
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_item)
        layout.addWidget(self.add_button)

        # scroll_area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        layout.addWidget(self.scroll_area)

        # content
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.scroll_area.setWidget(self.content_widget)

        self.item_count = 0
        for i in range(5):
            self.add_label(f"init {i + 1}")
        self.item_count = 5
        self.setLayout(layout)

    def add_label(self, text: str):
        label = QLabel(text)
        self.content_layout.addWidget(label)

    @Slot()
    def add_item(self):
        self.item_count += 1
        new_text = f"추가된 항목: {self.item_count}"
        self.add_label(new_text)
        print(new_text)


class ListWidgetTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        # button
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_item)
        layout.addWidget(self.add_button)

        # list_widget
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.item_count = 0
        for i in range(10):
            self.list_widget.addItem(f"init {i + 1}")
        self.item_count = 10
        self.setLayout(layout)

    @Slot()
    def add_item(self):
        self.item_count += 1
        new_text = f"추가된 항목: {self.item_count}"
        self.list_widget.addItem(new_text)
        print(new_text)
        self.list_widget.scrollToBottom()


class LogTextEditTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.log_count = 0
        self.log_edit = QTextEdit()
        self.log_edit.setReadOnly(True)

        self.log_button = QPushButton("Add Log")
        self.log_button.clicked.connect(self.add_log)

        layout.addWidget(self.log_edit)
        layout.addWidget(self.log_button)
        self.setLayout(layout)

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
