from fastapi import FastAPI
from src.app.environments import Environments
from .repo.item_repository_mock import ItemRepositoryMock
from .errors.entity_errors import ParamNotValidated
from .entities.item import Item, ItemInput


app = FastAPI()

repo = Environments.get_item_repo()()

@app.get("/items/get_items")
def get_items():
    print("Entrando no get_items")
    items = repo.get_items()
    
    for item in items:
        print(f"Item: {item.name}, {item.email}, {item.item_id}, {item.password}")

    items_list = [item.to_dict() for item in items]
        
    return {
        "items": items_list
    }
    
item_repo = ItemRepositoryMock()

@app.post("/items/create_item")
async def create_item(item: ItemInput):
    data = item.dict()
    new_item = item_repo.create_item(ItemInput(**data))
    return new_item