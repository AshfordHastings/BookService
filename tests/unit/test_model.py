from domain.model.book import BookObject, Book, Author, MData
from domain.model.host import Shelf, DirHost, TempHost

# def test_add_book_to_author():
#     author1 = Author("John", "Steinbeck")
#     book1 = Book("Grapes of Wrath", 1937)
#     author1.add_book(book1)
#     assert author1.num_books_written == 1
#     assert book1 in author1.books_written

# def test_adding_books_is_idempotent():
#     author1 = Author("John", "Steinbeck")
#     book1 = Book("Grapes of Wrath", 1937)
#     author1.add_book(book1)
#     author1.add_book(book1)
#     assert author1.num_books_written == 1

def test_can_store_and_retrieve_book_from_dir(tmp_path):
    a = Author("John", "Steinbeck")
    f = MData("txt")
    i = Book("East of Eden", 1937, a)
    b = BookObject(i, f)
    s = Shelf(DirHost(tmp_path))
    s.store_book_and_content(b, b'Hello World!')
    (get_book, get_content) = s.get_book_and_content(b.id)
    assert get_book == b
    assert get_content == b'Hello World!'

def test_can_store_and_retrieve_book_from_dir():
    a = Author("John", "Steinbeck")
    f = MData("txt")
    i = Book("East of Eden", 1937, a)
    b = BookObject(i, f)
    s = Shelf(TempHost())
    s.store_book_and_content(b, b'Hello World!')
    (get_book, get_content) = s.get_book_and_content(b.id)
    assert get_book == b
    assert get_content == b'Hello World!'