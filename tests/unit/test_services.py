import pytest

from domain.model import Author, Book
#from adapters.respository import SQLAlchemyRepository
#from service_layer.services import update_author

@pytest.fixture()
def book_with_author(session):
    repo = SQLAlchemyRepository(session)
    author = Author("John", "Steinbeck")
    book = Book("The Sound and the Fury", 1931)
    author.add_book(book)
    repo.add_all([author, book])
    return book

@pytest.mark.skip(reason="Unfinished test.")
def test_add_book_to_author(session, book_with_author):
    # Adding... but not actually committing to the Database
    author = Author("William", "Faulkner")
    repo = SQLAlchemyRepository(session)
    update_author(repo, book_with_author, author)
    get_author = [author for author in repo.list(Author) if author.first_name == "William"]
    assert len(get_author) == 1
    assert get_author[0].first_name == "William"
    assert get_author[0].num_books_written == 1

    previous_author = [author for author in repo.list(Author) if author.first_name == "John"]
    assert len(previous_author) == 1
    assert previous_author[0].num_books_written == 0

    get_book = [book for book in repo.list(Book) if book.title == "The Sound and the Fury"]
    assert get_book[0]._author.first_name == "William"

