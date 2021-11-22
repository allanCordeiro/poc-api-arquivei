import requests
import logging


class ArquiveiRequest:
    def __init__(self, uri, endpoint, x_api_id, x_api_key, verb, limit=None, cursor=None, access_key=None):
        self._uri = uri
        self._endpoint = endpoint
        self._x_api_id = x_api_id
        self._x_api_key = x_api_key
        self._verb = verb
        self._limit = limit
        self._cursor = cursor
        self._access_key = access_key

    def _get_header(self):
        header = {
            "Content-Type": "application/json",
            "x-api-id": self._x_api_id,
            "x-api-key": self._x_api_key
        }
        return header

    def _get_endpoint(self):
        complete_url = f"{self._uri}{self._endpoint}"
        if self._limit is not None:
            complete_url += f"?limit={self._limit}"
        if self._cursor is not None:
            complete_url += f"&cursor={self._cursor}"
        if self._access_key is not None:
            complete_url += f"?access_key={self._access_key}"
        return complete_url

    def get_response(self):
        uri = self._get_endpoint()
        header = self._get_header()
        document: requests.Response
        if self._verb == "get":
            document = requests.get(uri, headers=header)
        # todo:: aqui não houve necessidade de trabalhar os outros verbos.
        if document.status_code == 200:
            return document.json()
        else:
            logging.error(f"Status code error: {document.status_code}")
            raise Exception("Erro de status code capturado. Olhar logs.")
