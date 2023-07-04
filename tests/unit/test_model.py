from domain.model import Author, Book

def test_add_book_to_author():
    author1 = Author("John", "Steinbeck")
    book1 = Book("Grapes of Wrath", 1937)
    author1.add_book(book1)
    assert author1.num_books_written == 1
    assert book1 in author1.books_written

def test_adding_books_is_idempotent():
    author1 = Author("John", "Steinbeck")
    book1 = Book("Grapes of Wrath", 1937)
    author1.add_book(book1)
    author1.add_book(book1)
    assert author1.num_books_written == 1