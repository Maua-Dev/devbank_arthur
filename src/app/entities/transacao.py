from typing import Tuple
from ..enums.item_type_enum import ItemTypeEnum
from ..errors.entity_errors import ParamNotValidated

class Transacao:
    
    type_transaction: ParamNotValidated
    value: float
    current_balance: float
    timestamp: float
    
    def __init__ (self, type_transaction: ItemTypeEnum = None, value: float = None, current_balance: float = None, timestamp: float = None):
    
        valid_type = self.valid_type(type_transaction, value)
        if valid_type[0] is False:
            raise ParamNotValidated("tipo", valid_type[1])
        self.type_transaction = type_transaction
        
        valid_value = self.valid_value(value) 
        if valid_value[0] is False:
            raise ParamNotValidated("valor", valid_value[1])
        self.value = value
        
        valid_current_balance_transac= self.valid_current_balance_transac(current_balance)
        if valid_current_balance_transac[0] is False:
            raise ParamNotValidated("saldo_atual", valid_current_balance_transac[1])
        self.current_balance = current_balance
        
        valid_timestamp = self.valid_timestamp(timestamp)
        if valid_timestamp[0] is False:
            raise ParamNotValidated("horario_transacao", valid_timestamp[1])
        self.timestamp = timestamp
        
    @staticmethod
    def valid_type(type_transaction: ItemTypeEnum, value: float) -> Tuple[bool, str]:
        if type_transaction is None:
            return (False, "Tipo de transação não pode ser nulo")
        if type(type_transaction) != ItemTypeEnum:
            return (False, "Tipo de transação deve ser de 'saque' ou 'depósito'")
        if value is None:
            return (False, "Valor da transação não pode ser nulo")
        if type_transaction == ItemTypeEnum.WITHDRAW and value < 0:    
            return (False, "Valor de saque não pode ser menor ou igual a zero")
        if type_transaction == ItemTypeEnum.DEPOSIT and value < 0:
            return (False, "Valor de deposito não pode ser menor ou igual a zero")
        else:
            return (True, "")
        
    @staticmethod
    def valid_value(value: float) -> Tuple[bool, str]:
        if value is None:
            return (False, "Valor da transação não pode ser nulo")
        if type(value) != float:
            return (False, 'Valor da transação deve ser um valor real')
        if value <= 0:
            return (False, 'Valor da transação deve ser um valor maior que zero')
        else:
            return (True, "")
        
    @staticmethod
    def valid_current_balance_transac(current_balance: float) -> Tuple[bool, str]:
        if current_balance is None:
            return (False, "Saldo atual não pode ser nulo")
        if type(current_balance) != float:
            return (False, 'Saldo atual deve ser um valor real')
        else:
            return (True, "")
        
    @staticmethod
    def valid_timestamp(timestamp: float) -> Tuple[bool, str]:
        if timestamp is None:
            return (False, "Horário da transação não pode ser nulo")
        # if type(timestamp) != float:
        #     return (False, 'Horário da transação deve ser um número real')
        if not isinstance(timestamp, (int, float)):
            return (False, "Horário deve ser um valor real")
        if timestamp < 0:
            return (False, "Horário deve ser um valor válido")
        else:
            return (True, "")
    
    
    def to_dict_transac(self):
        return {
            "tipo": self.type_transaction,
            "valor": self.value,
            "saldo_atual": self.current_balance,
            "horario_transacao": self.timestamp
        }