import sys

from helper import *


def main():
    try:
        _, command, *args = sys.argv
        if command in commands:
            commands[command](*args)
        else:
            print("Command not found!")
    except TypeError:
        print('Argument Error')
    except ValueError:
        print('Command Error')


if __name__ == "__main__":
    main()
