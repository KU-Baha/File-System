from helper import check_command, plus, minus, division, multiplication


def test_check_command():
    arguments = '+'
    assert check_command(arguments)


def test_plus():
    num1, num2 = 5, 5
    expected = 10
    assert plus(num1, num2) == expected


def test_minus():
    num1, num2 = 5, 10
    expected = -5
    assert minus(num1, num2) == expected


def test_division():
    num1, num2 = 0, 5
    expected = 0
    assert division(num1, num2) == expected
    num1, num2 = 5, 5
    expected = 1
    assert division(num1, num2) == expected


def test_multiplication():
    num1, num2 = 5, 5
    expected = 25
    assert multiplication(num1, num2) == expected
