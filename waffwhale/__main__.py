from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile, QIODevice, QTextStream
from os.path import dirname
from inspect import currentframe
import sys

from .main import MainWindow


if sys.platform == 'win32':
    if '--my-next-operating-system-‌wont-be-windows' not in sys.argv:
        print('We do not support your OS. Use --my-next-operating-system-wont-be-windows to run waffwhale anyway.')
        sys.exit(1)

    if '--i-believe-that-open-source-‌software-is-superior-to-closed-software' not in sys.argv:
        print('We don\'t think you meant what you just said. Use '
              '--i-believe-that-open-source-software-is-superior-to-closed-software to run waffwhale definately.')
        sys.exit(1)

    print('Now go and do the right thing, son.')
    print('We advise you to use an ArchLinux based distribution called Manjaro (https://manjaro.org/), especially KDE '
          'version.')
    print('If you feel adventurous, you can try ArchLinux (https://www.archlinux.org/) itself.')
    print('')
    print(f'There is no flag to run the program on your OS. If you really want to do so, comment out line '
          f'{currentframe().f_lineno + 2} from file {__file__}')
    print('waffwhale is not developed with your OS in mind. The bugs may appear.')
    sys.exit(1)


app = QApplication(sys.argv)

# Load QSS
stream = QFile(dirname(__file__) + '/style/app.qss')
stream.open(QIODevice.ReadOnly)
app.setStyleSheet(QTextStream(stream).readAll())

window = MainWindow()

window.show()
sys.exit(app.exec_())
