import pytest
from biblioteca.library import Library
from biblioteca.user import User

def test_user_register():
    library = Library('Biblioteca')
    user = User('Cicrano de tal', 'cicrano@gmail.com')
    library.add_user(user)

    assert len(library.users) == 1
    assert user in library.users
    
def test_diferent_id():
    fulano = User('Fulano', 'fulano@email.com')
    cicrano = User('Cicrano', 'cicrano@email.com')
    
    assert fulano.user_id != cicrano.user_id
    
def test_valid_email():
    cicrano = User('Cicrano', 'cicrano@email.com')
    
    assert cicrano.is_valid_email('cicrano@email.com')

def test_invalid_email():
    with pytest.raises(ValueError):
        User('Fulano', 'fulano.com')
        User('Cicrano', '@gmail.com')
        User('João', '@gmail')
        User('Maria', '12345')
    