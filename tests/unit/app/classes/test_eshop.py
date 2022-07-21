import pytest
from app.classes.eshop import Item, Category, Basket, User


@pytest.mark.parametrize(
    'address, telephone, books, readers, genre, title, author, firstName, lastName, iD, birthDate, ans',
    [
        ('10, Downing str', '555-123', None, None,
         'novel', 'Lord of the Flies', 'William Golding',
         'Peter', 'Larson', 12, 1980,
         'Peter Larson took the following book: novel, Lord of the Flies, William Golding'
         ),
    ]
)
def test_add(address: str, telephone: str, books: list,  ans):
    book_1 = Book(genre, title, author)
    reader_1 = Reader(firstName, lastName, iD, birthDate, telephone)

    books_list = [book_1]
    readers_list = [reader_1]

    library = Library(address, telephone, books_list, readers_list)
    assert library.takeBook(reader_1, book_1) == ans