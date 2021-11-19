from utils.filemanager import FileManager


class DocumentHandler:
    def __init__(self, path, obj, file_extension, data_type=None):
        self._path = path
        self._object = obj
        self._extension = file_extension
        self._type = data_type

    def create_file(self):
        for item in self._object:
            file = FileManager(self._path, item['access_key'], self._extension, item['value'], self._type)
            file.create_file()

