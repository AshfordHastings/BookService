import pytest, requests

from domain.model import Book, Author
import config

@pytest.fixture()
def persisted_author(session):
    author = Author(
        first_name="John",
        last_name="Steinbeck"
    )
    session.add(author)
    session.commit()
    return author

@pytest.fixture()
def persisted_book(session, persisted_author):
    book = Book(
        title="Grapes of Wrath",
        year=1937,
        author=persisted_author
    )
    session.add(book)
    session.commit()
    return book

@pytest.mark.skip(reason="Unfinished test.")
def test_post_book_returns_2011(client):
    data = {"title": "Grapes of Wrath", "year": 1937}
    url = config.get_api_url()
    resp = client.post(f"{url}/books", json=data)
    assert resp.status_code == 201


def test_get_book_returns_book_and_200(client, persisted_book):
    book_id = persisted_book.id
    url = config.get_api_url()
    resp = client.get(f"{url}/books/{book_id}")
    assert resp.status_code == 200
    assert resp.json['id'] == persisted_book.id
    assert resp.json['title'] == persisted_book.title
    assert resp.json['author']['first_name'] == persisted_book.author.first_name

def test_post_book_returns_201(client):
    data = {
        "title": "Grapes of Wrath",
        "year": 1937,
        "first_name": "John",
        "last_name": "Steinbeck",
        "extension": "txt"
    }
    url = config.get_api_url()
    resp = client.post(f"{url}/books", json=data)
    assert resp.status_code == 201