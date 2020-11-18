from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize
from ..ui.history_entry import Ui_HistoryEntry


class HistoryEntry(QWidget):
    def __init__(self, entry, api):
        super().__init__()

        self.ui = Ui_HistoryEntry()
        self.ui.setupUi(self)

        self.ui.artist.setText(entry['track']['artist']['name'])
        self.ui.title.setText(entry['track']['title'])
        self.ui.user.setText(entry['actor']['preferred_username'])
        self.ui.date.setText(entry['creation_date'])
        self.ui.title.setText(entry['track']['title'])

        cover_url = entry['track']['album']['cover']['urls']['medium_square_crop']

        size = self.ui.cover.geometry().height()
        self.ui.cover.setIconSize(QSize(size, size))
        api.cover(cover_url, size).connect(lambda pixmap: self.ui.cover.setIcon(QIcon(pixmap)))
