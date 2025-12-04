from PySide6.QtWidgets import QWidget, QHBoxLayout
from PySide6.QtCore import Slot

from image_button import ImageButton


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        img_btn_1 = ImageButton(self)
        img_btn_2 = ImageButton(self)

        # connect
        img_btn_1.hovering.connect(self.on_hovering)
        img_btn_1.clicked.connect(self.on_clicked)
        img_btn_2.hovering.connect(self.on_hovering)
        img_btn_2.clicked.connect(self.on_clicked)

        # set_layout, add_widgets
        layout = QHBoxLayout(self)
        layout.addWidget(img_btn_1)
        layout.addWidget(img_btn_2)
        self.setLayout(layout)

    @Slot()
    def on_hovering(self):
        print("ImageButton 1 Hovering.")

    @Slot()
    def on_clicked(self):
        print("ImageButton 1 Clicked.")
