# from typing import List
# from src.app.entities.item import Item, ItemInput
# from src.app.repo.item_repository_interface import IItemRepository

# class ItemRepositoryMock(IItemRepository):
#     items: List[Item]
    
#     def __init__ (self):
#         self.items = [
#             Item(name="Miguel", email="mneto.devmaua@gmail.com", item_id=1, password="psswd123"),
#             Item(name="Arthur", email="asilva.devmaua@gmail.com", item_id=2, password="psswd456"),
#             Item(name="Mateus", email="msobrenome.devmaua@gmail.com", item_id=3, password="psswd789"),
#             Item(name="Victor", email="vsoller.devmaua@gmail.com", item_id=4, password="psswd000")
#         ]
        
#     def get_items(self) -> List[Item]:
#         return self.items
    
#     def create_item(self, item: Item) -> Item:
#         self.items.append(item)
#         return item