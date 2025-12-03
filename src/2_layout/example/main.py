import sys
from PySide6.QtWidgets import QApplication
from widget import SizePolicyExample

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SizePolicyExample()
    window.show()
    app.exec()
