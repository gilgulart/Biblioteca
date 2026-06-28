import random

class User:
    def __init__(self, name, email):
        
        if not self.is_valid_email(email):
            raise ValueError('Email inválido')
        
        self.name = name
        self.email = email
        self.user_id = random.randint(100000, 999999)
        self.books_on_loan = []
        
    def __str__(self):
        return f"Usuário: {self.name} - {self.user_id}, {self.email}, Livros emprestados: {self.books_on_loan}"
    
    def __repr__(self):
        return self.__str__()
    
    @staticmethod
    def is_valid_email(email):
        import re
        
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None
    