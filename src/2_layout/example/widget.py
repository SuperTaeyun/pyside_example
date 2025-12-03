from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QPushButton, QLabel, QLineEdit, \
    QSpacerItem


class SizePolicyExample(QWidget):
    def __init__(self):
        super().__init__()

        # widgets

        # form
        form_layout = QHBoxLayout()
        self.input_label = QLabel("Text Input:")
        self.input_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.input_field = QLineEdit()
        self.input_field.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        # add form widgets to layout
        form_layout.addWidget(self.input_label)
        form_layout.addWidget(self.input_field)

        # btn
        btn_layout = QHBoxLayout()
        self.btn_1 = QPushButton("Button 1")
        self.btn_1.clicked.connect(self.btn_print_input_field)
        self.btn_2 = QPushButton("Button 2")
        self.btn_3 = QPushButton("Button 3")

        # add btn widgets to layout
        btn_layout.addWidget(self.btn_1, stretch=1)
        btn_layout.addWidget(self.btn_2, stretch=1)
        btn_layout.addWidget(self.btn_3, stretch=2)

        # layouts
        vertical_layout = QVBoxLayout()
        vertical_layout.addLayout(form_layout)
        vertical_layout.addLayout(btn_layout)

        self.setLayout(vertical_layout)

    @Slot()
    def btn_print_input_field(self):
        print(self.input_field.text())
