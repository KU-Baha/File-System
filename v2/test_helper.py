from helper import *


def test_parse_input():
    arguments = []
    assert parse_input(arguments) is None

    arguments = ["main.py"]
    assert parse_input(arguments) is None

    arguments = ["main.py", "init"]
    expected = ["init"]
    actual = parse_input(arguments)
    assert expected == actual

    arguments = ["main.py", "add", "file.txt"]
    expected = ["add", "file.txt"]
    actual = parse_input(arguments)
    assert expected == actual
