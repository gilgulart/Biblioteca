class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} -  {self.author}, {self.year}"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if not isinstance(self, Book):
            return NotImplemented
        return (self.title, self.author, self.year) == (other.title, other.author, other.year)
    
    def __hash__(self):
        return hash(self.title, self.author, self.year) 