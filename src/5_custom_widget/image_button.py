from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QImage
from PySide6.QtCore import Signal

import assets_rc

NORMAL = 0
NORMAL_IMG = ":/assets/normal"

ENTER = 1
ENTER_IMG = ":/assets/enter"

LEAVE = 2
LEAVE_IMG = ":/assets/normal"

PRESS = 3
PRESS_IMG = ":/assets/press"

DISABLE = 4
DISABLE_IMG = ":/assets/disable"


class ImageButton(QWidget):
    clicked = Signal()
    hovering = Signal()

    def __init__(self, parent=None):
        super(ImageButton, self).__init__(parent)
        # state
        self._checked = False
        self._disabled = False
        self._behaviour = NORMAL
        self._image_name = ""

        # set_width/height
        image = QImage(NORMAL_IMG)
        self.setFixedWidth(image.width())
        self.setFixedHeight(image.height())

    def setDisabled(self, value: bool) -> None:
        self._disabled = value
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        # set image_name
        if self._disabled:
            self._image_name = DISABLE_IMG
        if self._checked:
            self._image_name = PRESS_IMG
        else:
            if self._behaviour == NORMAL:
                self._image_name = NORMAL_IMG

            elif self._behaviour == ENTER:
                self._image_name = ENTER_IMG

            elif self._behaviour == LEAVE:
                self._image_name = LEAVE_IMG

            elif self._behaviour == PRESS:
                self._image_name = PRESS_IMG
        print(f"image_name: {self._image_name}")
        painter.drawImage(0, 0, QImage(self._image_name))

    def enterEvent(self, event):
        self._behaviour = ENTER
        self.update()
        self.hovering.emit()

    def leaveEvent(self, event):
        self._behaviour = NORMAL
        self.update()

    def mousePressEvent(self, event):
        self._behaviour = PRESS
        self.update()
        self.clicked.emit()

    def mouseReleaseEvent(self, event):
        if self._disabled:
            return
        if self.rect().contains(event.position().toPoint()):
            self._checked = not self._checked
            self._behaviour = ENTER
            self.clicked.emit()
        else:
            self._behaviour = NORMAL
        self.update()
