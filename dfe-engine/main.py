from config import LocalConfig
from manageInterface import ManageEndpoint

def poc():
    x_api_id = LocalConfig.get_credentials("x-api-id")
    x_api_key = LocalConfig.get_credentials("x-api-key")
    url = LocalConfig.get_config("url")
    nfe_received = LocalConfig.get_endpoint("nfe/received")
    response = ManageEndpoint(
        url,
        nfe_received["endpoint"],
        x_api_id,
        x_api_key,
        nfe_received["verb"],
        nfe_received["limit"],
        nfe_received["cursor"]
    )
    return response.get_received_list()

if __name__ == '__main__':
    print(poc())



