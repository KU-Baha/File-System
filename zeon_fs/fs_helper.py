from database_helper import init_db, get_by_key_from_index, add_to_database, delete_from_database, hash_file
from configs import DB_BY_HASH, DB_BY_NAME, BASE_DIR_PATH
from pathlib import Path
import os
import shutil


def init_fs(dir_name: str = BASE_DIR_PATH, *args, **kwargs) -> None:
    os.makedirs(dir_name, exist_ok=True)
    init_db()


def add_file(file_path: str, dir_name: str, *args, **kwargs) -> bool:
    if not Path(file_path).exists():
        return False
    file_name = Path(file_path).name
    file_hash = hash_file(file_path)
    if (
            get_by_key_from_index(index=DB_BY_NAME, key=file_name) == ""
            and get_by_key_from_index(index=DB_BY_HASH, key=file_hash) == ""
    ):
        shutil.copyfile(file_path, f"{dir_name}/{file_name}")
        add_to_database(file_name, file_hash)
        return True
    return False


def delete_file(file_path: str, *args, **kwargs) -> bool:
    if not Path(file_path).exists():
        return False
    delete_from_database(file_name=Path(file_path).name, file_hash=hash_file(file_path))
    os.remove(file_path)
    return True


def list_files(dir_path: str = BASE_DIR_PATH, *args, **kwargs) -> list:
    dir_list = os.listdir(path=dir_path)
    for i in dir_list:
        print(i)
    return dir_list


def get_file(file_path: str, file_name: str, dir_name: str, *args, **kwargs) -> bool:
    if not Path(file_path).is_file():
        return False
    shutil.copyfile(file_path, f"{dir_name}/{file_name}")
    return True
