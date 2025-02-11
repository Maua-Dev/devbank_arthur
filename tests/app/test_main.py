import pytest
import fastapi.exceptions
from fastapi.exceptions import HTTPException
from src.app.main import get_all_clients, get_client, create_deposit, create_withdraw
from src.app.repo.cliente_repository_mock import ClienteRepositoryMock
from src.app.repo.transacao_repository_mock import TransacaoRepositoryMock
from src.app.entities.cliente import Cliente
from src.app.entities.transacao import Transacao

class Test_Main:
    def test_get_all_clients(self):
        repo = ClienteRepositoryMock()
        response = get_all_clients()
        assert all([client_expect.to_dict() == client for client_expect, client in
                    zip(repo.clientes.values(), response.get("clients"))])

    def test_get_client(self):
        repo = ClienteRepositoryMock()
        client_id = 1
        response = get_client(client_id=client_id)
        assert response == {
            'ID do Cliente': client_id,
            'Dados do Cliente': repo.clientes.get(client_id).to_dict()
        }

    def test_create_deposit(self):
        repo = ClienteRepositoryMock()
        response = create_deposit(request={
            "2": 2,
            "5": 4,
            "10": 1,
            "20": 3,
            "50": 0,
            "100": 2,
            "200": 0
        })
        total_esperado = 294 + repo.get_client(1).saldo_atual
        assert total_esperado == response.get("saldo_atual")

    def test_saldo_suspeito(self):
        with pytest.raises(fastapi.exceptions.HTTPException) as exc_info:
            response = create_deposit(request={
                "2": 2,
                "5": 4,
                "10": 1,
                "20": 3,
                "50": 30,
                "100": 10,
                "200": 20
            })
        assert exc_info.value.status_code == 403
        assert exc_info.value.detail == "Saldo suspeito"

    def test_create_withdraw(self):
        repo = ClienteRepositoryMock()
        response = create_withdraw(request={
            "2": 2,
            "5": 4,
            "10": 1,
            "20": 3,
            "50": 0,
            "100": 1,
            "200": 0
        })
        total_esperado = repo.get_client(1).saldo_atual + 294 - 194
        assert total_esperado == response.get("saldo_atual")

    def test_saldo_insuficiente(self):
        with pytest.raises(fastapi.exceptions.HTTPException) as exc_info:
            response = create_withdraw(request={
                "2": 2,
                "5": 4,
                "10": 1,
                "20": 3,
                "50": 30,
                "100": 10,
                "200": 40
            })
        assert exc_info.value.status_code == 403
        assert exc_info.value.detail == "Saldo insuficiente"

# class Test_Main:
#     def test_main(self):
#         response = get_items()
        
#         expected_response = {
#             "items":[{"nome":"Miguel","email":"mneto.devmaua@gmail.com","item_id":1,"password":"psswd123"},{"nome":"Arthur","email":"asilva.devmaua@gmail.com","item_id":2,"password":"psswd456"},{"nome":"Mateus","email":"msobrenome.devmaua@gmail.com","item_id":3,"password":"psswd789"},{"nome":"Victor","email":"vsoller.devmaua@gmail.com","item_id":4,"password":"psswd000"}]
#             }

#         assert type(response) == dict
#         assert response == expected_response