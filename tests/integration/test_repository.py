from domain.model.book import BookObject, Author, MData, Book
from sqlalchemy import text, select
 

def test_repository_can_save_a_book(session):
    a = Author("John", "Steinbeck")
    f = MData("txt")
    i = Book("East of Eden", 1937, a)
    b = BookObject(i, f)

    session.add(b)

    stmt = select(Author.first_name, Author.last_name)
    row = session.execute(stmt).first()
    assert row == ("John", "Steinbeck")

    stmt = select(Author)
    author = session.scalars(stmt).first()
    assert author.first_name == "John" and author.last_name == "Steinbeck"

    stmt = select(BookObject, Book).join(BookObject.book)
    book, book_info = session.execute(stmt).first()
    assert book_info.title == "East of Eden"
    assert book_info.year == 1937
    assert book_info.author.first_name == "John"

    stmt = select(BookObject)
    book = session.scalars(stmt).first()
    assert book.book.title == "East of Eden"
    assert book.book.year == 1937
    assert book.book.author.first_name == "John"
    assert book.m_data.ext == "txt"



# def test_repository_can_save_a_book(session):
#     book1 = Book("Grapes of Wrath", 1937)

#     repo = SQLAlchemyRepository(session)
#     repo.add(book1)
#     session.commit()

#     rows = session.execute(text(
#         'SELECT title, year FROM "book"'
#     ))
#     assert list(rows) == [('Grapes of Wrath', 1937)]

# def test_repository_can_add_many_books(session):
#     book1 = Book("Grapes of Wrath", 1937)
#     book2 = Book("East of Eden", 1943)
#     book3 = Book("Of Mice and Men", 1950)

#     repo = SQLAlchemyRepository(session)
#     repo.add_all([book1, book2, book3])
#     session.commit()

#     rows = session.execute(text(
#         'SELECT title, year FROM "book"'
#     ))
#     assert list(rows) == [('Grapes of Wrath', 1937), ("East of Eden", 1943), ("Of Mice and Men", 1950)]

# def test_respository_can_save_an_author(session):
#     author1 = Author("John", "Steinbeck")

#     repo = SQLAlchemyRepository(session)
#     repo.add(author1)
#     session.commit()

#     rows = session.execute(text(
#         'SELECT first_name, last_name FROM "author"'
#     ))
#     assert list(rows) == [("John", "Steinbeck")]

# def test_repository_can_save_an_author_with_book(session):
#     author1 = Author("John", "Steinbeck")
#     book1 = Book("Grapes of Wrath", 1937)
#     author1.add_book(book1)

#     repo = SQLAlchemyRepository(session)
#     repo.add(author1)
#     session.commit()

#     rows = session.execute(text(
#         'SELECT title, first_name, last_name FROM "author" \
#         JOIN "book" on author.id==book.author_id'
#     ))
#     assert list(rows) == [("Grapes of Wrath", "John", "Steinbeck")]

# def test_repository_can_save_an_author_with_many_books(session):
#     author1 = Author("John", "Steinbeck")
#     book1 = Book("Grapes of Wrath", 1937)
#     book2 = Book("East of Eden", 1943)
#     book3 = Book("Of Mice and Men", 1950)
#     author1.add_books([book1, book2, book3])

#     repo = SQLAlchemyRepository(session)
#     repo.add(author1)
#     session.commit()

#     rows = session.execute(text(
#         'SELECT title, first_name, last_name FROM "author" \
#         JOIN "book" on author.id==book.author_id \
#         ORDER BY title'
#     ))
#     # print(type(rows))
#     assert rows.all() == [
#         ("East of Eden", "John", "Steinbeck"),
#         ("Grapes of Wrath", "John", "Steinbeck"),
#         ('Of Mice and Men', 'John', 'Steinbeck')
#     ]