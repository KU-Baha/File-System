from fs_helper import init_fs, add_file, delete_file, list_files, get_file, hash_file
from database_helper import database_list

# Main commands

commands = {
    "init": init_fs,
    "add": add_file,
    "del": delete_file,
    "list": list_files,
    "get": get_file,
    "hash": hash_file,
    "database": database_list,
}

# Helper config

BASE_DIR_PATH = ".zeon_fs"
DATABASE_PATH = f"{BASE_DIR_PATH}/database.txt"
DB_BY_NAME = "BY_NAME"
DB_BY_HASH = "BY_HASH"
DB_START_DATA = {DB_BY_NAME: {}, DB_BY_HASH: {}}

# Test config

target_path = "test_directory_zeon_fs"
fake_target_path = "test_directory_zeon_fs_fake"
source_path = "test_values"
test_files = ["file.txt", "file2.txt", "file3.txt"]
files_hashes = {
    "file.txt": "81a5e57bdb8e47d91329a632b72158bc",
    "file2.txt": "b4165c4e90f2120c9f561ec59f6110b0",
    "file3.txt": "ff4bc5d2ef8a470a1c37d14520e845f5",
}
