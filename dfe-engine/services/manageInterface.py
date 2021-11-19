from urllib.parse import urlparse, parse_qs
from utils import base64Conversion
from .apidata import ArquiveiRequest


class ManageEndpoint(ArquiveiRequest):
    def __init__(self, uri, endpoint, x_api_id, x_api_key, verb, limit=None, cursor=None, access_key=None):
        super().__init__(uri, endpoint, x_api_id, x_api_key, verb, limit, cursor, access_key)
        self._current_cursor = 0
        self._next_page_cursor = 0
        self._previous_page_cursor = 0

    @property
    def next_page(self):
        return self._next_page_cursor

    @property
    def previous_page(self):
        return self._previous_page_cursor

    def get_received_list(self):
        data = super().get_response()

        document_list = []
        if data['status']['code'] == 200:
            for item in data['data']:
                document = {'access_key': item['access_key'], 'value': base64Conversion.base64_decode(item['xml'])}
                document_list.append(document)
            self._current_cursor = int(data['count'])
            self._get_page_cursors(data['page'])
        return document_list

    def get_doc_event(self):
        pass

    def get_doc_danfe(self):
        data = super().get_response()
        danfe_data = {}
        if data['status']['code'] == 200:
            danfe_data[data['data']['access_key']] = base64Conversion.base64_decode(data['data']['encoded_pdf'], 'pdf')
        return danfe_data

    def get_document_count(self):
        return self._current_cursor

    def _get_page_cursors(self, page):
        next = urlparse(page['next'])
        previous = urlparse(page['previous'])
        self._next_page_cursor = parse_qs(next.query)['cursor'][0]
        self._previous_page_cursor = parse_qs(previous.query)['cursor'][0]


