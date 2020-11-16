# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Sidebar(object):
    def setupUi(self, Sidebar):
        if not Sidebar.objectName():
            Sidebar.setObjectName(u"Sidebar")
        Sidebar.resize(320, 801)
        Sidebar.setMinimumSize(QSize(320, 0))
        Sidebar.setMaximumSize(QSize(320, 16777215))
        Sidebar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(Sidebar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Sidebar)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.avatar = QPushButton(self.frame)
        self.avatar.setObjectName(u"avatar")
        self.avatar.setMinimumSize(QSize(42, 42))
        self.avatar.setMaximumSize(QSize(42, 42))
        self.avatar.setStyleSheet(u"border: none;\n"
"background-color: rgb(225, 225, 231);")

        self.horizontalLayout_2.addWidget(self.avatar)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 48))
        self.label.setStyleSheet(u"color: rgb(13, 17, 19);")

        self.horizontalLayout_2.addWidget(self.label)

        self.alerts = QPushButton(self.frame)
        self.alerts.setObjectName(u"alerts")
        self.alerts.setMinimumSize(QSize(42, 42))
        self.alerts.setMaximumSize(QSize(42, 42))
        self.alerts.setStyleSheet(u"border: none;")

        self.horizontalLayout_2.addWidget(self.alerts)

        self.upload = QPushButton(self.frame)
        self.upload.setObjectName(u"upload")
        self.upload.setMinimumSize(QSize(42, 42))
        self.upload.setMaximumSize(QSize(42, 42))
        self.upload.setStyleSheet(u"border: none;")

        self.horizontalLayout_2.addWidget(self.upload)

        self.logout = QPushButton(self.frame)
        self.logout.setObjectName(u"logout")
        self.logout.setMinimumSize(QSize(42, 42))
        self.logout.setMaximumSize(QSize(42, 42))
        self.logout.setStyleSheet(u"border: none;")

        self.horizontalLayout_2.addWidget(self.logout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 314, 747))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(17, -1, 17, -1)
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"margin: 7px 0;")

        self.horizontalLayout.addWidget(self.label_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.exp_browse = QPushButton(self.scrollAreaWidgetContents)
        self.exp_browse.setObjectName(u"exp_browse")
        self.exp_browse.setMinimumSize(QSize(0, 42))
        self.exp_browse.setMaximumSize(QSize(16777215, 42))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.exp_browse.setFont(font)
        self.exp_browse.setStyleSheet(u"text-align: left;\n"
"padding: 0 17px;\n"
"border: none;\n"
"color: #878787;")
        self.exp_browse.setCheckable(False)

        self.verticalLayout_3.addWidget(self.exp_browse)

        self.exp_albums = QPushButton(self.scrollAreaWidgetContents)
        self.exp_albums.setObjectName(u"exp_albums")
        self.exp_albums.setMinimumSize(QSize(0, 42))
        self.exp_albums.setMaximumSize(QSize(16777215, 42))
        self.exp_albums.setStyleSheet(u"text-align: left;\n"
"padding: 0 17px;\n"
"border: none;\n"
"color: #878787;")

        self.verticalLayout_3.addWidget(self.exp_albums)

        self.exp_artists = QPushButton(self.scrollAreaWidgetContents)
        self.exp_artists.setObjectName(u"exp_artists")
        self.exp_artists.setMinimumSize(QSize(0, 42))
        self.exp_artists.setMaximumSize(QSize(16777215, 42))
        self.exp_artists.setStyleSheet(u"text-align: left;\n"
"padding: 0 17px;\n"
"border: none;\n"
"color: #878787;")

        self.verticalLayout_3.addWidget(self.exp_artists)

        self.exp_playlists = QPushButton(self.scrollAreaWidgetContents)
        self.exp_playlists.setObjectName(u"exp_playlists")
        self.exp_playlists.setMinimumSize(QSize(0, 42))
        self.exp_playlists.setMaximumSize(QSize(16777215, 42))
        self.exp_playlists.setStyleSheet(u"text-align: left;\n"
"padding: 0 17px;\n"
"border: none;\n"
"color: #878787;")

        self.verticalLayout_3.addWidget(self.exp_playlists)

        self.exp_radios = QPushButton(self.scrollAreaWidgetContents)
        self.exp_radios.setObjectName(u"exp_radios")
        self.exp_radios.setMinimumSize(QSize(0, 42))
        self.exp_radios.setMaximumSize(QSize(16777215, 42))
        self.exp_radios.setStyleSheet(u"text-align: left;\n"
"padding: 0 17px;\n"
"border: none;\n"
"color: #878787;")

        self.verticalLayout_3.addWidget(self.exp_radios)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(17, -1, 17, -1)
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"margin: 7px 0;")

        self.horizontalLayout_4.addWidget(self.label_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.lib_browse = QPushButton(self.scrollAreaWidgetContents)
        self.lib_browse.setObjectName(u"lib_browse")
        self.lib_browse.setMinimumSize(QSize(0, 42))
        self.lib_browse.setMaximumSize(QSize(16777215, 42))
        self.lib_browse.setStyleSheet(u"text-align: left;\n"
"padding: 0 17px;\n"
"border: none;\n"
"color: #878787;")

        self.verticalLayout_3.addWidget(self.lib_browse)

        self.lib_albums = QPushButton(self.scrollAreaWidgetContents)
        self.lib_albums.setObjectName(u"lib_albums")
        self.lib_albums.setMinimumSize(QSize(0, 42))
        self.lib_albums.setMaximumSize(QSize(16777215, 42))
        self.lib_albums.setStyleSheet(u"text-align: left;\n"
"padding: 0 17px;\n"
"border: none;\n"
"color: #878787;")

        self.verticalLayout_3.addWidget(self.lib_albums)

        self.lib_artists = QPushButton(self.scrollAreaWidgetContents)
        self.lib_artists.setObjectName(u"lib_artists")
        self.lib_artists.setMinimumSize(QSize(0, 42))
        self.lib_artists.setMaximumSize(QSize(16777215, 42))
        self.lib_artists.setStyleSheet(u"text-align: left;\n"
"padding: 0 17px;\n"
"border: none;\n"
"color: #878787;")

        self.verticalLayout_3.addWidget(self.lib_artists)

        self.lib_playlists = QPushButton(self.scrollAreaWidgetContents)
        self.lib_playlists.setObjectName(u"lib_playlists")
        self.lib_playlists.setMinimumSize(QSize(0, 42))
        self.lib_playlists.setMaximumSize(QSize(16777215, 42))
        self.lib_playlists.setStyleSheet(u"text-align: left;\n"
"padding: 0 17px;\n"
"border: none;\n"
"color: #878787;")

        self.verticalLayout_3.addWidget(self.lib_playlists)

        self.lib_radios = QPushButton(self.scrollAreaWidgetContents)
        self.lib_radios.setObjectName(u"lib_radios")
        self.lib_radios.setMinimumSize(QSize(0, 42))
        self.lib_radios.setMaximumSize(QSize(16777215, 42))
        self.lib_radios.setStyleSheet(u"text-align: left;\n"
"padding: 0 17px;\n"
"border: none;\n"
"color: #878787;")

        self.verticalLayout_3.addWidget(self.lib_radios)

        self.lib_favourites = QPushButton(self.scrollAreaWidgetContents)
        self.lib_favourites.setObjectName(u"lib_favourites")
        self.lib_favourites.setMinimumSize(QSize(0, 42))
        self.lib_favourites.setMaximumSize(QSize(16777215, 42))
        self.lib_favourites.setStyleSheet(u"text-align: left;\n"
"padding: 0 17px;\n"
"border: none;\n"
"color: #878787;")

        self.verticalLayout_3.addWidget(self.lib_favourites)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(17, -1, 17, -1)
        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMaximumSize(QSize(16777215, 16777215))
        self.label_9.setStyleSheet(u"margin: 7px 0;")

        self.horizontalLayout_6.addWidget(self.label_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.pod_info = QPushButton(self.scrollAreaWidgetContents)
        self.pod_info.setObjectName(u"pod_info")
        self.pod_info.setMinimumSize(QSize(0, 42))
        self.pod_info.setMaximumSize(QSize(16777215, 42))
        self.pod_info.setStyleSheet(u"text-align: left;\n"
"padding: 0 17px;\n"
"border: none;\n"
"color: #878787;")

        self.verticalLayout_3.addWidget(self.pod_info)

        self.third_party = QPushButton(self.scrollAreaWidgetContents)
        self.third_party.setObjectName(u"third_party")
        self.third_party.setMinimumSize(QSize(0, 42))
        self.third_party.setMaximumSize(QSize(16777215, 42))
        self.third_party.setStyleSheet(u"text-align: left;\n"
"padding: 0 17px;\n"
"border: none;\n"
"color: #878787;")

        self.verticalLayout_3.addWidget(self.third_party)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Sidebar)

        QMetaObject.connectSlotsByName(Sidebar)
    # setupUi

    def retranslateUi(self, Sidebar):
        Sidebar.setWindowTitle(QCoreApplication.translate("Sidebar", u"Form", None))
        self.avatar.setText("")
        self.label.setText(QCoreApplication.translate("Sidebar", u"User", None))
        self.alerts.setText("")
        self.upload.setText("")
        self.logout.setText("")
        self.label_6.setText(QCoreApplication.translate("Sidebar", u"Explore", None))
        self.exp_browse.setText(QCoreApplication.translate("Sidebar", u"Browse", None))
        self.exp_albums.setText(QCoreApplication.translate("Sidebar", u"Albums", None))
        self.exp_artists.setText(QCoreApplication.translate("Sidebar", u"Artists", None))
        self.exp_playlists.setText(QCoreApplication.translate("Sidebar", u"Playlists", None))
        self.exp_radios.setText(QCoreApplication.translate("Sidebar", u"Radios", None))
        self.label_7.setText(QCoreApplication.translate("Sidebar", u"My Library", None))
        self.lib_browse.setText(QCoreApplication.translate("Sidebar", u"Browse", None))
        self.lib_albums.setText(QCoreApplication.translate("Sidebar", u"Albums", None))
        self.lib_artists.setText(QCoreApplication.translate("Sidebar", u"Artists", None))
        self.lib_playlists.setText(QCoreApplication.translate("Sidebar", u"Playlists", None))
        self.lib_radios.setText(QCoreApplication.translate("Sidebar", u"Radios", None))
        self.lib_favourites.setText(QCoreApplication.translate("Sidebar", u"Favorites", None))
        self.label_9.setText(QCoreApplication.translate("Sidebar", u"More", None))
        self.pod_info.setText(QCoreApplication.translate("Sidebar", u"Pod info", None))
        self.third_party.setText(QCoreApplication.translate("Sidebar", u"Third Party Software", None))
    # retranslateUi

