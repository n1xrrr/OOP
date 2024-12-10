class Power:
    def init(self, power):
        self.power = power
    def __call__(self, x):
        return x ** self.power
    
class Repeat:
    def __init__(self, repetitions):
        self.repetitions = repetitions
        
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(self.repetitions):
                result = func(*args, **kwargs)
            return result
        return wrapper
