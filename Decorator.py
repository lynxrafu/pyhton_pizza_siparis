from Pizza import Pizza

#Parent class ve subclasslar
class Decorator(Pizza):
    def __init__(self):
        super().__init__()
    def get_cost(self):
       return self.component.get_cost() + Pizza.get_cost(self)
    def get_description(self):
       return self.component.get_description() +' '+ Pizza.get_description(self)
    
class Zeytin(Decorator):
    def __init__(self):
        super().__init__()
        self.__cost = 3
        self.__description = "Zeytin"
    def get_cost(self):
        return self.__cost
    def get_description(self):
        return self.__description
    
class Mantar(Decorator):
    def __init__(self):
        super().__init__()
        self.__cost = 5
        self.__description = "Mantar"
    def get_cost(self):
        return self.__cost
    def get_description(self):
        return self.__description
    
class KeciPeyniri(Decorator):
    def __init__(self):
        super().__init__()
        self.__cost = 7
        self.__description = "KeciPeyniri"
    def get_cost(self):
        return self.__cost
    def get_description(self):
        return self.__description
    
class Et(Decorator):
    def __init__(self):
        super().__init__()
        self.__cost = 9
        self.__description = "Et"
    def get_cost(self):
        return self.__cost
    def get_description(self):
        return self.__description
    
class Sogan(Decorator):
    def __init__(self):
        super().__init__()
        self.__cost = 12
        self.__description = "Soğan"
    def get_cost(self):
        return self.__cost
    def get_description(self):
        return self.__description
    
    
class Misir(Decorator):
    def __init__(self):
        super().__init__()
        self.__cost = 15
        self.__description = "Mısır"
    def get_cost(self):
        return self.__cost
    def get_description(self):
        return self.__description
    




