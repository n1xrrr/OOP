class list:
    
    def __init__(self, num):
        self.num = []
    
    def __add__(self, other):
        if other not in self.num:
            self.num.append(other)
        return self
    
    def __sub__(self, other):
        if other not in self.num:
            return self.num
        else:
            self.num.pop(other)

    def __mul__(self, other):
        ...#c. __mul__ – делет список(делет список в большенство) - ? 
    

class name:
    
    def __init__(self, num):
        self.num = []

    