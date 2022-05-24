command = ['+', '-', '/', '*']


def check_command(command):
    if command not in command:
        return False
    return True


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def division(a, b):
    if a == 0:
        return 0
    return a / b


def multiplication(a, b):
    return a * b
