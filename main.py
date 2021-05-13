import sys
import os
import inotify.adapters

from PySide6.QtCore import QThread, QObject, Signal, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

main = os.path.join(os.path.dirname(__file__), 'qml', "main.qml")


class Master(QObject):
    command = Signal()

    def __init__(self):
        QObject.__init__(self)

    @Slot()
    def reload(self):
        print("Loading UI")

        for window in engine.rootObjects():
            window.destroy()

        engine.clearComponentCache()
        engine.load(main)

        if not engine.rootObjects():
            sys.exit(-1)

        # TODO: Move new window to old window position


class Worker(QObject):
    requestReload = Signal()

    def __init__(self):
        QObject.__init__(self)

    @Slot()
    def run(self):
        self.requestReload.emit()
        i = inotify.adapters.InotifyTree('./qml')

        for event in i.event_gen(yield_nones=False):
            (_, type_names, path, filename) = event

            print(filename, type_names)
            if filename[-3:] == 'qml' and 'IN_MODIFY' in type_names:
                self.requestReload.emit()


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    workerThread = QThread()
    workerThread.start()
    worker = Worker()
    worker.moveToThread(workerThread)

    master = Master()
    master.command.connect(worker.run)
    worker.requestReload.connect(master.reload)
    master.command.emit()

    # TODO: Stop worker on application stop

    sys.exit(app.exec_())
