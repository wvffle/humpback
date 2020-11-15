import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PyQt5 import uic


class OnUiWatch:
    watchDirectory = "./ui"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event, **kwargs):
        if event.is_directory:
            return None

        if event.event_type == 'created' or event.event_type == 'modified':
            uic.compileUiDir('./ui', map=lambda src, name: ('./waffwhale/ui', name))
            print('Ui files regenerated')


if __name__ == '__main__':
    watch = OnUiWatch()
    uic.compileUiDir('./ui', map=lambda src, name: ('./waffwhale/ui', name))
    print('Ui files generated')
    watch.run()
