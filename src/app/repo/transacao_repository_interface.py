from abc import ABC, abstractmethod
from typing import List, Optional
from src.app.entities.transacao import Transacao

class ITransacaoRepository(ABC):
    
    @abstractmethod
    def get_all_transactions(self) -> List[Transacao]:
        '''
        Retorna todas as transações realizadas (para o histórico)
        '''
        pass
    
    @abstractmethod
    def get_transaction(self) -> Optional[Transacao]:
        '''
        Retorna uma transação específica
        Determinada pelo id
        '''
        pass
    
    @abstractmethod
    def create_transaction(self, transaction: Transacao) -> Transacao:
        '''
        Cria um novo registro de transação
        '''
        pass