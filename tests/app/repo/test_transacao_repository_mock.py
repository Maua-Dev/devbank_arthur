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
        
    def test_create_transaction(self):
        repo = TransacaoRepositoryMock()
        
        transacao = repo.create_transaction(repo.transacoes[1])
        
        assert transacao == repo.transacoes[1]
        
    def test_create_withdraw(self):
        repo = TransacaoRepositoryMock()
        
        transacao_saque = repo.create_withdraw(100.00, 900.00, 1620000000.0)
        
        assert transacao_saque == repo.transacoes[3]
        
    def test_create_deposit(self):
        repo = TransacaoRepositoryMock()
        
        transacao_deposito = repo.create_deposit(200.00, 1000.00, 1620000000.0)
        
        assert transacao_deposito == repo.transacoes[3]
        
        #DÚVIDA: POR QUÊ O ID FUNCIONA COM 3 EM TRANSAÇÃO SOMENTE?