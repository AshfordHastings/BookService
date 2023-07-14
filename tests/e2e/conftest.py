import pytest, requests, json

from domain.model.book import Book, Author
from api.schemas.book import BookSchema

def create_persisted_author(session, first_name, last_name):
    author = Author(
        first_name=first_name,
        last_name=last_name
    )
    session.add(author)
    session.commit()
    return author

def create_persisted_book(session, title, year, persisted_author):
    book = Book(
        title,
        year,
        author=persisted_author
    )
    session.add(book)
    session.commit()
    return book

@pytest.fixture()
def persisted_book_list(session):
    b_list = [('Of Mice and Men', 1937), ('Grapes of Wrath', 1945), ('The Pearl', 1951)]
    a = create_persisted_author(session, 'John', 'Steinbeck')
    return [create_persisted_book(session, b[0], b[1], a) for b in b_list]

@pytest.fixture()
def persisted_author(session):
    return create_persisted_author(session, 'John', 'Steinbeck')

@pytest.fixture()
def persisted_book(session, persisted_author):
    return create_persisted_book(session, "Grapes of Wrath", 1937, persisted_author)

@pytest.mark.skip(reason="Unfinished test.")
def test_post_book_returns_2011(client):
    data = {"title": "Grapes of Wrath", "year": 1937}
    url = config.get_api_url()
    resp = client.post(f"{url}/books", json=data)
    assert resp.status_code == 201