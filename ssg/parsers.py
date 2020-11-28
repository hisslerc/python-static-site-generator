from pathlib import Path
from typing import List
import shutil


class Parser:
    extensions : List[str] = []

    def __init__(self):
        pass

    def valid_extension(self, extension):
        return True if extension in self.extensions else False

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path: Path):
        with open(path, "r") as file:
            return file.read()

    def write(self, path: Path, dest, content, ext='.html'):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, 'w') as file:
            file.write(content)

    def copy(self, path: Path, source, dest):
        destination = dest / path.relative_to(source)
        shutil.copy2(path, destination)


class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        self.copy(path, source, dest)
