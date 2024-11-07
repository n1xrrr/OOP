#Задание 1 
class test:
    _inst = None
    _count = 0
    _maxint = 5

    def __new__(cls, *args, **kwargs):
        if cls._count < cls._maxint:
            cls._count += 1
            instance = super(test, cls).__new__(cls)
            cls._inst = instance
            return instance
        else:
            return cls._inst

#Задание 2 
class Book:
    title = None
    author = None
    year = None
    
    def __new__(cls, title, author, year):
        if cls.title is None or cls.author is None:
            obj = super().__new__(cls)
            obj.title = title
            obj.author = author
            obj.year = year
            cls.title = title
            cls.author = author
            return obj
        else:
            raise ValueError("чо")
        
book1 = Book("Title1", "Author1", 2021)
print(book1.title)
book2 = Book("Title1", "Author1", 2022)
print(book2.__dict__)
