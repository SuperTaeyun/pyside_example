from PySide6.QtCore import Slot
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import (QVBoxLayout, QPushButton, QTextEdit)

from log_model import LogModel
from log_view import LogView


class TextEditView(LogView):
    def __init__(self, model: LogModel, parent=None):
        super().__init__(model, "TextEditView", parent)

        # TextEdit
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        # 로그 추가 버튼
        self.add_button = QPushButton("Add log to TextEditView")
        self.add_button.clicked.connect(self._add_log)

        # layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.add_button)

        # 초기화
        self._refresh_view()

    @Slot()
    def _refresh_view(self):
        self.text_edit.clear()
        for log in self._model.logs():
            self.text_edit.append(log)
        cursor = self.text_edit.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.text_edit.setTextCursor(cursor)
        self.text_edit.ensureCursorVisible()
