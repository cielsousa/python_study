

class Client():
    def __init__(self, name, number) -> None:
        
        self._name = name
        self._number = number

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

