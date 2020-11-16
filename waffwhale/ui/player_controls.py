# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'player_controls.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PlayerControls(object):
    def setupUi(self, PlayerControls):
        if not PlayerControls.objectName():
            PlayerControls.setObjectName(u"PlayerControls")
        PlayerControls.resize(932, 84)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PlayerControls.sizePolicy().hasHeightForWidth())
        PlayerControls.setSizePolicy(sizePolicy)
        PlayerControls.setMinimumSize(QSize(0, 84))
        PlayerControls.setMaximumSize(QSize(16777215, 84))
        PlayerControls.setStyleSheet(u"")
        self.gridLayout = QGridLayout(PlayerControls)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(PlayerControls)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(0, 84))
        self.frame_2.setMaximumSize(QSize(16777215, 84))
        self.frame_2.setStyleSheet(u"background-color: rgb(240, 240, 246);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cover_art = QPushButton(self.frame_2)
        self.cover_art.setObjectName(u"cover_art")
        self.cover_art.setMinimumSize(QSize(84, 84))
        self.cover_art.setMaximumSize(QSize(84, 84))
        self.cover_art.setStyleSheet(u"border: none;")

        self.horizontalLayout_3.addWidget(self.cover_art)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(236, 0))
        self.frame_3.setMaximumSize(QSize(236, 16777215))
        self.frame_3.setStyleSheet(u"background-color: rgb(225, 225, 231);\n"
"color: rgb(13, 17, 19);")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.title = QLabel(self.frame_3)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout_2.addWidget(self.title)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.album = QLabel(self.frame_4)
        self.album.setObjectName(u"album")
        font1 = QFont()
        font1.setPointSize(10)
        self.album.setFont(font1)

        self.horizontalLayout_4.addWidget(self.album)

        self.divider = QLabel(self.frame_4)
        self.divider.setObjectName(u"divider")
        self.divider.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.divider)

        self.artist = QLabel(self.frame_4)
        self.artist.setObjectName(u"artist")
        self.artist.setFont(font1)

        self.horizontalLayout_4.addWidget(self.artist)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addWidget(self.frame_3)

        self.horizontalSpacer_11 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_11)

        self.fav = QPushButton(self.frame_2)
        self.fav.setObjectName(u"fav")
        self.fav.setMinimumSize(QSize(44, 44))
        self.fav.setMaximumSize(QSize(44, 44))
        self.fav.setStyleSheet(u"background-color: rgb(240, 240, 246);\n"
"border-style: outset;")

        self.horizontalLayout_3.addWidget(self.fav)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.playlist = QPushButton(self.frame_2)
        self.playlist.setObjectName(u"playlist")
        self.playlist.setMinimumSize(QSize(44, 44))
        self.playlist.setMaximumSize(QSize(44, 44))
        self.playlist.setStyleSheet(u"background-color: rgb(240, 240, 246);\n"
"border-style: outset;")

        self.horizontalLayout_3.addWidget(self.playlist)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.hide = QPushButton(self.frame_2)
        self.hide.setObjectName(u"hide")
        self.hide.setMinimumSize(QSize(44, 44))
        self.hide.setMaximumSize(QSize(44, 44))
        self.hide.setStyleSheet(u"background-color: rgb(240, 240, 246);\n"
"border-style: outset;")

        self.horizontalLayout_3.addWidget(self.hide)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.prev = QPushButton(self.frame_2)
        self.prev.setObjectName(u"prev")
        self.prev.setMinimumSize(QSize(44, 44))
        self.prev.setMaximumSize(QSize(44, 44))
        self.prev.setStyleSheet(u"background-color: rgb(240, 240, 246);\n"
"border-style: outset;")

        self.horizontalLayout_3.addWidget(self.prev)

        self.horizontalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.play = QPushButton(self.frame_2)
        self.play.setObjectName(u"play")
        self.play.setMinimumSize(QSize(44, 44))
        self.play.setMaximumSize(QSize(44, 44))
        self.play.setStyleSheet(u"background-color: #ffaa00;\n"
"border-style: outset;\n"
"border-radius: 22px;")

        self.horizontalLayout_3.addWidget(self.play)

        self.horizontalSpacer_7 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.next = QPushButton(self.frame_2)
        self.next.setObjectName(u"next")
        self.next.setMinimumSize(QSize(44, 44))
        self.next.setMaximumSize(QSize(44, 44))
        self.next.setStyleSheet(u"background-color: rgb(240, 240, 246);\n"
"border-style: outset;")

        self.horizontalLayout_3.addWidget(self.next)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.mute = QPushButton(self.frame_2)
        self.mute.setObjectName(u"mute")
        self.mute.setMinimumSize(QSize(44, 44))
        self.mute.setMaximumSize(QSize(44, 44))
        self.mute.setStyleSheet(u"background-color: rgb(240, 240, 246);\n"
"border-style: outset;")

        self.horizontalLayout_3.addWidget(self.mute)

        self.horizontalSpacer_10 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)

        self.volume = QSlider(self.frame_2)
        self.volume.setObjectName(u"volume")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.volume.sizePolicy().hasHeightForWidth())
        self.volume.setSizePolicy(sizePolicy2)
        self.volume.setMinimumSize(QSize(100, 32))
        self.volume.setMaximumSize(QSize(150, 16777215))
        self.volume.setMaximum(99)
        self.volume.setValue(50)
        self.volume.setOrientation(Qt.Horizontal)
        self.volume.setInvertedAppearance(False)
        self.volume.setInvertedControls(False)

        self.horizontalLayout_3.addWidget(self.volume)

        self.horizontalSpacer_6 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.queue = QPushButton(self.frame_2)
        self.queue.setObjectName(u"queue")
        self.queue.setMinimumSize(QSize(44, 44))
        self.queue.setMaximumSize(QSize(44, 44))
        self.queue.setStyleSheet(u"background-color: rgb(240, 240, 246);\n"
"border-style: outset;")

        self.horizontalLayout_3.addWidget(self.queue)

        self.horizontalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)


        self.retranslateUi(PlayerControls)

        QMetaObject.connectSlotsByName(PlayerControls)
    # setupUi

    def retranslateUi(self, PlayerControls):
        PlayerControls.setWindowTitle(QCoreApplication.translate("PlayerControls", u"Form", None))
        self.cover_art.setText("")
        self.title.setText(QCoreApplication.translate("PlayerControls", u"Track Title", None))
        self.album.setText(QCoreApplication.translate("PlayerControls", u"Album", None))
        self.divider.setText(QCoreApplication.translate("PlayerControls", u" / ", None))
        self.artist.setText(QCoreApplication.translate("PlayerControls", u"Artist", None))
        self.fav.setText("")
        self.playlist.setText("")
        self.hide.setText("")
        self.prev.setText("")
        self.play.setText("")
        self.next.setText("")
        self.mute.setText("")
        self.queue.setText("")
    # retranslateUi

