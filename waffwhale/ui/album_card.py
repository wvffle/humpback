# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'album_card.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AlbumCard(object):
    def setupUi(self, AlbumCard):
        if not AlbumCard.objectName():
            AlbumCard.setObjectName(u"AlbumCard")
        AlbumCard.resize(272, 400)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AlbumCard.sizePolicy().hasHeightForWidth())
        AlbumCard.setSizePolicy(sizePolicy)
        AlbumCard.setMinimumSize(QSize(0, 300))
        self.horizontalLayout = QHBoxLayout(AlbumCard)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 8, 8, 8)
        self.frame = QFrame(AlbumCard)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 8px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.cover = QGraphicsView(self.frame)
        self.cover.setObjectName(u"cover")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cover.sizePolicy().hasHeightForWidth())
        self.cover.setSizePolicy(sizePolicy1)
        self.cover.setStyleSheet(u"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;")
        self.cover.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cover.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cover.setInteractive(True)

        self.verticalLayout.addWidget(self.cover)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(8, 8, 8, 8)
        self.title = QLabel(self.frame)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(12)
        self.title.setFont(font)

        self.verticalLayout_2.addWidget(self.title)

        self.artist = QLabel(self.frame)
        self.artist.setObjectName(u"artist")

        self.verticalLayout_2.addWidget(self.artist)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.songs = QLabel(self.frame)
        self.songs.setObjectName(u"songs")
        font1 = QFont()
        font1.setPointSize(8)
        self.songs.setFont(font1)

        self.horizontalLayout_2.addWidget(self.songs)

        self.count = QLabel(self.frame)
        self.count.setObjectName(u"count")
        self.count.setFont(font1)

        self.horizontalLayout_2.addWidget(self.count)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.more = QPushButton(self.frame)
        self.more.setObjectName(u"more")

        self.horizontalLayout_2.addWidget(self.more)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(AlbumCard)

        QMetaObject.connectSlotsByName(AlbumCard)
    # setupUi

    def retranslateUi(self, AlbumCard):
        AlbumCard.setWindowTitle(QCoreApplication.translate("AlbumCard", u"Form", None))
        self.title.setText(QCoreApplication.translate("AlbumCard", u"Title", None))
        self.artist.setText(QCoreApplication.translate("AlbumCard", u"Artist", None))
        self.songs.setText(QCoreApplication.translate("AlbumCard", u"Songs:", None))
        self.count.setText(QCoreApplication.translate("AlbumCard", u"0", None))
        self.more.setText("")
    # retranslateUi

