from abc import ABC, abstractmethod
from typing import List, Optional
from src.app.entities.cliente import Cliente

class IClienteRepository(ABC):

    @abstractmethod
    def get_all_clients(self) -> List[Cliente]:
        '''
        Retorna todos os clientes
        '''
        pass
    
    @abstractmethod
    def get_client(self) -> Optional[Cliente]:
        '''
        Retorna um cliente específico
        Determinado pelo id
        '''
        pass