from config import LocalConfig

def poc():
    # variavel = LocalConfig.get_config('endpoints["nfe/received"]')
    # variavel = LocalConfig.get_endpoint('nfe/received')
    # return variavel
    variavel = LocalConfig.set_cursor('nfe/received', 35)
    return variavel

if __name__ == '__main__':
    print(poc())



