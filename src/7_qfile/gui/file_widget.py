from PySide6.QtWidgets import (
    QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout,
    QTextEdit, QPushButton, QLineEdit, QLabel,
    QFileDialog, QMessageBox
)
from PySide6.QtCore import QFile, QTextStream, Slot


class FileEditorWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("QFile GUI Demo")
        self.resize(600, 400)

        # current_file_name: 어떠한 파일을 불러왔을 때 저장되는 값.
        self.__current_file_name = ""

        # central_widget: QMainWindow는 반드시 central_widget이 필요하다.
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # [상단] 파일 읽기/쓰기 버튼
        self.read_btn = QPushButton("불러오기")
        self.save_btn = QPushButton("저장")
        self.save_as_btn = QPushButton("다른 이름으로 저장")

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.read_btn)
        btn_layout.addWidget(self.save_btn)
        btn_layout.addWidget(self.save_as_btn)

        # [중단] 텍스트 편집기
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("여기에 텍스트를 입력하세요.")

        # [하단] 파일 복사
        src_label = QLabel("원본 파일 경로:")
        self.src_line = QLineEdit()
        self.src_btn = QPushButton("찾기")

        dst_label = QLabel("복사 대상 경로:")
        self.dst_line = QLineEdit()
        self.dst_btn = QPushButton("찾기")
        # 복사 버튼
        self.copy_btn = QPushButton("파일 복사")

        # src/dst layout
        src_layout = QHBoxLayout()
        src_layout.addWidget(src_label)
        src_layout.addWidget(self.src_line)
        src_layout.addWidget(self.src_btn)

        dst_layout = QHBoxLayout()
        dst_layout.addWidget(dst_label)
        dst_layout.addWidget(self.dst_line)
        dst_layout.addWidget(self.dst_btn)

        copy_layout = QHBoxLayout()
        copy_layout.addStretch()
        copy_layout.addWidget(self.copy_btn)

        # connect
        self.save_btn.clicked.connect(self.on_save_clicked)
        self.save_as_btn.clicked.connect(self.on_save_as_clicked)
        self.read_btn.clicked.connect(self.on_read_clicked)

        self.src_btn.clicked.connect(self.on_src_clicked)
        self.dst_btn.clicked.connect(self.on_dst_clicked)
        self.copy_btn.clicked.connect(self.on_copy_clicked)

        # layout
        root_layout = QVBoxLayout(central_widget)
        root_layout.addLayout(btn_layout)
        root_layout.addWidget(self.text_edit)
        root_layout.addLayout(src_layout)
        root_layout.addLayout(dst_layout)
        root_layout.addLayout(copy_layout)

    def _open_file(self, file_name: str, flag: QFile.OpenModeFlag) -> QFile | None:
        file = QFile(file_name)
        if not file.open(flag):
            QMessageBox.critical(self, "오류", f"파일 {file_name} 을/를 열 수 없습니다.")
            return None
        return file

    def _get_open_file_name(self, dialog_caption="파일 열기", dialog_dir="",
                            dialog_filter="텍스트 파일 (*.txt);;모든 파일 (*.*)"):
        file_name, _ = QFileDialog.getOpenFileName(self, dialog_caption, dialog_dir, dialog_filter)
        if not file_name:
            return None
        return file_name

    def _get_save_file_name(self, dialog_caption="파일 저장", dialog_dir="",
                            dialog_filter="텍스트 파일 (*.txt);;모든 파일 (*.*)"):
        file_name, _ = QFileDialog.getSaveFileName(self, dialog_caption, dialog_dir, dialog_filter)
        if not file_name:
            return None
        return file_name

    @Slot()
    def on_src_clicked(self):
        file_name = self._get_open_file_name()
        if file_name:
            self.src_line.setText(file_name)

    @Slot()
    def on_dst_clicked(self):
        file_name = self._get_save_file_name()
        if file_name:
            self.dst_line.setText(file_name)

    @Slot()
    def on_read_clicked(self):
        file_name = self._get_open_file_name()
        if file_name:
            file = self._open_file(file_name, QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text)
            if file:
                # read_all
                stream = QTextStream(file)
                content = stream.readAll()
                file.close()
                # set src_line
                self.src_line.setText(file_name)
                self.__current_file_name = file_name
                # set content
                self.text_edit.setPlainText(content)
                QMessageBox.information(self, "알림", f"파일이 {file_name}을 불러왔습니다.")

    @Slot()
    def on_save_clicked(self):
        # 불러온 파일인 경우 해당 파일에 즉시 저장한다. 아닌 경우 save_as로 이어진다.
        if self.__current_file_name:
            file = self._open_file(self.__current_file_name, QFile.OpenModeFlag.WriteOnly | QFile.OpenModeFlag.Text)
            if file:
                text = self.text_edit.toPlainText()
                stream = QTextStream(file)
                stream << text
                # close
                file.close()
                # info
                QMessageBox.information(self, "알림", f"파일이 경로 {self.__current_file_name}에 저장되었습니다.")
        else:
            self.on_save_as_clicked()

    @Slot()
    def on_save_as_clicked(self):
        text = self.text_edit.toPlainText()
        file_name = self._get_save_file_name()
        if file_name:
            file = self._open_file(file_name, QFile.OpenModeFlag.WriteOnly | QFile.OpenModeFlag.Text)
            if file:
                stream = QTextStream(file)
                stream << text
                file.close()
                # info
                QMessageBox.information(self, "알림", f"파일이 경로 {file_name}에 저장되었습니다.")

    @Slot()
    def on_copy_clicked(self):
        src_path = self.src_line.text().strip()
        dst_path = self.dst_line.text().strip()

        # paths 검증
        if not src_path:
            QMessageBox.warning(self, "경고", "원본 파일 경로를 입력하세요.")
            return
        if not dst_path:
            QMessageBox.warning(self, "경고", "복사 대상 파일 경로를 입력하세요.")
            return

        # 파일이 존재하지 않을 경우
        if not QFile.exists(src_path):
            QMessageBox.critical(self, "오류", f"원본 파일이 존재하지 않습니다.\n경로: {src_path}")
            return

        # 대상 파일이 이미 존재하는 경우
        if QFile.exists(dst_path):
            ret = QMessageBox.question(
                self,
                "다른 이름으로 저장 확인",
                f"{dst_path}이(가) 이미 있습니다. \n바꾸시겠습니까?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            if ret == QMessageBox.StandardButton.No:
                return
            # QFile.copy는 대상이 존재할 때 실패한다.
            if not QFile.remove(dst_path):
                QMessageBox.critical(
                    self,
                    "오류",
                    f"파일 {dst_path}의 저장에 실패하였습니다."
                )
                return

        # 복사
        src_file = QFile(src_path)
        if not src_file.copy(dst_path):
            QMessageBox.critical(
                self,
                "오류",
                f"파일 복사에 실패했습니다.\n원본: {src_path}\n대상: {dst_path}"
            )
        else:
            QMessageBox.information(
                self,
                "복사 완료",
                f"파일 복사가 완료되었습니다.\n원본: {src_path}\n대상: {dst_path}"
            )
