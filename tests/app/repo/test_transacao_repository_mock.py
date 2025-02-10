import pytest
from src.app.repo.transacao_repository_mock import TransacaoRepositoryMock

class Test_TransacaoRepositoryMock:
    def test_get_all_transactions(self):
        repo = TransacaoRepositoryMock()
        
        transacoes = repo.get_all_transactions()

        transacoes_esperadas = repo.transacoes
        
        assert transacoes_esperadas == transacoes
        
    def test_get_transaction(self):
        repo = TransacaoRepositoryMock()
        
        transacao = repo.get_transaction(1)

        transacao_esperada = repo.transacoes.get(1)
        
        assert transacao_esperada == transacao