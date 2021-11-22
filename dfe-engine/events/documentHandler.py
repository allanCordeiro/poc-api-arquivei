from utils.filemanager import FileManager
from utils.logcapture import Logger


class DocumentHandler:
    def __init__(self, path, obj, file_extension, data_type=None):
        self._path = path
        self._object = obj
        self._extension = file_extension
        self._type = data_type
        self._logger = Logger()

    def create_file(self):
        for item in self._object:
            try:
                file = FileManager(self._path, item['access_key'], self._extension, item['value'], self._type)
                file.create_file()
                self._logger.log(f"Arquivo {item['access_key']} criado com sucesso.")
            except Exception as e:
                self._logger.log(f"Erro durante geração de arquivo de chave de acesso. Ex: {e=}", "error")

