from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTabWidget, QPushButton, QLabel, QLineEdit


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        # window title
        self.setWindowTitle("Tab Example")

        # tab widget
        self.tab_widget = QTabWidget(self)
        self.tab_widget.currentChanged.connect(self.tab_changed)

        # form tab
        widget_form = QWidget()
        label_full_name = QLabel("Name :")
        input_full_name = QLineEdit()
        input_full_name.setPlaceholderText("이름을 입력하세요")
        self.form_button = QPushButton("Buttons 탭으로 이동")
        self.form_button.clicked.connect(self.tab_change)
        # layout
        form_layout = QHBoxLayout()
        form_layout.addWidget(label_full_name)
        form_layout.addWidget(input_full_name)
        form_layout.addWidget(self.form_button)
        widget_form.setLayout(form_layout)

        # button tab
        widget_btn = QWidget()
        button_1 = QPushButton("button_1")
        button_2 = QPushButton("button_2")
        button_3 = QPushButton("button_3")
        # layout
        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(button_1)
        buttons_layout.addWidget(button_2)
        buttons_layout.addWidget(button_3)
        widget_btn.setLayout(buttons_layout)

        button_1.clicked.connect(self.button_clicked_1)
        button_2.clicked.connect(self.button_clicked_2)
        button_3.clicked.connect(self.button_clicked_3)

        # add to tab
        self.tab_widget.addTab(widget_form, "Form")
        self.tab_widget.addTab(widget_btn, "Buttons")

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

    @Slot()
    def button_clicked_1(self):
        print("button 1 clicked")

    @Slot()
    def button_clicked_2(self):
        print("button 2 clicked")

    @Slot()
    def button_clicked_3(self):
        print("button 3 clicked")

    @Slot(int)
    def tab_changed(self, index: int):
        print(f"current tab name: {self.tab_widget.tabText(index)}")

    @Slot()
    def tab_change(self):
        self.tab_widget.setCurrentIndex(1)
