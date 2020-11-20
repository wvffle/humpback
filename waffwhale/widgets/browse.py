from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Slot
from waffwhale.ui.browse import Ui_Browse
from .history_entry import HistoryEntry


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

        api.history.all().connect(self.on_history)
        api.favourites.all().connect(self.on_favourites)

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
