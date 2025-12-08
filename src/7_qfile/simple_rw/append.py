from PySide6.QtCore import QFile, QIODevice, QTextStream

file = QFile("sample.txt")

if file.open(QIODevice.OpenModeFlag.Append | QIODevice.OpenModeFlag.Text):
    stream = QTextStream(file)
    stream << "\n 새로운 줄"
    file.close()
    print("이어쓰기 완료.")
else:
    print("못 여는데?")
