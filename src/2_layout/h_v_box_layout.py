from PySide6.QtWidgets import (QApplication, QWidget, QPushButton,
                               QHBoxLayout, QVBoxLayout)

app = QApplication([])
root_widget = QWidget()

# buttons
button_1 = QPushButton("Button 1")
button_2 = QPushButton("Button 2")
button_3 = QPushButton("Button 3")
button_4 = QPushButton("Button 4")

# vertical layout
vertical_layout = QVBoxLayout()
vertical_layout.addWidget(button_1)
vertical_layout.addWidget(button_2)
vertical_layout.addWidget(button_3)

# horizontal layout
horizontal_layout = QHBoxLayout()
horizontal_layout.addLayout(vertical_layout)
horizontal_layout.addWidget(button_4)

# set layout
root_widget.setLayout(horizontal_layout)
root_widget.show()

app.exec()
