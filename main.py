import sys, os
from models import File


def main():
    command, *args = sys.argv[1:]
    file = File()
    commands = {
        'init': file.initializ,
        'add': file.add,
        'delete': file.delete,
        'list': file.list
    }
    if command in commands:
        try:
            commands[command](args[0], args[1:])
        except:
            commands[command]()
    else:
        print('Command not found!')


if __name__ == '__main__':
    main()
