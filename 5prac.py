#Задание 1 
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9/5 + 32

#Задание 2
class Employee:
    def init(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
        
@staticmethod
def is_valid_age(age):
    if age < 18 or age > 65:
        return False
    return True

@classmethod
def from_string(cls, employee_str):
    data = employee_str.split(',')
    name = data[0]
    age = int(data[1])
    position = data[2]
    
    if cls.is_valid_age(age):
        return cls(name, age, position)
    else:
        raise ValueError("sosi")