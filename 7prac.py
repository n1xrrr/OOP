class Product:
    def __init__(self, name, price, discount):
        self.name = name
        self._price = price
        self._discount = discount

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Какой минус")

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if 0 <= value <= 100:
            self._discount = value
        else:
            raise ValueError("Скидка должна але")

    @property
    def price_with_discount(self):
        return self.price * (1 - self.discount / 100) 
    
#Задание 2
class Employee:
    def __init__(self, name, salary, age):
        self._name = name
        self._salary = salary
        self._age = age

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value >= 30000:
            self._salary = value
        else:
            raise ValueError("че")
        
    @property
    def age(self):
        return self._age

    @age.deleter
    def age(self):
        self._age = None

    def apply_raise(self, amount):
        new_salary = self.salary + amount
        if new_salary >= 30000:
            self.salary = new_salary
        else:
            raise ValueError("зп <30к")