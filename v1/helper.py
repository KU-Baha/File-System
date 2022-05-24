from pathlib import Path
import subprocess
import os


def check_args(args):
    if not len(args) > 0:
        return False
    return True


def init(path):
    if not check_args(path):
        return False
    subprocess.Popen(f'mkdir {path[0]}', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)


def list_files(_):
    for i in os.listdir():
        print(i)


def add_file(filename):
    if not check_args(filename):
        return False
    subprocess.Popen(f'copy {filename[0]} zeon_sf/', shell=True, stderr=subprocess.PIPE,
                     stdout=subprocess.PIPE) if Path(
        filename[0]).is_file() else print('File not found')


def delete_file(filename):
    if not check_args(filename):
        return False
    subprocess.Popen(f"del zeon_sf/{filename[0]}", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)


def get_file(args):
    if not check_args(args):
        return False
    with open(args[0], 'rb') as file:
        with open(f'{os.getcwd()}\zeon_sf\{args[1]}', 'wb') as file2:
            file2.write(file.read())


commands = {
    'init': init,
    'add': add_file,
    'del': delete_file,
    'list': list_files,
    'get': get_file
}
