import sys
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import (QApplication, QWidget, QSlider,
                               QVBoxLayout, QLabel, QProgressBar, QLCDNumber)


class SliderWithCustomSignal(QWidget):
    # custom signal
    processed_value_signal = Signal(int)

    def __init__(self):
        super().__init__()
        # widget setting
        self.setWindowTitle("Custom Signal-Slot")
        self.resize(300, 150)

        # components
        # create layout
        layout = QVBoxLayout(self)

        # labels
        self.label_original = QLabel("original: -")
        self.label_processed = QLabel("processed(×2): -")

        # slider
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(100)
        self.slider.setValue(25)

        # add to layout
        # slider - label_original - label_processed
        layout.addWidget(self.slider)
        layout.addWidget(self.label_original)
        layout.addWidget(self.label_processed)

        # connect
        self.slider.valueChanged.connect(self.respond_to_slider)
        self.processed_value_signal.connect(self.on_processed_value)

    @Slot(int)
    def respond_to_slider(self, value):
        print("slider moved to:", value)
        self.label_original.setText(f"원본 값: {value}")
        processed_value = value * 2
        self.processed_value_signal.emit(processed_value)

    @Slot(int)
    def on_processed_value(self, value):
        print("커스텀 시그널:", value)
        self.label_processed.setText(f"처리된 값(×2): {value}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SliderWithCustomSignal()
    window.show()
    sys.exit(app.exec())
