from pathlib import Path

class FileManager:
    def __init__(self, file_dir, file_name, file_extension, file_content):
        self._dir = file_dir
        self._name = file_name
        self._extension = file_extension
        self._content = file_content

    def create_file(self):
        self._check_dir()
        path = f"{self._dir}/{self._name}.{self._extension}"
        with open(path, "w") as file:
            file.write(self._content)
        return path

    def _check_dir(self):
        Path(self._dir).mkdir(parents=True, exist_ok=True)