
#Pizza klasları burda oluşturuldu
class Pizza:
    def __init__(self):
        self.__description = ""
        self.__cost = 0
        self.__ingredients  = []
#Getter ve setter lar 
    def get_description(self):
        return self.__description

    def set_description(self,ndescription):
        self.__description = ndescription

    def get_cost(self):
        return self.__cost

    def set_cost(self,ncost):
        self.__cost = ncost

    def add_ingredient(self, ingredient):
        self.__ingredients.append(ingredient)
        

        
        

