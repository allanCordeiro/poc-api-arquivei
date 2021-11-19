from services.manageInterface import ManageEndpoint


class GetNfeData:
    def __init__(self, api_id, api_key, url, config, main_dir):
        self._api_id = api_id
        self._api_key = api_key
        self._url = url
        self._main_dir = main_dir
        self._doc_config = config

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
        return response.get_received_list()


