from services.manageInterface import ManageEndpoint


class GetNfeData:
    def __init__(self, api_id, api_key, url, config, main_dir):
        self._api_id = api_id
        self._api_key = api_key
        self._url = url
        self._main_dir = main_dir
        self._doc_config = config
        self._next_page = 0
        self._previous_page = 0
        self._count = 0

    @property
    def count(self):
        return self._count

    @property
    def next_page(self):
        return self._next_page

    @property
    def previous_page(self):
        return self._previous_page

    def get_data_list(self):
        response = ManageEndpoint(
            self._url,
            self._doc_config["endpoint"],
            self._api_id,
            self._api_key,
            self._doc_config["verb"],
            self._doc_config["limit"],
            self._doc_config["cursor"]
        )
        data_list = response.get_received_list()
        self._next_page = response.next_page
        self._previous_page = response.previous_page
        self._count = response.count

        return data_list


