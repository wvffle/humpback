from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from os.path import dirname
from ..ui.player_controls import Ui_PlayerControls


class PlayerControls(QWidget):
    def __init__(self):
        super(PlayerControls, self).__init__()

        self.ui = Ui_PlayerControls()
        self.ui.setupUi(self)

        self.play_icon = QIcon(dirname(__file__) + '/icons/play.svg')
        self.pause_icon = QIcon(dirname(__file__) + '/icons/pause.svg')

        size = self.ui.play.geometry().height()

        self.ui.play.setIcon(self.play_icon)
        self.ui.play.setIconSize(QSize(size - 4, size - 4))

        self.ui.fav.setIcon(QIcon(dirname(__file__) + '/icons/heart.svg'))
        self.ui.fav.setIconSize(QSize(size / 2, size / 2))

        self.ui.playlist.setIcon(QIcon(dirname(__file__) + '/icons/folder-plus.svg'))
        self.ui.playlist.setIconSize(QSize(size / 2, size / 2))

        self.ui.hide.setIcon(QIcon(dirname(__file__) + '/icons/eye-off.svg'))
        self.ui.hide.setIconSize(QSize(size / 2, size / 2))

        self.ui.prev.setIcon(QIcon(dirname(__file__) + '/icons/chevron-left.svg'))
        self.ui.prev.setIconSize(QSize(size - 12, size - 12))

        self.ui.next.setIcon(QIcon(dirname(__file__) + '/icons/chevron-right.svg'))
        self.ui.next.setIconSize(QSize(size - 12, size - 12))

        self.ui.mute.setIcon(QIcon(dirname(__file__) + '/icons/volume-2.svg'))
        self.ui.mute.setIconSize(QSize(size / 2, size / 2))

        self.ui.queue.setIcon(QIcon(dirname(__file__) + '/icons/list.svg'))
        self.ui.queue.setIconSize(QSize(size / 2, size / 2))
