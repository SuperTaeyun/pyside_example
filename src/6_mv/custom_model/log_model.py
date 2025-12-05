from PySide6.QtCore import QObject, Signal


class LogModel(QObject):
    log_changed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._logs: list[str] = []

    def len(self) -> int:
        return len(self._logs)

    def add(self, text: str) -> None:
        self._logs.append(text)
        self.log_changed.emit()

    def clear(self) -> None:
        self._logs.clear()
        self.log_changed.emit()

    def logs(self) -> list[str]:
        return list(self._logs)
