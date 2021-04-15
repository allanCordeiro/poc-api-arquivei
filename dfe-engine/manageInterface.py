import base64
from apidata import ArquiveiRequest


class ManageEndpoint(ArquiveiRequest):
    def __init__(self, uri, endpoint, x_api_id, x_api_key, verb, limit=0, cursor=0, access_key=''):
        super().__init__(uri, endpoint, x_api_id, x_api_key, verb, limit=0, cursor=0, access_key='')

    def get_received_list(self):
        data = super().get_response()
        dfe_list = {}
        if data['status']['code'] == 200:
            for item in data['data']:
                dfe_list[item['access_key']] = self._base64_decode(item['xml'])
        return dfe_list

    def get_doc_event(self):
        pass

    def get_doc_danfe(self):
        pass

    @staticmethod
    def _base64_decode(item):
        base64_bytes = item.encode('utf-8')
        decoded_data = base64.b64decode(base64_bytes)
        return decoded_data.decode('utf8')

