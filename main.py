import sys, os
from pathlib import Path


class Directory:
    def __init__(self, path=None, file_system_name='file_system.txt', mode='create'):
        self.file_system_name = file_system_name
        match mode:
            case 'load':
                self.load()
            case 'create':
                self.path = path

    def create(self, filename: str):
        filename = self.check_file_name(filename)
        open(filename, 'w').close()
        print(f'File was created! {self.path}\\{filename}')

    def delete(self, filename: str):
        if filename in os.listdir():
            os.remove(filename)
            print(f'File {filename} was deleted')
        else:
            print(f'File not found!')

    def check_file_name(self, filename: str):
        if filename in os.listdir():
            filename = f'{Path(filename).stem} - Копия.{Path(filename).suffix}'
            return self.check_file_name(filename)
        return filename

    def load(self):
        with open(self.file_system_name, 'r') as file:
            self.path = file.readline(0)

    def save(self):
        with open(self.file_system_name, 'w') as file:
            file.write(self.path)
        print(f'Initialized empty FileSystem in {self}')

    def __str__(self):
        return f'{self.path}'


def main(argv):
    match argv:
        case 'init', *argv:
            directory = Directory(os.getcwd())
            directory.save()
        case 'create', filename, *argv:
            directory = Directory(mode='load')
            directory.create(filename=filename)
        case 'delete', filename, *argv:
            directory = Directory(mode='load')
            directory.delete(filename=filename)


if __name__ == '__main__':
    main(sys.argv[1:])
