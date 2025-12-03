from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication

app = QApplication([])
root_widget = QWidget()

grid_layout = QGridLayout()
grid_layout.addWidget(QPushButton("0,0"), 0, 0)
grid_layout.addWidget(QPushButton("0,1"), 0, 1)
# row=1, col=0, rowSpan=1, colSpan=2
grid_layout.addWidget(QPushButton("1,0~1"), 1, 0, 1, 2)

# set layout
root_widget.setLayout(grid_layout)
root_widget.show()

app.exec()
