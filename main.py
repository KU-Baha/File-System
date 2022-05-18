import sys, os
from models import File


def main():
    _, command, *args = sys.argv
    file = File()
    commands = {
        'init': file.initializ,
        'add': file.add,
        'del': file.delete,
        'list': file.list
    }
    if command in commands:
        commands[command](args)
    else:
        print('Command not found!')


if __name__ == '__main__':
    main()
