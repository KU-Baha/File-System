from str_helper import only_letters


def test_only_letters():
    line = '124hellfoas 1245213123213'
    expected = 'hellfoas '
    assert only_letters(line) == expected