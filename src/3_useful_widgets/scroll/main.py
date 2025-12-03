import sys

from PySide6.QtWidgets import QApplication
from widget import Widget, ListWidgetTab, LogTextEditTab, ScrollAreaTab

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LogTextEditTab()
    w.show()
    sys.exit(app.exec())
