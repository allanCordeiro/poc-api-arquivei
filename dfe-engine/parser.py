import xmltodict


file_path = 'files/nfe/xml/31210411606543001811550010000136601158604209.xml'

with open(file_path, "r") as file:
    xml = file.read()

doc = xmltodict.parse(xml)
#NFE model
print(doc["nfeProc"]["NFe"]["infNFe"]["ide"]["dhEmi"])
print(doc["nfeProc"]["NFe"]["infNFe"]["emit"]["CNPJ"])
print(doc["nfeProc"]["NFe"]["infNFe"]["dest"]["CNPJ"])
