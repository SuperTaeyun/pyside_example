from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider


def respond_to_slider(value):
    print(f"slider moved to: {value}")


app = QApplication()
slider = QSlider(Qt.Orientation.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

# connect slot
slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()