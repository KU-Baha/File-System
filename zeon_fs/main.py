import sys

from helper import commands


def main():
    try:
        _, command, *args = sys.argv
        if command in commands:
            print(commands[command](*args))
        else:
            print("Command not found!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
