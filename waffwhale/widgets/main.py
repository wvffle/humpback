from PySide2.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QStackedLayout
from PySide2.QtGui import QPalette
from PySide2.QtCore import Qt, QSettings
from PySide2.QtMultimedia import QMediaPlayer

from waffwhale.widgets import Sidebar, PlayerControls, Browse
from ..api import API


class MainWindow(QMainWindow):
    def __init__(self, settings: QSettings):
        super().__init__()
        self.settings = settings
        self.api = API(settings)

        self.player = QMediaPlayer()
        # self.player.setMedia(self.api.listen('<UUID>'))

        self.setWindowTitle('waffwhale')

        self.mainLayout = QVBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)

        self.controls = PlayerControls(self.player)
        self.sidebar = Sidebar()

        self.contentLayout = QHBoxLayout()
        self.contentLayout.addWidget(self.sidebar)

        self.pagesView = QStackedLayout()
        self.contentLayout.addLayout(self.pagesView)

        # All pages
        self.pages = {
            'exp_browse': Browse(self.api)
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

