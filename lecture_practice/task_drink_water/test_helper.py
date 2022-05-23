import os

from helper import check_bottle, drink_bottle, fill_bottle, take_bottles_list, take_empty_bottles, take_fill_bottles, \
    fill_empty_bottles, drink_fill_bottles


def test_take_bottles_list():
    assert take_bottles_list() == [bottle for bottle in os.listdir() if 'bottle' in bottle]


def test_check_bottle():
    assert check_bottle()


def test_drink_bottle():
    assert drink_bottle()
    assert not check_bottle()


def test_fill_bottle():
    assert fill_bottle()
    assert check_bottle()


def test_take_empty_bottles():
    assert drink_bottle()
    assert take_empty_bottles() == ['bottle.txt']


def test_take_fill_bottles():
    assert fill_bottle()
    assert take_fill_bottles() == ['bottle.txt']


def test_fill_empty_bottles():
    assert fill_empty_bottles() is None


def test_drink_fill_bottles():
    assert drink_fill_bottles() is None
