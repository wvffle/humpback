from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread, Qt, QSize
from urllib.request import urlopen

from .widgets import Sidebar, PlayerControls


# https://stackoverflow.com/a/59537535/5565538
class CoverDownloader(QObject):
    resultsChanged = pyqtSignal(bytes)

    @pyqtSlot(str)
    def download(self, url):
        img = urlopen(url).read()
        self.resultsChanged.emit(img)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
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
        self.contentLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.mainLayout.addLayout(self.contentLayout)
        self.mainLayout.addWidget(self.controls)

        self.centralWidget = QWidget(self)
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)

    @pyqtSlot(bytes)
    def on_download(self, img):
        pixmap = QPixmap()
        pixmap.loadFromData(img)

        geometry = self.controls.ui.cover_art.geometry()
        size = geometry.height()

        icon = QIcon(pixmap.scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.controls.ui.cover_art.setIcon(icon)
        self.controls.ui.cover_art.setIconSize(QSize(size, size))

    def closeEvent(self, event):
        self.downloader_thread.quit()
        self.downloader_thread.wait()
        super().closeEvent(event)
