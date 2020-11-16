import inotify.adapters
import subprocess
from glob import glob
from os.path import dirname, basename

i = inotify.adapters.Inotify()
i.add_watch('ui')


def compile(path, filename):
    subprocess.call([
        'pyside2-uic',
        f'{path}/{filename}',
        '-o',
        f'waffwhale/{path}/{filename[:-3]}.py'
    ])


for file in glob('ui/*.ui'):
    compile(dirname(file), basename(file))

for event in i.event_gen(yield_nones=False):
    (_, type_names, path, filename) = event

    if filename[-3:] == '.ui':
        if 'IN_CLOSE_WRITE' in type_names or 'IN_MOVED_TO' in type_names:
            compile(path, filename)
            print(f'Generated {filename[:-3]}.py by {type_names}')
