from helper import *
from pathlib import Path

# Test config
target_path = ".zeon_fs"
fake_target_path = ".zeon_fs_fake"
source_path = "test_values"
test_files = ["file.txt", "file2.txt", "file3.txt"]
files_hashes = {
    "file.txt": "81a5e57bdb8e47d91329a632b72158bc",
    "file2.txt": "b4165c4e90f2120c9f561ec59f6110b0",
    "file3.txt": "ff4bc5d2ef8a470a1c37d14520e845f5",
}


def test_init_fs():
    assert init_fs(target_path) is None
    assert Path(target_path).is_dir()
    assert not Path(fake_target_path).is_dir()


def test_init_db():
    init_db()
    assert Path(DATABASE_PATH).exists()


def test_add_file():
    for file in test_files:
        assert add_file(f"{source_path}/{file}", target_path)
        assert Path(f"{target_path}/{file}").is_file()


def test_get_by_key_from_index():
    for file_name, file_hash in files_hashes.items():
        assert get_by_key_from_index(DB_BY_NAME, file_name) == file_hash
        assert get_by_key_from_index(DB_BY_HASH, file_hash) == file_name


def test_list_files():
    for file in test_files:
        assert file in list_files(source_path)


def test_delete_file():
    for file in test_files:
        assert delete_file(f"{target_path}/{file}")
        assert not Path(f"{target_path}/{file}").is_file()


def test_get_file():
    for num, file in enumerate(test_files):
        new_file_name = f"{num}.{file}"
        assert add_file(f"{source_path}/{file}", target_path, new_file_name)
        assert Path(f"{target_path}/{new_file_name}").is_file()
        assert delete_file(f"{target_path}/{new_file_name}")
        assert not Path(f"{target_path}/{new_file_name}").is_file()


def test_hash_file():
    for file in test_files:
        assert hash_file(f"{source_path}/{file}") == files_hashes[file]
    for file in test_files:
        assert hash_file(file) == ""


def test_database_list():
    assert database_list() == DB_START_DATA


def test_add_to_database():
    for file_name, file_hash in files_hashes.items():
        add_to_database(file_name, file_hash)
        assert get_by_key_from_index(DB_BY_NAME, file_name) == file_hash
        assert get_by_key_from_index(DB_BY_HASH, file_hash) == file_name


def test_delete_from_database():
    for file_name, file_hash in files_hashes.items():
        delete_from_database(file_name, file_hash)
        assert get_by_key_from_index(DB_BY_NAME, file_name) == ""
        assert get_by_key_from_index(DB_BY_HASH, file_hash) == ""


def test_checking_database():
    for file_name in test_files:
        shutil.copyfile(f"{source_path}/{file_name}", f"{target_path}/{file_name}")
    checking_database()
    for file_name, file_hash in files_hashes.items():
        assert get_by_key_from_index(DB_BY_NAME, file_name) == file_hash
        assert get_by_key_from_index(DB_BY_HASH, file_hash) == file_name
