# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history_entry.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_HistoryEntry(object):
    def setupUi(self, HistoryEntry):
        if not HistoryEntry.objectName():
            HistoryEntry.setObjectName(u"HistoryEntry")
        HistoryEntry.resize(404, 80)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HistoryEntry.sizePolicy().hasHeightForWidth())
        HistoryEntry.setSizePolicy(sizePolicy)
        HistoryEntry.setMinimumSize(QSize(0, 80))
        HistoryEntry.setMaximumSize(QSize(16777215, 90))
        font = QFont()
        font.setPointSize(14)
        HistoryEntry.setFont(font)
        self.horizontalLayout = QHBoxLayout(HistoryEntry)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 16)
        self.cover = QPushButton(HistoryEntry)
        self.cover.setObjectName(u"cover")
        self.cover.setMinimumSize(QSize(64, 64))
        self.cover.setMaximumSize(QSize(64, 64))

        self.horizontalLayout.addWidget(self.cover)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 0)
        self.title = QLabel(HistoryEntry)
        self.title.setObjectName(u"title")
        font1 = QFont()
        font1.setPointSize(10)
        self.title.setFont(font1)

        self.verticalLayout.addWidget(self.title)

        self.artist = QLabel(HistoryEntry)
        self.artist.setObjectName(u"artist")
        self.artist.setFont(font1)

        self.verticalLayout.addWidget(self.artist)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.user = QLabel(HistoryEntry)
        self.user.setObjectName(u"user")
        font2 = QFont()
        font2.setPointSize(8)
        self.user.setFont(font2)

        self.horizontalLayout_2.addWidget(self.user)

        self.date = QLabel(HistoryEntry)
        self.date.setObjectName(u"date")
        self.date.setFont(font2)

        self.horizontalLayout_2.addWidget(self.date)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.horizontalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(HistoryEntry)

        QMetaObject.connectSlotsByName(HistoryEntry)
    # setupUi

    def retranslateUi(self, HistoryEntry):
        HistoryEntry.setWindowTitle(QCoreApplication.translate("HistoryEntry", u"Form", None))
        self.cover.setText("")
        self.title.setText(QCoreApplication.translate("HistoryEntry", u"Title", None))
        self.artist.setText(QCoreApplication.translate("HistoryEntry", u"Artist", None))
        self.user.setText(QCoreApplication.translate("HistoryEntry", u"@user", None))
        self.date.setText(QCoreApplication.translate("HistoryEntry", u"Date", None))
    # retranslateUi

