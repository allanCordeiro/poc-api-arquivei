import logging
import json
from datetime import datetime
from decouple import config, UndefinedValueError

file_timestamp = datetime.now().strftime('%Y-%m-%d')
logging.basicConfig(filename=f'files/logs/log_{file_timestamp}.log',
                    filemode='a',
                    level=logging.INFO,
                    format='%(asctime)s ::%(levelname)s :: %(message)s')


class LocalConfig:
    @staticmethod
    def __open_json():
        with open("config.json", "r") as json_file:
            return json.load(json_file)

    @staticmethod
    def get_credentials(credential_key):
        try:
            if credential_key == 'x-api-id':
                return config('x-api-id')
            elif credential_key == 'x-api-key':
                return config('x-api-key')
            else:
                logging.error('Chave solicitada é inválida')
                return False
        except UndefinedValueError as e:
            logging.info('A chave não foi encontrada. Verifique se o arquivo .env existe')
            logging.error(f'Exception -> {e}')

    @staticmethod
    def get_api_address():
        try:
            return config("api-address")
        except UndefinedValueError as e:
            logging.info('Endereco do ambiente nao encontrado. Verifique se o arquivo .env existe')
            logging.error(f'Exception -> {e}')


    @staticmethod
    def get_config(tag):
        json_file = LocalConfig.__open_json()
        return json_file[tag]

    @staticmethod
    def get_endpoint(endpoint_name):
        json_file = LocalConfig.get_config("endpoints")
        return json_file[endpoint_name]

    @staticmethod
    def set_cursor(endpoint_name, cursor):
        json_file = LocalConfig.__open_json()
        with open("config.json", "w") as full_config:
            json_file['endpoints'][endpoint_name]['cursor'] = cursor
            json.dump(json_file, full_config, indent=4)