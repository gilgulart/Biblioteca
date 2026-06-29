from datetime import datetime, timedelta
from biblioteca.book import Book
from biblioteca.user import User
from biblioteca.loan import Loan

class Library:
    def __init__(self, name):
        self.name = name
        self.collection = []
        self.users = []
        self.loans = []
        self.available = []
        self.date = datetime
    
        
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
        open_loans = [loan for loan in self.loans if not loan.is_returned]
        if not open_loans:
            return 'Nenhum livro emprestado.'
        
        print('========= Livros Emprestados =========\n')
        for loan in open_loans:
            print(f"- {loan.book}\n")
        
            
    def display_user_stats(self, user: User):
        if not self.users:
            return 'Nenhum usuário cadastrado'
        
        if not user in self.users:
            return 'Usuário não cadastrado'
        
        print(f"{user}\n")
        
                
    def add_user(self, user: User):
        if user in self.users:
            return "Usuário já foi cadastrado anteriormente"

        self.users.append(user)
    
    
    def add_book(self, book: Book):
        if book in self.collection:
            return 'Este livro já foi catalogado anteriormente'
        
        self.collection.append(book)
        return self.available.append(book)
    
    
    def is_available(self, book: Book):
        return book in self.available
    
    
    def is_on_loan(self, book: Book):   
        return any(loan.book == book and not loan.is_returned for loan in self.loans)


    def loan_book(self, book: Book, user: User):
        if user not in self.users:
            return 'Usuário não cadastrado'
        
        if not self.is_available(book):
            return f'Livro: {book} não está disponível'
        
        self.available.remove(book)
        loan = Loan(book, user)
        self.loans.append(loan)
        user.books_on_loan.append(book)
        
        return (
        f"Livro: {book}\nEmprestado dia {loan.loan_date.strftime('%d-%m-%Y')}\n"
        f"Prazo de renovação {loan.due_date.strftime('%d-%m-%Y')}"
            ) 
    
    def return_book(self, book: Book, user: User):
        loan = self._find_open_loan(book)
        if loan is None:
            return 'Livro não está em empréstimo'
        
        loan.mark_as_returned()
        user.books_on_loan.remove(book)
        self.available.append(book)
        return f"Livro: {book} devolvido"
            
    def _find_open_loan(self, book: Book):
        for loan in self.loans:
            if loan.book == book and not loan.is_returned:
                return loan
        return None
    
    def loan_history(self, user: User):
        return [loan for loan in self.loans if loan.user == user]

library = Library('Biblioteca Pessoal')
user = User('Gilberto', 'gilberto@gmail.com')
library.add_user(user)

book = Book('Antifrágil', 'Nassim Taleb', 2012)
library.add_book(book)

library.loan_book(book, user)
library.return_book(book, user)

print(library.loan_history(user))