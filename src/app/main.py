from fastapi import FastAPI
from src.app.environments import Environments
from .repo.item_repository_mock import ItemRepositoryMock
from .errors.entity_errors import ParamNotValidated
from .entities.item import Item


app = FastAPI()

repo = Environments.get_item_repo()()

@app.get("/items/get_items")
def get_items():
    print("Entrando no get_items")
    items = repo.get_items()
    
    items_list = list()
    for item in items:
        items_list.append(item.to_dict())
        
    return {
        "items": items_list
    }