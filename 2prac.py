#Задание 1,2
class CLASS:
    created_objects = []

    def create(self, name):
        obj = CLASS(name)
        self.created_objects.append(obj)
        return obj

    def search(self, attr, value):
        return [obj for obj in self.created_objects if getattr(obj, attr) == value]
    
#Задание 3 
class Translator:
    def __init__(self,dick):
        dick = {}
        self.dick = dick
        
    def add(self, rus, eng):
        if eng in self.dick:
            if rus not in self.dick[eng]:
                self.dick[eng].append(rus)  
        else:
            self.dick[eng] = [rus]

    def remove(self, eng):
        if eng in self.dick:
            del self.dick[eng]

    def translate(self, eng):
        if eng in self.dick:
            return self.dick[eng][0]