import sys
from PySide6.QtWidgets import QApplication
from widget import Widget


def main():
    app = QApplication(sys.argv)
    widget = Widget()
    widget.setWindowTitle("Custom Image Button Demo")
    widget.resize(220, 100)
    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
