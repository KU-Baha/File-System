from hashlib import md5
from pathlib import Path
import os
import shutil
import pickle

# Helper config
BASE_DIR_PATH = ".zeon_fs"
DATABASE_PATH = f"{BASE_DIR_PATH}/database.txt"
DB_BY_NAME = "BY_NAME"
DB_BY_HASH = "BY_HASH"
DB_START_DATA = {DB_BY_NAME: {}, DB_BY_HASH: {}}


# FS helper


def init_fs(dir_name: str = BASE_DIR_PATH, *args, **kwargs) -> None:
    os.makedirs(dir_name, exist_ok=True)
    init_db()


def add_file(
    file_path: str, dir_name: str, new_file_name: str = None, *args, **kwargs
) -> bool:
    if not Path(file_path).exists():
        return False
    file_name = Path(file_path).name if not new_file_name else new_file_name
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


def list_files(*args, **kwargs) -> list:
    if not Path(DATABASE_PATH).exists():
        raise "Database not found!"
    with open(DATABASE_PATH, "rb") as file:
        data = pickle.load(file)
        file_names = data[DB_BY_NAME].keys()
        for file_name in file_names:
            print(file_name)
    return file_names


# Database helper


def init_db(*args, **kwargs) -> None:
    if not Path(DATABASE_PATH).exists():
        with open(DATABASE_PATH, "wb") as file:
            pickle.dump(DB_START_DATA, file)


def checking_database(*args, **kwargs) -> bool:
    files = os.listdir(BASE_DIR_PATH)
    files.remove(DATABASE_PATH.split("/")[1])
    for file_name in files:
        file_hash = hash_file(f"{BASE_DIR_PATH}/{file_name}")
        add_to_database(file_name, file_hash)


def add_to_database(file_name: str, file_hash: str, *args, **kwargs) -> None:
    if Path(DATABASE_PATH).exists():
        with open(DATABASE_PATH, "rb") as file:
            data = pickle.load(file)
            data[DB_BY_NAME][file_name] = file_hash
            data[DB_BY_HASH][file_hash] = file_name
        with open(DATABASE_PATH, "wb") as file:
            pickle.dump(data, file)


def delete_from_database(file_name: str, file_hash: str, *args, **kwargs) -> None:
    with open(DATABASE_PATH, "rb") as file:
        data = pickle.load(file)
        del data[DB_BY_NAME][file_name]
        del data[DB_BY_HASH][file_hash]
    with open(DATABASE_PATH, "wb") as file:
        pickle.dump(data, file)


def get_by_key_from_index(index: str, key: str, *args, **kwargs) -> str:
    with open(DATABASE_PATH, "rb") as file:
        data = pickle.load(file)
        if index in data.keys():
            if key in data[index]:
                return data[index][key]
    return ""


def hash_file(file_path: str, *args, **kwargs) -> str:
    if not Path(file_path).exists():
        raise "File not found!"
    with open(file_path, "rb") as file:
        return md5(file.read()).hexdigest()


def database_list(*args, **kwargs) -> list:
    if not Path(DATABASE_PATH).exists():
        raise "Database not initialized!"
    with open(DATABASE_PATH, "rb") as file:
        data = pickle.load(file)
        return data


commands = {
    "init": init_fs,
    "add": add_file,
    "del": delete_file,
    "list": list_files,
    "get": add_file,
    "hash": hash_file,
    "db-list": database_list,
    "db-check": checking_database,
}
