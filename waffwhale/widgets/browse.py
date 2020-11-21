from PySide2.QtWidgets import QWidget, QHBoxLayout
from PySide2.QtCore import Slot
from waffwhale.ui.browse import Ui_Browse
from .history_entry import HistoryEntry
from .album_card import AlbumCard


RECENTLY_ADDED_COLUMNS = 7
RECENTLY_ADDED_ROWS = 3


class Browse(QWidget):
    def __init__(self, api):
        super().__init__()

        self.api = api

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

        recently_added_count = RECENTLY_ADDED_COLUMNS * RECENTLY_ADDED_ROWS

        for i in range(RECENTLY_ADDED_ROWS):
            layout = QHBoxLayout()
            self.ui.__dict__[f'row{i}'] = layout
            self.ui.recently_added.addLayout(layout)

        api.history.all().connect(self.on_history)
        api.favourites.all().connect(self.on_favourites)
        api.albums.all.with_params({
            'page_size': recently_added_count,
        }).connect(self.on_recently_added)

    @Slot(dict)
    def on_history(self, history):
        for entry in history['results']:
            history_entry = HistoryEntry(entry, self.api)
            self.ui.history.addWidget(history_entry)

    @Slot(dict)
    def on_favourites(self, history):
        for entry in history['results']:
            history_entry = HistoryEntry(entry, self.api)
            self.ui.favourites.addWidget(history_entry)

    @Slot(dict)
    def on_recently_added(self, albums):
        for i, entry in enumerate(albums['results']):
            album_card = AlbumCard(entry, self.api)
            self.ui.__dict__[f'row{i // RECENTLY_ADDED_COLUMNS}'].addWidget(album_card)
