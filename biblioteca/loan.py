from biblioteca.book import Book
from biblioteca.user import User
from datetime import datetime, timedelta

class Loan:
    
    def __init__(self, book: Book, user: User, loan_date= None, days_to_return=7):
        self.book = book
        self.user = user
        self.loan_date = loan_date or datetime.now()
        self.due_date = self.loan_date + timedelta(days=days_to_return)
        self.return_date = None
        
    @property
    def is_returned(self):
        return self.return_date is not None
    
    @property
    def is_overdue(self):
        if self.is_returned:
            return self.return_date > self.due_date
        
        return datetime.now() > self.due_date
    
    def mark_as_returned(self, return_date= None):
        self.return_date = return_date or datetime.now()
        
    def __str__(self):
        status = 'Devolvido' if self.is_returned else 'Em andamento'
        return (
            f"Empréstimo: {self.book} para {self.user.name}\n"
            f"{self.loan_date.strftime('%d-%m-%Y')} -> {self.due_date.strftime('%d-%m-%Y')}\n"
            f"{status}"
        )
        
    def __repr__(self):
        return self.__str__()