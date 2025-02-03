#DEFINIÇÃO DE ENTIDADE A PARTIR DE UMA CLASSE ITEM
# from pydantic import BaseModel
# from ..errors.entity_errors import ParamNotValidated

# class Item:
#     def __init__ (self, name: str, email: str, item_id: int, password: str):
#         self.name = name
#         self.email = email
#         self.item_id = item_id
#         self.password = password
        
#     def to_dict(self) -> dict:
#         return {
#             "nome": self.name,
#             "email": self.email,
#             "item_id": self.item_id,
#             "password": self.password
#         }
        
# class ItemInput(BaseModel):
#     name = str
#     email = str
#     item_id = int
#     password = str

# class Config:
#     arbitrary_types_allowed = True