from PyQt5.QtWidgets import QWidget
from ..ui.sidebar import Ui_Sidebar


class Sidebar(QWidget):
    def __init__(self):
        super(Sidebar, self).__init__()

        self.ui = Ui_Sidebar()
        self.ui.setupUi(self)
