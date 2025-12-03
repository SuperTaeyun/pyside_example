from PySide6.QtWidgets import QWidget, QLineEdit, QSpinBox, QFormLayout, QApplication

app = QApplication([])
root_widget = QWidget()

form = QFormLayout()
form.addRow("이름", QLineEdit())
form.addRow("나이", QSpinBox())

# set layout
root_widget.setLayout(form)
root_widget.show()

app.exec()
