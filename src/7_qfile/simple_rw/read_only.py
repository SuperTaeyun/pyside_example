from PySide6.QtCore import QFile, QIODevice, QTextStream

file = QFile("sample.txt")

if file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
    stream = QTextStream(file)
    print(f"파일 내용: {stream.readAll()}")
    file.close()
else:
    print("못 여는데?")
