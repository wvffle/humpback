from PyQt5.QtWidgets import QWidget
from ..ui.player_controls import Ui_PlayerControls


class PlayerControls(QWidget):
    def __init__(self):
        super(PlayerControls, self).__init__()

        self.ui = Ui_PlayerControls()
        self.ui.setupUi(self)
