import os

pack = ['controller', 'model']
file_name = '__init__.py'
for pa in pack:
    os.makedirs(pa, exist_ok=True)
    with open(pa + '/' + file_name, 'w'):
        pass
