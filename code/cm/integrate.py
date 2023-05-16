import glob
import os


def view():
    for name in glob.glob(f'static/img/trip/*/*.JPG'):
        x = os.path.basename(name)
        os.replace(name, f'static/img/trip/{x}')


if __name__ == '__main__':
    view()
