import sys
from PySide6.QtWidgets import QApplication
from root_widget import RootWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # widget show
    window = RootWidget()
    window.show()
    # exec
    sys.exit(app.exec())
