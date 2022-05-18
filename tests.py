import unittest
from helper import *


class TestSys(unittest.TestCase):

    def test_init(self):
        self.assertEqual(init(['zeon_sf']), None)

    def test_list_filter(self):
        self.assertEqual(list_files(''), None)

    def test_add_file(self):
        self.assertEqual(add_file(['Me.txt']), None)

    def test_delete_file(self):
        self.assertEqual(delete_file(['Me.txt']), None)

    def test_get_file(self):
        self.assertEqual(get_file(['Me.txt', 'You.txt']), None)


if __name__ == '__main__':
    unittest.main()