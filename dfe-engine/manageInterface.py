from utils import Base64Conversion
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
                dfe = {'access_key': item['access_key'], 'value': Base64Conversion.base64_decode(item['xml'])}
                dfe_list.append(dfe)
        self._current_cursor = int(data['count'])
        return dfe_list

    def get_doc_event(self):
        pass

    def get_doc_danfe(self):
        data = super().get_response()
        danfe_data = {}
        if data['status']['code'] == 200:
            danfe_data[data['data']['access_key']] = Base64Conversion.base64_decode(data['data']['encoded_pdf'], 'pdf')
        return danfe_data

    def get_document_count(self):
        return self._current_cursor



