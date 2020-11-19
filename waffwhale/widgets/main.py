from PySide2.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QStackedLayout
from PySide2.QtGui import QPalette
from PySide2.QtCore import Slot, Qt, QSettings

from waffwhale.widgets import Sidebar, PlayerControls, Browse, HistoryEntry
from ..api import API


class MainWindow(QMainWindow):
    def __init__(self, settings: QSettings):
        super().__init__()
        self.settings = settings
        self.api = API(settings)
        self.api.history.all().connect(self.on_history)

        self.setWindowTitle('waffwhale')

        self.mainLayout = QVBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)

        self.controls = PlayerControls()
        self.sidebar = Sidebar()

        self.contentLayout = QHBoxLayout()
        self.contentLayout.addWidget(self.sidebar)

        self.pagesView = QStackedLayout()
        self.contentLayout.addLayout(self.pagesView)

        # All pages
        self.pages = {
            'exp_browse': Browse()
        }

        page_palette = QPalette()
        page_palette.setColor(QPalette.Background, Qt.white)
        for page in self.pages.values():
            page.ui.frame.setPalette(page_palette)
            page.ui.frame.setAutoFillBackground(True)

        self.pagesView.insertWidget(0, self.pages.get('exp_browse'))

        self.mainLayout.addLayout(self.contentLayout)
        self.mainLayout.addWidget(self.controls)

        self.centralWidget = QWidget(self)
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)

    @Slot(dict)
    def on_history(self, history):
        for entry in history['results']:
            history_entry = HistoryEntry(entry, self.api)
            self.pages.get('exp_browse').ui.history.addWidget(history_entry)
