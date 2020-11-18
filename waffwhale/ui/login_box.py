# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_box.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        if not LoginDialog.objectName():
            LoginDialog.setObjectName(u"LoginDialog")
        LoginDialog.resize(192, 262)
        self.verticalLayout = QVBoxLayout(LoginDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.server = QLineEdit(LoginDialog)
        self.server.setObjectName(u"server")
        self.server.setEchoMode(QLineEdit.Normal)
        self.server.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.server)

        self.login = QLineEdit(LoginDialog)
        self.login.setObjectName(u"login")
        self.login.setEchoMode(QLineEdit.Normal)
        self.login.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.login)

        self.password = QLineEdit(LoginDialog)
        self.password.setObjectName(u"password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.password)

        self.buttonBox = QDialogButtonBox(LoginDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(LoginDialog)
        self.buttonBox.accepted.connect(LoginDialog.accept)
        self.buttonBox.rejected.connect(LoginDialog.reject)

        QMetaObject.connectSlotsByName(LoginDialog)
    # setupUi

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QCoreApplication.translate("LoginDialog", u"Dialog", None))
        self.server.setPlaceholderText(QCoreApplication.translate("LoginDialog", u"Server", None))
        self.login.setPlaceholderText(QCoreApplication.translate("LoginDialog", u"Login", None))
        self.password.setPlaceholderText(QCoreApplication.translate("LoginDialog", u"Password", None))
    # retranslateUi

