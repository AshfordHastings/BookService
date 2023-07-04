from domain.model import Book, Author
from adapters.respository import SQLAlchemyRepository
from sqlalchemy import text

def test_repository_can_save_a_book(session):
    book1 = Book("Grapes of Wrath", 1937)

    repo = SQLAlchemyRepository(session)
    repo.add(book1)
    session.commit()

    rows = session.execute(text(
        'SELECT title, year FROM "book"'
    ))
    assert list(rows) == [('Grapes of Wrath', 1937)]

def test_repository_can_add_many_books(session):
    book1 = Book("Grapes of Wrath", 1937)
    book2 = Book("East of Eden", 1943)
    book3 = Book("Of Mice and Men", 1950)

    repo = SQLAlchemyRepository(session)
    repo.add_all([book1, book2, book3])
    session.commit()

    rows = session.execute(text(
        'SELECT title, year FROM "book"'
    ))
    assert list(rows) == [('Grapes of Wrath', 1937), ("East of Eden", 1943), ("Of Mice and Men", 1950)]

def test_respository_can_save_an_author(session):
    author1 = Author("John", "Steinbeck")

    repo = SQLAlchemyRepository(session)
    repo.add(author1)
    session.commit()

    rows = session.execute(text(
        'SELECT first_name, last_name FROM "author"'
    ))
    assert list(rows) == [("John", "Steinbeck")]

def test_repository_can_save_an_author_with_book(session):
    author1 = Author("John", "Steinbeck")
    book1 = Book("Grapes of Wrath", 1937)
    author1.add_book(book1)

    repo = SQLAlchemyRepository(session)
    repo.add(author1)
    session.commit()

    rows = session.execute(text(
        'SELECT title, first_name, last_name FROM "author" \
        JOIN "book" on author.id==book.author_id'
    ))
    assert list(rows) == [("Grapes of Wrath", "John", "Steinbeck")]

def test_repository_can_save_an_author_with_many_books(session):
    author1 = Author("John", "Steinbeck")
    book1 = Book("Grapes of Wrath", 1937)
    book2 = Book("East of Eden", 1943)
    book3 = Book("Of Mice and Men", 1950)
    author1.add_books([book1, book2, book3])

    repo = SQLAlchemyRepository(session)
    repo.add(author1)
    session.commit()

    rows = session.execute(text(
        'SELECT title, first_name, last_name FROM "author" \
        JOIN "book" on author.id==book.author_id \
        ORDER BY title'
    ))
    # print(type(rows))
    assert rows.all() == [
        ("East of Eden", "John", "Steinbeck"),
        ("Grapes of Wrath", "John", "Steinbeck"),
        ('Of Mice and Men', 'John', 'Steinbeck')
    ]