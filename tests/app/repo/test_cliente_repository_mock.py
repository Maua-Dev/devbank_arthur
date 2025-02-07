import pytest
from src.app.repo.cliente_repository_mock import ClienteRepositoryMock

class Test_ClienteRepositoryMock:
    def test_get_all_clients(self):
        repo = ClienteRepositoryMock()
        
        clientes = repo.get_all_clients()

        clientes_esperados = repo.clientes

        assert clientes_esperados == clientes
        
    def test_get_clients(self):
        repo = ClienteRepositoryMock()
        
        cliente = repo.get_client(1)

        cliente_esperado = repo.clientes.get(1)

        assert cliente_esperado == cliente