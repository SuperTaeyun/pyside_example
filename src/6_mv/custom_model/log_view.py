from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from log_model import LogModel


class LogView(QWidget):
    def __init__(self, model: LogModel, view_name="", parent=None):
        super().__init__(parent)
        self._model = model
        self._view_name = view_name
        self._model.log_changed.connect(self._refresh_view)

    @Slot()
    def _add_log(self):
        log_count = self._model.len()
        self._model.add(f"[{self._view_name}] 추가 로그 {log_count}")

    @Slot()
    def _refresh_view(self):
        pass
