from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PySide6.QtGui import QIcon

import res_rc


class Widget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        btn_open = QPushButton("Sign")
        btn_open.setIcon(QIcon(":/icons/sign"))
        layout.addWidget(btn_open)
