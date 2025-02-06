from abc import ABC
from typing import List
from src.app.entities.cliente import Cliente

class IItemRepository(ABC):

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