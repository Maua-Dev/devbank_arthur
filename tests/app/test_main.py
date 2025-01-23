from src.app.main import get_items

class Test_Main:
    def test_main(self):
        response = get_items()
        
        expected_response = {
            "items":[{"nome":"Miguel","email":"mneto.devmaua@gmail.com","item_id":1,"password":"psswd123"},{"nome":"Arthur","email":"asilva.devmaua@gmail.com","item_id":2,"password":"psswd456"},{"nome":"Mateus","email":"msobrenome.devmaua@gmail.com","item_id":3,"password":"psswd789"},{"nome":"Victor","email":"vsoller.devmaua@gmail.com","item_id":4,"password":"psswd000"}]
            }

        assert type(response) == dict
        assert response == expected_response