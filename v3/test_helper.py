from helper import *
from pathlib import Path

target_path = "test_directory_zeon_fs"
source_path = "test_values"
test_files = ["file.txt", "file2.txt", "file3.txt"]


def test_init_fs():
    assert init_fs(target_path) is None
    assert Path(target_path).is_dir()


def test_add_file():
    for file in test_files:
        assert add_file(f"{source_path}/{file}", target_path)
        assert Path(f"{target_path}/{file}").is_file()


def test_delete_file():
    for file in test_files:
        assert delete_file(f"{target_path}/{file}")
        assert not Path(f"{target_path}/{file}").is_file()


def test_list_files():
    for file in test_files:
        assert file in list_files(source_path)


def test_get_file():
    for num, file in enumerate(test_files):
        assert get_file(f"{source_path}/{file}", f"{num}.{file}", target_path)
        assert Path(f"{target_path}/{num}.{file}").is_file()
