from pathlib import Path

class FileManager:
    def __init__(self, file_dir, file_name, file_extension, file_content, type=None):
        self._dir = file_dir
        self._name = file_name
        self._extension = file_extension
        self._content = file_content
        self._type = type
        self._write_mode = 'w'

    def create_file(self):
        _check_dir(self._dir)
        if self._type is not None:
            self._write_mode = 'wb'
        path = f"{self._dir}/{self._name}.{self._extension}"
        with open(path, self._write_mode) as file:
            file.write(self._content)
        return path


def _check_dir(path_structure):
    Path(path_structure).mkdir(parents=True, exist_ok=True)
