import base64
from apidata import ArquiveiRequest


class ManageEndpoint(ArquiveiRequest):
    def __init__(self, uri, endpoint, x_api_id, x_api_key, verb, limit=None, cursor=None, access_key=None):
        super().__init__(uri, endpoint, x_api_id, x_api_key, verb, limit, cursor, access_key)
        self._current_cursor = 0

    def get_received_list(self):
        data = super().get_response()

        dfe_list = []
        if data['status']['code'] == 200:
            for item in data['data']:
                dfe = {'access_key': item['access_key'], 'value': self._base64_decode(item['xml'])}
                dfe_list.append(dfe)
        self._current_cursor = int(data['count'])
        return dfe_list

    def get_doc_event(self):
        pass

    def get_doc_danfe(self):
        data = super().get_response()
        danfe_data = {}
        if data['status']['code'] == 200:
            danfe_data[data['data']['access_key']] = self._base64_decode(data['data']['encoded_pdf'], 'pdf')
        return danfe_data

    def get_document_count(self):
        return self._current_cursor

    @staticmethod
    def _base64_decode(item, extension=None):
        base64_bytes = item.encode('utf-8')
        if extension == 'pdf':
            return base64.decodebytes(base64_bytes)
        decoded_data = base64.b64decode(base64_bytes)
        return decoded_data.decode('utf-8')


