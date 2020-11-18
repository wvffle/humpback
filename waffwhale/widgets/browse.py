from PySide2.QtWidgets import QWidget
from ..ui.browse import Ui_Browse


class Browse(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Browse()
        self.ui.setupUi(self)

        self.ui.frame.setStyleSheet("""
            QScrollBar::sub-page,
            QScrollBar::sub-line {
                border-top-left-radius: 7px;
                border-top-right-radius: 7px;
            }
            
            QScrollBar::add-page,
            QScrollBar::add-line {
                border-bottom-left-radius: 7px;
                border-bottom-right-radius: 7px;
            }
        """)
