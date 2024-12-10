class ShoppingCart:
    def __init__(self, cart):
        self.cart = cart

    def __len__(self):
        return len(self.cart)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __len__(self):
        return len(self.pages)    
    
    def __str__(self):
        return f"{self.title}, author {self.author}, pages {self.pages})"
    
    def __repr__(self):
        f"Book(title='{self.name}', author = {self.author}, pages = {self.pages})"