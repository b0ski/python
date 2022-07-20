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
    def __init__(self, address: str, telephone: str, books: list, readers: list):
        self.address = address
        self.telephone = telephone
        self.books = books
        self.readers = readers

    def takeBook(self):
        print(f'{self.readers[0].firstName} {self.readers[0].lastName}'
              f' took the following book: {self.books[1].genre}, {self.books[1].title}, {self.books[1].author}')
        self.books.remove(book_1)

    def returnBook(self):
        print(f'{self.readers[0].firstName} {self.readers[0].lastName}'
              f' has returned the following book: {self.books[2].genre}, {self.books[2].title}, {self.books[2].author}')
        self.books.append(book_2)


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

library.takeBook()
library.returnBook()

print(books_list)
