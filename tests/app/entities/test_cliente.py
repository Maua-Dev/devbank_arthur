import pytest
from src.app.entities.cliente import Cliente
from src.app.errors.entity_errors import ParamNotValidated

class Test_cliente:
    def test_cliente(self):
        cliente = Cliente(name="Arthur", agency="1234", account="123456", current_balance=100.0)
        assert cliente.name == "Arthur"
        assert cliente.agency == "1234"
        assert cliente.account == "123456"
        assert cliente.current_balance == 100.0
        
#TESTES DE VALIDAÇÃO DE PARÂMETROS

#testando nome

def test_name():
    with pytest.raises(ParamNotValidated) as error:
        cliente1 = Cliente(None, "1234", "123456", 100.0)
        cliente2 = Cliente(123, "1234", "123456", 100.0)
        
#testando agência

def test_agency():
    with pytest.raises(ParamNotValidated) as error:
        cliente3 = Cliente("Arthur", None, "123456", 100.0)
        cliente4 = Cliente("Arthur", 1234, "123456", 100.0)
        cliente5 = Cliente("Arthur", "987654", "123456", 100.0)
        
def test_account():
    with pytest.raises(ParamNotValidated) as error:
        cliente6 = Cliente("Arthur", "1234", None, 100.0)
        cliente7 = Cliente("Arthur", "1234", 123456, 100.0)
        cliente8 = Cliente("Arthur", "1234", "98", 100.0)
        
def test_cuttent_balance():
    with pytest.raises(ParamNotValidated) as error:
        cliente9 = Cliente("Arthur", "1234", "123456", None)
        cliente10 = Cliente("Arthur", "1234", "123456", "valor_real")