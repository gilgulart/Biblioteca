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
    
def test_return_book():
    library = Library('Biblioteca')
    user = User('Gilberto', 'gilberto@email.com')
    library.add_user(user)
    
    book = Book('O Morro dos ventos uivantes', 'Emily Bronte', 1847)
    
    library.add_book(book)
    
    library.loan_book(book, user)
    
    response = library.return_book(book,user)
        
    assert library.is_available(book)
    assert not library.is_on_loan(book)
    assert book in library.collection
    assert f"Livro: {book} devolvido" == response
    
def test_book_not_available():
    library = Library('Biblioteca')
    user = User('Gilberto', 'gilberto@email.com')
    library.add_user(user)
    
    book = Book('O Morro dos ventos uivantes', 'Emily Bronte', 1847)
    
    library.add_book(book)
    
    library.loan_book(book, user)
    
    
    response =  library.loan_book(book, user)
    
    assert f"Livro: {book} não está disponível" == response
    
    
def test_add_the_same_book():
    library = Library('Biblioteca')
    user = User('Gilberto', 'gilberto@email.com')
    
    
    book = Book('O Morro dos ventos uivantes', 'Emily Bronte', 1847)
    
    library.add_book(book)
    library.add_user(user)
    user_response = library.add_user(user)
    response = library.add_book(book)
    
    assert 'Este livro já foi catalogado anteriormente' == response
    assert 'Usuário já foi cadastrado anteriormente' == user_response