from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QSplitter

from log_model import LogModel
from list_view import ListView
from scroll_view import ScrollView
from text_edit_view import TextEditView


class Widget(QWidget):
    def __init__(self, model: LogModel, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Model/View")
        self.resize(600, 400)

        # View를 구분하기 위한 Splitter
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setSizes([300, 300, 300])

        # Add Views
        splitter.addWidget(ScrollView(model))
        splitter.addWidget(ListView(model))
        splitter.addWidget(TextEditView(model))

        # root_layout
        layout = QVBoxLayout(self)
        layout.addWidget(splitter)
