#DEFINIÇÃO DOS ATRIBUTOS A PARTIR DE UMA CLASSE ITEM

from ..errors.entity_errors import ParamNotValidated

class Item:
    def __init__ (self, name: str, email: str, item_id: int, password: str):
        self.name = name
        self.email = email
        self.item_id = item_id
        self.password = password
        if not self.password_controler(password):
            raise ParamNotValidated("password", "must have at least 5 characters")
    
    @staticmethod    
    def password_controler(password: str):
        if len(password) < 5:
            return False
        else:
            return True