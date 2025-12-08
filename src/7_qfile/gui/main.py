import sys
from PySide6.QtWidgets import QApplication
from file_widget import FileEditorWindow


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("QFile GUI 데모")
    window = FileEditorWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()