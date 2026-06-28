from biblioteca.library import Library
from biblioteca.user import User
from biblioteca.book import Book

def test_book_avaiable():
    library = Library('Biblioteca')
    book = Book('O Morro dos ventos uivantes', 'Emily Bronte', 1847)
    
    library.add_book(book)
    
    assert book in library.available

def test_loan_book():
    library = Library('Biblioteca')
    
    user = User('Gilberto', 'gilberto@email.com')
    library.add_user(user)
    
    book = Book('O Morro dos ventos uivantes', 'Emily Bronte', 1847)
    book_2 = Book('Antifrágil', 'Nassim Taleb', 2012)
    
    library.add_book(book)
    library.add_book(book_2)
    
    library.loan_book(book, user)
    
    
    assert library.is_on_loan(book)
    assert not library.is_available(book)
    assert library.is_available(book_2)
    assert book in user.books_on_loan
    assert (f"Livro: {book}\nEmprestado dia {library.loan_date.strftime('%d-%m-%Y')}\n"
            f"Prazo de renovação {library.renewal_date.strftime('%d-%m-%Y')}")
    
def test_return_book():
    library = Library('Biblioteca')
    user = User('Gilberto', 'gilberto@email.com')
    
    book = Book('O Morro dos ventos uivantes', 'Emily Bronte', 1847)
    
    library.add_book(book)
    
    library.loan_book(book, user)
    
    library.return_book(book)
        
    assert library.is_available(book)
    assert not library.is_on_loan(book)
    assert book in library.collection
    assert f"Livro: {book} devolvido"
    
def test_book_not_available():
    library = Library('Biblioteca')
    user = User('Gilberto', 'gilberto@email.com')
    
    book = Book('O Morro dos ventos uivantes', 'Emily Bronte', 1847)
    
    library.add_book(book)
    
    library.loan_book(book, user)
    
    
    library.loan_book(book, user)
    
    assert f"Livro: {book} não está disponível"
    
    
    