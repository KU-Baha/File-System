from string import digits


def only_letters(line):
    return ''.join([letter for letter in line if letter not in digits])
