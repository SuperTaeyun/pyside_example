from PySide6.QtCore import QDir, QModelIndex, Slot
from PySide6.QtWidgets import (
    QWidget, QSplitter,
    QFileSystemModel, QTreeView, QListView,
    QVBoxLayout, QTableView
)


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 화면 설정
        self.setWindowTitle("Model/View")
        self.resize(800, 400)

        # 모델 생성
        self.model = QFileSystemModel(self)

        # 현재 work_dir을 루트로 설정
        root_path = QDir.currentPath()
        self.model.setRootPath(root_path)

        # Tree, ListView를 구분하기 위한 Splitter
        splitter = QSplitter(self)

        # TreeView
        self.tree_view = QTreeView(splitter)
        self.tree_view.setModel(self.model)
        # TreeView의 root_index 설정
        self.tree_view.setRootIndex(self.model.index(root_path))

        # ListView
        self.list_view = QListView(splitter)
        self.list_view.setModel(self.model)
        # ListView의 root_index 설정
        self.list_view.setRootIndex(self.model.index(root_path))

        # TableView
        self.table_view = QTableView(splitter)
        self.table_view.setModel(self.model)
        # TableView의 root_index 설정
        self.table_view.setRootIndex(self.model.index(root_path))

        # TreeView의 SelectionModel의 변경에 따라 ListView도 같이 변경되도록 한다.
        self.tree_view.selectionModel().currentChanged.connect(self.on_tree_selection_changed)

        # root_layout
        layout = QVBoxLayout(self)
        layout.addWidget(splitter)

    @Slot(QModelIndex, QModelIndex)
    def on_tree_selection_changed(self, current: QModelIndex, _previous: QModelIndex) -> None:
        """
        TreeView의 SelectionModel이 변경될 때 호출될 Slot. `current`가 폴더일 경우 해당 폴더를 ListView의 Root로 사용한다.
        파일인 경우에는 그 파일이 속한 부모의 폴더를 ListView에 표시한다.

        :param current: 현재 선택된 QModelIndex
        :param _previous: 이전의 QModelIndex
        :return: None
        """
        if self.model.isDir(current):
            self.list_view.setRootIndex(current)
            self.table_view.setRootIndex(current)
        else:
            parent_index = current.parent()
            self.list_view.setRootIndex(parent_index)
            self.table_view.setRootIndex(parent_index)
