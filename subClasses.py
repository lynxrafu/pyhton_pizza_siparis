from Pizza import Pizza


class Klasik(Pizza):
    def __init__(self):
        super().__init__()
        self.__cost = 10
        self.__description = "Klasik Pizza"
    def get_cost(self):
        return self.__cost
    def get_description(self):
        return self.__description
    

class Margarita(Pizza):
    def __init__(self):
        super().__init__()
        self.__cost = 15
        self.__description = "Margarita Pizza"
    def get_cost(self):
        return self.__cost
    def get_description(self):
        return self.__description

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.__cost = 20
        self.__description = "Turk Pizza" 
    def get_cost(self):
        return self.__cost
    def get_description(self):
        return self.__description   

class SadePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.__cost = 25
        self.__description = "Sade Pizza"
    def get_cost(self):
        return self.__cost
    def get_description(self):
        return self.__description