import sys
from PySide6.QtWidgets import QApplication
from widget import Widget

from log_model import LogModel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # log_model (global)
    model = LogModel()
    model.add("[Init] 프로그램 시작")
    model.add("[Init] Model/View Ready")
    # main widget
    window = Widget(model)
    window.show()
    sys.exit(app.exec())
