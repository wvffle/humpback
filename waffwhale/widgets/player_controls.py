from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import QSize
from os.path import dirname
from ..ui.player_controls import Ui_PlayerControls


class PlayerControls(QWidget):
    def __init__(self):
        super(PlayerControls, self).__init__()

        self.ui = Ui_PlayerControls()
        self.ui.setupUi(self)

        size = self.ui.play.geometry().height() / 2

        self.empty_cover_icon = QIcon(dirname(__file__) + '/icons/image.svg')
        self.set_cover_art()

        # Play/Pause button
        self.play_icon = QIcon(dirname(__file__) + '/icons/play.svg')
        self.pause_icon = QIcon(dirname(__file__) + '/icons/pause.svg')

        self.ui.play.setIcon(self.play_icon)
        self.ui.play.setIconSize(QSize(size, size))

        self.play_shadow = QGraphicsDropShadowEffect()
        self.play_shadow.setYOffset(10)
        self.play_shadow.setXOffset(0)
        self.play_shadow.setBlurRadius(15)
        self.play_shadow.setColor(QColor(0xff, 0xaa, 0x00, 0x4c))
        self.ui.play.setGraphicsEffect(self.play_shadow)

        # Favourite button
        self.ui.fav.setIcon(QIcon(dirname(__file__) + '/icons/heart.svg'))
        self.ui.fav.setIconSize(QSize(size, size))

        # Add to playlist button
        self.ui.playlist.setIcon(QIcon(dirname(__file__) + '/icons/folder-plus.svg'))
        self.ui.playlist.setIconSize(QSize(size, size))

        # Hide this artist button
        self.ui.hide.setIcon(QIcon(dirname(__file__) + '/icons/eye-off.svg'))
        self.ui.hide.setIconSize(QSize(size, size))

        # Previous track button
        self.ui.prev.setIcon(QIcon(dirname(__file__) + '/icons/skip-back.svg'))
        self.ui.prev.setIconSize(QSize(size, size))

        # Next track button
        self.ui.next.setIcon(QIcon(dirname(__file__) + '/icons/skip-forward.svg'))
        self.ui.next.setIconSize(QSize(size, size))

        # Mute button
        self.ui.mute.setIcon(QIcon(dirname(__file__) + '/icons/volume-2.svg'))
        self.ui.mute.setIconSize(QSize(size, size))

        # Queue button
        self.ui.queue.setIcon(QIcon(dirname(__file__) + '/icons/list.svg'))
        self.ui.queue.setIconSize(QSize(size, size))

        # Volume slider
        # self.ui.volume

    def set_cover_art(self, icon: QIcon = None):
        size = self.ui.cover_art.geometry().height()

        if icon is None:
            self.ui.cover_art.setIcon(self.empty_cover_icon)
            size /= 2
        else:
            self.ui.cover_art.setIcon(icon)

        self.ui.cover_art.setIconSize(QSize(size, size))
