from PySide2.QtWidgets import QSlider
from PySide2.QtCore import Qt
from PySide2.QtGui import QMouseEvent


class TrackSlider(QSlider):
    def __init__(self):
        super().__init__(Qt.Horizontal)

        self.setStyleSheet("""
            QSlider::handle::horizontal {
                background-color: none;
                margin: 0;
            }
            
            QSlider::sub-page {
                background-color: #ffaa00;
            }
        """)

        self.setRange(0, 100)

    def mousePressEvent(self, ev: QMouseEvent):
        if ev.button() == Qt.LeftButton:
            ev.accept()
            x = ev.pos().x()
            self.setValue((self.maximum() - self.minimum()) * x / self.width() + self.minimum())
        else:
            super().mousePressEvent(self, ev)