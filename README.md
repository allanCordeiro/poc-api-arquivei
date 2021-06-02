# poc-api-arquivei

O objetivo desse script é mostrar o processo de consumo e orquestração dos endpoints da API disponibilizados pelo Arquivei (https://www.arquivei.com.br).

Este aplicativo foi feito por mim, excluindo do Arquivei qualquer responsabilidade a respeito de suporte do mesmo.

Pullrequests e sugestões são sempre bem-vindas. :) 

## Começando

As instruções abaixo lhe guiarão em como realizar uma cópia do projeto e executá-lo.


### Pré-requisitos

É recomendado utilizar o virtualenv caso a proposta seja melhorar/desenvolver o split-cnab. No mais, são utilizadas 
todas as bibliotecas nativas do Python.

Linux via apt:
```
$ apt-get install python-pip
$ sudo pip install virtualenv
```

Linux via yum:
```
$ yum install python-pip
$ sudo pip install virtualenv
```

### Instalando

Realize o download ou o clone do repositório. Em seguida execute o arquivo de dependencia:

```
$ pip install -r requirements.txt
```

Após, crie um arquivo .env. É neste arquivo que serão inseridas as credenciais de acesso da API. No seguinte modelo:

```
x-api-id=hash-do-id-das-credenciais
x-api-key=hash-do-key-das-credenciais
```


### Uso

A utilização é auto-explicativa. São tratados os endpoints da API do Arquivei (https://docs.arquivei.com.br/). A função do script é disponibilizar os xmls e danfes das notas fiscais em um diretório específico. Cada endpoint tem sua configuração em um arquivo json. Neste arquivo, além do diretório, é possível também gerenciar a paginação através do uso do cursor como contador de notas, assim é possível evitar consultas repetidas.

config.json
```
{
    "data_dir": "data",
    "xml_dir": "data/nfe",
    "url": "https://api.arquivei.com.br/",
    "endpoints": {
        "nfe/received": {
            "endpoint": "v1/nfe/received",
            "dir": "xml",
            "extension": "xml",
            "verb": "get",
            "limit": "50",
            "cursor": 100
        },
        "nfe/events": {
            "endpoint": "v2/nfe/events",
            "dir": "event",
            "extension": "xml",
            "verb": "get",
            "limit": "0",
            "cursor": 0
        },
        "nfe/danfe": {
            "endpoint": "v1/nfe/danfe",
            "dir": "danfe",
            "extension": "pdf",
            "verb": "get",
            "limit": "0",
            "cursor": 0
        }
    }
}
```

### Backlog

- Download de eventos da NFe;
- Controle de dados chave de um documento fiscal através de uma base de dados;
- Download de dados de CTes;
- Download de dados de NFSes;
- Upload de NFes;
- Upload de NFSes (manual, proposta via OCR)