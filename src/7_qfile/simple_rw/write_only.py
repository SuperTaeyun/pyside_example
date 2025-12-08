from PySide6.QtCore import QFile, QIODevice, QTextStream

file = QFile("sample.txt")

if file.open(QIODevice.OpenModeFlag.WriteOnly | QIODevice.OpenModeFlag.Text):
    stream = QTextStream(file)
    stream << "첫 번째 줄. \n"
    stream << "두 번째 줄."
    file.close()
    print("쓰기 완료.")
else:
    print("못 여는데?")
