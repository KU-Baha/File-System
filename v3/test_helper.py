from helper import *
from pathlib import Path


def test_init_fs():
    assert init_fs('test_directory_zeon_fs') is None
    assert Path('test_directory_zeon_fs').is_dir()


def test_add_file():
    assert add_file('test_values/MyFile.txt', 'test_directory_zeon_fs')
    assert Path('test_directory_zeon_fs/MyFile.txt').is_file()


def test_delete_file():
    assert delete_file('test_directory_zeon_fs/MyFile.txt')
    assert not Path('test_directory_zeon_fs/MyFile.txt').is_file()


def test_list_files():
    assert list_files('test_values') == ['MyFile.txt']


def test_get_file():
    assert get_file('test_values/MyFile.txt', 'MyFavoriteFile.txt', 'test_directory_zeon_fs')
