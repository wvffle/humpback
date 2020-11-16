from PySide2.QtWidgets import QSlider, QStyle
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
            
            QSlider::add-page {
                margin-top: -4px;
                margin-bottom: 4px;
            }
            
            QSlider::sub-page {
                background-color: #ffaa00;
                margin-top: -4px;
                margin-bottom: 4px;
            }
        """)

        self.setRange(0, 100)

    def mousePressEvent(self, ev: QMouseEvent):
        if ev.button() == Qt.LeftButton:
            ev.accept()
            self.setValue(QStyle.sliderValueFromPosition(
                self.minimum(),
                self.maximum(),
                ev.pos().x(),
                self.width(),
                False
            ))
        else:
            super().mousePressEvent(ev)
