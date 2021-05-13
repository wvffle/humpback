import signal
import sys
import os

import inotify.adapters

from PySide6.QtCore import QThread, QObject, Signal, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

main = os.path.join(os.path.dirname(__file__), 'qml', "main.qml")


class Master(QObject):
    command = Signal()

    @Slot()
    def reload(self):
        print("Loading UI")

        windows = engine.rootObjects()
        if len(windows) > 0:
            pos = windows[-1].position()
            width = windows[-1].width()
            height = windows[-1].height()
            state = windows[-1].windowState()

            for window in windows:
                window.close()
                window.destroy()

            engine.clearComponentCache()
            engine.load(main)

            if not engine.rootObjects():
                sys.exit(-1)

            # NOTE: Every load creates new rootObject
            window = engine.rootObjects()[-1]
            window.setPosition(pos); window.setWindowState(state)
            window.resize(width, height)
        else:
            engine.load(main)

            if not engine.rootObjects():
                sys.exit(-1)


class Worker(QObject):
    requestReload = Signal()
    isRunning = True

    @Slot()
    def stop(self):
        self.isRunning = False

    @Slot()
    def run(self):
        self.requestReload.emit()
        i = inotify.adapters.InotifyTree('./qml')

        while self.isRunning:
            events = i.event_gen(yield_nones=False, timeout_s=1)

            reload = False
            for event in list(events):
                (_, type_names, path, filename) = event

                if filename[-3:] == 'qml' and 'IN_MODIFY' in type_names:
                    reload = True
                    break

            if reload:
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

    # Stop application gracefully:
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    status = app.exec_()
    worker.stop()
    workerThread.quit()
    workerThread.wait()
    sys.exit(status)
