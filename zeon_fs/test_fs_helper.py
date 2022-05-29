from zeon_fs.fs_helper import *
from pathlib import Path


def test_init_fs():
    assert init_fs(target_path) is None
    assert Path(target_path).is_dir()
    assert not Path(fake_target_path).is_dir()


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


def test_hash_file():
    for file in test_files:
        assert hash_file(f"{source_path}/{file}") == files_hashes[file]
    for file in test_files:
        assert hash_file(file) == ""
