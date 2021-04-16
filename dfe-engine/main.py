from config import LocalConfig
from manageInterface import ManageEndpoint
from filemanager import FileManager

def poc():
    x_api_id = LocalConfig.get_credentials("x-api-id")
    x_api_key = LocalConfig.get_credentials("x-api-key")
    url = LocalConfig.get_config("url")
    nfe_received = LocalConfig.get_endpoint("nfe/received")
    xml_dir = f"{LocalConfig.get_config('xml_dir')}/{nfe_received['dir']}"
    extension = nfe_received['extension']
    response = ManageEndpoint(
        url,
        nfe_received["endpoint"],
        x_api_id,
        x_api_key,
        nfe_received["verb"],
        nfe_received["limit"],
        nfe_received["cursor"]
    )
    nfes = response.get_received_list()
    # vamos iterar por cada uma delas, gerando os xmls
    for nfe in nfes:
        print(nfe['access_key'])
        file = FileManager(xml_dir, nfe['access_key'], extension, nfe['value'])
        file.create_file()
if __name__ == '__main__':
    nfes = poc()




