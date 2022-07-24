class Book:
    def __init__(self, genre: str, title: str, author: str):
        self.title = title
        self.genre = genre
        self.author = author


class Reader:
    def __init__(self, firstName: str, lastName: str, iD: int, birthDate: int, telephone: str):
        self.firstName = firstName
        self.lastName = lastName
        self.iD = iD
        self.birthDate = birthDate
        self.telephone = telephone


class Library:
    reader = None
    book = None
    has_book = {}

    def __init__(self, address: str, telephone: str, books: list, readers: list):
        self.address = address
        self.telephone = telephone
        self.books = books
        self.readers = readers

    def takeBook(self, reader, book):
        if book in self.books:
            self.books.remove(book)
            self.has_book[book] = reader
            return f'{reader.firstName} {reader.lastName} took the following book: {book.genre}, {book.title}, {book.author}'

        else:
            return 'Book is taken'

    def returnBook(self, reader, book):
        self.books.append(book)
        self.has_book[book] = None
        return f'{reader.firstName} {reader.lastName} returned the following book: {book.genre}, {book.title}, {book.author}'

    def book_log(self):
        for book in self.has_book:
            return f'{self.has_book[book].lastName} {self.has_book[book].lastName} has {book.title}'

    def write_off_book(self, book):
        self.books.remove(book)

    def write_on_book(self, book):
        self.books.append(book)

    def write_off_reader(self, reader):
        self.readers.remove(reader)

    def write_on_reader(self, reader):
        self.readers.append(reader)


book_1 = Book('novel', 'Lord of the Flies', 'William Golding')
book_2 = Book('detective', 'The Hound of the Baskervilles', 'Arthur Conan Doyle')
book_3 = Book('math', 'Gödel, Escher, Bach', 'Douglas Hofstadter')
book_4 = Book('programming', 'The Art of Assembly Language', 'Randall Hyde')
book_5 = Book('economics', 'Big Ideas Simply Explained', 'DK')

reader_1 = Reader('Peter', 'Larson', 12, 1980, '555-123')
reader_2 = Reader('Lisa', 'Kim', 24, 2000, '555-555')
reader_3 = Reader('Elizabeth', 'Johanson', 45, 1990, '555-777')

books_list = [book_1, book_2, book_3, book_4, book_5]
readers_list = [reader_1, reader_2, reader_3]

library = Library('10, Downing street', '555-505', books_list, readers_list)

library.takeBook(reader_1, book_1)
#library.takeBook(reader_2, book_1)
#library.book_log()



