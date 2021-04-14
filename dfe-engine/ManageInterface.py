from apidata import ArquiveiRequest


class ManageEndpoint(ArquiveiRequest):
    def __init__(self, uri, endpoint, x_api_id, x_api_key, verb, limit=0, cursor=0, access_key=''):
        super().__init__(uri, endpoint, x_api_id, x_api_key, verb, limit=0, cursor=0, access_key='')

    def get_received_list(self):
        pass

    def get_doc_event(self):
        pass

    def get_doc_danfe(self):
        pass
    