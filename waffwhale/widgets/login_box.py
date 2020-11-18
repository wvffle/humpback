from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal, Slot, QSettings
from ..ui.login_box import Ui_LoginDialog
from urllib.request import urlopen
from urllib.parse import urlencode
import json
import sys


class LoginDialog(QWidget):
    logged_in = Signal()

    def __init__(self, settings: QSettings):
        super().__init__()
        self.settings = settings

        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)

        self.setWindowTitle('Log into funkwhale server')

    @Slot()
    def accept(self):
        data = urlencode({'username': self.ui.login.text(), 'password': self.ui.password.text()}).encode()
        host = f'{self.ui.server.text()}/api/v1/token/'
        req = urlopen(host, data=data)
        token = json.loads(req.read())['token']

        self.settings.setValue('login_token', token)
        self.settings.setValue('api_host', self.ui.server.text())

        self.logged_in.emit()

    @Slot()
    def reject(self):
        sys.exit(-1)
