from PySide2.QtWidgets import QWidget
from ..ui.browse import Ui_Browse


class Browse(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Browse()
        self.ui.setupUi(self)
