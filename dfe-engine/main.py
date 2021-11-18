from config import LocalConfig
from manageInterface import ManageEndpoint
from filemanager import FileManager


def orchestrate():
    x_api_id = LocalConfig.get_credentials("x-api-id")
    x_api_key = LocalConfig.get_credentials("x-api-key")
    url = LocalConfig.get_api_address()
    nfe_received = LocalConfig.get_endpoint("nfe/received")
    xml_dir = f"{LocalConfig.get_config('files_dir')}/{nfe_received['dir']}"
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
        print(f'Obtendo dados da chave:: {nfe["access_key"]}')
        file = FileManager(xml_dir, nfe['access_key'], extension, nfe['value'])
        file.create_file()
        danfe_endpoint =  LocalConfig.get_endpoint("nfe/danfe")
        danfe_response = ManageEndpoint(
            url,
            danfe_endpoint["endpoint"],
            x_api_id,
            x_api_key,
            danfe_endpoint["verb"],
            access_key=nfe['access_key']
        )
        danfe_received = LocalConfig.get_endpoint("nfe/danfe")
        danfe_dir = f"{LocalConfig.get_config('files_dir')}/{danfe_received['dir']}"
        danfe = danfe_response.get_doc_danfe()
        pdf_file = FileManager(danfe_dir, nfe['access_key'], 'pdf', danfe[nfe['access_key']], 'pdf')
        pdf_file.create_file()

    # colocar um try aqui aqui
    # atualiza o cursor
    current_cursor = int(nfe_received["cursor"]) + response.get_document_count()
    LocalConfig.set_cursor('nfe/received', current_cursor)


if __name__ == '__main__':
    orchestrate()




