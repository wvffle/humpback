from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile, QIODevice, QTextStream
from os.path import dirname
import sys

from .main import MainWindow


if sys.platform == 'win32' and '--my-next-operating-system-wont-be-windows' not in sys.argv:
    print('We do not support your OS. Use --my-next-operating-system-wont-be-windows to run waffwhale anyway.')
    sys.exit(1)

app = QApplication(sys.argv)

# Load QSS
stream = QFile(dirname(__file__) + '/style/app.qss')
stream.open(QIODevice.ReadOnly)
app.setStyleSheet(QTextStream(stream).readAll())

window = MainWindow()

window.show()
sys.exit(app.exec_())
