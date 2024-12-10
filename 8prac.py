class Library:
    def __init__(self, name, max_books = 5):
            self.name = name
            self.max_books = max_books
            self.books = []
    
    def getattribute(self, name):
        return super().getattribute(name)
    
    def __getattr__(self, name):
        return f"Атрибут {name} не существует"
    
    def __setattr__(self, name):
        super().__setattr__(name)
        
    def add_book(self, book):
        if len(self.books) < self.max_books:
            self.books.append(book)
        else:
            print("ahuel?")
        
    def remove_book(self, book):
        if(book in self.books):
            self.books.remove(book)
            
    def list_books(self, books):
        return(books)
            
    def __delattr__(self, name):
        super().__delattr__(name)
