import time
from fastapi import FastAPI, HTTPException
from mangum import Mangum
from datetime import datetime
from .environments import Environments
from .errors.entity_errors import ParamNotValidated
from .enums.item_type_enum import ItemTypeEnum
from .entities.cliente import Cliente
from .entities.transacao import Transacao
from .repo.cliente_repository_mock import ClienteRepositoryMock
from .repo.transacao_repository_mock import TransacaoRepositoryMock

app = FastAPI()

repo_cliente = Environments.get_cliente_repo()()
repo_transacao = Environments.get_transacao_repo()()

clienteTeste = repo_cliente.get_client(1)

#CRIANDO AS ROTAS

#rota GET /clients
@app.get("/clientes/get_all_clients")
def get_all_clients():
    clientes = repo_cliente.get_all_clients()
    return {
        "clientes": [cliente.to_dict() for cliente in clientes]
    }

#rota GET /
@app.get("/clientes/get_client")
def get_client(client_id: int):
    valid_client_id = Cliente.client_id(client_id=client_id)
    if not valid_client_id[0]:
        raise HTTPException(status_code=400, detail=valid_client_id[1])
        print("Erro: ID de cliente inválido")

    cliente = repo_cliente.get_client(client_id)
    
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    return {
        "ID do Cliente": cliente.client_id(),
        "Dados do Cliente": cliente.to_dict()
    }

#rota POST /withdraw
@app.post("/withdraw", status_code=201)
def create_withdraw(request: dict):
    
    modelo = {
        "2": 0,
        "5": 0,
        "10": 0,
        "20": 0,
        "50": 0,
        "100": 0,
        "200": 0
    }
    
    quantia = 0.0
    
    for chave in request:
        if model.get(chave, None) is not None:
            quantia += float(chave) * float(request[chave])

    if quantia > clienteTeste.saldo_atual:
        raise HTTPException(status_code=403, detail="Saldo insuficiente")

    clienteTeste.saldo_atual -= quantia

    transacao = Transacao(type_transaction=ItemTypeEnum.DEPOSIT, value=quantia, current_balance=clienteTeste.saldo_atual, timestamp=time.time())

    repo_transacao.cria_transacao(transac=transacao, transac_id=int((transacao.saldoNaHora * transacao.quantia) / 1000))

    return {
        "horario_transacao": time.time(),
        "saldo_atual": clienteTeste.saldo_atual
    }

#rota POST /deposit
@app.post("/deposit", status_code=201)
def create_deposit(request: dict):
    
    modelo = {
        "2": 0,
        "5": 0,
        "10": 0,
        "20": 0,
        "50": 0,
        "100": 0,
        "200": 0
    }
    
    quantia = 0.0
    
    for chave in request:
        if model.get(chave, None) is not None:
            quantia += float(chave) * float(request[chave])

    if quantia > clienteTeste.saldo_atual*2:
        raise HTTPException(status_code=403, detail="Depósito Suspeito")

    clienteTeste.saldo_atual += quantia

    transacao = Transacao(type_transaction=ItemTypeEnum.DEPOSIT, value=quantia, current_balance=clienteTeste.saldo_atual, timestamp=time.time())

    repo_transacao.cria_transacao(transac=transacao, transac_id=int((transacao.saldoNaHora * transacao.quantia) / 1000))

    return {
        "horario_transacao": time.time(),
        "saldo_atual": clienteTeste.saldo_atual
    }

#rota GET /history
@app.get("/history", status_code=200)
def get_history():
    transacoes = repo_transacao.get_all_transactions()
    return {
        "transacoes": [transacao.to_dict() for transacao in transacoes]
    }
    
# from fastapi import FastAPI
# from src.app.environments import Environments
# from .repo.item_repository_mock import ItemRepositoryMock
# from .errors.entity_errors import ParamNotValidated
# from .entities.item import Item, ItemInput


# app = FastAPI()

# repo = Environments.get_item_repo()()

# @app.get("/items/get_items")
# def get_items():
#     print("Entrando no get_items")
#     items = repo.get_items()
    
#     for item in items:
#         print(f"Item: {item.name}, {item.email}, {item.item_id}, {item.password}")

#     items_list = [item.to_dict() for item in items]
        
#     return {
#         "items": items_list
#     }
    
# item_repo = ItemRepositoryMock()

# @app.post("/items/create_item")
# async def create_item(item: ItemInput):
#     data = item.dict()
#     new_item = item_repo.create_item(ItemInput(**data))
#     return new_item

handler = Mangum(app, lifespan="off")