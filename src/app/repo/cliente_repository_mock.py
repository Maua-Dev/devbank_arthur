from typing import Dict, Optional, List

from ..entities.cliente import Cliente
from ..enums.item_type_enum import ItemTypeEnum
from .cliente_repository_interface import IClienteRepository

class ClienteRepositoryMock(IClienteRepository):
    clientes: Dict[int, Cliente]
    
    def __init__(self):
        self.clientes = {
            
            # ao instanciar a classe Cliente, o valor inteiro se torna o id de cada cliente, como feito abaixo
            
            1: Cliente(name="Arthur", agency="0001", account="123456", current_balance=1000.00),
            2: Cliente(name="Miguel", agency="0001", account="654321", current_balance=1000.00)
        }
        
    def get_all_clients(self) -> List[Cliente]:
        return self.clientes.values()
    
    def get_client(self, client_id: int) -> Optional[Cliente]:
        return self.clientes.get(client_id, None)          