import pytest
from src.app.entities.transacao import Transacao
from src.app.enums.item_type_enum import ItemTypeEnum
from src.app.errors.entity_errors import ParamNotValidated

class Teste_Transacao:
    def test_transacao(self):
        transacao = Transacao(ItemTypeEnum.WITHDRAW, 100.0, 200.0, 10)
        assert transacao.type_transaction == ItemTypeEnum.WITHDRAW
        assert transacao.value == 100.0
        assert transacao.current_balance == 200.0
        assert transacao.timestamp == 10
        
#TESTES DE VALIDAÇÃO DE PARÂMETROS

def test_type_transaction():
    with pytest.raises(ParamNotValidated) as error:
        transacao1 = Transacao(None, 100.0, 200.0, 10)
        transacao2 = Transacao(1234567, 100.0, 200.0, 10)
        transacao3 = Transacao(ItemTypeEnum.WITHDRAW, -100.0, 200.0, 10)
        transacao4 = Transacao(ItemTypeEnum.DEPOSIT, -100.0, 200.0, 10)
        
def test_value():
    with pytest.raises(ParamNotValidated) as error:
        valor1 = Transacao(ItemTypeEnum.WITHDRAW, None, 200.0, 10)
        valor2 = Transacao(ItemTypeEnum.WITHDRAW, "chinchin", 200.0, 10)
        value3 = Transacao(ItemTypeEnum.WITHDRAW, 0, 200.0, 100.0)
        
def test_current_balance_transac():
    with pytest.raises(ParamNotValidated) as error:
        saldo_atual1 = Transacao(ItemTypeEnum.WITHDRAW, 100.0, None, 10)
        saldo__atual2 = Transacao(ItemTypeEnum.WITHDRAW, 100.0, "saldo sem valor real", 10)
    
def test_timestamp():
    with pytest.raises(ParamNotValidated) as error:
        horario_transacao1 = Transacao(ItemTypeEnum.WITHDRAW, 100.0, 200.0, None)
        horario_transacao2 = Transacao(ItemTypeEnum.WITHDRAW, 100.0, 200.0, "10 horas da manhã")