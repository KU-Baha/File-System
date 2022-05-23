import os


def check_bottle(file_name='bottle.txt'):
    with open(file_name, 'r') as file:
        if 'water' not in file.read():
            return False
        return True


def take_bottles_list():
    return [bottle for bottle in os.listdir() if 'bottle' in bottle]


def take_empty_bottles():
    empty_bottles = []
    for file_name in take_bottles_list():
        if not check_bottle(file_name):
            empty_bottles.append(file_name)
    return empty_bottles


def take_fill_bottles():
    fill_bottles = []
    for file_name in take_bottles_list():
        if check_bottle(file_name):
            fill_bottles.append(file_name)
    return fill_bottles


def drink_bottle(file_name='bottle.txt'):
    if not check_bottle(file_name):
        return False
    with open(file_name, 'r+') as file:
        file.truncate(0)
    return True


def fill_bottle(file_name='bottle.txt'):
    if check_bottle(file_name):
        return False
    with open(file_name, 'w') as file:
        file.write('water')
    return True


def fill_empty_bottles():
    for file_name in take_empty_bottles():
        fill_bottle(file_name)


def drink_fill_bottles():
    for file_name in take_fill_bottles():
        drink_bottle(file_name)
