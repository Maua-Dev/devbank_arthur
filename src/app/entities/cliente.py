from typing import Tuple
from ..errors.entity_errors import ParamNotValidated

class Cliente:
    
    name: str
    agency: str
    account: str
    current_balance: float
    
    def __init__ (self, name: str = None, agency: str = None, account: str = None, current_balance: float = None):
        
        valid_name = self.valid_name(name)
        if valid_name[0] is False:
            raise ParamNotValidated("nome", valid_name[1])
        self.name = name
        
        valid_agency = self.valid_agency(agency)
        if valid_agency[0] is False:
            raise ParamNotValidated("agencia", valid_agency[1])
        self.agency = agency
        
        valid_account = self.valid_account(account)
        if valid_account[0] is False:
            raise ParamNotValidated("conta", valid_account[1])
        self.account = account
        
        valid_current_balance = self.valid_current_balance(current_balance)
        if valid_current_balance[0] is False:
            raise ParamNotValidated("saldo_atual", valid_current_balance[1])
        self.current_balance = current_balance
        
    @staticmethod
    def valid_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return (False, "Nome não pode ser nulo")
        if type(name) != str:
            return (False, "Nome deve ser uma string")
        else:
            return (True, "")
        
    @staticmethod
    def valid_agency(agency: str) -> Tuple[bool, str]:
        if agency is None:
            return (False, "Agência não pode ser nula")
        if type(agency) != str:
            return (False, "Agência deve ser uma string")
        if len(agency) < 4 or len(agency) > 4:
            return (False, "O número da agência deve conter 4 dígitos")
        else:
            return (True, "")
        
    @staticmethod
    def valid_account(account: str) -> Tuple[bool, str]:
        if account is None:
            return (False, "Conta não pode ser nula")
        if type(account) != str:
            return (False, "Conta deve ser uma string")
        if len(account) < 6 or len(account) > 6:
            return (False, "O número da conta deve conter 6 dígitos")
        else:
            return (True, "")
        
    @staticmethod
    def valid_current_balance(current_balance: float) -> Tuple[bool, str]:
        if current_balance is None:
            return (False, "Saldo atual não pode ser um valor nulo")
        if type(current_balance) != float:
            return (False, "Saldo atual deve ser um número real")
        else:
            return (True, "")
        
    def to_dict(self) -> dict:
        return {
            "nome": self.name,
            "agencia": self.agency,
            "conta": self.account,
            "saldo_atual": self.current_balance
        }
    
    @staticmethod
    def client_id(client_id: int) -> Tuple[bool, str]:
        if client_id is None:
            return (False, "Id do cliente não pode ser nulo")
        if type(client_id) != int:
            return (False, "Id do cliente deve ser um número inteiro")
        else:
            return (True, "")