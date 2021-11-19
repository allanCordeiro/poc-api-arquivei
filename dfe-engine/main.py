from appConfig import LocalConfig
from services.manageInterface import ManageEndpoint
from utils.filemanager import FileManager
from events.nfe import GetNfeData
from events.documentHandler import DocumentHandler


def nfe():
    x_api_id = LocalConfig.get_credentials("x-api-id")
    x_api_key = LocalConfig.get_credentials("x-api-key")
    url = LocalConfig.get_api_address()
    nfe_received = LocalConfig.get_endpoint("nfe/received")
    xml_dir = f"{LocalConfig.get_config('files_dir')}/{nfe_received['dir']}"
    nfe_data = GetNfeData(x_api_id, x_api_key, url, nfe_received, xml_dir)
    nfe_list = nfe_data.get_data_list()
    doc_handler = DocumentHandler(xml_dir, nfe_list, 'xml')
    doc_handler.create_file()
    LocalConfig.set_cursor('nfe/received', nfe_data.next_page)

    return nfe_list


def danfe(nfe_list):
    x_api_id = LocalConfig.get_credentials("x-api-id")
    x_api_key = LocalConfig.get_credentials("x-api-key")
    url = LocalConfig.get_api_address()
    danfe_endpoint = LocalConfig.get_endpoint("nfe/danfe")
    file_dir = f"{LocalConfig.get_config('files_dir')}/{danfe_endpoint['dir']}"
    for nfe in nfe_list:
        danfe_response = ManageEndpoint(
            url,
            danfe_endpoint["endpoint"],
            x_api_id,
            x_api_key,
            danfe_endpoint["verb"],
            access_key=nfe['access_key']
        )
        danfe = danfe_response.get_doc_danfe()
        print(danfe)
        doc_handler = DocumentHandler(file_dir, danfe, 'pdf', 'pdf')
        doc_handler.create_file()


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
    # orchestrate()
    doc_list = nfe()
    danfe(doc_list)





