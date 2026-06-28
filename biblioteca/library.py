from datetime import datetime, timedelta
from biblioteca.book import Book
from biblioteca.user import User

class Library:
    def __init__(self, name):
        self.name = name
        self.collection = []
        self.users = []
        self.on_loan = []
        self.available = []
        self.loan_date = datetime.now()
        self.renewal_date = self.loan_date + timedelta(days=7)
        
    def __str__(self):
        return(
            f"Biblioteca: {self.name}\n"
            f"Acervo: {self.collection}\n"
            f"Usuários: {self.users}\n"
        )
        
        
    def display_collection(self):
        if not self.collection:
            return 'Nenhum livro cadastrado.'
        
        print('========= Livros Cadastrados =========\n')
        for book in self.collection:
            print(f"- {book}\n")
        
        
    def display_available_books(self):
        if not self.available:
            return 'Nenhum livro disponível.'
        
        print('========= Livros Disponíveis =========\n')
        for book in self.available:
            print(f"- {book}\n")
        
            
    def display_on_loan_books(self):
        if not self.on_loan:
            return 'Nenhum livro emprestado.'
        
        print('========= Livros Emprestados =========\n')
        for book in self.on_loan:
            print(f"- {book}\n")
        
            
    def display_user_stats(self, user: User):
        if not self.users:
            return 'Nenhum usuário cadastrado'
        
        if not user in self.users:
            return 'Usuário não cadastrado'
        
        print(f"{user}\n")
        
                
    def add_user(self, user: User):
        self.users.append(user)
    
    
    def add_book(self, book: Book):
        self.collection.append(book)
        return self.available.append(book)
    
    
    def is_available(self, book: Book):
        return book in self.available
    
    
    def is_on_loan(self, book: Book):   
        return book in self.on_loan


    def loan_book(self, book: Book, user: User):
        if user not in self.users:
            return 'Usuário não cadastrado'

        
        if self.is_available(book):
            self.available.remove(book)
            self.on_loan.append(book)
            user.books_on_loan.append(book)
            return (
            f"Livro: {book}\nEmprestado dia {self.loan_date.strftime('%d-%m-%Y')}\n"
            f"Prazo de renovação {self.renewal_date.strftime('%d-%m-%Y')}"
                ) 

        return f"Livro: {book} não está disponível"

    
    def return_book(self, book: Book):
        if self.is_on_loan(book):
            self.on_loan.remove(book)
            self.available.append(book)
            return f"Livro: {book} devolvido"
