 #Задание 1
class Car(): 
    def __init__(self, year, mileage,model):
        self.model = model
        self._year = year
        self.__mileage = mileage
    
    def get_model(self):
        ... #зачем
    
    def get_year(self):
        return self._year
    
    def set_year(self, year):
        if year > 1886 and year < 2024:
            self._year = year
        else:
            raise ValueError("sosi")
    
    def get_mileage(self):
        return self.__mileage
    
    def set_mileage(self, mileage):
        if mileage >= 0:
            self.__mileage = mileage
        else:
            raise ValueError("sosi")