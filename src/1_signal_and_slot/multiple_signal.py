import sys
from PySide6.QtWidgets import QWidget, QApplication

from ui import signal_slot_exam_ui


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # init
        self.ui = signal_slot_exam_ui.Ui_Form()
        self.ui.setupUi(self)


# main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
