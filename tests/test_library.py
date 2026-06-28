from biblioteca.library import Library
from biblioteca.book import Book
from biblioteca.user import User

def test_display_available_books():
    library = Library('Biblioteca')
    library.display_available_books()
    
    assert 'Nenhum livro disponível.'
    
def test_display_collection():
    library = Library('Biblioteca')
    library.display_collection()
    
    assert 'Nenhum livro cadastrado.'
    
def test_display_collection():
    library = Library('Biblioteca')
    user = User('Fulano', 'fulano@email.com')
    book = Book('O Morro dos ventos uivantes', 'Emily Bronte', 1847)
    
    library.add_book(book)
    library.loan_book(book, user)
    
    library.display_on_loan_books()

def test_return_undefined_book():
    
    library = Library('Biblioteca')
    user = User('Fulano', 'fulano@email.com')
    
    book = Book('O Morro dos ventos uivantes', 'Emily Bronte', 1847)
    book_2 = Book('Antifrágil', 'Nassim Taleb', 2012)
    
    library.add_user(user)
    library.add_book(book)
    library.add_book(book_2)
    
    library.loan_book(book, user)
    
    response = library.return_book(book_2)
    
    assert 'Livro não está em empréstimo' == response
