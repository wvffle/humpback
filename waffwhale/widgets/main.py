from PySide2.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QStackedLayout
from PySide2.QtGui import QPixmap, QIcon, QPalette
from PySide2.QtCore import QObject, Signal, Slot, QThread, Qt, QSettings
from PySide2.QtNetwork import QNetworkRequest
from urllib.request import urlopen, Request

from waffwhale.widgets import Sidebar, PlayerControls, Browse, HistoryEntry
from ..api import API


# https://stackoverflow.com/a/59537535/5565538
class CoverDownloader(QObject):
    resultsChanged = Signal(bytes)

    @Slot(str)
    def download(self, url):
        img = urlopen(url).read()
        self.resultsChanged.emit(img)


class MainWindow(QMainWindow):
    def __init__(self, settings: QSettings):
        super().__init__()
        self.settings = settings
        self.api = API(settings)
        self.api.history.all().connect(self.on_history)

        self.setWindowTitle('waffwhale')

        self.downloader_thread = QThread(self)
        self.downloader_thread.start()

        self.downloader = CoverDownloader()
        self.downloader.moveToThread(self.downloader_thread)
        self.downloader.resultsChanged.connect(self.on_download)

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

    @Slot(bytes)
    def on_download(self, img):
        pixmap = QPixmap()
        pixmap.loadFromData(img)

        size = self.controls.ui.cover_art.geometry().height()
        icon = QIcon(pixmap.scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.controls.set_cover_art(icon)

    @Slot(dict)
    def on_history(self, history):
        for entry in history['results']:
            history_entry = HistoryEntry(entry, self.api)
            self.pages.get('exp_browse').ui.history.addWidget(history_entry)

    def closeEvent(self, event):
        self.downloader_thread.quit()
        self.downloader_thread.wait()
        super().closeEvent(event)
