from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize
from datetime import datetime, timezone

import timeago

from ..ui.history_entry import Ui_HistoryEntry


class HistoryEntry(QWidget):
    def __init__(self, entry, api):
        super().__init__()

        self.ui = Ui_HistoryEntry()
        self.ui.setupUi(self)

        self.ui.artist.setText(entry['track']['artist']['name'])
        self.ui.title.setText(entry['track']['title'])
        self.ui.user.setText(entry['actor']['preferred_username'])
        date = datetime.fromisoformat(entry['creation_date'].replace('Z', '+00:00'))
        self.ui.date.setText(timeago.format(date, datetime.now(timezone.utc)))
        self.ui.title.setText(entry['track']['title'])

        try:
            cover_url = entry['track']['album']['cover']['urls']['medium_square_crop']

            size = self.ui.cover.geometry().height()
            self.ui.cover.setIconSize(QSize(size, size))
            api.cover(cover_url, size).connect(lambda pixmap: self.ui.cover.setIcon(QIcon(pixmap)))
        except:
            pass