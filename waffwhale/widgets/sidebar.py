from PySide2.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PySide2.QtGui import QIcon, QColor
from PySide2.QtCore import QSize
from os.path import dirname
from ..ui.sidebar import Ui_Sidebar


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Sidebar()
        self.ui.setupUi(self)

        shadow = QGraphicsDropShadowEffect()
        shadow.setXOffset(10)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0xff, 0xaa, 0x00, 0x4c))
        shadow.setBlurRadius(15)
        self.ui.frame.setGraphicsEffect(shadow)

        size = self.ui.exp_albums.geometry().height() / 2

        browse_icon = QIcon(QIcon(dirname(__file__) + '/icons/compass.svg'))
        self.ui.exp_browse.setIcon(browse_icon)
        self.ui.lib_browse.setIcon(browse_icon)
        self.ui.exp_browse.setIconSize(QSize(size, size))
        self.ui.lib_browse.setIconSize(QSize(size, size))

        album_icon = QIcon(QIcon(dirname(__file__) + '/icons/disc.svg'))
        self.ui.exp_albums.setIcon(album_icon)
        self.ui.lib_albums.setIcon(album_icon)
        self.ui.exp_albums.setIconSize(QSize(size, size))
        self.ui.lib_albums.setIconSize(QSize(size, size))

        artists_icon = QIcon(QIcon(dirname(__file__) + '/icons/users.svg'))
        self.ui.exp_artists.setIcon(artists_icon)
        self.ui.lib_artists.setIcon(artists_icon)
        self.ui.exp_artists.setIconSize(QSize(size, size))
        self.ui.lib_artists.setIconSize(QSize(size, size))

        playlists_icon = QIcon(QIcon(dirname(__file__) + '/icons/list.svg'))
        self.ui.exp_playlists.setIcon(playlists_icon)
        self.ui.lib_playlists.setIcon(playlists_icon)
        self.ui.exp_playlists.setIconSize(QSize(size, size))
        self.ui.lib_playlists.setIconSize(QSize(size, size))

        radios_icon = QIcon(QIcon(dirname(__file__) + '/icons/radio.svg'))
        self.ui.exp_radios.setIcon(radios_icon)
        self.ui.lib_radios.setIcon(radios_icon)
        self.ui.exp_radios.setIconSize(QSize(size, size))
        self.ui.lib_radios.setIconSize(QSize(size, size))

        favourites_icon = QIcon(QIcon(dirname(__file__) + '/icons/heart.svg'))
        self.ui.lib_favourites.setIcon(favourites_icon)
        self.ui.lib_favourites.setIconSize(QSize(size, size))

        info_icon = QIcon(QIcon(dirname(__file__) + '/icons/info.svg'))
        self.ui.pod_info.setIcon(info_icon)
        self.ui.pod_info.setIconSize(QSize(size, size))

        third_party_icon = QIcon(QIcon(dirname(__file__) + '/icons/code.svg'))
        self.ui.third_party.setIcon(third_party_icon)
        self.ui.third_party.setIconSize(QSize(size, size))

        upload = QIcon(QIcon(dirname(__file__) + '/icons/upload.svg'))
        self.ui.upload.setIcon(upload)
        self.ui.upload.setIconSize(QSize(size, size))

        self.logout_icon = QIcon(QIcon(dirname(__file__) + '/icons/log-out.svg'))
        self.login_icon = QIcon(QIcon(dirname(__file__) + '/icons/log-in.svg'))
        self.ui.logout.setIcon(self.logout_icon)
        self.ui.logout.setIconSize(QSize(size, size))

        notifications_icon = QIcon(QIcon(dirname(__file__) + '/icons/bell.svg'))
        self.ui.alerts.setIcon(notifications_icon)
        self.ui.alerts.setIconSize(QSize(size, size))

        self.avatar_icon = QIcon(QIcon(dirname(__file__) + '/icons/user.svg'))
        self.ui.avatar.setIcon(self.avatar_icon)
        self.ui.avatar.setIconSize(QSize(size, size))
