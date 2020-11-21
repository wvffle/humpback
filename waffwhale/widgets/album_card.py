from PySide2.QtWidgets import QWidget, QGraphicsScene, QGraphicsDropShadowEffect
from PySide2.QtGui import QColor
from ..ui.album_card import Ui_AlbumCard


class AlbumCard(QWidget):
    def __init__(self, album, api):
        super().__init__()

        self.ui = Ui_AlbumCard()
        self.ui.setupUi(self)

        self.api = api

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setYOffset(3)
        self.shadow.setXOffset(0)
        self.shadow.setBlurRadius(10)
        self.shadow.setColor(QColor(0xaa, 0xaa, 0xaa, 0x4c))
        self.ui.frame.setGraphicsEffect(self.shadow)

        self.ui.artist.setText(album['artist']['name'])
        self.ui.title.setText(album['title'])
        self.ui.count.setText(str(album['tracks_count']))

        self.ui.cover.heightForWidth(True)
        self.api.cover(album['cover']['urls']['medium_square_crop'], self.ui.cover.geometry().width()).connect(self.set_cover)

    def set_cover(self, pixmap):
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        self.ui.cover.setScene(scene)