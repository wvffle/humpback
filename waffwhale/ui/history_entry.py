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
        HistoryEntry.resize(359, 114)
        self.horizontalLayout = QHBoxLayout(HistoryEntry)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cover = QPushButton(HistoryEntry)
        self.cover.setObjectName(u"cover")
        self.cover.setMinimumSize(QSize(96, 96))
        self.cover.setMaximumSize(QSize(96, 96))

        self.horizontalLayout.addWidget(self.cover)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(HistoryEntry)
        self.title.setObjectName(u"title")

        self.verticalLayout.addWidget(self.title)

        self.artist = QLabel(HistoryEntry)
        self.artist.setObjectName(u"artist")

        self.verticalLayout.addWidget(self.artist)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.user = QLabel(HistoryEntry)
        self.user.setObjectName(u"user")

        self.horizontalLayout_2.addWidget(self.user)

        self.date = QLabel(HistoryEntry)
        self.date.setObjectName(u"date")

        self.horizontalLayout_2.addWidget(self.date)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(107, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

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

