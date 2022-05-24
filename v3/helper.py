from pathlib import Path
import os


def init_fs(dir_name: str, *args) -> None:
    os.makedirs(dir_name, exist_ok=True)


def add_file(file_path: str, dir_name: str, *args) -> bool:
    if not check_file(file_path):
        return False
    with open(file_path, "rb") as read_file:
        with open(
                f"{dir_name}/{Path(file_path).stem}{Path(file_path).suffix}", "wb"
        ) as write_file:
            write_file.write(read_file.read())
    return True


def delete_file(file_path: str, *args) -> bool:
    if not check_file(file_path):
        return False
    os.remove(file_path)
    return True


def list_files(dir_path: str, *args) -> list:
    dir_list = os.listdir(path=dir_path)
    for i in dir_list:
        print(i)
    return dir_list


def get_file(file_path: str, file_name: str, dir_name: str, *args) -> bool:
    if not check_file(file_path):
        return False
    with open(file_path, "rb") as read_file:
        with open(f"{dir_name}/{file_name}", "wb") as write_file:
            write_file.write(read_file.read())
    return True


def check_file(file_path: str, *args) -> bool:
    if not Path(file_path).is_file():
        return False
    return True


commands = {
    "init": init_fs,
    "add": add_file,
    "del": delete_file,
    "list": list_files,
    "get": get_file,
}
