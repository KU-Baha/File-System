from pathlib import Path
import subprocess
import os


class File:
    def initializ(self, *args, **kwargs) -> None:
        subprocess.Popen('mkdir .zeon_fs', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    def add(self, file_path, *args, **kwargs) -> None:
        if Path(file_path).is_file():
            subprocess.Popen(f'copy {file_path} .', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    def delete(self, file_name, *args, **kwargs) -> None:
        subprocess.Popen(f"del {file_name}", shell=True,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)

    def list(self, *args, **kwargs) -> None:
        for i in os.listdir():
            print(i)