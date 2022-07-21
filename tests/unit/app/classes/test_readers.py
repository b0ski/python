import pytest
from app.classes.readers import Book, Reader, Library


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
def test_take_book(address: str, telephone: str, books: list, readers: list, genre: str, title: str, author: str, firstName: str, lastName: str, iD: int, birthDate: int, ans):
    book_1 = Book(genre, title, author)
    reader_1 = Reader(firstName, lastName, iD, birthDate, telephone)

    books_list = [book_1]
    readers_list = [reader_1]

    library = Library(address, telephone, books_list, readers_list)
    assert library.takeBook(reader_1, book_1) == ans


@pytest.mark.parametrize(
    'address, telephone, books, readers, genre, title, author, firstName, lastName, iD, birthDate, ans',
    [
        ('10, Downing str', '555-123', None, None,
         'novel', 'Lord of the Flies', 'William Golding',
         'Peter', 'Larson', 12, 1980,
         'Peter Larson returned the following book: novel, Lord of the Flies, William Golding'
         ),
    ]
)
def test_return_book(address: str, telephone: str, books: list, readers: list, genre: str, title: str, author: str, firstName: str, lastName: str, iD: int, birthDate: int, ans):
    book_1 = Book(genre, title, author)
    reader_1 = Reader(firstName, lastName, iD, birthDate, telephone)

    books_list = [book_1]
    readers_list = [reader_1]

    library = Library(address, telephone, books_list, readers_list)
    assert library.returnBook(reader_1, book_1) == ans

