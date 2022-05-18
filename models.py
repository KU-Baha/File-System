from pathlib import Path
import subprocess
import os


class File:
    def initializ(self, *args, **kwargs) -> None:
        subprocess.Popen('mkdir .zeon_fs', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    def add(self, *args, **kwargs) -> None:
        if Path(args[0]).is_file():
            subprocess.Popen(f'copy {args[0]} .', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    def delete(self, *args, **kwargs) -> None:
        subprocess.Popen(f"del {args[0]}", shell=True,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)

    def list(self, *args, **kwargs) -> None:
        for i in os.listdir():
            print(i)