from config import LocalConfig
from apidata import ArquiveiRequest

def poc():
    x_api_id = LocalConfig.get_credentials("x-api-id")
    x_api_key = LocalConfig.get_credentials("x-api-key")
    url = LocalConfig.get_config("url")
    #nfe_received = LocalConfig.get_endpoint("nfe/received")
    #response = ArquiveiRequest(
    #    url,
    #    nfe_received["endpoint"],
    #    x_api_id,
    #    x_api_key,
    #    nfe_received["verb"],
    #    nfe_received["limit"],
    #    nfe_received["cursor"]
     #)

    event = LocalConfig.get_endpoint("nfe/danfe")
    response = ArquiveiRequest(
        url,
        event["endpoint"],
        x_api_id,
        x_api_key,
        event["verb"],
        access_key="35210461186888000274550170022498411055679080"
    )


    return response.get_response()

if __name__ == '__main__':
    print(poc())



