from typing import Dict, List, Optional
from src.app.entities.transacao import Transacao
from src.app.repo.transacao_repository_interface import ITransacaoRepository
from src.app.enums.item_type_enum import ItemTypeEnum

class TransacaoRepositoryMock(ITransacaoRepository):
    transacoes: Dict[int, Transacao]
    
    def __init__(self):
        self.transacoes = {
            1: Transacao(type_transaction=ItemTypeEnum.WITHDRAW, value=100.00, current_balance=900.00, timestamp=1620000000.0),
            2: Transacao(type_transaction=ItemTypeEnum.DEPOSIT, value=200.00, current_balance=1000.00, timestamp=1620000000.0)
        }
    
    def get_all_transactions(self) -> List[Transacao]:
        return self.transacoes
    
    def get_transaction(self, transaction_id: int) -> Optional[Transacao]:
        return self.transacoes.get(transaction_id, None)
    
    def create_transaction(self, transaction: Transacao) -> Transacao:
        transaction_id = max(self.transacoes.keys()) + 1
        self.transacoes[transaction_id] = transaction
        return transaction
    
    def create_withdraw(self, value: float, current_balance: float, timestamp: float) -> Transacao:
        withdraw = Transacao(type_transaction=ItemTypeEnum.WITHDRAW, value=value, current_balance=current_balance, timestamp=timestamp)
        return self.create_transaction(transaction)
    
    def create_deposit(self, value: float, current_balance: float, timestamp: float) -> Transacao:
        deposit = Transacao(type_transaction=ItemTypeEnum.DEPOSIT, value=value, current_balance=current_balance, timestamp=timestamp)
        return self.create_transaction(transaction)