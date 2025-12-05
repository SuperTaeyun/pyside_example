from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QVBoxLayout, QPushButton, QListWidget)

from log_model import LogModel
from log_view import LogView


class ListView(LogView):
    def __init__(self, model: LogModel, parent=None):
        super().__init__(model, "ListView", parent)

        # ListWidget
        self.list_widget = QListWidget()

        # 로그 추가 버튼
        self.add_button = QPushButton("Add log to ListView")
        self.add_button.clicked.connect(self._add_log)

        # layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.list_widget)
        layout.addWidget(self.add_button)

        # 초기화
        self._refresh_view()

    @Slot()
    def _refresh_view(self):
        self.list_widget.clear()
        for log in self._model.logs():
            self.list_widget.addItem(log)
        self.list_widget.scrollToBottom()
