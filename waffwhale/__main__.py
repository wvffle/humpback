from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile, QIODevice, QTextStream
from os.path import dirname
import sys

from .main import MainWindow


app = QApplication(sys.argv)

# Load QSS
stream = QFile(dirname(__file__) + '/style/app.qss')
stream.open(QIODevice.ReadOnly)
app.setStyleSheet(QTextStream(stream).readAll())


window = MainWindow()

window.show()
sys.exit(app.exec_())
