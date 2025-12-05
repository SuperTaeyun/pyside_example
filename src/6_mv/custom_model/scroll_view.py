from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QScrollArea,
    QLabel, QPushButton
)

from log_model import LogModel
from log_view import LogView


class ScrollView(LogView):
    def __init__(self, model: LogModel, parent=None):
        super().__init__(model, "ScrollView", parent)

        # ScrollArea
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # 로그 추가 버튼
        self.add_button = QPushButton("Add log to ScrollView")
        self.add_button.clicked.connect(self._add_log)

        # 컨텐츠
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scroll_area.setWidget(self.content_widget)

        # layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.scroll_area)
        layout.addWidget(self.add_button)

        # 초기화
        self._refresh_view()

    @Slot()
    def _refresh_view(self):
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        for log in self._model.logs():
            label = QLabel(log)
            self.content_layout.addWidget(label)
        bar = self.scroll_area.verticalScrollBar()
        bar.setValue(bar.maximum())
