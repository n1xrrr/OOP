#Задание 1 
class Goods():
    title = "Мороженое"
    weight = 151
    tp = '"Еда"'
    price = 12321
    
price_p = Goods
weight_p = Goods

price_p.price = 123
weight_p.weight = 322

#Задание 2
class Car():
    None
add = Car
add.model = "Тойота"
add.color = "черный"
add.number = "П34А123"

asd = Car.__dict__
print(asd)

#Задание 3
#Словарь аргументов класса 
